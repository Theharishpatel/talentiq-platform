"""
Candidate metadata extraction.

Extracts searchable metadata from
clean candidate records.

No scoring is performed here.
"""


def build_candidate_metadata(
    candidate: dict,
) -> dict:

    profile = candidate.get(
        "profile",
        {}
    )

    skills = candidate.get(
        "skills",
        []
    )

    languages = candidate.get(
        "languages",
        []
    )

    # ------ Skills -----

    skill_names = []

    for skill in skills:

        name = skill.get(
            "name"
        )

        if name:

            skill_names.append(
                name
            )

    # ------ Languages -----

    language_names = []

    for language in languages:

        name = language.get(
            "language"
        )

        if name:

            language_names.append(
                name
            )

    # ----- Metadata ----

    return {

        "candidate_id":

            candidate.get(
                "candidate_id"
            ),

        "headline":

            profile.get(
                "headline"
            ),

        "current_title":

            profile.get(
                "current_title"
            ),

        "current_company":

            profile.get(
                "current_company"
            ),

        "current_industry":

            profile.get(
                "current_industry"
            ),

        "current_company_size":

            profile.get(
                "current_company_size"
            ),

        "location":

            profile.get(
                "location"
            ),

        "country":

            profile.get(
                "country"
            ),

        "years_experience":

            profile.get(
                "years_of_experience"
            ),

        "skills":

            skill_names,

        "languages":

            language_names,

    }