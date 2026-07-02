from collections import Counter

from src.ingestion.jsonl_reader import read_jsonl

counter = Counter()

for candidate in read_jsonl(
    "data/raw/candidates.jsonl"
):
    
   profile = candidate.get("profile", {})

   location = profile.get(
      "location",
      ""
   )

   counter[location] += 1

report_lines = []

for location, count in counter.most_common(100):
    line = f"{location:<40} {count}"
    print(line)
    report_lines.append(line)

with open(
    "data/reports/profiling/locations_profile.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write("\n".join(report_lines))