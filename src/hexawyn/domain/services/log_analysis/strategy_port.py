from abc import ABC, abstractmethod
from collections import Counter

from hexawyn.domain.models.log import LogAnalysisContext, LogAnalysisResult


class LogAnalysisStrategy(ABC):
    """Abstract strategy for log analysis — one implementation per approach.

    This is the ILogAnalysisStrategy port: the domain service (and any
    selector/factory) must depend on this abstraction only, never on a
    concrete strategy class (Dependency Inversion).
    """

    @abstractmethod
    def analyze(self, logs: list[str], context: LogAnalysisContext) -> LogAnalysisResult: ...

    @abstractmethod
    def supports(self, context: LogAnalysisContext) -> bool: ...

    @staticmethod
    def _extract_patterns(logs: list[str]) -> list[str]:
        error_lines = [line for line in logs if "error" in line.lower()]
        if not error_lines:
            return []
        counter: Counter[str] = Counter()
        for line in error_lines:
            words = line.lower().split()
            for i, word in enumerate(words):
                if word in ("error", "failed", "oomkilled", "timeout", "denied"):
                    phrase = " ".join(words[i : i + 4])
                    counter[phrase] += 1
        return [pattern for pattern, _ in counter.most_common(5)]

    @staticmethod
    def _count_severity(logs: list[str]) -> str:
        error_count = sum(1 for line in logs if "error" in line.lower())
        warning_count = sum(1 for line in logs if "warning" in line.lower())
        if error_count > warning_count * 2:
            return "critical"
        if error_count > warning_count:
            return "high"
        if warning_count > 0:
            return "medium"
        return "low"
