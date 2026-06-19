import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.common.logging import get_logger

logger = get_logger(__name__)

logger.info("TalentIQ logger working")
