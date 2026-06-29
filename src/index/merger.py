"""
Candidate index merger.

Combines metadata, engineered features,
and embedding into a single index row.

No file I/O is performed here.
"""


def merge_candidate_index(

    metadata: dict,

    features: dict,

    embedding: list[float],

) -> dict:
    """
    Merge candidate metadata, features
    and embedding into one index record.

    Parameters
    ----------
    metadata : dict

    features : dict

    embedding : list[float]

    Returns
    -------
    dict
    """

    # ----- Safety Checks ----

    if metadata["candidate_id"] != features["candidate_id"]:

        raise ValueError(

            "Candidate ID mismatch between metadata and features."

        )

    # ---- Merge ------

    index_record = {

        **metadata,

        **features,

        "embedding": embedding,

    }

    return index_record