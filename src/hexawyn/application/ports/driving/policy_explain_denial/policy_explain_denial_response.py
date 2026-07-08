from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PolicyExplainDenialResponse:
    policy_name: str = ""
    rule_name: str = ""
    raw_message: str = ""
    human_explanation: str = ""
    fix_suggestion: str = ""
    error: str | None = None
