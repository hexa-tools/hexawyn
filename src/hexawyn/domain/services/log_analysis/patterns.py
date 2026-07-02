import re

from hexawyn.domain.models.analyze_pod_logs import (
    ConnectionIssue,
    ConnectionIssueCategory,
    PodLogLine,
)

_TIMEOUT_PATTERNS = (
    re.compile(r"connection timeout", re.IGNORECASE),
    re.compile(r"timed out connecting", re.IGNORECASE),
    re.compile(r"i/o timeout", re.IGNORECASE),
)
_REFUSED_PATTERNS = (
    re.compile(r"connection refused", re.IGNORECASE),
    re.compile(r"upstream connect error", re.IGNORECASE),
    re.compile(r"dial tcp.*refused", re.IGNORECASE),
)
_CONFIDENCE_BASE = 0.5
_CONFIDENCE_STEP = 0.05


def categorize_connection_issues(
    lines: list[PodLogLine],
) -> tuple[list[ConnectionIssue], list[ConnectionIssue]]:
    """Extract and separately categorize connection-timeout vs connection-refused lines."""
    timeout_counts: dict[str, int] = {}
    refused_counts: dict[str, int] = {}

    for line in lines:
        if _matches_any(line.message, _TIMEOUT_PATTERNS):
            timeout_counts[line.message] = timeout_counts.get(line.message, 0) + 1
        elif _matches_any(line.message, _REFUSED_PATTERNS):
            refused_counts[line.message] = refused_counts.get(line.message, 0) + 1

    timeouts = _build_issues("connection_timeout", timeout_counts)
    refused = _build_issues("connection_refused", refused_counts)
    return timeouts, refused


def _matches_any(message: str, patterns: tuple[re.Pattern[str], ...]) -> bool:
    return any(pattern.search(message) for pattern in patterns)


def _build_issues(
    category: ConnectionIssueCategory, counts: dict[str, int]
) -> list[ConnectionIssue]:
    return [
        ConnectionIssue(
            category=category,
            message_sample=message,
            count=count,
            confidence=_confidence(count),
        )
        for message, count in counts.items()
    ]


def _confidence(count: int) -> float:
    return min(1.0, _CONFIDENCE_BASE + _CONFIDENCE_STEP * count)
