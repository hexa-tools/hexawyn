from abc import ABC, abstractmethod

from hexawyn.domain.models.canary_comparison import (
    CanaryComparisonRequest,
    VersionMetrics,
)


class CanaryComparisonPort(ABC):
    @abstractmethod
    def fetch_canary_metrics(self, request: CanaryComparisonRequest) -> VersionMetrics: ...
    @abstractmethod
    def fetch_stable_metrics(self, request: CanaryComparisonRequest) -> VersionMetrics: ...
