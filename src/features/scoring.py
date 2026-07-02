"""
Reusable scoring utilities.
"""


def percentile_score(
    value,
    p25,
    p50,
    p75,
    p90,
):
    """
    Convert a value into a percentile-based score.

    Returns:
        25, 50, 75, 90, 100
    """

    if value >= p90:
        return 100

    if value >= p75:
        return 90

    if value >= p50:
        return 75

    if value >= p25:
        return 50

    return 25

def reverse_percentile_score(
        value,
        p25,
        p50,
        p75,
        p90,

):
    """
    Lower value is better.
    """

    if value <= p25:
        return 100
    
    if value <= p50:
        return 90

    if value <= p75:
        return 75

    if value <= p90:
        return 50

    return 25