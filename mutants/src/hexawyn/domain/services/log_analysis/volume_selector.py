from hexawyn.domain.services.log_analysis.strategy import (
    HybridStrategy,
    SmartSummaryStrategy,
    StreamingStrategy,
)
from hexawyn.domain.services.log_analysis.strategy_port import LogAnalysisStrategy

_SMART_MAX_LINES = 999
_HYBRID_MAX_LINES = 10000


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_select_strategy_by_volume__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_select_strategy_by_volume__mutmut)
def select_strategy_by_volume(line_count: int) -> LogAnalysisStrategy:
    """Select a LogAnalysisStrategy purely by log line count.

    SMART   <1000 lines
    HYBRID  1000-10000 lines
    STREAMING >10000 lines
    """
    if line_count <= _SMART_MAX_LINES:
        return SmartSummaryStrategy()
    if line_count <= _HYBRID_MAX_LINES:
        return HybridStrategy()
    return StreamingStrategy()


def x_select_strategy_by_volume__mutmut_orig(line_count: int) -> LogAnalysisStrategy:
    """Select a LogAnalysisStrategy purely by log line count.

    SMART   <1000 lines
    HYBRID  1000-10000 lines
    STREAMING >10000 lines
    """
    if line_count <= _SMART_MAX_LINES:
        return SmartSummaryStrategy()
    if line_count <= _HYBRID_MAX_LINES:
        return HybridStrategy()
    return StreamingStrategy()


def x_select_strategy_by_volume__mutmut_1(line_count: int) -> LogAnalysisStrategy:
    """Select a LogAnalysisStrategy purely by log line count.

    SMART   <1000 lines
    HYBRID  1000-10000 lines
    STREAMING >10000 lines
    """
    if line_count < _SMART_MAX_LINES:
        return SmartSummaryStrategy()
    if line_count <= _HYBRID_MAX_LINES:
        return HybridStrategy()
    return StreamingStrategy()


def x_select_strategy_by_volume__mutmut_2(line_count: int) -> LogAnalysisStrategy:
    """Select a LogAnalysisStrategy purely by log line count.

    SMART   <1000 lines
    HYBRID  1000-10000 lines
    STREAMING >10000 lines
    """
    if line_count <= _SMART_MAX_LINES:
        return SmartSummaryStrategy()
    if line_count < _HYBRID_MAX_LINES:
        return HybridStrategy()
    return StreamingStrategy()

mutants_x_select_strategy_by_volume__mutmut['_mutmut_orig'] = x_select_strategy_by_volume__mutmut_orig # type: ignore # mutmut generated
mutants_x_select_strategy_by_volume__mutmut['x_select_strategy_by_volume__mutmut_1'] = x_select_strategy_by_volume__mutmut_1 # type: ignore # mutmut generated
mutants_x_select_strategy_by_volume__mutmut['x_select_strategy_by_volume__mutmut_2'] = x_select_strategy_by_volume__mutmut_2 # type: ignore # mutmut generated
