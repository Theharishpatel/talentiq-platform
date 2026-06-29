import orjson

from .config import INPUT_FILE

def load_candidate_texts():

    records = []

    with open(INPUT_FILE, "rb") as f:

        for line in f:

            records.append(
                orjson.loads(line)
            )

        print(f"Candidates: {len(records)}\n")

        return records