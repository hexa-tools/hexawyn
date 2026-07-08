from abc import ABC, abstractmethod


class RouteInfo(dict[str, str | bool]):
    """Ingress route info: name + tls flag."""


class PipelineRunInfo(dict[str, str]):
    """CI/CD pipeline run info: name + status."""


class ExtendedClusterPort(ABC):
    """Port for extended cluster features — projects, routes, pipelines (OpenShift, Tekton, etc.)."""

    @abstractmethod
    def list_projects(self) -> list[dict[str, str]]:
        """List cluster projects (OpenShift projects / labeled namespaces)."""

    @abstractmethod
    def list_routes(self) -> list[dict[str, str | bool]]:
        """List ingress routes."""

    @abstractmethod
    def list_pipeline_runs(self) -> list[dict[str, str]]:
        """List CI/CD pipeline runs (Tekton, ArgoCD, etc.)."""
