from collections import Counter

from src.ingestion.jsonl_reader import read_jsonl

counter = Counter()

for candidate in read_jsonl(
    "data/raw/candidates.jsonl"
):
    
   for edu in candidate.get(
      "education",
      []
   ):
      counter[
      edu.get("degree", "")
   ] += 1

for degree, count in counter.most_common(50):
   print(f"{degree:<40} {count}")