from collections import defaultdict

import re

from src.ingestion.jsonl_reader import read_jsonl


def canonical(value: str) -> str:
    """
    Normalize text for duplicate detection.
    """

    if not value:
        return ""

    value = value.lower()

    value = re.sub(
        r"[^a-z0-9]",
        "",
        value
    )

    return value


skill_groups = defaultdict(set)
title_groups = defaultdict(set)
company_groups = defaultdict(set)
location_groups = defaultdict(set)
degree_groups = defaultdict(set)
field_groups = defaultdict(set)

print("Scanning dataset...")


for candidate in read_jsonl(
    "data/raw/candidates.jsonl"
):

    # ------------------
    # Skills
    # ------------------

    for skill in candidate.get(
        "skills",
        []
    ):

        name = skill.get("name")

        if name:

            skill_groups[
                canonical(name)
            ].add(name)

    # ------------------
    # Profile
    # ------------------

    profile = candidate.get(
        "profile",
        {}
    )

    title = profile.get(
        "current_title"
    )

    if title:

        title_groups[
            canonical(title)
        ].add(title)

    company = profile.get(
        "current_company"
    )

    if company:

        company_groups[
            canonical(company)
        ].add(company)

    location = profile.get(
        "location"
    )

    if location:

        location_groups[
            canonical(location)
        ].add(location)

    # ------------------
    # Education
    # ------------------

    for edu in candidate.get(
        "education",
        []
    ):

        degree = edu.get(
            "degree"
        )

        if degree:

            degree_groups[
                canonical(degree)
            ].add(degree)

        field = edu.get(
            "field_of_study"
        )

        if field:

            field_groups[
                canonical(field)
            ].add(field)


report = []


def write_section(
    title,
    groups
):

    report.append(
        "\n" + "=" * 60
    )

    report.append(title)

    report.append(
        "=" * 60
    )

    found = 0

    for key, values in sorted(
        groups.items()
    ):

        if len(values) > 1:

            found += 1

            report.append(
                f"\n{key}"
            )

            for value in sorted(values):

                report.append(
                    f"  - {value}"
                )

    if found == 0:

        report.append(
            "\nNo normalization candidates found."
        )


write_section(
    "SKILL DUPLICATES",
    skill_groups
)

write_section(
    "TITLE DUPLICATES",
    title_groups
)

write_section(
    "COMPANY DUPLICATES",
    company_groups
)

write_section(
    "LOCATION DUPLICATES",
    location_groups
)

write_section(
    "DEGREE DUPLICATES",
    degree_groups
)

write_section(
    "FIELD DUPLICATES",
    field_groups
)

report_text = "\n".join(
    report
)

print(report_text)

with open(
    "data/reports/profiling/normalization_candidates.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        report_text
    )

print(
    "\nSaved:"
    " data/reports/profiling/normalization_candidates.txt"
)