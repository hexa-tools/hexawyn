from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.kubearchive_port import KubeArchivePort
from hexawyn.application.use_case.troubleshooting.query_kubearchive.command import (
    QueryKubearchiveCommand,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.response import (
    QueryKubearchiveResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁQueryKubeArchiveUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class QueryKubeArchiveUseCase:
    @_mutmut_mutated(mutants_xǁQueryKubeArchiveUseCaseǁ__init____mutmut)
    def __init__(self, kubearchive_port: KubeArchivePort, k8s_port: K8sPort) -> None:
        self._kubearchive_port = kubearchive_port
        self._k8s_port = k8s_port
    def xǁQueryKubeArchiveUseCaseǁ__init____mutmut_orig(self, kubearchive_port: KubeArchivePort, k8s_port: K8sPort) -> None:
        self._kubearchive_port = kubearchive_port
        self._k8s_port = k8s_port
    def xǁQueryKubeArchiveUseCaseǁ__init____mutmut_1(self, kubearchive_port: KubeArchivePort, k8s_port: K8sPort) -> None:
        self._kubearchive_port = None
        self._k8s_port = k8s_port
    def xǁQueryKubeArchiveUseCaseǁ__init____mutmut_2(self, kubearchive_port: KubeArchivePort, k8s_port: K8sPort) -> None:
        self._kubearchive_port = kubearchive_port
        self._k8s_port = None

    @_mutmut_mutated(mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut)
    def execute(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_orig(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_1(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = None

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_2(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            None
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_3(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "XXnamespaceXX": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_4(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "NAMESPACE": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_5(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "XXresource_typeXX": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_6(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "RESOURCE_TYPE": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_7(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "XXtimestampXX": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_8(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "TIMESTAMP": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_9(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "XXcompare_with_currentXX": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_10(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "COMPARE_WITH_CURRENT": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_11(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = None

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_12(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(None) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_13(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get(None, [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_14(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", None)]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_15(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get([])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_16(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", )]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_17(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("XXpodsXX", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_18(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("PODS", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_19(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = ""
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_20(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current or command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_21(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type != "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_22(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "XXpodsXX":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_23(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "PODS":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_24(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = None
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_25(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(None)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_26(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = None  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_27(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = None

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_28(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(None) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_29(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get(None, "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_30(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", None)) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_31(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_32(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", )) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_33(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("XXnameXX", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_34(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("NAME", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_35(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "XXXX")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_36(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = None
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_37(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(None)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_38(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names + historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_39(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = None

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_40(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(None)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_41(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names + current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_42(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = None
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_43(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "XXhistorical_countXX": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_44(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "HISTORICAL_COUNT": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_45(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get(None, 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_46(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", None),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_47(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get(0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_48(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", ),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_49(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("XXtotal_resourcesXX", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_50(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("TOTAL_RESOURCES", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_51(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 1),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_52(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "XXcurrent_countXX": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_53(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "CURRENT_COUNT": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_54(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "XXpods_addedXX": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_55(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "PODS_ADDED": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_56(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "XXpods_removedXX": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_57(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "PODS_REMOVED": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_58(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "XXadded_pod_namesXX": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_59(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "ADDED_POD_NAMES": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_60(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "XXremoved_pod_namesXX": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_61(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "REMOVED_POD_NAMES": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_62(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "XXdelta_messageXX": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_63(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "DELTA_MESSAGE": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_64(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = ""

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_65(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=None,
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_66(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=None,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_67(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=None,
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_68(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=None,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_69(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=None,
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_70(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_71(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_72(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_73(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_74(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_75(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get(None, 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_76(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", None),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_77(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get(0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_78(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", ),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_79(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("XXtotal_resourcesXX", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_80(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("TOTAL_RESOURCES", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_81(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 1),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_82(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get(None),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_83(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("XXqueried_timestampXX"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_84(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("QUERIED_TIMESTAMP"),
            comparison=comparison,
            error=result.get("error"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_85(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get(None),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_86(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("XXerrorXX"),
        )

    def xǁQueryKubeArchiveUseCaseǁexecute__mutmut_87(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        result = self._kubearchive_port.query_historical_state(
            {
                "namespace": command.namespace,
                "resource_type": command.resource_type,
                "timestamp": command.timestamp,
                "compare_with_current": command.compare_with_current,
            }
        )

        pods: list[dict[str, object]] = [dict(p) for p in result.get("pods", [])]

        comparison: dict[str, object] | None = None
        if command.compare_with_current and command.resource_type == "pods":
            try:
                current_pods = self._k8s_port.list_pods(command.namespace)
                current_names = {p.name for p in current_pods}  # type: ignore
                historical_names = {str(p.get("name", "")) for p in pods}

                added = list(current_names - historical_names)
                removed = list(historical_names - current_names)

                comparison = {
                    "historical_count": result.get("total_resources", 0),
                    "current_count": len(current_pods),
                    "pods_added": len(added),
                    "pods_removed": len(removed),
                    "added_pod_names": added,
                    "removed_pod_names": removed,
                    "delta_message": f"Added: {len(added)}, Removed: {len(removed)}",
                }
            except Exception:
                comparison = None

        return QueryKubearchiveResponse(
            total_resources=result.get("total_resources", 0),
            pods=pods,
            queried_timestamp=result.get("queried_timestamp"),
            comparison=comparison,
            error=result.get("ERROR"),
        )

mutants_xǁQueryKubeArchiveUseCaseǁ__init____mutmut['_mutmut_orig'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁ__init____mutmut['xǁQueryKubeArchiveUseCaseǁ__init____mutmut_1'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁ__init____mutmut['xǁQueryKubeArchiveUseCaseǁ__init____mutmut_2'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['_mutmut_orig'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_1'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_2'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_3'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_4'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_5'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_6'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_7'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_8'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_9'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_10'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_11'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_12'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_13'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_14'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_15'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_16'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_17'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_18'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_19'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_20'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_21'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_22'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_23'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_24'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_25'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_26'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_27'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_28'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_29'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_30'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_31'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_32'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_33'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_34'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_35'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_36'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_37'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_38'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_39'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_40'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_41'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_42'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_43'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_44'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_45'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_46'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_47'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_48'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_49'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_50'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_51'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_52'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_53'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_54'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_55'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_56'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_57'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_58'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_59'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_60'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_61'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_62'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_62 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_63'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_63 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_64'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_64 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_65'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_65 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_66'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_66 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_67'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_67 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_68'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_68 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_69'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_69 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_70'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_70 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_71'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_71 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_72'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_72 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_73'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_73 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_74'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_74 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_75'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_75 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_76'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_76 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_77'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_77 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_78'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_78 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_79'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_79 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_80'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_80 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_81'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_81 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_82'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_82 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_83'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_83 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_84'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_84 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_85'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_85 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_86'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_86 # type: ignore # mutmut generated
mutants_xǁQueryKubeArchiveUseCaseǁexecute__mutmut['xǁQueryKubeArchiveUseCaseǁexecute__mutmut_87'] = QueryKubeArchiveUseCase.xǁQueryKubeArchiveUseCaseǁexecute__mutmut_87 # type: ignore # mutmut generated
