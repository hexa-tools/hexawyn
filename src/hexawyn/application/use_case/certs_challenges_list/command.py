from dataclasses import dataclass


@dataclass(frozen=True)
class CertsChallengesListCommand:
    namespace: str | None = None
