# `resume_analyzer/core/scoring.py`

**Path:** `resume_analyzer/core/scoring.py`
**Purpose:** Turns a resume and a job description into a single match score.

## What it does

Vectorises both documents with TF-IDF and compares them with cosine
similarity.

- **TF-IDF** weighs a word by how often it appears in one document against how
  often it appears in the other, so a word repeated thirty times in a job
  advert does not drown out every other signal.
- **Cosine similarity** measures the angle between the two term vectors, so
  only the *direction* (which words are present) matters, not the length of
  either document.
- The result is scaled to 0-100 and rounded to one decimal place.

## Public API

| Name | Kind | Description |
| --- | --- | --- |
| `compute_match_score(resume_text, job_description)` | function | Returns a float from 0.0 to 100.0 |

## Behaviour notes

- The vectoriser stays on unigrams. Adding bigrams was measured and made the
  score consistently lower - about ten points on a realistic resume - because
  the extra phrase dimensions do not match, and cosine similarity divides by
  the length of both vectors. Phrase-level matching is handled by the skill
  extractor, which knows the real equivalences ("Amazon Web Services" is
  "aws") and reports matched skills separately.
- `stop_words="english"` removes the most common English words, which carry
  no matching signal.
- If the documents share no usable vocabulary, Scikit-learn raises
  `ValueError` for an empty vocabulary. That is caught and the score becomes
  `0.0` rather than an error.
- The score measures vocabulary overlap only. It is not a judgement about
  seniority or relevance.

## Used by

`core/pipeline.py`.
