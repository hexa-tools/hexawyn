SEVERITY_ORDER: dict[str, int] = {"critical": 3, "high": 2, "medium": 1, "info": 0}

_SEVERITY_KEYWORDS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("critical", ("panic", "fatal", "oomkilled", "segmentation fault")),
    ("high", ("error",)),
    ("medium", ("warn",)),
)


def classify_event_severity(line: str) -> str:
    """Deterministic severity classifier for a single log line."""
    lower = line.lower()
    for severity, keywords in _SEVERITY_KEYWORDS:
        if any(keyword in lower for keyword in keywords):
            return severity
    return "info"
