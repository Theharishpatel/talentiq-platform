"""
Ranking weight configuration.

All ranking weights are centralized here
to make tuning easy.
"""

# ==========================================================
# POSITIVE WEIGHTS
# ==========================================================

SIMILARITY_WEIGHT = 0.35

EXPERIENCE_WEIGHT = 0.20

RECRUITABILITY_WEIGHT = 0.15

GROWTH_WEIGHT = 0.10

BEHAVIOR_WEIGHT = 0.10

CONSISTENCY_WEIGHT = 0.10


# ==========================================================
# NEGATIVE WEIGHTS
# ==========================================================

RISK_WEIGHT = 0.10


# ==========================================================
# OUTPUT
# ==========================================================

TOP_K_RESULTS = 100