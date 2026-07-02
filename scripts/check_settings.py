import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.config.settings import (
    DATA_DIR,
    FEATURES_DATA_DIR,
    PROCESSED_DATA_DIR,
    RAW_DATA_DIR,
)

print(DATA_DIR)
print(RAW_DATA_DIR)
print(PROCESSED_DATA_DIR)
print(FEATURES_DATA_DIR)
