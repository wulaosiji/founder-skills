---
name: pitch-deck-creator
description: "Generate an editable 10-slide startup pitch deck as a PPTX file from structured JSON. Use when a founder needs a concrete fundraising deck covering problem, solution, business model, product, competition, traction, roadmap, team, and fundraising. Supports Chinese and English content through a bundled Python script."
---

# Pitch Deck Creator

Generate a consistent 10-slide fundraising deck from structured startup data. This skill is the executable option in the BP collection: it produces a PPTX instead of only an outline or writing framework.

## When to Use

Use this skill when the user wants an editable PPTX generated from known company information. Use a planning or narrative skill first when the user still needs to decide the story:

- `fundraising-bp-planner` for a Chinese outline
- `investor-pitch-planner` for an English outline
- `sequoia-structured-bp`, `yc-insight-driven-bp`, or `raskin-narrative-bp` for a specific narrative framework
- `business-plan-ppt` for the separate 18-page Chinese content and visual specification

## Bundled Implementation

- Script: `scripts/generate_pitch_deck.py`
- Dependency: `python-pptx>=0.6.21` from `requirements.txt`
- Input: UTF-8 JSON
- Output: editable 16:9 PPTX
- Default filename: `{project_name}_BP.pptx`

The bundled script does not export PDF. Convert the generated PPTX separately when the user explicitly needs PDF or web delivery.

The two files under `references/` document the legacy 18-page reference style. They are not the output contract of this 10-slide generator; use `business-plan-ppt` when that longer structure is the actual requirement.

## Input Expectations

Collect or extract these JSON fields:

- `project_name`, `tagline`, and up to three `value_props`
- `pain_points` and `market_size` (`tam`, `sam`, `som`)
- `solution.features` and `solution.differentiation`
- `business_model.revenue_streams` and `business_model.pricing`
- `product_status`, `competitors`, `traction`, and `roadmap`
- `team` and `fundraising`
- `language`: `zh` or `en`
- Optional `colors`: `primary`, `dark`, and `accent`

Do not invent traction, market size, customer evidence, team credentials, or fundraising terms. Leave unknown values empty or mark them for confirmation before generation.

## Workflow

1. Extract the company information and list any missing decision-critical fields.
2. Confirm every factual claim that will appear in the deck.
3. Create a UTF-8 JSON input file using the schema in `README.md`.
4. Install the local dependency with `python3 -m pip install -r requirements.txt` when needed.
5. Run:

   ```bash
   python3 scripts/generate_pitch_deck.py --input startup.json --output Company_BP.pptx
   ```

6. Open the PPTX and review text overflow, missing fields, contrast, and factual accuracy.
7. Revise the JSON and regenerate rather than manually patching repeated content.

## Fixed 10-Slide Output

| # | Slide | Primary input |
|---|-------|---------------|
| 1 | Cover | `project_name`, `tagline`, `value_props` |
| 2 | Market Pain Points | `pain_points`, `market_size` |
| 3 | Solution | `solution` |
| 4 | Business Model | `business_model` |
| 5 | Product Demo | `product_status` |
| 6 | Competitive Analysis | `competitors` |
| 7 | Traction | `traction` |
| 8 | Roadmap | `roadmap` |
| 9 | Team | `team` |
| 10 | Fundraising | `fundraising` |

## Output Standards

- Confirm that the generated file contains exactly 10 slides.
- Keep the 16:9 dimensions and the chosen color tokens consistent.
- Treat generated layouts as a first draft: review overflow and sparse slides manually.
- Replace empty placeholders before external sharing.
- Keep source data and claims traceable; never present assumptions as verified facts.
