from dataclasses import dataclass


@dataclass(frozen=True)
class AnalyzePodLogsCommand:
    namespace: str | None = None
