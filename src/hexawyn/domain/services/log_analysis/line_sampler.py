def should_keep_line(line_index: int, sample_rate: int) -> bool:
    """Keep every `sample_rate`-th line — bounds memory under high log volume.

    Only applies to non-critical lines: callers must always retain a line
    that matched a critical pattern regardless of this sampling decision.
    """
    return line_index % sample_rate == 0
