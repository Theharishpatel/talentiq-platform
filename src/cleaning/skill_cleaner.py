from src.cleaning.rules import (
    clean_string,
)

def clean_skills( skills: list) -> list:

    seen = set()

    cleaned_skills = []

    for skill in skills:

        name = clean_string(
            skill.get
            ("name")
        )

        if not name:
            continue

        normalized = name.lower()

        if normalized in seen:
            continue

        seen.add(normalized)

        skill["name"] = name

        cleaned_skills.append(skill)

    return cleaned_skills