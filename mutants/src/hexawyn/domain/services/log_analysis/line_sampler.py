

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_should_keep_line__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_should_keep_line__mutmut)
def should_keep_line(line_index: int, sample_rate: int) -> bool:
    """Keep every `sample_rate`-th line — bounds memory under high log volume.

    Only applies to non-critical lines: callers must always retain a line
    that matched a critical pattern regardless of this sampling decision.
    """
    return line_index % sample_rate == 0
def x_should_keep_line__mutmut_orig(line_index: int, sample_rate: int) -> bool:
    """Keep every `sample_rate`-th line — bounds memory under high log volume.

    Only applies to non-critical lines: callers must always retain a line
    that matched a critical pattern regardless of this sampling decision.
    """
    return line_index % sample_rate == 0
def x_should_keep_line__mutmut_1(line_index: int, sample_rate: int) -> bool:
    """Keep every `sample_rate`-th line — bounds memory under high log volume.

    Only applies to non-critical lines: callers must always retain a line
    that matched a critical pattern regardless of this sampling decision.
    """
    return line_index / sample_rate == 0
def x_should_keep_line__mutmut_2(line_index: int, sample_rate: int) -> bool:
    """Keep every `sample_rate`-th line — bounds memory under high log volume.

    Only applies to non-critical lines: callers must always retain a line
    that matched a critical pattern regardless of this sampling decision.
    """
    return line_index % sample_rate != 0
def x_should_keep_line__mutmut_3(line_index: int, sample_rate: int) -> bool:
    """Keep every `sample_rate`-th line — bounds memory under high log volume.

    Only applies to non-critical lines: callers must always retain a line
    that matched a critical pattern regardless of this sampling decision.
    """
    return line_index % sample_rate == 1

mutants_x_should_keep_line__mutmut['_mutmut_orig'] = x_should_keep_line__mutmut_orig # type: ignore # mutmut generated
mutants_x_should_keep_line__mutmut['x_should_keep_line__mutmut_1'] = x_should_keep_line__mutmut_1 # type: ignore # mutmut generated
mutants_x_should_keep_line__mutmut['x_should_keep_line__mutmut_2'] = x_should_keep_line__mutmut_2 # type: ignore # mutmut generated
mutants_x_should_keep_line__mutmut['x_should_keep_line__mutmut_3'] = x_should_keep_line__mutmut_3 # type: ignore # mutmut generated
