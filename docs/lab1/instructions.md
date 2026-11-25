# Lab 1 Instructions — Tokenization, Text Preprocessing & PoS Tagging

- **Canvas Assignment**: [Lab 1 (ID 222324)](https://canvas.ltu.se/courses/29006/assignments/222324)
- **Deadline**: `2026-11-25 22:59:59 UTC` (`2026-11-25 23:59:59 CET`)
- **Submission Type**: `online_upload` (Colab / Jupyter notebook)
- **Group Format**: Group task (2–3 people). Present your Colab notebook directly (no slides) in **4 minutes** during the lab session in **A3012** / Zoom.
- **Instructor Reference Notebook**: [`text_mining1_instructor.ipynb`](text_mining1_instructor.ipynb) (untouched copy of `text_mining1.ipynb`)
- **Starter Notebook**: [`notebooks/lab1_starter.ipynb`](../../notebooks/lab1_starter.ipynb)

## Learning Objectives

At the end of Lab 1, students should be able to:

1. Perform tokenization & text preprocessing.
2. Experience vibe (AI-assisted) coding responsibly.

## AI Usage & Group Attribution Rules

From the Canvas announcement (*"Lab 1 & Other Important Info"*, Oluwatosin Adewumi, 2026-11-18) and `text_mining1.ipynb`:

- **Group Attribution**: Group members **must write which part each member completed** inside the notebook.
- **AI Declaration**: You are free to use AI ("vibe") coding in any task, **provided you declare it in your notebook** and **understand what the AI produced** so you can present and defend your solution during the lab session.

## Instructor Reference Examples & Resources

[`text_mining1_instructor.ipynb`](text_mining1_instructor.ipynb) covers:

- Python fundamentals (types, loops, duplicate removal, conditionals, functions, module imports)
- Tokenization and frequency distribution with **NLTK** (`nltk.word_tokenize`, `nltk.FreqDist`, `punkt`)
- Regex-based text preprocessing with **Pandas** (`preprocess_pandas`: lowercasing, email/IP/punctuation/digit removal)
- External references:
  - NLTK Book Ch. 1: <https://www.nltk.org/book/ch01.html>
  - spaCy 101: <https://spacy.io/usage/spacy-101>

## Task 1 Requirements

Complete both parts of Task 1 (in [`notebooks/lab1_starter.ipynb`](../../notebooks/lab1_starter.ipynb) and/or [`src/text_mining_labs/lab1.py`](../../src/text_mining_labs/lab1.py)):

1. **Task 1.1 — spaCy Tokenization**:
   Implement tokenization using the **spaCy** library instead of the **NLTK** library.
2. **Task 1.2 — Part-of-Speech (PoS) Tagging on IMDB Reviews**:
   Implement part-of-speech (**PoS**) tagging using **spaCy** or **NLTK** for the **first 20 samples** in the training set of the IMDB dataset:
   - Dataset: <https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews>
   - Store downloaded dataset files locally under `data/` (which is excluded by `.gitignore`; never commit large datasets to Git).

## Grading Questions (4-Minute Lab Discussion)

During your 4-minute Colab presentation (plus any relevant follow-up questions):

1. Show your code outcome, go through it and explain what it does.
2. Is there any part of the code that may be optimized (made better)?
3. What other challenges can this solution be adapted for?
4. Will you like to discuss the time & space complexities of parts of your solution (optional)?
