from dataclasses import dataclass


@dataclass(frozen=True)
class SemanticLogSearchCommand:
    is_regex: str = ""
    namespace: str = ""
    pattern: str = ""
    time_window_minutes: str = ""
