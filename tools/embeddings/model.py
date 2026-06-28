from sentence_transformers import SentenceTransformer

from .config import (
    MODEL_NAME,
    DEVICE,
)

def load_embedding_model():

    print("=" * 60)
    print("loading embedding model...")
    print("=" * 60)

    model = SentenceTransformer(
        MODEL_NAME,
        device=DEVICE,
    )

    print("model loaded \n")

    return model