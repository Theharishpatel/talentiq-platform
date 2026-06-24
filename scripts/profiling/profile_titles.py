from collections import Counter

from src.ingestion.jsonl_reader import read_jsonl

counter = Counter()

for candidate in read_jsonl(
    "data/raw/candidates.jsonl"
):
    
   profile = candidate.get("profile", {})

   title = profile.get(
      "current_title",
      ""
   )

   counter[title] += 1

report_lines = []

for title, count in counter.most_common(100):
    line = f"{title:<40} {count}"
    print(line)
    report_lines.append(line)

with open(
    "data/reports/profiling/titles_profile.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write("\n".join(report_lines))