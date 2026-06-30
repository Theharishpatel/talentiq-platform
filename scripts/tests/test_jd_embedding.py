"""
Test JD Embedding Pipeline.
"""

from pprint import pprint

import numpy as np

from src.ranking.jd_embedding.pipeline import (
    build_jd_embedding,
)


from src.utils.document_loader import (
    load_document,
)

JD = load_document(
    "data/raw/job_description.docx"
)


def main() -> None:

    result = build_jd_embedding(
        JD
    )

    print("=" * 60)
    print("ROLE PROFILE")
    print("=" * 60)

    pprint(
        result["role_profile"]
    )

    print()

    print("=" * 60)
    print("EMBEDDING TEXT")
    print("=" * 60)

    print(
        result["embedding_text"]
    )

    embedding = result[
        "embedding"
    ]

    print()

    print("=" * 60)
    print("EMBEDDING INFO")
    print("=" * 60)

    print(
        "Shape :",
        embedding.shape,
    )

    print(
        "Dtype :",
        embedding.dtype,
    )

    print(
        "Norm :",
        round(
            np.linalg.norm(
                embedding
            ),
            6,
        ),
    )

    print()

    print(
        "First 10 Values"
    )

    print(
        embedding[:10]
    )

    print()

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    print(
        "Role :",
        result["role_profile"]["role"],
    )

    print(
        "Experience :",
        result["role_profile"]["min_experience"],
    )

    print(
        "Skills :",
        len(
            result["role_profile"]["skills"]
        ),
    )

    print(
        "Embedding Dimension :",
        len(
            embedding
        ),
    )


if __name__ == "__main__":

    main()