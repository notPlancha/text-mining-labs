# Text Mining Labs (LTU D7058E)

Workspace and scaffolding for the **Text Mining (`D7058E 27014 HT2026`)** laboratory assignments at Luleå University of Technology (LTU), currently scoped to **Lab 1**.

## Repository Structure

- `docs/` — Original course/lab documents and slides relevant to Lab 1:
  - [`docs/text_mining1.ipynb`](docs/text_mining1.ipynb)
  - [`docs/TM_Intro.pptx`](docs/TM_Intro.pptx)
  - [`docs/TM_Structural.pptx`](docs/TM_Structural.pptx)
  - [`docs/lab-1-and-other-important-info.md`](docs/lab-1-and-other-important-info.md)
  - [`docs/lab-grading-criteria.md`](docs/lab-grading-criteria.md)
  - [`docs/welcome.md`](docs/welcome.md)
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
