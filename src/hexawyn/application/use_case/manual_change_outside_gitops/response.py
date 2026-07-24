from dataclasses import dataclass


@dataclass
class ManualChangeOutsideGitopsResponse:
    error: str | None = None
