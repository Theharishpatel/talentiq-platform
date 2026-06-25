"""
Candidate text builder.
"""

from src.text_builder.templates import (
    CANDIDATE_TEMPLATE,
)

def build_skills_section(
        candidate: dict,
) -> str:
    
    skills = candidate.get(
        "skills",
        []
    )

    skill_names = []

    for skill in skills:

        name = skill.get(
            "name"
        )

        if name:

            skill_names.append(
                name
            )

    return "\n".join(
        f"- {skill}"
        for skill in skill_names
    )

def build_career_section(
        candidate: dict,
) -> str:
    
    jobs = candidate.get(
        "career_history",
        []
    )

    lines = []

    for job in jobs:

        title = job.get(
            "title",
            "Unknonwn Role",
        )

        company = job.get(
            "company",
            "unknown company",
        )

        duration = job.get(
            "duration_months",
            0,
        )

        lines.append(
            f"Role: {title}\n"
            f"Company: {company}\n"
            f"Duration: {duration} months\n"
        )

    return "\n".join(
        lines
    )

def build_education_section(
        candidate : dict,
) -> str: 
    
    education = candidate.get(
        "education",
        []
    )

    lines = []

    for edu in education:

        degree = edu.get(
            "degree",
            ""
        )

        field = edu.get(
            "field_of_study",
            ""
        )

        if degree and field:

            lines.append(
                f"Degree: {degree}\n"
                f"Field: {field}\n"
            )

        elif degree:

            lines.append(
                degree
            )

    return "\n".join(
        lines
    )

def build_candidate_text(
        candidate: dict,
) -> str:
    

    profile = candidate.get(
        "profile",
        {}
    )

    text = CANDIDATE_TEMPLATE.format(

        candidate_id = candidate.get(
            "candidate_id",
            ""

        ),

        current_title = profile.get(
            "current_title",
            ""
        ),

        headline = profile.get(
            "headline",
            ""
        ),

        summary = profile.get(
            "summary",
            ""
        ),

        years_experience = profile.get(
            "years_of_experience",
            ""
        ),

        location = (
            f"{profile.get('location', '')}, "
            f"{profile.get('country', '')}"
        ),

        skills = build_skills_section(
            candidate
        ),

        career_history = build_career_section(
            candidate
        ),

        education = build_education_section(
            candidate
        ),
    )

    return text.strip()