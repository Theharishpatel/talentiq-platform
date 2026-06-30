"""
Test Role Intelligence Engine.
"""

from pprint import pprint

from src.ranking.role_intelligence.builder import (
    build_role_intelligence,
)


def main():

    jd = """
    We are looking for a Senior Backend Engineer.

    Requirements

    - Python
    - FastAPI
    - PostgreSQL
    - Redis
    - Docker
    - Kubernetes
    - AWS
    - REST APIs
    - Microservices

    Experience:
    5+ years

    Nice to have

    - Kafka
    - gRPC

    Remote
    """

    result = build_role_intelligence(jd)

    print("=" * 60)
    print("ROLE PROFILE")
    print("=" * 60)

    pprint(result)

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    print("Role :", result["role"])
    print("Min Experience :", result["min_experience"])
    print("Skills :", len(result["skills"]))


if __name__ == "__main__":
    main()