

"""
Upload candidates to Qdrant.
"""

import time
from math import ceil

from tqdm import tqdm
from qdrant_client.models import PointStruct

from src.config.settings import (
    QDRANT_COLLECTION,
)

from src.qdrant.client import (
    get_qdrant_client,
)

from src.qdrant.point import (
    build_point,
)


# ==========================================================
# CONFIG
# ==========================================================

BATCH_SIZE = 100

MAX_RETRIES = 5

BASE_RETRY_DELAY = 3


# ==========================================================
# HELPERS
# ==========================================================

def get_uploaded_count() -> int:
    """
    Return current number of uploaded
    points inside the collection.
    """

    client = get_qdrant_client()

    info = client.get_collection(
        collection_name=QDRANT_COLLECTION,
    )

    data = info.model_dump()

    return data.get(
        "points_count",
        0,
    ) or 0


# ==========================================================
# UPLOAD
# ==========================================================

def upload_candidates(
    dataframe,
    batch_size: int = BATCH_SIZE,
) -> None:
    """
    Upload candidates into Qdrant.
    Automatically resumes upload
    if collection already contains
    vectors.
    """

    client = get_qdrant_client()

    total = len(dataframe)

    uploaded_count = get_uploaded_count()

    if uploaded_count >= total:

        print()

        print("=" * 60)
        print("All candidates already uploaded.")
        print("=" * 60)

        return

    remaining = total - uploaded_count

    total_batches = ceil(
        remaining / batch_size
    )

    print()

    print("=" * 60)
    print("Qdrant Upload Started")
    print("=" * 60)

    print(f"Total Candidates : {total}")
    print(f"Already Uploaded : {uploaded_count}")
    print(f"Remaining         : {remaining}")
    print(f"Batch Size        : {batch_size}")

    print("=" * 60)
    print()

    start_time = time.time()

    progress = tqdm(

        range(
            uploaded_count,
            total,
            batch_size,
        ),

        total=total_batches,

        desc="Uploading",

    )

    for start in progress:

        batch = dataframe.iloc[
            start:start + batch_size
        ]

        points: list[PointStruct] = [

            build_point(candidate)

            for candidate in batch.to_dict(
                orient="records"
            )

        ]

        success = False

        for attempt in range(MAX_RETRIES):

            try:

                client.upsert(

                    collection_name=QDRANT_COLLECTION,

                    wait=True,

                    points=points,

                )

                success = True

                break

            except Exception as e:

                delay = BASE_RETRY_DELAY * (
                    2 ** attempt
                )

                print()

                print(
                    f"[Retry {attempt+1}/{MAX_RETRIES}] "
                    f"Batch starting at {start}"
                )

                print(
                    f"Waiting {delay} seconds..."
                )

                if attempt == MAX_RETRIES - 1:

                    print()

                    print("=" * 60)
                    print("UPLOAD FAILED")
                    print("=" * 60)

                    print(
                        f"Failed Batch : {start}"
                    )

                    print(
                        f"Uploaded Till : {start}"
                    )

                    raise e

                time.sleep(delay)

        if success:

            progress.set_postfix(

                uploaded=start + len(batch)

            )

    elapsed = time.time() - start_time

    print()

    print("=" * 60)
    print("Upload Completed")
    print("=" * 60)

    print(f"Candidates : {total}")

    print(
        f"Time : {elapsed/60:.2f} minutes"
    )

    print("=" * 60)