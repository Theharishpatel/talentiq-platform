from collections import Counter

from src.ingestion.jsonl_reader import read_jsonl

counter = Counter()

for candidate in read_jsonl(
    "data/raw/candidates.jsonl"
):
    
    for skill in candidate.get("skills", []):
        counter[skill.get("name", "")] += 1

report_lines = []

for skill, count in counter.most_common(100):
    line = (f"{skill:<40} {count}")
    print(line)
    report_lines.append(line)

with open(
    "data/reports/profiling/skills_profile.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write("\n".join(report_lines))