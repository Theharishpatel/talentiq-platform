from statistics import mean, median

from src.ingestion.jsonl_reader import read_jsonl

notice_periods = []

salary_mins = []
salary_maxs = []
salary_midpoints = []

salary_per_year_exp = []

open_to_work_true = 0
open_to_work_false = 0

verified_email_true = 0
verified_email_false = 0

verified_phone_true = 0
verified_phone_false = 0

linkedin_true = 0
linkedin_false = 0

relocate_true = 0
relocate_false = 0

work_mode_counts = {}


def percentile(values, p):

    values = sorted(values)

    index = int(
        (len(values) - 1) * p
    )

    return values[index]


for candidate in read_jsonl(
    "data/processed/clean_candidates.jsonl"
):

    profile = candidate.get(
        "profile",
        {}
    )

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    # --------------------
    # Availability
    # --------------------

    if signals.get(
        "open_to_work_flag"
    ):
        open_to_work_true += 1
    else:
        open_to_work_false += 1

    notice = signals.get(
        "notice_period_days"
    )

    if notice is not None:
        notice_periods.append(
            notice
        )

    # --------------------
    # Verification
    # --------------------

    if signals.get(
        "verified_email"
    ):
        verified_email_true += 1
    else:
        verified_email_false += 1

    if signals.get(
        "verified_phone"
    ):
        verified_phone_true += 1
    else:
        verified_phone_false += 1

    if signals.get(
        "linkedin_connected"
    ):
        linkedin_true += 1
    else:
        linkedin_false += 1

    # --------------------
    # Mobility
    # --------------------

    if signals.get(
        "willing_to_relocate"
    ):
        relocate_true += 1
    else:
        relocate_false += 1

    mode = signals.get(
        "preferred_work_mode"
    )

    if mode:
        work_mode_counts[mode] = (
            work_mode_counts.get(
                mode,
                0
            ) + 1
        )

    # --------------------
    # Salary
    # --------------------

    salary = signals.get(
        "expected_salary_range_inr_lpa",
        {}
    )

    salary_min = salary.get(
        "min"
    )

    salary_max = salary.get(
        "max"
    )

    if (
        salary_min is not None
        and salary_max is not None
    ):

        salary_mins.append(
            salary_min
        )

        salary_maxs.append(
            salary_max
        )

        midpoint = (
            salary_min
            + salary_max
        ) / 2

        salary_midpoints.append(
            midpoint
        )

        years_exp = profile.get(
            "years_of_experience",
            0
        )

        if years_exp > 0:

            ratio = (
                midpoint
                / years_exp
            )

            salary_per_year_exp.append(
                ratio
            )


def numeric_section(
    name,
    values
):

    return f"""
============================================================
{name}
============================================================

count   : {len(values)}
min     : {min(values)}
max     : {max(values)}
avg     : {mean(values):.2f}
median  : {median(values):.2f}

p25     : {percentile(values, 0.25)}
p50     : {percentile(values, 0.50)}
p75     : {percentile(values, 0.75)}
p90     : {percentile(values, 0.90)}
"""


report = ""

report += numeric_section(
    "NOTICE PERIOD",
    notice_periods
)

report += numeric_section(
    "SALARY MIN",
    salary_mins
)

report += numeric_section(
    "SALARY MAX",
    salary_maxs
)

report += numeric_section(
    "SALARY MIDPOINT",
    salary_midpoints
)

report += numeric_section(
    "SALARY PER YEAR EXPERIENCE",
    salary_per_year_exp
)

report += f"""

============================================================
OPEN TO WORK
============================================================

True    : {open_to_work_true}
False   : {open_to_work_false}

============================================================
VERIFIED EMAIL
============================================================

True    : {verified_email_true}
False   : {verified_email_false}

============================================================
VERIFIED PHONE
============================================================

True    : {verified_phone_true}
False   : {verified_phone_false}

============================================================
LINKEDIN CONNECTED
============================================================

True    : {linkedin_true}
False   : {linkedin_false}

============================================================
WILLING TO RELOCATE
============================================================

True    : {relocate_true}
False   : {relocate_false}

============================================================
WORK MODES
============================================================
"""

for mode, count in sorted(
    work_mode_counts.items(),
    key=lambda x: x[1],
    reverse=True,
):
    report += (
        f"\n{mode:<15} {count}"
    )

print(report)

with open(
    "data/reports/profiling/recruitability_metrics_profile.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(report)

print(
    "\nSaved: data/reports/profiling/"
    "recruitability_metrics_profile.txt"
)