"""
Experience feature extraction engine.

Extracts raw experience-related features from a single candidate.

"""

from statistics import mean


HIGH_PROFICIENCY = {
    "advanced",
}


def extract_experience_features(
    candidate: dict,
) -> dict:

    profile = candidate.get(
        "profile",
        {}
    )

    jobs = candidate.get(
        "career_history",
        []
    )

    skills = candidate.get(
        "skills",
        []
    )

    # ----- Experience ------

    years_experience = profile.get(
        "years_of_experience",
        0,
    )

    # ------- Job Features ------

    job_count = len(jobs)

    job_durations = []

    current_job_duration = 0

    companies = set()

    industries = set()

    roles = set()

    for job in jobs:

        duration = job.get(
            "duration_months"
        )

        if duration is not None:

            job_durations.append(
                duration
            )

        if job.get(
            "is_current"
        ):

            current_job_duration = (
                duration or 0
            )

        company = job.get(
            "company"
        )

        if company:

            companies.add(
                company
            )

        industry = job.get(
            "industry"
        )

        if industry:

            industries.add(
                industry
            )

        role = job.get(
            "title"
        )

        if role:

            roles.add(
                role
            )

    career_span_months = sum(
        job_durations
    )

    avg_job_duration = (
        mean(job_durations)
        if job_durations
        else 0
    )

    longest_job_duration = (
        max(job_durations)
        if job_durations
        else 0
    )

    shortest_job_duration = (
        min(job_durations)
        if job_durations
        else 0
    )

    company_count = len(
        companies
    )

    industry_count = len(
        industries
    )

    role_count = len(
        roles
    )

    # ------ Skill Features ------

    skill_count = len(
        skills
    )

    skill_durations = []

    endorsements = []

    high_proficiency_skill_count = 0

    for skill in skills:

        duration = skill.get(
            "duration_months"
        )

        if duration is not None:

            skill_durations.append(
                duration
            )

        endorsement = skill.get(
            "endorsements"
        )

        if endorsement is not None:

            endorsements.append(
                endorsement
            )

        proficiency = (
            skill.get(
                "proficiency",
                ""
            )
            .lower()
            .strip()
        )

        if proficiency in HIGH_PROFICIENCY:

            high_proficiency_skill_count += 1

    avg_skill_duration = (
        mean(skill_durations)
        if skill_durations
        else 0
    )

    longest_skill_duration = (
        max(skill_durations)
        if skill_durations
        else 0
    )

    avg_endorsements = (
        mean(endorsements)
        if endorsements
        else 0
    )

    # ---- Output ----

    return {

        "years_experience":
            years_experience,

        "career_span_months":
            career_span_months,

        "job_count":
            job_count,

        "current_job_duration":
            current_job_duration,

        "avg_job_duration":
            round(
                avg_job_duration,
                2,
            ),

        "longest_job_duration":
            longest_job_duration,

        "shortest_job_duration":
            shortest_job_duration,

        "company_count":
            company_count,

        "industry_count":
            industry_count,

        "role_count":
            role_count,

        "skill_count":
            skill_count,

        "avg_skill_duration":
            round(
                avg_skill_duration,
                2,
            ),

        "longest_skill_duration":
            longest_skill_duration,

        "avg_endorsements":
            round(
                avg_endorsements,
                2,
            ),

        "high_proficiency_skill_count":
            high_proficiency_skill_count,
    }