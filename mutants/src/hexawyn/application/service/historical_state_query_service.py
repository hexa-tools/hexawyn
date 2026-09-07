from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort, PodInfo
from hexawyn.application.ports.driven.kubearchive_port import (
    HistoricalComparisonResult,
    HistoricalPodInfo,
    KubeArchivePort,
    KubeArchiveQuery,
)
from hexawyn.application.ports.driving.query_kubearchive.query_kubearchive_service_port import (
    QueryKubeArchiveServicePort,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.command import (
    QueryKubearchiveCommand,
)
from hexawyn.application.use_case.troubleshooting.query_kubearchive.response import (
    QueryKubearchiveResponse,
)
from hexawyn.domain.models.historical_pod import (
    HistoricalPod,
    StateComparison,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁHistoricalStateQueryServiceǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut: MutantDict = {}  # type: ignore
mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut: MutantDict = {}  # type: ignore


class HistoricalStateQueryService(QueryKubeArchiveServicePort):
    @_mutmut_mutated(mutants_xǁHistoricalStateQueryServiceǁ__init____mutmut)
    def __init__(self, kubearchive_port: KubeArchivePort, k8s_port: K8sPort) -> None:
        self._kubearchive = kubearchive_port
        self._k8s = k8s_port
    def xǁHistoricalStateQueryServiceǁ__init____mutmut_orig(self, kubearchive_port: KubeArchivePort, k8s_port: K8sPort) -> None:
        self._kubearchive = kubearchive_port
        self._k8s = k8s_port
    def xǁHistoricalStateQueryServiceǁ__init____mutmut_1(self, kubearchive_port: KubeArchivePort, k8s_port: K8sPort) -> None:
        self._kubearchive = None
        self._k8s = k8s_port
    def xǁHistoricalStateQueryServiceǁ__init____mutmut_2(self, kubearchive_port: KubeArchivePort, k8s_port: K8sPort) -> None:
        self._kubearchive = kubearchive_port
        self._k8s = None

    @_mutmut_mutated(mutants_xǁHistoricalStateQueryServiceǁquery__mutmut)
    def query(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_orig(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_1(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = None
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_2(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "XXnamespaceXX": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_3(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "NAMESPACE": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_4(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "XXresource_typeXX": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_5(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "RESOURCE_TYPE": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_6(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "XXtimestampXX": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_7(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "TIMESTAMP": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_8(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = None
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_9(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(None)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_10(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=None)

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_11(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(None))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_12(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = None

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_13(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["XXpodsXX"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_14(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["PODS"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_15(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = None
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_16(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=None)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_17(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = None
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_18(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=None,
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_19(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=None,
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_20(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=None,
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_21(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=None,
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_22(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=None,
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_23(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=None,
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_24(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_25(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_26(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_27(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_28(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_29(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_30(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["XXnameXX"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_31(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["NAME"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_32(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get(None, command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_33(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", None),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_34(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get(command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_35(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", ),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_36(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("XXnamespaceXX", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_37(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("NAMESPACE", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_38(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["XXphaseXX"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_39(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["PHASE"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_40(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["XXrestart_countXX"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_41(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["RESTART_COUNT"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_42(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["XXqueried_timestampXX"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_43(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["QUERIED_TIMESTAMP"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_44(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(None, current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_45(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], None),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_46(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_47(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], ),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_48(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["XXnameXX"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_49(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["NAME"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_50(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = None
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_51(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=None,
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_52(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=None,
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_53(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=None,
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_54(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=None,
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_55(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp=None,
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_56(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=None,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_57(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_58(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_59(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_60(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_61(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_62(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_63(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["XXnameXX"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_64(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["NAME"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_65(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["XXnamespaceXX"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_66(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["NAMESPACE"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_67(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["XXstatusXX"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_68(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["STATUS"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_69(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["XXrestartsXX"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_70(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["RESTARTS"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_71(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="XXnowXX",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_72(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="NOW",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_73(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=False,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_74(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = None
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_75(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=None,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_76(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=None,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_77(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=None,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_78(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=None,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_79(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_80(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_81(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_82(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_83(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = None
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_84(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "XXhistorical_countXX": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_85(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "HISTORICAL_COUNT": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_86(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "XXcurrent_countXX": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_87(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "CURRENT_COUNT": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_88(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "XXpods_addedXX": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_89(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "PODS_ADDED": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_90(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "XXpods_removedXX": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_91(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "PODS_REMOVED": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_92(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "XXadded_pod_namesXX": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_93(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "ADDED_POD_NAMES": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_94(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "XXremoved_pod_namesXX": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_95(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "REMOVED_POD_NAMES": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_96(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "XXdelta_messageXX": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_97(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "DELTA_MESSAGE": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_98(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(None),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_99(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=None,
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_100(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=None,  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_101(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=None,
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_102(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=None,
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_103(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_104(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_105(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_106(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_107(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["XXtotal_resourcesXX"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_108(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["TOTAL_RESOURCES"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_109(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(None),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_110(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["XXqueried_timestampXX"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_111(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["QUERIED_TIMESTAMP"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_112(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(None),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_113(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=None,
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_114(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=None,  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_115(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=None,
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_116(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_117(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_118(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_119(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["XXtotal_resourcesXX"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_120(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["TOTAL_RESOURCES"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_121(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(None),  # type: ignore[arg-type]
            queried_timestamp=archive_response["queried_timestamp"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_122(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["XXqueried_timestampXX"],
        )

    def xǁHistoricalStateQueryServiceǁquery__mutmut_123(self, command: QueryKubearchiveCommand) -> QueryKubearchiveResponse:
        archive_query: KubeArchiveQuery = {
            "namespace": command.namespace,
            "resource_type": command.resource_type,
            "timestamp": command.timestamp,
        }
        try:
            archive_response = self._kubearchive.query_historical_state(archive_query)
        except Exception as exc:
            return QueryKubearchiveResponse(error=str(exc))

        pods: list[HistoricalPodInfo] = archive_response["pods"]

        if command.compare_with_current:
            current_pods = self._k8s.list_pods(namespace=command.namespace)
            historical_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p.get("namespace", command.namespace),
                    phase=p["phase"],
                    restart_count=p["restart_count"],
                    queried_timestamp=p["queried_timestamp"],
                    currently_exists=self._pod_exists_in_current(p["name"], current_pods),
                )
                for p in pods
            ]
            current_pod_models = [
                HistoricalPod(
                    name=p["name"],
                    namespace=p["namespace"],
                    phase=p["status"],
                    restart_count=p["restarts"],
                    queried_timestamp="now",
                    currently_exists=True,
                )
                for p in current_pods
            ]
            comparison = StateComparison.compare(
                namespace=command.namespace,
                historical_pods=historical_pod_models,
                current_pods=current_pod_models,
                historical_timestamp=command.timestamp,
            )
            result: HistoricalComparisonResult = {
                "historical_count": comparison.historical_count,
                "current_count": comparison.current_count,
                "pods_added": comparison.pods_added,
                "pods_removed": comparison.pods_removed,
                "added_pod_names": comparison.added_pod_names,
                "removed_pod_names": comparison.removed_pod_names,
                "delta_message": self._build_delta_message(comparison),
            }
            return QueryKubearchiveResponse(
                total_resources=archive_response["total_resources"],
                pods=list(pods),  # type: ignore[arg-type]
                queried_timestamp=archive_response["queried_timestamp"],
                comparison=dict(result),
            )

        return QueryKubearchiveResponse(
            total_resources=archive_response["total_resources"],
            pods=list(pods),  # type: ignore[arg-type]
            queried_timestamp=archive_response["QUERIED_TIMESTAMP"],
        )

    @staticmethod
    @_mutmut_mutated(mutants_xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut)
    def _pod_exists_in_current(pod_name: str, current_pods: list[PodInfo]) -> bool:
        return any(p["name"] == pod_name for p in current_pods)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_orig(pod_name: str, current_pods: list[PodInfo]) -> bool:
        return any(p["name"] == pod_name for p in current_pods)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_1(pod_name: str, current_pods: list[PodInfo]) -> bool:
        return any(None)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_2(pod_name: str, current_pods: list[PodInfo]) -> bool:
        return any(p["XXnameXX"] == pod_name for p in current_pods)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_3(pod_name: str, current_pods: list[PodInfo]) -> bool:
        return any(p["NAME"] == pod_name for p in current_pods)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_4(pod_name: str, current_pods: list[PodInfo]) -> bool:
        return any(p["name"] != pod_name for p in current_pods)

    @staticmethod
    @_mutmut_mutated(mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut)
    def _build_delta_message(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed > 0:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"  # noqa: E501
            )
        if comparison.pods_added > 0:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if not parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "; ".join(parts)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_orig(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed > 0:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"  # noqa: E501
            )
        if comparison.pods_added > 0:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if not parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "; ".join(parts)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_1(comparison: StateComparison) -> str:
        parts: list[str] = None
        if comparison.pods_removed > 0:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"  # noqa: E501
            )
        if comparison.pods_added > 0:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if not parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "; ".join(parts)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_2(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed >= 0:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"  # noqa: E501
            )
        if comparison.pods_added > 0:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if not parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "; ".join(parts)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_3(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed > 1:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"  # noqa: E501
            )
        if comparison.pods_added > 0:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if not parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "; ".join(parts)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_4(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed > 0:
            parts.append(
                None  # noqa: E501
            )
        if comparison.pods_added > 0:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if not parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "; ".join(parts)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_5(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed > 0:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"  # noqa: E501
            )
        if comparison.pods_added >= 0:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if not parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "; ".join(parts)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_6(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed > 0:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"  # noqa: E501
            )
        if comparison.pods_added > 1:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if not parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "; ".join(parts)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_7(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed > 0:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"  # noqa: E501
            )
        if comparison.pods_added > 0:
            parts.append(
                None
            )
        if not parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "; ".join(parts)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_8(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed > 0:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"  # noqa: E501
            )
        if comparison.pods_added > 0:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "; ".join(parts)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_9(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed > 0:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"  # noqa: E501
            )
        if comparison.pods_added > 0:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if not parts:
            parts.append(None)
        return "; ".join(parts)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_10(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed > 0:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"  # noqa: E501
            )
        if comparison.pods_added > 0:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if not parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "; ".join(None)

    @staticmethod
    def xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_11(comparison: StateComparison) -> str:
        parts: list[str] = []
        if comparison.pods_removed > 0:
            parts.append(
                f"\u2212{comparison.pods_removed} pods removed since {comparison.historical_timestamp}"  # noqa: E501
            )
        if comparison.pods_added > 0:
            parts.append(
                f"+{comparison.pods_added} pods added since {comparison.historical_timestamp}"
            )
        if not parts:
            parts.append(f"No changes since {comparison.historical_timestamp}")
        return "XX; XX".join(parts)

mutants_xǁHistoricalStateQueryServiceǁ__init____mutmut['_mutmut_orig'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ__init____mutmut['xǁHistoricalStateQueryServiceǁ__init____mutmut_1'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ__init____mutmut['xǁHistoricalStateQueryServiceǁ__init____mutmut_2'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['_mutmut_orig'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_1'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_2'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_3'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_4'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_5'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_6'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_7'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_8'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_9'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_10'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_11'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_11 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_12'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_12 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_13'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_13 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_14'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_14 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_15'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_15 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_16'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_16 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_17'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_17 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_18'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_18 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_19'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_19 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_20'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_20 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_21'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_21 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_22'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_22 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_23'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_23 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_24'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_24 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_25'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_25 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_26'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_26 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_27'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_27 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_28'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_28 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_29'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_29 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_30'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_30 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_31'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_31 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_32'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_32 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_33'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_33 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_34'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_34 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_35'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_35 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_36'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_36 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_37'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_37 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_38'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_38 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_39'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_39 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_40'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_40 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_41'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_41 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_42'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_42 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_43'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_43 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_44'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_44 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_45'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_45 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_46'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_46 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_47'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_47 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_48'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_48 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_49'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_49 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_50'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_50 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_51'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_51 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_52'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_52 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_53'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_53 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_54'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_54 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_55'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_55 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_56'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_56 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_57'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_57 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_58'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_58 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_59'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_59 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_60'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_60 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_61'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_61 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_62'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_62 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_63'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_63 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_64'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_64 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_65'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_65 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_66'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_66 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_67'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_67 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_68'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_68 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_69'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_69 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_70'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_70 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_71'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_71 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_72'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_72 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_73'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_73 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_74'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_74 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_75'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_75 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_76'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_76 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_77'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_77 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_78'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_78 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_79'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_79 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_80'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_80 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_81'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_81 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_82'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_82 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_83'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_83 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_84'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_84 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_85'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_85 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_86'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_86 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_87'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_87 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_88'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_88 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_89'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_89 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_90'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_90 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_91'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_91 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_92'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_92 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_93'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_93 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_94'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_94 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_95'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_95 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_96'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_96 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_97'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_97 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_98'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_98 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_99'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_99 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_100'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_100 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_101'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_101 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_102'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_102 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_103'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_103 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_104'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_104 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_105'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_105 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_106'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_106 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_107'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_107 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_108'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_108 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_109'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_109 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_110'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_110 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_111'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_111 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_112'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_112 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_113'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_113 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_114'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_114 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_115'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_115 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_116'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_116 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_117'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_117 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_118'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_118 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_119'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_119 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_120'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_120 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_121'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_121 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_122'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_122 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁquery__mutmut['xǁHistoricalStateQueryServiceǁquery__mutmut_123'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁquery__mutmut_123 # type: ignore # mutmut generated

mutants_xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut['_mutmut_orig'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut['xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_1'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut['xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_2'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut['xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_3'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut['xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_4'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_pod_exists_in_current__mutmut_4 # type: ignore # mutmut generated

mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut['_mutmut_orig'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_orig # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut['xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_1'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_1 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut['xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_2'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_2 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut['xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_3'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_3 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut['xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_4'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_4 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut['xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_5'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_5 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut['xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_6'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_6 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut['xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_7'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_7 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut['xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_8'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_8 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut['xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_9'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_9 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut['xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_10'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_10 # type: ignore # mutmut generated
mutants_xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut['xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_11'] = HistoricalStateQueryService.xǁHistoricalStateQueryServiceǁ_build_delta_message__mutmut_11 # type: ignore # mutmut generated
