"""
TalentiQ Demo

Gradio interface for recruiter demo.
"""

from pathlib import Path

import pandas as pd
import gradio as gr

from docx import Document

from src.ranking.jd_embedding.pipeline import (
    build_jd_embedding,
)

from src.demo.search import (
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

from src.submission.exporter import (
    export_submission,
)


# ----- Helpers ------

def load_jd(
    file_path,
):

    document = Document(file_path)

    paragraphs = [

        p.text.strip()

        for p in document.paragraphs

        if p.text.strip()

    ]

    return "\n".join(paragraphs)


# ---- Pipeline -----

def run_pipeline(
    jd_file,
):

    if jd_file is None:

        raise gr.Error(
            "Please upload a JD."
        )

    jd = load_jd(
        jd_file
    )

    embedding = (

        build_jd_embedding(
            jd
        )["embedding"]

    )

    candidates = search_candidates(

        embedding,

        limit=1000,

    )

    ranked = rank_candidates(

        candidates,

        top_k=100,

    )

    ranked = generate_reasons(
        ranked
    )

    submission = build_submission(
        ranked
    )

    Path("outputs").mkdir(
    parents=True,
    exist_ok=True,
)

    output_path = Path(
        "outputs/submission.csv"
    )

    export_submission(

        submission,

        output_path,

    )

    dataframe = pd.DataFrame(
        submission
    )

    return (

        dataframe.head(20),

        str(output_path),

    )


# ----- UI ------

with gr.Blocks(

    title="TalentiQ",

) as demo:

    gr.Markdown(

        """
# 🎯 TalentiQ Hiring Platform

Upload a Job Description (.docx)

The platform will:

- Extract Role Intelligence
- Generate JD Embedding
- Retrieve Candidates
- Rank Top Candidates
- Generate Recruiter Reasoning
- Export submission.csv

"""
    )

    jd = gr.File(

        label="Upload JD",

        file_types=[".docx"],

    )

    run = gr.Button(

        "Run Ranking",

        variant="primary",

    )

    preview = gr.Dataframe(

        label="Top Candidates",

    )

    csv = gr.File(

        label="Download Submission",

    )

    run.click(

        fn=run_pipeline,

        inputs=jd,

        outputs=[

            preview,

            csv,

        ],

    )


demo.launch()