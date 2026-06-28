from tqdm import tqdm

from .config import BATCH_SIZE


def generate_embeddings(
    model,
    records,
    writer,
):

    for i in tqdm(

        range(
            0,
            len(records),
            BATCH_SIZE,
        ),

        desc="Embedding",

    ):

        batch = records[
            i:i+BATCH_SIZE
        ]

        texts = [

            item["text"]

            for item in batch

        ]

        vectors = model.encode(

            texts,

            batch_size=BATCH_SIZE,

            normalize_embeddings=True,

            show_progress_bar=False,

        )

        candidate_ids = [

            item["candidate_id"]

            for item in batch

        ]

        writer.write(

            candidate_ids,

            vectors,

        )