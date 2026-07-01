"""
Submission validator.

Validate submission records
before CSV export.
"""

from typing import Any

import pandas as pd


REQUIRED_COLUMNS = [

    "candidate_id",

    "rank",

    "score",

    "reasoning",

]


def validate_submission(
    submission: list[dict[str, Any]],
) -> None:
    """
    Validate submission records.

    Parameters
    ----------
    submission : list[dict]

    Raises
    ------
    ValueError
        If validation fails.
    """

    dataframe = pd.DataFrame(
        submission
    )

    print()

    print("=" * 60)
    print("Submission Validation")
    print("=" * 60)

    # --- EMPTY CHECK -----

    if dataframe.empty:

        raise ValueError(
            "Submission is empty."
        )

    print("Submission Empty      : PASSED")

    # ------ REQUIRED COLUMNS ----

    missing = [

        column

        for column in REQUIRED_COLUMNS

        if column not in dataframe.columns

    ]

    if missing:

        raise ValueError(

            f"Missing columns: {missing}"

        )

    print("Required Columns      : PASSED")

    # ---- NULL VALUES -----

    if dataframe.isnull().any().any():

        raise ValueError(

            "Submission contains null values."

        )

    print("Null Values           : PASSED")

    # ---- DUPLICATE CANDIDATES -----

    duplicates = dataframe[
        "candidate_id"
    ].duplicated().sum()

    if duplicates:

        raise ValueError(

            f"Duplicate candidate IDs: {duplicates}"

        )

    print("Duplicate IDs         : PASSED")

    # ------ RANK CHECK ------

    expected_rank = list(

        range(

            1,

            len(dataframe) + 1,

        )

    )

    if dataframe["rank"].tolist() != expected_rank:

        raise ValueError(

            "Ranks are not sequential."

        )

    print("Rank Sequence         : PASSED")

    # ---- SCORE CHECK -----

    scores = dataframe[
        "score"
    ].tolist()

    if scores != sorted(

        scores,

        reverse=True,

    ):

        raise ValueError(

            "Scores are not sorted."

        )

    print("Score Ordering        : PASSED")

    # ---- REASONING CHECK ----

    empty_reasoning = (

        dataframe[
            "reasoning"
        ]

        .astype(str)

        .str.strip()

        == ""

    ).sum()

    if empty_reasoning:

        raise ValueError(

            "Empty reasoning detected."

        )

    print("Reasoning             : PASSED")

    # ------ SUMMARY -----

    print()

    print("=" * 60)

    print("Submission Validation PASSED")

    print("=" * 60)

    print(

        f"Candidates : {len(dataframe)}"

    )

    print(

        f"Columns    : {len(dataframe.columns)}"

    )

    print("=" * 60)