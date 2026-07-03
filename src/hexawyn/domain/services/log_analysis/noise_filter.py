import re

_NOISE_PATTERNS = (
    re.compile(r"GET\s+/health(z)?\b", re.IGNORECASE),
    re.compile(r"GET\s+/ready(z)?\b", re.IGNORECASE),
    re.compile(r"GET\s+/live(z)?\b", re.IGNORECASE),
    re.compile(r"readiness probe (succeeded|passed)", re.IGNORECASE),
    re.compile(r"liveness probe (succeeded|passed)", re.IGNORECASE),
    re.compile(r"health ?check", re.IGNORECASE),
)


def is_noise(line: str) -> bool:
    """Deterministic classifier for health-check/informational noise lines."""
    return any(pattern.search(line) for pattern in _NOISE_PATTERNS)
