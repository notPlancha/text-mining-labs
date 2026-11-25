"""Smoke tests verifying the Lab 1 repository scaffold."""

import pytest

import text_mining_labs
from text_mining_labs import lab1


def test_package_exports() -> None:
    """Package exposes expected Lab 1 stub callables."""
    assert callable(text_mining_labs.tokenize_spacy)
    assert callable(text_mining_labs.pos_tag_imdb_samples)
    assert text_mining_labs.tokenize_spacy is lab1.tokenize_spacy
    assert text_mining_labs.pos_tag_imdb_samples is lab1.pos_tag_imdb_samples


def test_tokenize_spacy_stub_raises() -> None:
    """Task 1.1 stub remains unimplemented in the scaffold."""
    with pytest.raises(NotImplementedError):
        lab1.tokenize_spacy("Sample sentence for tokenization.")


def test_pos_tag_imdb_samples_stub_raises() -> None:
    """Task 1.2 stub remains unimplemented in the scaffold."""
    with pytest.raises(NotImplementedError):
        lab1.pos_tag_imdb_samples(["Sample review."], n_samples=1)
