from collections import Counter

from src.ingestion.jsonl_reader import read_jsonl

missing = Counter()

for candidate in read_jsonl(
    "data/raw/candidates.jsonl"
):
    
   profile = candidate.get("profile", {})

   if not profile.get("headline"):
      missing["headline"] += 1

   if not profile.get("summary"):
      missing["summary"] += 1

   if not profile.get("education"):
      missing["education"] += 1

   if not profile.get("skills"):
      missing["skills"] += 1

   if not profile.get("career_history"):
      missing["career_history"] += 1

for field, count in missing.items():
   print(f"{field:<30} {count}")