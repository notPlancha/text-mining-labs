# Text Mining Labs (LTU D7058E)

Workspace for the **Text Mining (`D7058E 27014 HT2026`)** laboratory assignments at Luleå University of Technology (LTU), currently scoped to **Lab 1**.

## Repository Structure

- `docs/` — Assignment-specific original docs for Lab 1:
  - [`docs/text_mining1.ipynb`](docs/text_mining1.ipynb)
  - [`docs/TM_Structural.pptx`](docs/TM_Structural.pptx)
  - [`docs/lab-grading-criteria.md`](docs/lab-grading-criteria.md)
- `src/` — Lab notebooks:
  - [`src/lab1.ipynb`](src/lab1.ipynb)
- [`Taskfile.yml`](Taskfile.yml) — Task runner shortcuts (`task sync`, `task check`, `task lint`, `task fmt`)

## Setup & Verification

This project uses [`uv`](https://docs.astral.sh/uv/) with Python `>=3.15`, `ruff`, and `ty`.

```powershell
# Sync environment and dependencies
task sync

# Run lint, formatting check, and type check
task check
```
