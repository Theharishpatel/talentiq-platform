"""
JD Text Builder.

Converts a structured Job Description into
a deterministic text representation for
embedding generation.
"""


def build_jd_text(
    role_profile: dict,
) -> str:
    """
    Build embedding text from a structured JD.

    Parameters
    ----------
    role_profile : dict

    Returns
    -------
    str
    """

    lines = []

    # ----- Role ------

    role = role_profile.get("role")

    if role:

        lines.append(f"Role: {role}")

    # ----- Experience -----

    experience = role_profile.get(
        "min_experience"
    )

    if experience is not None:

        lines.append(
            f"Minimum Experience: {experience} years"
        )

    # ----- Skills -----

    skills = role_profile.get(
        "skills",
        [],
    )

    if skills:

        lines.append("Required Skills:")

        for skill in sorted(skills):

            lines.append(skill)

    # ------ Work Mode ------

    work_mode = role_profile.get(
        "work_mode"
    )

    if work_mode:

        lines.append(
            f"Work Mode: {work_mode}"
        )

    # ----- Employment Type ------

    employment_type = role_profile.get(
        "employment_type"
    )

    if employment_type:

        lines.append(
            f"Employment Type: {employment_type}"
        )

    #----- Location -----

    location = role_profile.get(
        "location"
    )

    if location:

        lines.append(
            f"Location: {location}"
        )

    return "\n".join(lines)