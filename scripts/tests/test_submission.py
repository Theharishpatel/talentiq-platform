"""
Integration test for the
submission engine.
"""

from pathlib import Path

import pandas as pd

from src.config.settings import (
    CANDIDATE_INDEX_FILE,
)

from src.ranking.engine import (
    rank_candidates,
)

from src.reasoning.engine import (
    generate_reasons,
)

from src.submission.generator import (
    build_submission,
)

from src.submission.validator import (
    validate_submission,
)

from src.submission.exporter import (
    export_submission,
)


# ==========================================================
# LOAD SAMPLE CANDIDATES
# ==========================================================

print()

print("=" * 60)
print("Loading Candidate Index")
print("=" * 60)

df = pd.read_parquet(
    CANDIDATE_INDEX_FILE
)

print(f"Candidates : {len(df)}")

print()

# ==========================================================
# BUILD SEARCH RESULTS
# ==========================================================

print("=" * 60)
print("Building Search Results")
print("=" * 60)

search_results = []

for candidate in df.head(20).to_dict(
    orient="records",
):

    search_results.append(

        {

            "payload": candidate,

            # Mock semantic similarity

            "similarity_score": 0.90,

        }

    )

print(
    f"Search Results : {len(search_results)}"
)

print()

# ==========================================================
# RANK
# ==========================================================

print("=" * 60)
print("Ranking Candidates")
print("=" * 60)

ranked = rank_candidates(
    search_results
)

print(
    f"Ranked : {len(ranked)}"
)

print()

# ==========================================================
# GENERATE REASONING
# ==========================================================

print("=" * 60)
print("Generating Reasons")
print("=" * 60)

reasoned = generate_reasons(
    ranked
)

print(
    f"Reasoned : {len(reasoned)}"
)

print()

# ==========================================================
# BUILD SUBMISSION
# ==========================================================

print("=" * 60)
print("Building Submission")
print("=" * 60)

submission = build_submission(
    reasoned
)

print(
    f"Submission Rows : {len(submission)}"
)

print()

# ==========================================================
# VALIDATE
# ==========================================================

validate_submission(
    submission
)

print()

# ==========================================================
# EXPORT
# ==========================================================

output_file = Path(
    "outputs/submission.csv"
)

export_submission(

    submission,

    output_file,

)

print()

# ==========================================================
# PREVIEW
# ==========================================================

print("=" * 60)
print("Submission Preview")
print("=" * 60)

preview = pd.DataFrame(
    submission
)

print(
    preview.head(10)
)

print()

print("=" * 60)
print("Submission Integration Test : PASSED")
print("=" * 60)