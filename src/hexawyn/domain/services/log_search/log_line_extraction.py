from __future__ import annotations

import re

from hexawyn.domain.models.log_search import MatchedLogLine
from hexawyn.domain.services.log_search.pattern_matcher import similarity_score

_MIN_TIMESTAMP_LENGTH = 20


def extract_matching_lines(
    pattern: re.Pattern[str],
    pattern_text: str,
    raw_lines: list[str],
    max_lines: int,
    semantic_threshold: float,
) -> list[MatchedLogLine]:
    """Extracts up to `max_lines` matching lines from one container's raw
    K8s log output. Exact matches (via `pattern`) always take priority; only
    when a container has zero exact matches does the best-scoring line above
    `semantic_threshold` surface as a single `match_type="semantic"` result.
    """
    exact_matches: list[MatchedLogLine] = []
    for raw_line in raw_lines:
        timestamp, message = _split_timestamp(raw_line)
        if pattern.search(message):
            exact_matches.append(
                MatchedLogLine(timestamp=timestamp, message=message, match_type="exact")
            )
            if len(exact_matches) >= max_lines:
                break

    if exact_matches:
        return exact_matches

    return _best_semantic_match(pattern_text, raw_lines, semantic_threshold)


def _best_semantic_match(
    pattern_text: str, raw_lines: list[str], semantic_threshold: float
) -> list[MatchedLogLine]:
    best_line: MatchedLogLine | None = None
    best_score = 0.0
    for raw_line in raw_lines:
        timestamp, message = _split_timestamp(raw_line)
        score = similarity_score(pattern_text, message)
        if score > best_score:
            best_score = score
            best_line = MatchedLogLine(timestamp=timestamp, message=message, match_type="semantic")

    if best_line is not None and best_score >= semantic_threshold:
        return [best_line]
    return []


def _split_timestamp(raw_line: str) -> tuple[str, str]:
    """Splits a K8s `timestamps=True` log line ("2024-01-01T10:32:15Z msg")
    into (timestamp, message) — same heuristic used by the existing single-pod
    log adapters (first-token check, not a regex)."""
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line
