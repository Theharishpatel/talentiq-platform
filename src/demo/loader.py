"""
Demo dataset loader.

Loads a small subset of candidates
for the Hugging Face demo.
"""

from pathlib import Path

import pandas as pd


DEMO_DATASET = Path(
    "data/demo_candidates.jsonl"
)


def load_demo_candidates(
    limit: int = 100,
) -> pd.DataFrame:
    """
    Load demo candidates.

    Parameters
    ----------
    limit : int

    Returns
    -------
    pd.DataFrame
    """

    dataframe = pd.read_json(
        DEMO_DATASET,
        lines=True,
    )

    return dataframe.head(
        limit,
    ).copy()