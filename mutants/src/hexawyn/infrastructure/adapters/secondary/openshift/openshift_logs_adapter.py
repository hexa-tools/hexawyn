from __future__ import annotations

from hexawyn.application.ports.driven.log_search_port import LogSearchPort, RawContainerLog


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOpenShiftLogsAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenShiftLogsAdapterǁ_logs_source__mutmut: MutantDict = {}  # type: ignore


class OpenShiftLogsAdapter(LogSearchPort):
    """LogSearchPort for OpenShift clusters.

    Pod logs on OpenShift are served by the same Kubernetes API as vanilla
    clusters (`oc logs` wraps `kubectl logs`), so container log reads are
    delegated to the shared Kubernetes pod-log adapter.
    """

    @_mutmut_mutated(mutants_xǁOpenShiftLogsAdapterǁ__init____mutmut)
    def __init__(self, delegate: LogSearchPort | None = None) -> None:
        self._delegate = delegate

    def xǁOpenShiftLogsAdapterǁ__init____mutmut_orig(self, delegate: LogSearchPort | None = None) -> None:
        self._delegate = delegate

    def xǁOpenShiftLogsAdapterǁ__init____mutmut_1(self, delegate: LogSearchPort | None = None) -> None:
        self._delegate = None

    @_mutmut_mutated(mutants_xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut)
    def fetch_pod_container_logs(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        return self._logs_source().fetch_pod_container_logs(
            pod_name, namespace, time_window_minutes
        )

    def xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_orig(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        return self._logs_source().fetch_pod_container_logs(
            pod_name, namespace, time_window_minutes
        )

    def xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_1(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        return self._logs_source().fetch_pod_container_logs(
            None, namespace, time_window_minutes
        )

    def xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_2(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        return self._logs_source().fetch_pod_container_logs(
            pod_name, None, time_window_minutes
        )

    def xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_3(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        return self._logs_source().fetch_pod_container_logs(
            pod_name, namespace, None
        )

    def xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_4(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        return self._logs_source().fetch_pod_container_logs(
            namespace, time_window_minutes
        )

    def xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_5(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        return self._logs_source().fetch_pod_container_logs(
            pod_name, time_window_minutes
        )

    def xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_6(
        self, pod_name: str, namespace: str, time_window_minutes: int
    ) -> list[RawContainerLog]:
        return self._logs_source().fetch_pod_container_logs(
            pod_name, namespace, )

    @_mutmut_mutated(mutants_xǁOpenShiftLogsAdapterǁ_logs_source__mutmut)
    def _logs_source(self) -> LogSearchPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (  # noqa: E501
                KubernetesPodLogSearchAdapter,
            )

            self._delegate = KubernetesPodLogSearchAdapter()
        return self._delegate

    def xǁOpenShiftLogsAdapterǁ_logs_source__mutmut_orig(self) -> LogSearchPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (  # noqa: E501
                KubernetesPodLogSearchAdapter,
            )

            self._delegate = KubernetesPodLogSearchAdapter()
        return self._delegate

    def xǁOpenShiftLogsAdapterǁ_logs_source__mutmut_1(self) -> LogSearchPort:
        if self._delegate is not None:
            from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (  # noqa: E501
                KubernetesPodLogSearchAdapter,
            )

            self._delegate = KubernetesPodLogSearchAdapter()
        return self._delegate

    def xǁOpenShiftLogsAdapterǁ_logs_source__mutmut_2(self) -> LogSearchPort:
        if self._delegate is None:
            from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (  # noqa: E501
                KubernetesPodLogSearchAdapter,
            )

            self._delegate = None
        return self._delegate

mutants_xǁOpenShiftLogsAdapterǁ__init____mutmut['_mutmut_orig'] = OpenShiftLogsAdapter.xǁOpenShiftLogsAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftLogsAdapterǁ__init____mutmut['xǁOpenShiftLogsAdapterǁ__init____mutmut_1'] = OpenShiftLogsAdapter.xǁOpenShiftLogsAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut['_mutmut_orig'] = OpenShiftLogsAdapter.xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut['xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_1'] = OpenShiftLogsAdapter.xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut['xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_2'] = OpenShiftLogsAdapter.xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut['xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_3'] = OpenShiftLogsAdapter.xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut['xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_4'] = OpenShiftLogsAdapter.xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut['xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_5'] = OpenShiftLogsAdapter.xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut['xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_6'] = OpenShiftLogsAdapter.xǁOpenShiftLogsAdapterǁfetch_pod_container_logs__mutmut_6 # type: ignore # mutmut generated

mutants_xǁOpenShiftLogsAdapterǁ_logs_source__mutmut['_mutmut_orig'] = OpenShiftLogsAdapter.xǁOpenShiftLogsAdapterǁ_logs_source__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenShiftLogsAdapterǁ_logs_source__mutmut['xǁOpenShiftLogsAdapterǁ_logs_source__mutmut_1'] = OpenShiftLogsAdapter.xǁOpenShiftLogsAdapterǁ_logs_source__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenShiftLogsAdapterǁ_logs_source__mutmut['xǁOpenShiftLogsAdapterǁ_logs_source__mutmut_2'] = OpenShiftLogsAdapter.xǁOpenShiftLogsAdapterǁ_logs_source__mutmut_2 # type: ignore # mutmut generated
