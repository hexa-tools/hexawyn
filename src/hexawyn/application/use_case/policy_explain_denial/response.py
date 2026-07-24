from dataclasses import dataclass


@dataclass
class PolicyExplainDenialResponse:
    explanation: str = ""
    error: str | None = None
