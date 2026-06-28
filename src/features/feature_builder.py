"""
Candidate feature builder.

Runs all feature extraction engines and feature scorers
to produce a single feature dictionary for one candidate.
"""

from src.features.experience.engine import (
    extract_experience_features,
)

from src.features.experience.scorer import (
    score_experience_features,
)

from src.features.behavior.engine import (
    build_behavior_features,
)

from src.features.behavior.scorer import (
    score_behavior_features,
)

from src.features.recruitability.engine import (
    build_recruitability_features,
)

from src.features.recruitability.scorer import (
    score_recruitability_features,
)

from src.features.career.engine import (
    build_growth_features,
)

from src.features.career.scorer import (
    score_growth_features,
)

from src.features.consistency.engine import (
    build_consistency_features,
)

from src.features.consistency.scorer import (
    score_consistency_features,
)

from src.features.honeypot.engine import (
    build_honeypot_features,
)

from src.features.honeypot.scorer import (
    score_honeypot_features,
)



def build_candidate_features(
    candidate: dict,
) -> dict:
    """
    Build all candidate features.

    Parameters
    ----------
    candidate : dict

    Returns
    -------
    dict
    """

    candidate_id = candidate.get(
        "candidate_id"
    )

    # ----- Experience -----

    experience_features = (
        extract_experience_features(
            candidate
        )
    )

    experience_scores = (
        score_experience_features(
            experience_features
        )
    )

    # ----- Behavior ----

    behavior_features = (
        build_behavior_features(

            candidate
        )
    )

    behavior_scores = (
        score_behavior_features(
            behavior_features
        )
    )

    # ----- Recruitability ----

    recruitability_features = (
        build_recruitability_features(
            candidate
        )
    )

    recruitability_scores = (
        score_recruitability_features(
            recruitability_features
        )
    )

    # ----- Career Growth ----

    career_features = (
        build_growth_features(
            candidate
        )
    )

    career_scores = (
        score_growth_features(
           career_features
        )
    )

    # ----- consistency ----

    consistency_features = (
        build_consistency_features(
            candidate
        )
    )

    consistency_scores = (
        score_consistency_features(
           consistency_features
        )
    )

    # ----- honeypot ----

    honeypot_features = (
        build_honeypot_features(
            candidate
        )
    )

    honeypot_scores = (
        score_honeypot_features(
           honeypot_features
        )
    )

    # ----- Merge -----

    features = {

        "candidate_id":
            candidate_id,

        **experience_features,

        **experience_scores,

        **behavior_features,

        **behavior_scores,

        **recruitability_features,

        **recruitability_scores,

        **career_features,

        **career_scores,

        **consistency_features,

        **consistency_scores,

        **honeypot_features,

        **honeypot_scores,

    }

    return features