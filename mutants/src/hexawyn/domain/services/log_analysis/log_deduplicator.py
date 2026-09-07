from hexawyn.domain.models.log import DeduplicatedLine


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_deduplicate_lines__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_deduplicate_lines__mutmut)
def deduplicate_lines(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, 0) + 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_orig(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, 0) + 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_1(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = None
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, 0) + 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_2(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = None

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, 0) + 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_3(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line in counts:
            order.append(line)
        counts[line] = counts.get(line, 0) + 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_4(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(None)
        counts[line] = counts.get(line, 0) + 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_5(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = None

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_6(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, 0) - 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_7(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(None, 0) + 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_8(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, None) + 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_9(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(0) + 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_10(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, ) + 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_11(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, 1) + 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_12(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, 0) + 2

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_13(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, 0) + 1

    return [DeduplicatedLine(line=None, count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_14(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, 0) + 1

    return [DeduplicatedLine(line=line, count=None) for line in order]


def x_deduplicate_lines__mutmut_15(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, 0) + 1

    return [DeduplicatedLine(count=counts[line]) for line in order]


def x_deduplicate_lines__mutmut_16(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, 0) + 1

    return [DeduplicatedLine(line=line, ) for line in order]

mutants_x_deduplicate_lines__mutmut['_mutmut_orig'] = x_deduplicate_lines__mutmut_orig # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_1'] = x_deduplicate_lines__mutmut_1 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_2'] = x_deduplicate_lines__mutmut_2 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_3'] = x_deduplicate_lines__mutmut_3 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_4'] = x_deduplicate_lines__mutmut_4 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_5'] = x_deduplicate_lines__mutmut_5 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_6'] = x_deduplicate_lines__mutmut_6 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_7'] = x_deduplicate_lines__mutmut_7 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_8'] = x_deduplicate_lines__mutmut_8 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_9'] = x_deduplicate_lines__mutmut_9 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_10'] = x_deduplicate_lines__mutmut_10 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_11'] = x_deduplicate_lines__mutmut_11 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_12'] = x_deduplicate_lines__mutmut_12 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_13'] = x_deduplicate_lines__mutmut_13 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_14'] = x_deduplicate_lines__mutmut_14 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_15'] = x_deduplicate_lines__mutmut_15 # type: ignore # mutmut generated
mutants_x_deduplicate_lines__mutmut['x_deduplicate_lines__mutmut_16'] = x_deduplicate_lines__mutmut_16 # type: ignore # mutmut generated
