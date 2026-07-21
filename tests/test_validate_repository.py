import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Tuple
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.validate_repository import validate_repository


class ValidateRepositoryTests(unittest.TestCase):
    VALID_SKILL = (
        "---\n"
        "name: sample-skill\n"
        "description: Use when validating a sample.\n"
        "---\n"
        "# Sample\n"
    )

    def make_repo(self, skill_body: str) -> Tuple[TemporaryDirectory, Path]:
        temporary = TemporaryDirectory()
        root = Path(temporary.name)
        skill_dir = root / "skills" / "sample-skill"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(skill_body, encoding="utf-8")
        return temporary, root

    def test_valid_repository_has_no_errors(self):
        temporary, root = self.make_repo(self.VALID_SKILL)
        self.addCleanup(temporary.cleanup)
        errors, skill_count = validate_repository(root)
        self.assertEqual(errors, [])
        self.assertEqual(skill_count, 1)

    def test_name_must_match_directory(self):
        temporary, root = self.make_repo(
            self.VALID_SKILL.replace("name: sample-skill", "name: wrong-name")
        )
        self.addCleanup(temporary.cleanup)
        errors, _ = validate_repository(root)
        self.assertTrue(any("does not match directory" in error for error in errors))

    def test_broken_markdown_link_is_reported(self):
        temporary, root = self.make_repo(self.VALID_SKILL)
        self.addCleanup(temporary.cleanup)
        (root / "README.md").write_text("[Missing](missing.md)\n", encoding="utf-8")
        errors, _ = validate_repository(root)
        self.assertTrue(any("broken local link" in error for error in errors))

    def test_missing_skill_resource_is_reported(self):
        temporary, root = self.make_repo(
            self.VALID_SKILL + "Run `scripts/missing.py`.\n"
        )
        self.addCleanup(temporary.cleanup)
        errors, _ = validate_repository(root)
        self.assertTrue(any("missing resource" in error for error in errors))

    def test_skill_over_500_lines_is_reported(self):
        temporary, root = self.make_repo(self.VALID_SKILL + ("line\n" * 496))
        self.addCleanup(temporary.cleanup)
        errors, _ = validate_repository(root)
        self.assertTrue(any("maximum is 500" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
