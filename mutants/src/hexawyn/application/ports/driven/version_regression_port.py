from abc import ABC, abstractmethod

from hexawyn.domain.models.version_regression import VersionComparisonRequest, VersionMetrics


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class VersionRegressionPort(ABC):
    @abstractmethod
    def fetch_baseline_metrics(self, request: VersionComparisonRequest) -> VersionMetrics: ...
    @abstractmethod
    def fetch_current_metrics(self, request: VersionComparisonRequest) -> VersionMetrics: ...
