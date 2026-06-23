from abc import ABC, abstractmethod


class RouteInfo(dict[str, str | bool]):
    """OpenShift route info: name + tls flag."""


class PipelineRunInfo(dict[str, str]):
    """Tekton pipeline run info: name + status."""


class OpenshiftPort(ABC):
    """Port for OpenShift-specific operations."""

    @abstractmethod
    def list_projects(self) -> list[dict[str, str]]:
        """List OpenShift projects (not namespaces)."""

    @abstractmethod
    def list_routes(self) -> list[dict[str, str | bool]]:
        """List OpenShift routes."""

    @abstractmethod
    def list_pipeline_runs(self) -> list[dict[str, str]]:
        """List Tekton pipeline runs."""
