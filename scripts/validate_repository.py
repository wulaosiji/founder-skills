#!/usr/bin/env python3
import argparse
import ast
from pathlib import Path
import re
from typing import Dict, List, Tuple
from urllib.parse import unquote


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
RESOURCE_PATTERN = re.compile(
    r"`((?:scripts|references|assets|examples)/[^`\s]+)`"
)


def relative_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def parse_scalar(value: str) -> str:
    value = value.strip()
    if value.startswith(('"', "'")):
        try:
            parsed = ast.literal_eval(value)
            return str(parsed)
        except (SyntaxError, ValueError):
            return value.strip('"\'')
    return value


def extract_frontmatter(text: str) -> Dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening frontmatter delimiter")
    try:
        closing = next(
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.strip() == "---"
        )
    except StopIteration as error:
        raise ValueError("missing closing frontmatter delimiter") from error

    metadata: Dict[str, str] = {}
    index = 1
    while index < closing:
        line = lines[index]
        if not line.strip() or line[:1].isspace():
            index += 1
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if raw_value in {"|", ">"}:
            block: List[str] = []
            index += 1
            while index < closing and (
                not lines[index].strip() or lines[index][:1].isspace()
            ):
                block.append(lines[index].strip())
                index += 1
            metadata[key] = " ".join(part for part in block if part)
            continue
        metadata[key] = parse_scalar(raw_value)
        index += 1
    return metadata


def validate_skill(skill_file: Path, root: Path) -> List[str]:
    label = relative_path(skill_file, root)
    text = skill_file.read_text(encoding="utf-8")
    errors: List[str] = []
    line_count = len(text.splitlines())
    if line_count > 500:
        errors.append(f"{label}: has {line_count} lines; maximum is 500")
    try:
        metadata = extract_frontmatter(text)
    except ValueError as error:
        return errors + [f"{label}: {error}"]

    name = metadata.get("name", "")
    description = metadata.get("description", "")
    directory_name = skill_file.parent.name
    if not name:
        errors.append(f"{label}: missing name")
    elif name != directory_name:
        errors.append(
            f"{label}: name '{name}' does not match directory '{directory_name}'"
        )
    if name and (len(name) > 64 or not NAME_PATTERN.fullmatch(name)):
        errors.append(f"{label}: invalid skill name '{name}'")
    if not description:
        errors.append(f"{label}: missing description")
    elif len(description) > 1024:
        errors.append(f"{label}: description exceeds 1024 characters")
    return errors


def validate_markdown_links(root: Path) -> List[str]:
    errors: List[str] = []
    for markdown_file in sorted(root.rglob("*.md")):
        text = markdown_file.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            resolved = markdown_file.parent / target
            if not resolved.exists():
                errors.append(
                    f"{relative_path(markdown_file, root)}: "
                    f"broken local link '{raw_target}'"
                )
    return errors


def validate_resource_references(root: Path) -> List[str]:
    errors: List[str] = []
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        return errors
    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        for markdown_file in sorted(skill_dir.rglob("*.md")):
            text = markdown_file.read_text(encoding="utf-8")
            for target in RESOURCE_PATTERN.findall(text):
                if not (skill_dir / target).exists():
                    errors.append(
                        f"{relative_path(markdown_file, root)}: "
                        f"missing resource '{target}'"
                    )
    return errors


def validate_repository(root: Path) -> Tuple[List[str], int]:
    root = root.resolve()
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        return ["skills: directory not found"], 0
    skill_files = sorted(skills_dir.glob("*/SKILL.md"))
    errors: List[str] = []
    for skill_file in skill_files:
        errors.extend(validate_skill(skill_file, root))
    errors.extend(validate_markdown_links(root))
    errors.extend(validate_resource_references(root))
    return sorted(set(errors)), len(skill_files)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the founder-skills repository"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root (defaults to the parent of scripts/)",
    )
    args = parser.parse_args()
    errors, skill_count = validate_repository(args.root)
    if errors:
        print(f"FAILED: {len(errors)} issue(s) across {skill_count} skills")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OK: {skill_count} skills validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
