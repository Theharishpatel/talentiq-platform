"""
Candidate ranking engine.
"""

from src.ranking.scorer import (
    score_candidate,
)

from src.ranking.weights import (
    TOP_K_RESULTS,
)


def rank_candidates(
    candidates: list[dict],
    top_k: int = TOP_K_RESULTS,
) -> list[dict]:
    """
    Rank candidates using the
    ranking scorer.

    Parameters
    ----------
    candidates : list[dict]

    top_k : int

    Returns
    -------
    list[dict]
    """

    ranked_candidates = []

    # ======================================================
    # SCORE
    # ======================================================

    for candidate in candidates:

        candidate = candidate.copy()

        score = score_candidate(
            candidate
        )

        candidate[
            "final_score"
        ] = score[
            "final_score"
        ]

        candidate[
            "score_breakdown"
        ] = score[
            "score_breakdown"
        ]

        ranked_candidates.append(
            candidate
        )

    # ======================================================
    # SORT
    # ======================================================

    ranked_candidates.sort(

        key=lambda candidate: (
            -round(candidate["final_score"],2),

            candidate["payload"]["candidate_id"],
        )

    )

    # ======================================================
    # ASSIGN RANK
    # ======================================================

    for rank, candidate in enumerate(

        ranked_candidates,

        start=1,

    ):

        candidate[
            "rank"
        ] = rank

    # ======================================================
    # RETURN
    # ======================================================

    return ranked_candidates[
        :top_k
    ]