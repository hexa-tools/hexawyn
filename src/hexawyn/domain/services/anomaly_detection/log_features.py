import re

_LATENCY_PATTERN = re.compile(r"(\d+(?:\.\d+)?)\s*(ms|s)\b", re.IGNORECASE)
_DIGIT_PATTERN = re.compile(r"\d")


def extract_log_features(line: str) -> list[float]:
    """Pure numeric feature vector for a single log line.

    No NLP/embeddings — length, digit density, latency (normalized to ms),
    and word count are enough signal for IsolationForest to isolate
    lines whose shape diverges from the baseline (e.g. a silent slow
    query with no "ERROR" keyword but a 1000x latency spike).
    """
    return [
        float(len(line)),
        float(len(_DIGIT_PATTERN.findall(line))),
        _extract_latency_ms(line),
        float(len(line.split())),
    ]


def _extract_latency_ms(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value * 1000 if unit == "s" else value
