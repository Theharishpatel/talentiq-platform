"""
Qdrant point builder.
"""

from typing import Any

from pprint import pprint

import numpy as np

from qdrant_client.models import (
    PointStruct,
)

from src.qdrant.payload import (
    build_payload,
)


def normalize_embedding(
    embedding: Any,
) -> list[float]:
    """
    Normalize embedding into
    list[float].
    """

    if isinstance(
        embedding,
        np.ndarray,
    ):

        return embedding.astype(
            float
        ).tolist()

    if hasattr(
        embedding,
        "tolist",
    ):

        return embedding.tolist()

    return list(
        embedding
    )


def build_point(candidate: dict) -> PointStruct:

    payload = build_payload(candidate)

    # print(type(candidate["embedding"]))

    # for key, value in payload.items():

    #     print(key, type(value))

    point_id = int(
        candidate["candidate_id"].replace(
            "CAND_",
            ""
        )
    )

    return PointStruct(

        id=point_id,

        vector=normalize_embedding(
            candidate["embedding"]
        ),

        payload=payload,

    )