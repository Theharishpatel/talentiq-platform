"""
Submission exporter.

Export submission records
to CSV.
"""

from pathlib import Path

import pandas as pd


def export_submission(
    submission: list[dict],
    output_file: str | Path,
) -> Path:
    """
    Export submission records
    to CSV.

    Parameters
    ----------
    submission : list[dict]

    output_file : str | Path

    Returns
    -------
    Path
        Path to exported CSV.
    """

    output_path = Path(
        output_file
    )

    output_path.parent.mkdir(

        parents=True,

        exist_ok=True,

    )

    dataframe = pd.DataFrame(
        submission
    )

    dataframe.to_csv(

        output_path,

        index=False,

    )

    print()

    print("=" * 60)
    print("Submission Export")
    print("=" * 60)

    print(
        f"Rows      : {len(dataframe)}"
    )

    print(
        f"Columns   : {len(dataframe.columns)}"
    )

    print(
        f"Output    : {output_path}"
    )

    print("=" * 60)

    return output_path