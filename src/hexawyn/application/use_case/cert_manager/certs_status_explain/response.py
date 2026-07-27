from dataclasses import dataclass


@dataclass
class CertsStatusExplainResponse:
    status: str = "unknown"
    message: str | None = None
    explanation: str = ""
    fix_suggestion: str = ""
    error: str | None = None
