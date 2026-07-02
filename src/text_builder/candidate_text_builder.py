"""
Candidate text builder.
"""

from src.text_builder.templates import (
    CANDIDATE_TEMPLATE,
)

MAX_SUMMARY_LENGTH = 1000
MAX_DESCRIPTION_LENGTH = 700


def build_skills_section(
    candidate: dict,
) -> str:

    skills = []

    for skill in candidate.get(
        "skills",
        [],
    ):

        name = skill.get(
            "name",
        )

        if name:
            skills.append(name)

    skills = sorted(set(skills))

    return ", ".join(skills)


def build_career_section(
    candidate: dict,
) -> str:

    jobs = candidate.get(
        "career_history",
        [],
    )

    lines = []

    for job in jobs:

        title = job.get(
            "title",
            "Unknown Role",
        )

        company = job.get(
            "company",
            "Unknown Company",
        )

        industry = job.get(
            "industry",
            "",
        )

        duration = job.get(
            "duration_months",
            0,
        )

        description = job.get(
            "description",
            "",
        ).strip()

        if len(description) > MAX_DESCRIPTION_LENGTH:

            description = (
                description[:MAX_DESCRIPTION_LENGTH]
                + "..."
            )

        section = (
            f"{title}\n"
            f"{company}\n"
            f"Industry: {industry}\n"
            f"Duration: {duration} months"
        )

        if description:

            section += (
                f"\nDescription:\n"
                f"{description}"
            )

        lines.append(section)

    return "\n\n".join(lines)


def build_education_section(
    candidate: dict,
) -> str:

    education = candidate.get(
        "education",
        [],
    )

    lines = []

    for edu in education:

        degree = edu.get(
            "degree",
            "",
        )

        field = edu.get(
            "field_of_study",
            "",
        )

        institution = edu.get(
            "institution",
            "",
        )

        end_year = edu.get(
            "end_year",
            "",
        )

        text = ""

        if degree:
            text += degree

        if field:
            text += f" in {field}"

        if institution:
            text += f"\n{institution}"

        if end_year:
            text += f"\nGraduated: {end_year}"

        if text:
            lines.append(text)

    return "\n\n".join(lines)


def build_languages_section(
    candidate: dict,
) -> str:

    languages = []

    for lang in candidate.get(
        "languages",
        [],
    ):

        name = lang.get(
            "language",
        )

        proficiency = lang.get(
            "proficiency",
        )

        if name:

            if proficiency:

                languages.append(
                    f"{name} ({proficiency})"
                )

            else:

                languages.append(name)

    return ", ".join(languages)


def build_candidate_text(
    candidate: dict,
) -> str:

    profile = candidate.get(
        "profile",
        {},
    )

    summary = profile.get(
        "summary",
        "",
    ).strip()

    if len(summary) > MAX_SUMMARY_LENGTH:

        summary = (
            summary[:MAX_SUMMARY_LENGTH]
            + "..."
        )

    return CANDIDATE_TEMPLATE.format(

        current_title=profile.get(
            "current_title",
            "",
        ),

        headline=profile.get(
            "headline",
            "",
        ),

        summary=summary,

        years_experience=profile.get(
            "years_of_experience",
            "",
        ),

        location=f"{profile.get('location','')}, {profile.get('country','')}",

        skills=build_skills_section(
            candidate,
        ),

        career_history=build_career_section(
            candidate,
        ),

        education=build_education_section(
            candidate,
        ),

        languages=build_languages_section(
            candidate,
        ),
    ).strip()