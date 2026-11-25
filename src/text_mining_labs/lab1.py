"""Lab 1 function stubs for tokenization and part-of-speech (PoS) tagging.

See ``docs/text_mining1.ipynb`` and ``docs/lab-grading-criteria.md``.
"""

from collections.abc import Sequence
from typing import Literal


def tokenize_spacy(text: str, model: str = "en_core_web_sm") -> list[str]:
    """Tokenize an input text string using spaCy.

    Args:
        text: Raw input text to tokenize.
        model: Name of the spaCy language pipeline to load.

    Returns:
        List of extracted token strings.
    """
    # TODO: Solution
    raise NotImplementedError("Task 1.1: implement spaCy tokenization.")


def pos_tag_imdb_samples(
    texts: Sequence[str],
    n_samples: int = 20,
    backend: Literal["spacy", "nltk"] = "spacy",
) -> list[list[tuple[str, str]]]:
    """Perform PoS tagging on the first ``n_samples`` IMDB training reviews.

    Args:
        texts: Sequence of training review texts.
        n_samples: Number of leading samples to tag (Lab 1 specifies 20).
        backend: NLP library used for PoS tagging (``"spacy"`` or ``"nltk"``).

    Returns:
        A list containing ``(token, pos_tag)`` pairs for each processed sample.
    """
    # TODO: Solution
    raise NotImplementedError("Task 1.2: implement PoS tagging for IMDB samples.")
