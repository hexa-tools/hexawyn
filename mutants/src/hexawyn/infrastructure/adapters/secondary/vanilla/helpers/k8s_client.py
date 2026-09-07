from __future__ import annotations

from typing import Protocol


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class KubernetesCoreApi(Protocol):
    def list_pod_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List pods across all namespaces."""

    def list_namespaced_pod(self, namespace: str, timeout_seconds: int) -> object:
        """List pods in a namespace."""

    def list_node(self, timeout_seconds: int) -> object:
        """List cluster nodes."""

    def list_namespace(self, timeout_seconds: int) -> object:
        """List all namespaces."""


class KubernetesAppsApi(Protocol):
    def list_deployment_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List all deployments across namespaces."""

    def list_stateful_set_for_all_namespaces(self, timeout_seconds: int) -> object:
        """List all stateful sets across namespaces."""


class KubernetesMetricsApi(Protocol):
    def list_cluster_custom_object(self, group: str, version: str, plural: str) -> object:
        """List cluster-scoped custom objects."""
mutants_xǁKubernetesCRDApiǁlist_namespaced_custom_object__mutmut: MutantDict = {}  # type: ignore


class KubernetesCRDApi(Protocol):
    @_mutmut_mutated(mutants_xǁKubernetesCRDApiǁlist_namespaced_custom_object__mutmut)
    def list_namespaced_custom_object(  # noqa: PLR0913
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        label_selector: str = "",
    ) -> object:
        """List namespace-scoped custom objects."""
    def xǁKubernetesCRDApiǁlist_namespaced_custom_object__mutmut_orig(  # noqa: PLR0913
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        label_selector: str = "",
    ) -> object:
        """List namespace-scoped custom objects."""
    def xǁKubernetesCRDApiǁlist_namespaced_custom_object__mutmut_1(  # noqa: PLR0913
        self,
        group: str,
        version: str,
        namespace: str,
        plural: str,
        label_selector: str = "XXXX",
    ) -> object:
        """List namespace-scoped custom objects."""

mutants_xǁKubernetesCRDApiǁlist_namespaced_custom_object__mutmut['_mutmut_orig'] = KubernetesCRDApi.xǁKubernetesCRDApiǁlist_namespaced_custom_object__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesCRDApiǁlist_namespaced_custom_object__mutmut['xǁKubernetesCRDApiǁlist_namespaced_custom_object__mutmut_1'] = KubernetesCRDApi.xǁKubernetesCRDApiǁlist_namespaced_custom_object__mutmut_1 # type: ignore # mutmut generated
