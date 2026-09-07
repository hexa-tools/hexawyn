import re

_LATENCY_PATTERN = re.compile(r"(\d+(?:\.\d+)?)\s*(ms|s)\b", re.IGNORECASE)
_DIGIT_PATTERN = re.compile(r"\d")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_extract_log_features__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_extract_log_features__mutmut)
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


def x_extract_log_features__mutmut_orig(line: str) -> list[float]:
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


def x_extract_log_features__mutmut_1(line: str) -> list[float]:
    """Pure numeric feature vector for a single log line.

    No NLP/embeddings — length, digit density, latency (normalized to ms),
    and word count are enough signal for IsolationForest to isolate
    lines whose shape diverges from the baseline (e.g. a silent slow
    query with no "ERROR" keyword but a 1000x latency spike).
    """
    return [
        float(None),
        float(len(_DIGIT_PATTERN.findall(line))),
        _extract_latency_ms(line),
        float(len(line.split())),
    ]


def x_extract_log_features__mutmut_2(line: str) -> list[float]:
    """Pure numeric feature vector for a single log line.

    No NLP/embeddings — length, digit density, latency (normalized to ms),
    and word count are enough signal for IsolationForest to isolate
    lines whose shape diverges from the baseline (e.g. a silent slow
    query with no "ERROR" keyword but a 1000x latency spike).
    """
    return [
        float(len(line)),
        float(None),
        _extract_latency_ms(line),
        float(len(line.split())),
    ]


def x_extract_log_features__mutmut_3(line: str) -> list[float]:
    """Pure numeric feature vector for a single log line.

    No NLP/embeddings — length, digit density, latency (normalized to ms),
    and word count are enough signal for IsolationForest to isolate
    lines whose shape diverges from the baseline (e.g. a silent slow
    query with no "ERROR" keyword but a 1000x latency spike).
    """
    return [
        float(len(line)),
        float(len(_DIGIT_PATTERN.findall(line))),
        _extract_latency_ms(None),
        float(len(line.split())),
    ]


def x_extract_log_features__mutmut_4(line: str) -> list[float]:
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
        float(None),
    ]

mutants_x_extract_log_features__mutmut['_mutmut_orig'] = x_extract_log_features__mutmut_orig # type: ignore # mutmut generated
mutants_x_extract_log_features__mutmut['x_extract_log_features__mutmut_1'] = x_extract_log_features__mutmut_1 # type: ignore # mutmut generated
mutants_x_extract_log_features__mutmut['x_extract_log_features__mutmut_2'] = x_extract_log_features__mutmut_2 # type: ignore # mutmut generated
mutants_x_extract_log_features__mutmut['x_extract_log_features__mutmut_3'] = x_extract_log_features__mutmut_3 # type: ignore # mutmut generated
mutants_x_extract_log_features__mutmut['x_extract_log_features__mutmut_4'] = x_extract_log_features__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_latency_ms__mutmut)
def _extract_latency_ms(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_orig(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_1(line: str) -> float:
    match = None
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_2(line: str) -> float:
    match = _LATENCY_PATTERN.search(None)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_3(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_4(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 1.0
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_5(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = None
    unit = match.group(2).lower()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_6(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(None)
    unit = match.group(2).lower()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_7(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(None))
    unit = match.group(2).lower()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_8(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(2))
    unit = match.group(2).lower()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_9(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = None
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_10(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(2).upper()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_11(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(None).lower()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_12(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(3).lower()
    return value * 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_13(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value / 1000 if unit == "s" else value


def x__extract_latency_ms__mutmut_14(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value * 1001 if unit == "s" else value


def x__extract_latency_ms__mutmut_15(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value * 1000 if unit != "s" else value


def x__extract_latency_ms__mutmut_16(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value * 1000 if unit == "XXsXX" else value


def x__extract_latency_ms__mutmut_17(line: str) -> float:
    match = _LATENCY_PATTERN.search(line)
    if not match:
        return 0.0
    value = float(match.group(1))
    unit = match.group(2).lower()
    return value * 1000 if unit == "S" else value

mutants_x__extract_latency_ms__mutmut['_mutmut_orig'] = x__extract_latency_ms__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_1'] = x__extract_latency_ms__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_2'] = x__extract_latency_ms__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_3'] = x__extract_latency_ms__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_4'] = x__extract_latency_ms__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_5'] = x__extract_latency_ms__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_6'] = x__extract_latency_ms__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_7'] = x__extract_latency_ms__mutmut_7 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_8'] = x__extract_latency_ms__mutmut_8 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_9'] = x__extract_latency_ms__mutmut_9 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_10'] = x__extract_latency_ms__mutmut_10 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_11'] = x__extract_latency_ms__mutmut_11 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_12'] = x__extract_latency_ms__mutmut_12 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_13'] = x__extract_latency_ms__mutmut_13 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_14'] = x__extract_latency_ms__mutmut_14 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_15'] = x__extract_latency_ms__mutmut_15 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_16'] = x__extract_latency_ms__mutmut_16 # type: ignore # mutmut generated
mutants_x__extract_latency_ms__mutmut['x__extract_latency_ms__mutmut_17'] = x__extract_latency_ms__mutmut_17 # type: ignore # mutmut generated
