# Text Mining Labs (LTU D7058E)

Workspace and scaffolding for the **Text Mining (`D7058E 27014 HT2026`)** laboratory assignments at Luleå University of Technology (LTU), currently scoped to **Lab 1**.

## Repository Structure

- `docs/` — Original Canvas pages, announcements, slides, and instructor Lab 1 notebook:
  - [`docs/pages/welcome.md`](docs/pages/welcome.md)
  - [`docs/pages/course-information.md`](docs/pages/course-information.md)
  - [`docs/pages/lab-grading-criteria.md`](docs/pages/lab-grading-criteria.md)
  - [`docs/pages/recordings-of-class-and-labs.md`](docs/pages/recordings-of-class-and-labs.md)
  - [`docs/pages/introduction-to-text-mining.md`](docs/pages/introduction-to-text-mining.md)
  - [`docs/pages/structural-analysis.md`](docs/pages/structural-analysis.md)
  - [`docs/pages/neuralnets-for-text-mining.md`](docs/pages/neuralnets-for-text-mining.md)
  - [`docs/announcements/lab-1-and-other-important-info.md`](docs/announcements/lab-1-and-other-important-info.md)
  - [`docs/lab1/text_mining1.ipynb`](docs/lab1/text_mining1.ipynb)
  - [`docs/lecture_slides/TM_Intro.pptx`](docs/lecture_slides/TM_Intro.pptx)
  - [`docs/lecture_slides/TM_Structural.pptx`](docs/lecture_slides/TM_Structural.pptx)
- [`src/text_mining_labs/`](src/text_mining_labs/__init__.py) — Python package stubs for lab exercises ([`lab1.py`](src/text_mining_labs/lab1.py))
- [`notebooks/`](notebooks/lab1_starter.ipynb) — Starter Jupyter/Colab notebook template ([`lab1_starter.ipynb`](notebooks/lab1_starter.ipynb))
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
