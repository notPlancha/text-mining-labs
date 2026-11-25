# Text Mining Labs (LTU D7058E)

Workspace and scaffolding for the **Text Mining (`D7058E 27014 HT2026`)** laboratory assignments at Luleå University of Technology (LTU), currently scoped to **Lab 1**.

## Repository Structure

- [`docs/`](docs/course-overview.md) — Course overview, policies, grading criteria, materials index, and Lab 1 instructions:
  - [`docs/course-overview.md`](docs/course-overview.md) — Schedule, rooms (`A3002`, `A3012`), Zoom link, lab/quiz prerequisites, late submission rules, and oral exam dates
  - [`docs/course-information.md`](docs/course-information.md) — Textbooks, evaluation metrics reference, AI usage & acknowledgment policy, and `U`/`G`/`VG` grading scale
  - [`docs/lab-grading-criteria.md`](docs/lab-grading-criteria.md) — 4-minute Colab presentation format, grading questions, and group project requirements
  - [`docs/recordings-and-materials.md`](docs/recordings-and-materials.md) — Links and local `.canvas-vault` paths for lecture slides, videos, and lab notebooks
  - [`docs/lab1/instructions.md`](docs/lab1/instructions.md) — Lab 1 deadline, Task 1 requirements, dataset link, and AI declaration notes
  - [`docs/lab1/text_mining1_instructor.ipynb`](docs/lab1/text_mining1_instructor.ipynb) — Untouched instructor reference notebook (`text_mining1.ipynb`)
- [`src/text_mining_labs/`](src/text_mining_labs/__init__.py) — Python package stubs for lab exercises (`lab1.py`)
- [`notebooks/`](notebooks/lab1_starter.ipynb) — Starter Jupyter/Colab notebook templates (`lab1_starter.ipynb`)
- [`tests/`](tests/test_scaffold.py) — Scaffold smoke tests

## Setup & Verification

This project uses [`uv`](https://docs.astral.sh/uv/) with Python `>=3.11`, `ruff`, `ty`, and `pytest`.

```powershell
# Sync environment and dependencies
uv sync

# Run lint, formatting check, type check, and smoke tests
uv run ruff check .
uv run ruff format --check .
uv run ty check src/
uv run pytest
```
