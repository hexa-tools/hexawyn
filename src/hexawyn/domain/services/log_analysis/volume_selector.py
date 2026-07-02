from hexawyn.domain.services.log_analysis.strategy import (
    HybridStrategy,
    SmartSummaryStrategy,
    StreamingStrategy,
)
from hexawyn.domain.services.log_analysis.strategy_port import LogAnalysisStrategy

_SMART_MAX_LINES = 999
_HYBRID_MAX_LINES = 10000


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
