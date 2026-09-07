from hexawyn.domain.models.log import PatternClassification

_KEYWORDS = ("error", "failed", "oomkilled", "timeout", "denied", "refused")
_PHRASE_WINDOW = 4
_HEAD_TAIL_SAMPLE_SIZE = 50


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_extract_error_patterns__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_extract_error_patterns__mutmut)
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


def x_extract_error_patterns__mutmut_orig(logs: list[str]) -> list[PatternClassification]:
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


def x_extract_error_patterns__mutmut_1(logs: list[str]) -> list[PatternClassification]:
    """Deterministic pattern extraction — regex/keyword classifier, no LLM.

    Groups lines by a keyword-anchored phrase, counts occurrences, and
    keeps one representative sample line per distinct pattern.
    """
    counts: dict[str, int] = None
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


def x_extract_error_patterns__mutmut_2(logs: list[str]) -> list[PatternClassification]:
    """Deterministic pattern extraction — regex/keyword classifier, no LLM.

    Groups lines by a keyword-anchored phrase, counts occurrences, and
    keeps one representative sample line per distinct pattern.
    """
    counts: dict[str, int] = {}
    samples: dict[str, str] = None

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


def x_extract_error_patterns__mutmut_3(logs: list[str]) -> list[PatternClassification]:
    """Deterministic pattern extraction — regex/keyword classifier, no LLM.

    Groups lines by a keyword-anchored phrase, counts occurrences, and
    keeps one representative sample line per distinct pattern.
    """
    counts: dict[str, int] = {}
    samples: dict[str, str] = {}

    for line in logs:
        words = None
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


def x_extract_error_patterns__mutmut_4(logs: list[str]) -> list[PatternClassification]:
    """Deterministic pattern extraction — regex/keyword classifier, no LLM.

    Groups lines by a keyword-anchored phrase, counts occurrences, and
    keeps one representative sample line per distinct pattern.
    """
    counts: dict[str, int] = {}
    samples: dict[str, str] = {}

    for line in logs:
        words = line.upper().split()
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


def x_extract_error_patterns__mutmut_5(logs: list[str]) -> list[PatternClassification]:
    """Deterministic pattern extraction — regex/keyword classifier, no LLM.

    Groups lines by a keyword-anchored phrase, counts occurrences, and
    keeps one representative sample line per distinct pattern.
    """
    counts: dict[str, int] = {}
    samples: dict[str, str] = {}

    for line in logs:
        words = line.lower().split()
        for i, word in enumerate(None):
            if word in _KEYWORDS:
                phrase = " ".join(words[i : i + _PHRASE_WINDOW])
                counts[phrase] = counts.get(phrase, 0) + 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_6(logs: list[str]) -> list[PatternClassification]:
    """Deterministic pattern extraction — regex/keyword classifier, no LLM.

    Groups lines by a keyword-anchored phrase, counts occurrences, and
    keeps one representative sample line per distinct pattern.
    """
    counts: dict[str, int] = {}
    samples: dict[str, str] = {}

    for line in logs:
        words = line.lower().split()
        for i, word in enumerate(words):
            if word not in _KEYWORDS:
                phrase = " ".join(words[i : i + _PHRASE_WINDOW])
                counts[phrase] = counts.get(phrase, 0) + 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_7(logs: list[str]) -> list[PatternClassification]:
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
                phrase = None
                counts[phrase] = counts.get(phrase, 0) + 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_8(logs: list[str]) -> list[PatternClassification]:
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
                phrase = " ".join(None)
                counts[phrase] = counts.get(phrase, 0) + 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_9(logs: list[str]) -> list[PatternClassification]:
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
                phrase = "XX XX".join(words[i : i + _PHRASE_WINDOW])
                counts[phrase] = counts.get(phrase, 0) + 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_10(logs: list[str]) -> list[PatternClassification]:
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
                phrase = " ".join(words[i : i - _PHRASE_WINDOW])
                counts[phrase] = counts.get(phrase, 0) + 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_11(logs: list[str]) -> list[PatternClassification]:
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
                counts[phrase] = None
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_12(logs: list[str]) -> list[PatternClassification]:
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
                counts[phrase] = counts.get(phrase, 0) - 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_13(logs: list[str]) -> list[PatternClassification]:
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
                counts[phrase] = counts.get(None, 0) + 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_14(logs: list[str]) -> list[PatternClassification]:
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
                counts[phrase] = counts.get(phrase, None) + 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_15(logs: list[str]) -> list[PatternClassification]:
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
                counts[phrase] = counts.get(0) + 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_16(logs: list[str]) -> list[PatternClassification]:
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
                counts[phrase] = counts.get(phrase, ) + 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_17(logs: list[str]) -> list[PatternClassification]:
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
                counts[phrase] = counts.get(phrase, 1) + 1
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_18(logs: list[str]) -> list[PatternClassification]:
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
                counts[phrase] = counts.get(phrase, 0) + 2
                samples.setdefault(phrase, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_19(logs: list[str]) -> list[PatternClassification]:
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
                samples.setdefault(None, line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_20(logs: list[str]) -> list[PatternClassification]:
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
                samples.setdefault(phrase, None)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_21(logs: list[str]) -> list[PatternClassification]:
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
                samples.setdefault(line)

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_22(logs: list[str]) -> list[PatternClassification]:
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
                samples.setdefault(phrase, )

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_23(logs: list[str]) -> list[PatternClassification]:
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

    ranked = None
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_24(logs: list[str]) -> list[PatternClassification]:
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

    ranked = sorted(None, key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_25(logs: list[str]) -> list[PatternClassification]:
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

    ranked = sorted(counts.items(), key=None, reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_26(logs: list[str]) -> list[PatternClassification]:
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

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=None)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_27(logs: list[str]) -> list[PatternClassification]:
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

    ranked = sorted(key=lambda item: item[1], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_28(logs: list[str]) -> list[PatternClassification]:
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

    ranked = sorted(counts.items(), reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_29(logs: list[str]) -> list[PatternClassification]:
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

    ranked = sorted(counts.items(), key=lambda item: item[1], )
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_30(logs: list[str]) -> list[PatternClassification]:
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

    ranked = sorted(counts.items(), key=lambda item: None, reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_31(logs: list[str]) -> list[PatternClassification]:
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

    ranked = sorted(counts.items(), key=lambda item: item[2], reverse=True)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_32(logs: list[str]) -> list[PatternClassification]:
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

    ranked = sorted(counts.items(), key=lambda item: item[1], reverse=False)
    return [
        PatternClassification(pattern=phrase, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_33(logs: list[str]) -> list[PatternClassification]:
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
        PatternClassification(pattern=None, count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_34(logs: list[str]) -> list[PatternClassification]:
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
        PatternClassification(pattern=phrase, count=None, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_35(logs: list[str]) -> list[PatternClassification]:
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
        PatternClassification(pattern=phrase, count=count, sample_line=None)
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_36(logs: list[str]) -> list[PatternClassification]:
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
        PatternClassification(count=count, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_37(logs: list[str]) -> list[PatternClassification]:
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
        PatternClassification(pattern=phrase, sample_line=samples[phrase])
        for phrase, count in ranked
    ]


def x_extract_error_patterns__mutmut_38(logs: list[str]) -> list[PatternClassification]:
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
        PatternClassification(pattern=phrase, count=count, )
        for phrase, count in ranked
    ]

mutants_x_extract_error_patterns__mutmut['_mutmut_orig'] = x_extract_error_patterns__mutmut_orig # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_1'] = x_extract_error_patterns__mutmut_1 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_2'] = x_extract_error_patterns__mutmut_2 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_3'] = x_extract_error_patterns__mutmut_3 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_4'] = x_extract_error_patterns__mutmut_4 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_5'] = x_extract_error_patterns__mutmut_5 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_6'] = x_extract_error_patterns__mutmut_6 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_7'] = x_extract_error_patterns__mutmut_7 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_8'] = x_extract_error_patterns__mutmut_8 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_9'] = x_extract_error_patterns__mutmut_9 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_10'] = x_extract_error_patterns__mutmut_10 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_11'] = x_extract_error_patterns__mutmut_11 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_12'] = x_extract_error_patterns__mutmut_12 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_13'] = x_extract_error_patterns__mutmut_13 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_14'] = x_extract_error_patterns__mutmut_14 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_15'] = x_extract_error_patterns__mutmut_15 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_16'] = x_extract_error_patterns__mutmut_16 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_17'] = x_extract_error_patterns__mutmut_17 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_18'] = x_extract_error_patterns__mutmut_18 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_19'] = x_extract_error_patterns__mutmut_19 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_20'] = x_extract_error_patterns__mutmut_20 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_21'] = x_extract_error_patterns__mutmut_21 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_22'] = x_extract_error_patterns__mutmut_22 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_23'] = x_extract_error_patterns__mutmut_23 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_24'] = x_extract_error_patterns__mutmut_24 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_25'] = x_extract_error_patterns__mutmut_25 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_26'] = x_extract_error_patterns__mutmut_26 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_27'] = x_extract_error_patterns__mutmut_27 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_28'] = x_extract_error_patterns__mutmut_28 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_29'] = x_extract_error_patterns__mutmut_29 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_30'] = x_extract_error_patterns__mutmut_30 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_31'] = x_extract_error_patterns__mutmut_31 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_32'] = x_extract_error_patterns__mutmut_32 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_33'] = x_extract_error_patterns__mutmut_33 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_34'] = x_extract_error_patterns__mutmut_34 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_35'] = x_extract_error_patterns__mutmut_35 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_36'] = x_extract_error_patterns__mutmut_36 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_37'] = x_extract_error_patterns__mutmut_37 # type: ignore # mutmut generated
mutants_x_extract_error_patterns__mutmut['x_extract_error_patterns__mutmut_38'] = x_extract_error_patterns__mutmut_38 # type: ignore # mutmut generated
mutants_x_reduce_logs_for_summarization__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_reduce_logs_for_summarization__mutmut)
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


def x_reduce_logs_for_summarization__mutmut_orig(logs: list[str]) -> list[str]:
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


def x_reduce_logs_for_summarization__mutmut_1(logs: list[str]) -> list[str]:
    """Build the condensed representation actually handed to the summarizer.

    One line per distinct classified pattern when patterns are found;
    otherwise a bounded head/tail sample of the raw, unrecognized-format
    logs so there is always some reduced context window.
    """
    if logs:
        return []

    classifications = extract_error_patterns(logs)
    if classifications:
        return [f"[{c.count}x] {c.pattern} — e.g. {c.sample_line!r}" for c in classifications]

    return _head_tail_sample(logs)


def x_reduce_logs_for_summarization__mutmut_2(logs: list[str]) -> list[str]:
    """Build the condensed representation actually handed to the summarizer.

    One line per distinct classified pattern when patterns are found;
    otherwise a bounded head/tail sample of the raw, unrecognized-format
    logs so there is always some reduced context window.
    """
    if not logs:
        return []

    classifications = None
    if classifications:
        return [f"[{c.count}x] {c.pattern} — e.g. {c.sample_line!r}" for c in classifications]

    return _head_tail_sample(logs)


def x_reduce_logs_for_summarization__mutmut_3(logs: list[str]) -> list[str]:
    """Build the condensed representation actually handed to the summarizer.

    One line per distinct classified pattern when patterns are found;
    otherwise a bounded head/tail sample of the raw, unrecognized-format
    logs so there is always some reduced context window.
    """
    if not logs:
        return []

    classifications = extract_error_patterns(None)
    if classifications:
        return [f"[{c.count}x] {c.pattern} — e.g. {c.sample_line!r}" for c in classifications]

    return _head_tail_sample(logs)


def x_reduce_logs_for_summarization__mutmut_4(logs: list[str]) -> list[str]:
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

    return _head_tail_sample(None)

mutants_x_reduce_logs_for_summarization__mutmut['_mutmut_orig'] = x_reduce_logs_for_summarization__mutmut_orig # type: ignore # mutmut generated
mutants_x_reduce_logs_for_summarization__mutmut['x_reduce_logs_for_summarization__mutmut_1'] = x_reduce_logs_for_summarization__mutmut_1 # type: ignore # mutmut generated
mutants_x_reduce_logs_for_summarization__mutmut['x_reduce_logs_for_summarization__mutmut_2'] = x_reduce_logs_for_summarization__mutmut_2 # type: ignore # mutmut generated
mutants_x_reduce_logs_for_summarization__mutmut['x_reduce_logs_for_summarization__mutmut_3'] = x_reduce_logs_for_summarization__mutmut_3 # type: ignore # mutmut generated
mutants_x_reduce_logs_for_summarization__mutmut['x_reduce_logs_for_summarization__mutmut_4'] = x_reduce_logs_for_summarization__mutmut_4 # type: ignore # mutmut generated
mutants_x__head_tail_sample__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__head_tail_sample__mutmut)
def _head_tail_sample(logs: list[str]) -> list[str]:
    if len(logs) <= _HEAD_TAIL_SAMPLE_SIZE * 2:
        return list(logs)
    return logs[:_HEAD_TAIL_SAMPLE_SIZE] + logs[-_HEAD_TAIL_SAMPLE_SIZE:]


def x__head_tail_sample__mutmut_orig(logs: list[str]) -> list[str]:
    if len(logs) <= _HEAD_TAIL_SAMPLE_SIZE * 2:
        return list(logs)
    return logs[:_HEAD_TAIL_SAMPLE_SIZE] + logs[-_HEAD_TAIL_SAMPLE_SIZE:]


def x__head_tail_sample__mutmut_1(logs: list[str]) -> list[str]:
    if len(logs) < _HEAD_TAIL_SAMPLE_SIZE * 2:
        return list(logs)
    return logs[:_HEAD_TAIL_SAMPLE_SIZE] + logs[-_HEAD_TAIL_SAMPLE_SIZE:]


def x__head_tail_sample__mutmut_2(logs: list[str]) -> list[str]:
    if len(logs) <= _HEAD_TAIL_SAMPLE_SIZE / 2:
        return list(logs)
    return logs[:_HEAD_TAIL_SAMPLE_SIZE] + logs[-_HEAD_TAIL_SAMPLE_SIZE:]


def x__head_tail_sample__mutmut_3(logs: list[str]) -> list[str]:
    if len(logs) <= _HEAD_TAIL_SAMPLE_SIZE * 3:
        return list(logs)
    return logs[:_HEAD_TAIL_SAMPLE_SIZE] + logs[-_HEAD_TAIL_SAMPLE_SIZE:]


def x__head_tail_sample__mutmut_4(logs: list[str]) -> list[str]:
    if len(logs) <= _HEAD_TAIL_SAMPLE_SIZE * 2:
        return list(None)
    return logs[:_HEAD_TAIL_SAMPLE_SIZE] + logs[-_HEAD_TAIL_SAMPLE_SIZE:]


def x__head_tail_sample__mutmut_5(logs: list[str]) -> list[str]:
    if len(logs) <= _HEAD_TAIL_SAMPLE_SIZE * 2:
        return list(logs)
    return logs[:_HEAD_TAIL_SAMPLE_SIZE] - logs[-_HEAD_TAIL_SAMPLE_SIZE:]


def x__head_tail_sample__mutmut_6(logs: list[str]) -> list[str]:
    if len(logs) <= _HEAD_TAIL_SAMPLE_SIZE * 2:
        return list(logs)
    return logs[:_HEAD_TAIL_SAMPLE_SIZE] + logs[+_HEAD_TAIL_SAMPLE_SIZE:]

mutants_x__head_tail_sample__mutmut['_mutmut_orig'] = x__head_tail_sample__mutmut_orig # type: ignore # mutmut generated
mutants_x__head_tail_sample__mutmut['x__head_tail_sample__mutmut_1'] = x__head_tail_sample__mutmut_1 # type: ignore # mutmut generated
mutants_x__head_tail_sample__mutmut['x__head_tail_sample__mutmut_2'] = x__head_tail_sample__mutmut_2 # type: ignore # mutmut generated
mutants_x__head_tail_sample__mutmut['x__head_tail_sample__mutmut_3'] = x__head_tail_sample__mutmut_3 # type: ignore # mutmut generated
mutants_x__head_tail_sample__mutmut['x__head_tail_sample__mutmut_4'] = x__head_tail_sample__mutmut_4 # type: ignore # mutmut generated
mutants_x__head_tail_sample__mutmut['x__head_tail_sample__mutmut_5'] = x__head_tail_sample__mutmut_5 # type: ignore # mutmut generated
mutants_x__head_tail_sample__mutmut['x__head_tail_sample__mutmut_6'] = x__head_tail_sample__mutmut_6 # type: ignore # mutmut generated
