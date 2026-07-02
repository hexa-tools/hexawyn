from dataclasses import dataclass, field


@dataclass
class LogAnalysisContext:
    """Context for selecting and executing a log analysis strategy."""

    log_size_estimate: int = 0
    pod_name: str = ""
    namespace: str = "default"
    request_type: str = "troubleshooting"
    urgency: str = "low"
    time_sensitive: bool = False
    follow_up_analysis: bool = False


@dataclass
class LogAnalysisResult:
    """Output of a log analysis strategy."""

    summary: str = ""
    patterns: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)
    severity: str = ""
    confidence: float = 0.0
    strategy_used: str = ""
    token_reduction_percentage: float = 0.0
    degraded: bool = False


@dataclass(frozen=True)
class PatternClassification:
    """A single classified, counted log pattern with a representative sample."""

    pattern: str
    count: int
    sample_line: str
