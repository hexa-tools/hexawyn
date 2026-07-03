from hexawyn.domain.models.log import DeduplicatedLine


def deduplicate_lines(logs: list[str]) -> list[DeduplicatedLine]:
    """Collapse repeated lines into one entry each, preserving first-seen order."""
    counts: dict[str, int] = {}
    order: list[str] = []

    for line in logs:
        if line not in counts:
            order.append(line)
        counts[line] = counts.get(line, 0) + 1

    return [DeduplicatedLine(line=line, count=counts[line]) for line in order]
