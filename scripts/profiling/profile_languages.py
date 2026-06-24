from collections import Counter

from src.ingestion.jsonl_reader import read_jsonl

counter = Counter()

for candidate in read_jsonl(
    "data/raw/candidates.jsonl"
):
   for lang in candidate.get(
      "languages",
      []
   ):
      counter[
         lang.get(
            "language",
            ""
         )
      ] += 1

for lang, count in counter.most_common(50):
   print(f"{lang:<40} {count}")