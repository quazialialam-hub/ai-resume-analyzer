"""
The curated skill database.

Skills are grouped by category. Extend this list to widen coverage for your
target roles or industries - the matching logic picks new entries up
automatically.
"""

SKILL_DB = {
    # Programming languages
    "python", "java", "c++", "c#", "javascript", "typescript", "sql", "r",
    "go", "golang", "rust", "scala", "php", "ruby", "swift", "kotlin", "matlab",

    # Web / frameworks
    "react", "angular", "vue", "django", "flask", "streamlit", "fastapi",
    "node.js", "express", "spring", "asp.net", "html", "css",
    "bootstrap", "tailwind",

    # Data / ML / AI
    "machine learning", "deep learning", "nlp", "natural language processing",
    "computer vision", "scikit-learn", "tensorflow", "pytorch",
    "keras", "pandas", "numpy", "matplotlib", "seaborn", "opencv",
    "data analysis", "data visualization", "data science", "statistics",
    "regression", "classification", "clustering", "feature engineering",
    "neural networks", "llm", "large language models", "generative ai",
    "prompt engineering", "transformers", "spacy", "nltk", "hugging face",

    # Data engineering / cloud
    "aws", "azure", "gcp", "google cloud", "docker", "kubernetes",
    "terraform", "airflow", "spark", "hadoop", "kafka", "etl",
    "data pipeline", "snowflake", "redshift", "bigquery",

    # Databases
    "mysql", "postgresql", "mongodb", "oracle", "sqlite", "nosql",
    "database design", "data modeling",

    # Tools / practices
    "git", "github", "gitlab", "jira", "agile", "scrum", "ci/cd",
    "unit testing", "rest api", "restful api", "microservices",
    "linux", "bash", "shell scripting", "excel", "power bi", "tableau",

    # Soft / business skills
    "communication", "leadership", "teamwork", "problem solving",
    "project management", "stakeholder management", "time management",
    "critical thinking", "collaboration", "presentation skills",

    # Cybersecurity
    "cybersecurity", "penetration testing", "network security",
    "encryption", "vulnerability assessment",
}

# Skills whose surface form is also a common English word or a single letter
# ("go", "r"). These are only matched when written in their exact canonical
# form, which keeps phrases such as "go to market" from being mis-detected.
CASE_SENSITIVE_SKILLS = {"go", "r"}
