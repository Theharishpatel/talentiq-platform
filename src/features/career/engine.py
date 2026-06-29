"""
Career Growth Feature Engineering Engine.

Extracts raw career growth related features.

No scoring logic should exist in this file.
"""

from statistics import mean


PROMOTION_LEVELS = {
    "intern": 1,
    "trainee": 1,

    "junior": 2,
    "associate": 2,

    "engineer": 3,
    "developer": 3,
    "analyst": 3,

    "senior": 4,

    "lead": 5,
    "principal": 5,
    "staff": 5,

    "manager": 6,

    "senior manager": 7,

    "director": 8,

    "vp": 9,
    "vice president": 9,

    "head": 10,

    "cto": 11,
    "cio": 11,
    "ceo": 11,
}


COMPANY_SIZE_LEVEL = {

    "1-10": 1,
    "11-50": 2,
    "51-200": 3,
    "201-500": 4,
    "501-1000": 5,
    "1001-5000": 6,
    "5001-10000": 7,
    "10001+": 8,

}


DEGREE_LEVEL = {

    "high school": 1,

    "diploma": 2,

    "b.sc": 3,
    "b.tech": 3,
    "b.e.": 3,
    "bca": 3,
    "b.com": 3,

    "m.sc": 4,
    "m.tech": 4,
    "mba": 4,
    "mca": 4,

    "phd": 5,

}


ADVANCED_PROFICIENCY = {
    "advanced",
    "expert",
}


def get_role_level(title: str) -> int:

    if not title:
        return 0

    title = title.lower()

    for keyword, level in PROMOTION_LEVELS.items():

        if keyword in title:

            return level

    return 0


def build_growth_features(
        candidate: dict,
) -> dict:

    jobs = candidate.get(
        "career_history",
        []
    )

    skills = candidate.get(
        "skills",
        []
    )

    education = candidate.get(
        "education",
        []
    )

    profile = candidate.get(
        "profile",
        {}
    )

    # ----- Career Progression ----- 

    promotion_count = 0

    previous_level = None

    highest_role_level = 0

    company_size_levels = []

    for job in reversed(jobs):

        level = get_role_level(
            job.get(
                "title",
                ""
            )
        )

        highest_role_level = max(
            highest_role_level,
            level,
        )

        if previous_level is not None:

            if level > previous_level:

                promotion_count += 1

        previous_level = level

        size = job.get(
            "company_size"
        )

        if size in COMPANY_SIZE_LEVEL:

            company_size_levels.append(
                COMPANY_SIZE_LEVEL[size]
            )

    company_size_growth = 0

    if len(company_size_levels) >= 2:

        company_size_growth = (
            company_size_levels[-1]
            - company_size_levels[0]
        )

    # ----- Skill Evolution ----

    skill_count = len(
        skills
    )

    skill_durations = []

    advanced_skill_count = 0

    for skill in skills:

        duration = skill.get(
            "duration_months"
        )

        if duration is not None:

            skill_durations.append(
                duration
            )

        proficiency = (
            skill.get(
                "proficiency",
                "",
            )
            .lower()
            .strip()
        )

        if proficiency in ADVANCED_PROFICIENCY:

            advanced_skill_count += 1

    avg_skill_duration = (

        mean(skill_durations)

        if skill_durations

        else 0

    )

    # ----- Education -----

    education_count = len(
        education
    )

    highest_degree_level = 0

    highest_tier = 0

    for edu in education:

        degree = (
            edu.get(
                "degree",
                "",
            )
            .lower()
            .strip()
        )

        highest_degree_level = max(

            highest_degree_level,

            DEGREE_LEVEL.get(
                degree,
                0,
            ),

        )

        tier = edu.get(
            "tier",
            ""
        )

        if tier.startswith("tier_"):

            try:

                value = int(
                    tier.split("_")[1]
                )

                if highest_tier == 0:

                    highest_tier = value

                else:

                    highest_tier = min(
                        highest_tier,
                        value,
                    )

            except Exception:

                pass

    # ---- Certifications ---

    certification_count = len(

        candidate.get(
            "certifications",
            []
        )

    )

    # ---- Return ----- 

    return {

        "promotion_count":
            promotion_count,

        "highest_role_level":
            highest_role_level,

        "company_size_growth":
            company_size_growth,

        "skill_count":
            skill_count,

        "advanced_skill_count":
            advanced_skill_count,

        "avg_skill_duration":
            round(
                avg_skill_duration,
                2,
            ),

        "education_count":
            education_count,

        "highest_degree_level":
            highest_degree_level,

        "highest_education_tier":
            highest_tier,

        "certification_count":
            certification_count,

    }