"""
Memory efficient JSONL reader.
Supports 100K+ candidates without loading entire file into memory
"""

import json
from pathlib import Path
from typing import Generator

def read_jsonl(
    file_path: str
) -> Generator[dict, None, None]:
    """
    Read JSONL file line by line
    Parameters
    ----------
    file_path : str

    Yields
    ------
    dict
    """

    file_path = Path(file_path)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:
        
        for line in file:

            yield json.loads(line)
