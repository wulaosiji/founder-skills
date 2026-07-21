# Contributing to founder-skills

Contributions should make a founder workflow more specific, repeatable, and verifiable. A longer prompt is not automatically a better skill.

## Before You Start

1. Search the existing 24 skills for overlapping scope.
2. Decide whether the change belongs in an existing skill or needs a new skill.
3. Keep private company data, customer information, credentials, and unpublished material out of the repository.
4. Open an issue before proposing a broad restructuring or a new skill family.

## Skill Requirements

Every skill lives at `skills/<skill-name>/SKILL.md` and must include:

- A lowercase, hyphenated `name` that matches the directory name.
- A `description` that explains both what the skill does and when it should trigger.
- A clear scope, including cases where the skill should not be used.
- Expected inputs and a defined output or deliverable.
- A step-by-step workflow.
- At least one realistic usage example.
- Guardrails for missing information, unsupported claims, and sensitive data.
- Dependencies and environment requirements when scripts or external tools are needed.

Keep the main `SKILL.md` under 500 lines. Move detailed material into `references/`, reusable programs into `scripts/`, and templates or media into `assets/`.

## Resource Paths

Paths inside a skill must be relative to the skill root:

```markdown
Read `references/scoring-guide.md` before assigning a score.
Run `scripts/validate_input.py --input company.json` before generating the report.
```

Do not document a script, example, reference, or output that is not present or cannot be produced by the skill.

## Writing Quality

Prefer operating routines, decision rules, checklists, templates, and concrete examples. Avoid generic founder advice that the model could produce without the skill.

When facts depend on current market information, instruct the agent to verify dates and sources. Never invent funding amounts, customer evidence, traction, market size, or quotations.

## Local Validation

Run both commands from the repository root:

```bash
python3 -m unittest tests/test_validate_repository.py -v
python3 scripts/validate_repository.py
```

For a skill with a bundled Python script, also run:

```bash
python3 skills/<skill-name>/scripts/<script-name>.py --help
```

Add focused tests when changing executable behavior. A documentation-only change still needs the repository validator.

## Pull Request Checklist

- [ ] The skill name matches its directory.
- [ ] Trigger, scope, inputs, outputs, example, and guardrails are explicit.
- [ ] Local links and referenced resources exist.
- [ ] README and Founder Kit navigation remain accurate.
- [ ] Repository tests and validation pass.
- [ ] No secrets, private data, generated output, or cache files are included.
- [ ] The change stays within one reviewable purpose.

Repository maintainers decide when to push, open a pull request, release, or publish changes.
