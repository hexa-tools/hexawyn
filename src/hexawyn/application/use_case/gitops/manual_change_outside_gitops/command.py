from dataclasses import dataclass


@dataclass(frozen=True)
class ManualChangeOutsideGitopsCommand:
    namespace: str = ""
    window_days: int = 7
