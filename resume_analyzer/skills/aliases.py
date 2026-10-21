"""
Skill aliases.

Maps alternative surface forms used in resumes and job adverts onto the
canonical skill names held in ``skills.database``. This closes the gap between
"Amazon Web Services" and "AWS", or "Postgres" and "PostgreSQL", so that a
skill is counted as matched even when the two documents spell it differently.
"""

ALIASES = {
    # Cloud platforms
    "amazon web services": "aws",
    "amazon aws": "aws",
    "google cloud platform": "gcp",
    "apache kafka": "kafka",
    "apache spark": "spark",
    "apache airflow": "airflow",
    "apache hadoop": "hadoop",

    # Databases and tooling
    "postgres": "postgresql",
    "k8s": "kubernetes",
    "powerbi": "power bi",
    "node js": "node.js",
    "nodejs": "node.js",
    "sklearn": "scikit-learn",
    "containerization": "docker",
    "containers": "docker",

    # Data and ML
    "ml": "machine learning",
    "deep learning models": "deep learning",
    "gen ai": "generative ai",
    "large language model": "llm",
    "nlp": "nlp",
    "bash scripting": "shell scripting",
    "unit tests": "unit testing",
    "continuous integration": "ci/cd",
    "continuous delivery": "ci/cd",
}
