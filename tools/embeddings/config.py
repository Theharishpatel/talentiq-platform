from pathlib import Path

INPUT_FILE = Path("data/processed/candidate_text.jsonl")

OUTPUT_FILE = Path(
    "data/processed/candidate_embeddings.parquet"
)

MODEL_NAME = "BAAI/bge-base-en-v1.5"

DEVICE = "cuda"

BATCH_SIZE = 256

COMPRESSION = "snappy"