"""
End-to-end TalentiQ pipeline.

Usage
-----
python -m tools.run_pipeline <jd_file>
"""

import sys
import time
from pathlib import Path

from docx import Document

from src.ranking.jd_embedding.pipeline import (
    build_jd_embedding,
)

from src.retrieval.search import (
    search_candidates,
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


# ------ HELPERS ------

def load_jd(
    jd_path: str | Path,
) -> str:
    """
    Read JD from DOCX.
    """

    document = Document(
        jd_path
    )

    paragraphs = [

        paragraph.text.strip()

        for paragraph in document.paragraphs

        if paragraph.text.strip()

    ]

    return "\n".join(
        paragraphs
    )


# ----- MAIN -----

def main() -> None:

    start_time = time.time()

    if len(sys.argv) != 2:

        print()

        print(
            "Usage:"
        )

        print(
            "python -m tools.run_pipeline <jd.docx>"
        )

        sys.exit(1)

    jd_file = Path(
        sys.argv[1]
    )

    if not jd_file.exists():

        raise FileNotFoundError(
            jd_file
        )

    print()

    print("=" * 60)
    print("TalentiQ Hiring Pipeline")
    print("=" * 60)

    # ---- LOAD JD -----

    print()

    print("Loading JD...")

    jd = load_jd(
        jd_file
    )

    print("Done")

    # ----- JD EMBEDDING -----

    print()

    print(
        "Generating JD Embedding..."
    )

    embedding_result = (

        build_jd_embedding(
            jd
        )

    )

    embedding = embedding_result[
        "embedding"
    ]

    print("Done")

    # ----- SEARCH -----

    print()

    print(
        "Searching Candidates..."
    )

    candidates = search_candidates(

        embedding=embedding,

        limit=1000,

    )

    print(
        f"Retrieved : {len(candidates)}"
    )

    # ----- RANKING -----

    print()

    print(
        "Ranking Candidates..."
    )

    ranked = rank_candidates(
        candidates
    )

    print(
        f"Top Ranked : {len(ranked)}"
    )

    # ----- REASONING -----

    print()

    print(
        "Generating Reasons..."
    )

    reasoned = generate_reasons(
        ranked
    )

    # ---- SUBMISSION ----

    print()

    print(
        "Building Submission..."
    )

    submission = build_submission(
        reasoned
    )

    # ------ VALIDATION ----

    print()

    validate_submission(
        submission
    )

    # ---- EXPORT ----

    output_path = Path(
        "outputs/submission.csv"
    )

    export_submission(

        submission,

        output_path,

    )

    elapsed = time.time() - start_time

    print()

    print("=" * 60)
    print("Pipeline Completed")
    print("=" * 60)

    print(
        f"JD : {jd_file.name}"
    )

    print(
        f"Candidates Retrieved : {len(candidates)}"
    )

    print(
        f"Candidates Ranked : {len(ranked)}"
    )

    print(
        f"Submission Rows : {len(submission)}"
    )

    print(
        f"Output : {output_path}"
    )

    print(
        f"Time : {elapsed:.2f} seconds"
    )

    print("=" * 60)


if __name__ == "__main__":

    main()