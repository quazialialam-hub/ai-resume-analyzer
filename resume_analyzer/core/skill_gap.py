"""
Skill gap analysis.

Pure set operations that compare the skills found in a resume with the skills
requested by a job description.
"""


def get_matched_skills(resume_skills: set, jd_skills: set) -> set:
    """Return the skills the candidate already demonstrates."""
    return set(resume_skills) & set(jd_skills)


def get_missing_skills(resume_skills: set, jd_skills: set) -> set:
    """Return the skills the job asks for that the candidate never mentions."""
    return set(jd_skills) - set(resume_skills)
