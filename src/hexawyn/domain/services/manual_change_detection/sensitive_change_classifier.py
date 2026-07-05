from __future__ import annotations

from collections.abc import Sequence

from hexawyn.domain.models.manual_change import ManualChangeSeverity


def classify_severity(
    kind: str, name: str, sensitive_keywords: Sequence[str]
) -> ManualChangeSeverity:
    if kind == "Secret":
        return "critical"
    lowered_name = name.lower()
    if any(keyword in lowered_name for keyword in sensitive_keywords):
        return "critical"
    return "warning"
