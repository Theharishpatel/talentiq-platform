"""
Candidate index builder.

Builds merged candidate index rows from

- metadata
- engineered features
- embeddings

No file writing is performed here.
"""

from src.index.metadata import (
    build_candidate_metadata,
)

from src.index.merger import (
    merge_candidate_index,
)


def build_candidate_index(

    candidates: list[dict],

    feature_lookup: dict,

    embedding_lookup: dict,

) -> list[dict]:
    """
    Build merged candidate index.

    Parameters
    ----------
    candidates

    feature_lookup

    embedding_lookup

    Returns
    -------
    list[dict]
    """

    index_rows = []

    for candidate in candidates:

        candidate_id = candidate.get(
            "candidate_id"
        )

        # ------ Validate ----

        if candidate_id not in feature_lookup:

            raise KeyError(

                f"Missing features for {candidate_id}"

            )

        if candidate_id not in embedding_lookup:

            raise KeyError(

                f"Missing embedding for {candidate_id}"

            )

        # ----- Build Metadata -----

        metadata = build_candidate_metadata(
            candidate
        )

        # ----- Get Features ----

        features = feature_lookup[
            candidate_id
        ]

        # ------ Get Embedding ----

        embedding = embedding_lookup[
            candidate_id
        ]

        # ----- Validate Embedding -----

        if len(embedding) != 768:

            raise ValueError(

                f"Invalid embedding size for {candidate_id}"

            )

        # ----- Merge -----

        row = merge_candidate_index(

            metadata=metadata,

            features=features,

            embedding=embedding,

        )

        index_rows.append(
            row
        )

    return index_rows