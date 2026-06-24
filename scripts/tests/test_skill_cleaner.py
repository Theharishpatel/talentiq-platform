from src.cleaning.skill_cleaner import (
    clean_skills,
)

skills = [
    {"name": "Python"},
    {"name": " python "},
    {"name": "PYTHON"},
    {"name": "SQL"},
]

cleaned = clean_skills(
    skills
)

print(cleaned)