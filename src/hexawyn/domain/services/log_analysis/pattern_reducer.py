from hexawyn.domain.models.log import PatternClassification

_KEYWORDS = ("error", "failed", "oomkilled", "timeout", "denied", "refused")
_PHRASE_WINDOW = 4
_HEAD_TAIL_SAMPLE_SIZE = 50


def extract_error_patterns(logs: list[str]) -> list[PatternClassification]:
    """Deterministic pattern extraction — regex/keyword classifier, no LLM.

    Groups lines by a keyword-anchored phrase, counts occurrences, and
    keeps one representative sample line per distinct pattern.
    """
    counts: dict[str, int] = {}
    samples: dict[str, str] = {}

    for line in logs:
        words = line.lower().split()
        for i, word in enumerate(words):
            if word in _KEYWORDS:
                phrase = " ".join(words[i : i + _PHRASE_WINDOW])
                counts[phrase] = counts.get(phrase, 0) + 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def reduce_logs_for_summarization(logs: list[str]) -> list[str]:
    """Build the condensed representation actually handed to the summarizer.

    One line per distinct classified pattern when patterns are found;
    otherwise a bounded head/tail sample of the raw, unrecognized-format
    logs so there is always some reduced context window.
    """
    if not logs:
        return []

    classifications = extract_error_patterns(logs)
    if classifications:
        return [f"[{c.count}x] {c.pattern} — e.g. {c.sample_line!r}" for c in classifications]

    return _head_tail_sample(logs)


def _head_tail_sample(logs: list[str]) -> list[str]:
    if len(logs) <= _HEAD_TAIL_SAMPLE_SIZE * 2:
        return list(logs)
    return logs[:_HEAD_TAIL_SAMPLE_SIZE] + logs[-_HEAD_TAIL_SAMPLE_SIZE:]
