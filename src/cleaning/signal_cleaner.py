from src.cleaning.rules import (
    replace_negative_one,
)

def clean_signals(
        signals: dict,
) -> dict:
    
    if "github_activity_score" in signals:

        signals["github_activity_score"] = (
            replace_negative_one(
                signals["github_activity_score"]
            )
        )

    if "offer_acceptance_rate" in signals:
        signals["offer_acceptance_rate"] = (
            replace_negative_one(
                signals["offer_acceptance_rate"]
            )
        )

    return signals