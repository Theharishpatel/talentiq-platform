"""
Generate Role Intelligence metadata.

Input
-----
data/processed/clean_candidates.jsonl

Output
------
src/ranking/role_intelligence/generated_metadata.py
"""

from pathlib import Path
from collections import Counter, defaultdict
from pprint import pformat

import orjson


# ==========================================================
# CONFIG
# ==========================================================

INPUT_FILE = Path(
    "data/processed/clean_candidates.jsonl"
)

OUTPUT_FILE = Path(
    "src/ranking/role_intelligence/generated_metadata.py"
)


# ==========================================================
# STORAGE
# ==========================================================

role_counter = Counter()

skill_counter = Counter()

role_to_skills = defaultdict(Counter)


# ==========================================================
# READ DATA
# ==========================================================

print("=" * 60)
print("Scanning candidates...")
print("=" * 60)

with open(INPUT_FILE, "rb") as f:

    for line in f:

        candidate = orjson.loads(line)

        profile = candidate.get(
            "profile",
            {}
        )

        role = profile.get(
            "current_title"
        )

        if not role:

            role = profile.get(
                "headline",
                ""
            ).split("|")[0].strip()

        if not role:

            continue

        role_counter[role] += 1

        skills = candidate.get(
            "skills",
            []
        )

        for skill in skills:

            name = skill.get(
                "name"
            )

            if not name:

                continue

            skill_counter[name] += 1

            role_to_skills[role][name] += 1


# ==========================================================
# BUILD METADATA
# ==========================================================

role_metadata = {}

for role in sorted(role_counter):

    top_skills = [

        skill

        for skill, _ in

        role_to_skills[role].most_common(15)

    ]

    role_metadata[role] = {

        "candidate_count":
            role_counter[role],

        "core_skills":
            top_skills,

    }


all_roles = sorted(
    role_metadata.keys()
)

all_skills = [

    skill

    for skill, _ in

    skill_counter.most_common()

]


# ==========================================================
# WRITE PYTHON FILE
# ==========================================================

print("Writing metadata...")

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8",
) as f:

    f.write(
        '"""\n'
    )

    f.write(
        "AUTO GENERATED FILE.\n"
    )

    f.write(
        "DO NOT EDIT MANUALLY.\n"
    )

    f.write(
        '"""\n\n'
    )

    f.write(
        "ROLE_METADATA = "
    )

    f.write(

        pformat(

            role_metadata,

            width=120,

            sort_dicts=True,

        )

    )

    f.write("\n\n")

    f.write(
        "ALL_ROLES = "
    )

    f.write(

        pformat(

            all_roles,

            width=120,

        )

    )

    f.write("\n\n")

    f.write(
        "ALL_SKILLS = "
    )

    f.write(

        pformat(

            all_skills,

            width=120,

        )

    )

    f.write("\n")


print()
print("=" * 60)
print("Metadata Generated")
print("=" * 60)

print(f"Roles  : {len(all_roles)}")
print(f"Skills : {len(all_skills)}")

print(f"Saved  : {OUTPUT_FILE}")