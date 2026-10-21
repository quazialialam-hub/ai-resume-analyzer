"""
Similarity scoring between a resume and a job description.

Both documents are vectorised with TF-IDF and compared with cosine
similarity.

The vectoriser deliberately stays on unigrams. Adding bigrams was measured
and made the score consistently lower - about ten points on a realistic
resume - because the extra phrase dimensions do not match, and cosine
similarity divides by the length of both vectors. Phrase-level matching is
handled by the skill extractor, which knows the real equivalences
("Amazon Web Services" is "aws") and reports matched skills separately.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_match_score(resume_text: str, job_description: str) -> float:
    """
    Return a 0-100 similarity score between a resume and a job description.

    Returns 0.0 when the documents share no usable vocabulary (for example
    when both contain nothing but stop words).
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    try:
        matrix = vectorizer.fit_transform([resume_text, job_description])
        similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    except ValueError:
        # Empty vocabulary: the two documents cannot be compared.
        similarity = 0.0
    return round(similarity * 100, 1)
