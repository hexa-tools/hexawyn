from abc import ABC, abstractmethod

from hexawyn.domain.models.deployment_latency import DeploymentComparisonRequest, WindowLatency


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DeploymentLatencyComparisonPort(ABC):
    @abstractmethod
    def fetch_pre_deploy_latency(self, request: DeploymentComparisonRequest) -> WindowLatency: ...
    @abstractmethod
    def fetch_post_deploy_latency(self, request: DeploymentComparisonRequest) -> WindowLatency: ...
