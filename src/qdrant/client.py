"""
Qdrant client.

Creates and returns a reusable
Qdrant client instance.
"""

from dotenv import load_dotenv

import os

from qdrant_client import QdrantClient


# ==========================================================
# LOAD ENVIRONMENT
# ==========================================================

load_dotenv()


# ==========================================================
# CONFIG
# ==========================================================

QDRANT_URL = os.getenv(
    "QDRANT_URL"
)

QDRANT_API_KEY = os.getenv(
    "QDRANT_API_KEY"
)


# ==========================================================
# CLIENT
# ==========================================================

_client = None


def get_qdrant_client() -> QdrantClient:
    """
    Return singleton Qdrant client.
    """

    global _client

    if _client is None:

        if not QDRANT_URL:

            raise ValueError(
                "Missing QDRANT_URL."
            )

        if not QDRANT_API_KEY:

            raise ValueError(
                "Missing QDRANT_API_KEY."
            )

        _client = QdrantClient(

            url=QDRANT_URL,

            api_key=QDRANT_API_KEY,

            timeout=300,

        )

    return _client