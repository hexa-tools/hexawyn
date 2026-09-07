from __future__ import annotations

import json
from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)

if TYPE_CHECKING:
    from hexawyn.domain.models.analyze_pod_logs import AnalyzePodLogsRequest, PodLogLine

_K8S_FORBIDDEN = 403
_K8S_NOT_FOUND = 404
_CURRENT_RUN = 0
_PREVIOUS_RUN = 1
_LEVEL_KEYWORDS = ("FATAL", "ERROR", "WARN", "WARNING", "INFO", "DEBUG")
_MIN_TIMESTAMP_LENGTH = 20


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut: MutantDict = {}  # type: ignore


class KubernetesPodLogsAdapter(PodLogsPort):
    """Secondary adapter — reads pod logs from the Kubernetes API."""

    @_mutmut_mutated(mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut)
    def fetch_logs(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_orig(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_1(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = None
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_2(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = None

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_3(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes / 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_4(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 61

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_5(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = None
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_6(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(None, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_7(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, None, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_8(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, None, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_9(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=None)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_10(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_11(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_12(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_13(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, )
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_14(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=True)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_15(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = None

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_16(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(None, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_17(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=None)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_18(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_19(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, )

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_20(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(None, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_21(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, None):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_22(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_23(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, ):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_24(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = None
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_25(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(None, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_26(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, None, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_27(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, None, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_28(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=None)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_29(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_30(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_31(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, previous=True)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_32(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, )
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_33(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=False)
            lines += _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_34(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines = _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_35(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines -= _parse_lines(raw_previous, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_36(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(None, run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_37(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, run_index=None)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_38(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(run_index=_PREVIOUS_RUN)

        return lines

    def xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_39(self, request: AnalyzePodLogsRequest) -> list[PodLogLine]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        since_seconds = request.time_window_minutes * 60

        raw_current = self._read_logs(core_api, request, since_seconds, previous=False)
        lines = _parse_lines(raw_current, run_index=_CURRENT_RUN)

        if self._has_restarted(core_api, request):
            raw_previous = self._read_logs(core_api, request, since_seconds, previous=True)
            lines += _parse_lines(raw_previous, )

        return lines

    @_mutmut_mutated(mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut)
    def _read_logs(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_orig(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_1(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = None
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_2(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=None,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_3(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=None,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_4(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=None,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_5(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=None,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_6(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=None,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_7(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=None,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_8(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_9(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_10(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_11(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_12(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_13(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_14(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=False,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_15(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=True,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_16(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return "XXXX"
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_17(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(None, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_18(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, None) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_19(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_20(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, ) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_21(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = None
        return raw_bytes.decode("utf-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_22(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode(None, errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_23(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors=None)

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_24(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode(errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_25(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", )

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_26(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("XXutf-8XX", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_27(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("UTF-8", errors="replace")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_28(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="XXreplaceXX")

    def xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_29(
        self,
        core_api: object,
        request: AnalyzePodLogsRequest,
        since_seconds: int,
        previous: bool,
    ) -> str:
        try:
            response = core_api.read_namespaced_pod_log(  # type: ignore[attr-defined]
                name=request.pod_name,
                namespace=request.namespace,
                since_seconds=since_seconds,
                timestamps=True,
                previous=previous,
                _preload_content=False,
            )
        except Exception as exc:
            if previous:
                return ""
            raise _translate_error(exc, request) from exc
        raw_bytes: bytes = response.data
        return raw_bytes.decode("utf-8", errors="REPLACE")

    @_mutmut_mutated(mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut)
    def _has_restarted(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception:
            return False
        statuses = pod.status.container_statuses or []
        return any(status.restart_count > 0 for status in statuses)

    def xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_orig(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception:
            return False
        statuses = pod.status.container_statuses or []
        return any(status.restart_count > 0 for status in statuses)

    def xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_1(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = None
        except Exception:
            return False
        statuses = pod.status.container_statuses or []
        return any(status.restart_count > 0 for status in statuses)

    def xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_2(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=None, namespace=request.namespace
            )
        except Exception:
            return False
        statuses = pod.status.container_statuses or []
        return any(status.restart_count > 0 for status in statuses)

    def xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_3(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=None
            )
        except Exception:
            return False
        statuses = pod.status.container_statuses or []
        return any(status.restart_count > 0 for status in statuses)

    def xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_4(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                namespace=request.namespace
            )
        except Exception:
            return False
        statuses = pod.status.container_statuses or []
        return any(status.restart_count > 0 for status in statuses)

    def xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_5(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, )
        except Exception:
            return False
        statuses = pod.status.container_statuses or []
        return any(status.restart_count > 0 for status in statuses)

    def xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_6(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception:
            return True
        statuses = pod.status.container_statuses or []
        return any(status.restart_count > 0 for status in statuses)

    def xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_7(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception:
            return False
        statuses = None
        return any(status.restart_count > 0 for status in statuses)

    def xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_8(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception:
            return False
        statuses = pod.status.container_statuses and []
        return any(status.restart_count > 0 for status in statuses)

    def xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_9(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception:
            return False
        statuses = pod.status.container_statuses or []
        return any(None)

    def xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_10(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception:
            return False
        statuses = pod.status.container_statuses or []
        return any(status.restart_count >= 0 for status in statuses)

    def xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_11(self, core_api: object, request: AnalyzePodLogsRequest) -> bool:
        try:
            pod = core_api.read_namespaced_pod(  # type: ignore[attr-defined]
                name=request.pod_name, namespace=request.namespace
            )
        except Exception:
            return False
        statuses = pod.status.container_statuses or []
        return any(status.restart_count > 1 for status in statuses)

mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['_mutmut_orig'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_1'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_2'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_3'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_4'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_5'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_6'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_7'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_8'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_9'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_10'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_11'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_12'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_13'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_14'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_15'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_16'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_17'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_18'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_19'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_20'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_21'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_22'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_23'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_24'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_25'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_26'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_27'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_28'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_29'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_30'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_31'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_32'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_33'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_34'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_34 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_35'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_35 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_36'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_36 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_37'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_37 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_38'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_38 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut['xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_39'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁfetch_logs__mutmut_39 # type: ignore # mutmut generated

mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['_mutmut_orig'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_1'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_2'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_3'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_4'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_5'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_6'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_7'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_8'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_9'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_10'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_11'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_12'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_13'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_14'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_15'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_16'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_17'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_18'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_19'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_20'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_21'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_22'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_23'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_24'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_25'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_26'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_27'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_28'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut['xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_29'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_read_logs__mutmut_29 # type: ignore # mutmut generated

mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut['_mutmut_orig'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut['xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_1'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut['xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_2'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut['xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_3'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut['xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_4'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut['xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_5'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut['xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_6'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut['xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_7'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut['xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_8'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut['xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_9'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut['xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_10'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut['xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_11'] = KubernetesPodLogsAdapter.xǁKubernetesPodLogsAdapterǁ_has_restarted__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_orig(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_1(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = None
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_2(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(None, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_3(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, None, None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_4(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr("status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_5(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_6(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", )
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_7(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_8(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "STATUS", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_9(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = None
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_10(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"XXpod_nameXX": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_11(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"POD_NAME": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_12(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "XXnamespaceXX": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_13(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "NAMESPACE": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_14(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status != _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_15(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            None,
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_16(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=None,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_17(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_18(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_19(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_20(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            None,
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_21(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=None,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_22(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            context=context,
        )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_23(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            )
    return ClusterUnreachableError(f"Cannot read logs for pod {request.pod_name!r}: {exc}")


def x__translate_error__mutmut_24(exc: Exception, request: AnalyzePodLogsRequest) -> Exception:
    status = getattr(exc, "status", None)
    context = {"pod_name": request.pod_name, "namespace": request.namespace}
    if status == _K8S_NOT_FOUND:
        return ResourceNotFoundError(
            f"Pod {request.pod_name!r} not found or not running in namespace {request.namespace!r}",
            context=context,
        )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(
            f"RBAC denied access to logs for pod {request.pod_name!r}",
            context=context,
        )
    return ClusterUnreachableError(None)

mutants_x__translate_error__mutmut['_mutmut_orig'] = x__translate_error__mutmut_orig # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_1'] = x__translate_error__mutmut_1 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_2'] = x__translate_error__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_3'] = x__translate_error__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_4'] = x__translate_error__mutmut_4 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_5'] = x__translate_error__mutmut_5 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_6'] = x__translate_error__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_7'] = x__translate_error__mutmut_7 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_8'] = x__translate_error__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_9'] = x__translate_error__mutmut_9 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_10'] = x__translate_error__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_11'] = x__translate_error__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_12'] = x__translate_error__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_13'] = x__translate_error__mutmut_13 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_14'] = x__translate_error__mutmut_14 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_15'] = x__translate_error__mutmut_15 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_16'] = x__translate_error__mutmut_16 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_17'] = x__translate_error__mutmut_17 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_18'] = x__translate_error__mutmut_18 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_19'] = x__translate_error__mutmut_19 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_20'] = x__translate_error__mutmut_20 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_21'] = x__translate_error__mutmut_21 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_22'] = x__translate_error__mutmut_22 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_23'] = x__translate_error__mutmut_23 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_24'] = x__translate_error__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_lines__mutmut)
def _parse_lines(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_orig(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_1(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = None
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_2(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_3(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            break
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_4(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = None
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_5(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(None)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_6(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = None
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_7(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(None)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_8(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            None
        )
    return lines


def x__parse_lines__mutmut_9(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=None,
                level=level,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_10(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=None,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_11(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=None,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_12(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=None,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_13(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=run_index,
                is_json=None,
            )
        )
    return lines


def x__parse_lines__mutmut_14(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                level=level,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_15(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                message=message,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_16(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                run_index=run_index,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_17(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                is_json=is_json,
            )
        )
    return lines


def x__parse_lines__mutmut_18(raw: str, run_index: int) -> list[PodLogLine]:
    from hexawyn.domain.models.analyze_pod_logs import PodLogLine

    lines: list[PodLogLine] = []
    for raw_line in raw.splitlines():
        if not raw_line.strip():
            continue
        timestamp, message = _split_timestamp(raw_line)
        is_json, message, level = _parse_message(message)
        lines.append(
            PodLogLine(
                timestamp=timestamp,
                level=level,
                message=message,
                run_index=run_index,
                )
        )
    return lines

mutants_x__parse_lines__mutmut['_mutmut_orig'] = x__parse_lines__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_1'] = x__parse_lines__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_2'] = x__parse_lines__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_3'] = x__parse_lines__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_4'] = x__parse_lines__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_5'] = x__parse_lines__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_6'] = x__parse_lines__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_7'] = x__parse_lines__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_8'] = x__parse_lines__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_9'] = x__parse_lines__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_10'] = x__parse_lines__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_11'] = x__parse_lines__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_12'] = x__parse_lines__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_13'] = x__parse_lines__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_14'] = x__parse_lines__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_15'] = x__parse_lines__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_16'] = x__parse_lines__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_17'] = x__parse_lines__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_lines__mutmut['x__parse_lines__mutmut_18'] = x__parse_lines__mutmut_18 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__split_timestamp__mutmut)
def _split_timestamp(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_orig(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_1(raw_line: str) -> tuple[str, str]:
    token, _, rest = None
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_2(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(None)
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_3(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.rpartition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_4(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition("XX XX")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_5(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH or "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_6(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) > _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_7(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "XXTXX" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_8(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "t" in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_9(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" not in token:
        return token, rest
    return "", raw_line


def x__split_timestamp__mutmut_10(raw_line: str) -> tuple[str, str]:
    token, _, rest = raw_line.partition(" ")
    if len(token) >= _MIN_TIMESTAMP_LENGTH and "T" in token:
        return token, rest
    return "XXXX", raw_line

mutants_x__split_timestamp__mutmut['_mutmut_orig'] = x__split_timestamp__mutmut_orig # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_1'] = x__split_timestamp__mutmut_1 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_2'] = x__split_timestamp__mutmut_2 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_3'] = x__split_timestamp__mutmut_3 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_4'] = x__split_timestamp__mutmut_4 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_5'] = x__split_timestamp__mutmut_5 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_6'] = x__split_timestamp__mutmut_6 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_7'] = x__split_timestamp__mutmut_7 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_8'] = x__split_timestamp__mutmut_8 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_9'] = x__split_timestamp__mutmut_9 # type: ignore # mutmut generated
mutants_x__split_timestamp__mutmut['x__split_timestamp__mutmut_10'] = x__split_timestamp__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_message__mutmut)
def _parse_message(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_orig(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_1(message: str) -> tuple[bool, str, str]:
    stripped = None
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_2(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") or stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_3(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith(None) and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_4(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("XX{XX") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_5(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith(None):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_6(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("XX}XX"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_7(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = None
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_8(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(None)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_9(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = ""
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_10(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = None
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_11(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(None)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_12(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") and stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_13(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") and data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_14(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") and data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_15(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get(None) or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_16(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("XXmsgXX") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_17(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("MSG") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_18(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get(None) or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_19(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("XXmessageXX") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_20(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("MESSAGE") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_21(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get(None) or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_22(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("XXerrorXX") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_23(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("ERROR") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_24(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = None
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_25(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").lower()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_26(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(None).upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_27(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") and "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_28(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") and data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_29(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get(None) or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_30(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("XXlevelXX") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_31(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("LEVEL") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_32(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get(None) or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_33(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("XXseverityXX") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_34(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("SEVERITY") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_35(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "XXXX").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_36(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return False, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_37(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level and _detect_level(extracted)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_38(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(None)
    return False, message, _detect_level(message)


def x__parse_message__mutmut_39(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return True, message, _detect_level(message)


def x__parse_message__mutmut_40(message: str) -> tuple[bool, str, str]:
    stripped = message.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, dict):
            extracted = str(data.get("msg") or data.get("message") or data.get("error") or stripped)
            level = str(data.get("level") or data.get("severity") or "").upper()
            return True, extracted, level or _detect_level(extracted)
    return False, message, _detect_level(None)

mutants_x__parse_message__mutmut['_mutmut_orig'] = x__parse_message__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_1'] = x__parse_message__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_2'] = x__parse_message__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_3'] = x__parse_message__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_4'] = x__parse_message__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_5'] = x__parse_message__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_6'] = x__parse_message__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_7'] = x__parse_message__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_8'] = x__parse_message__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_9'] = x__parse_message__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_10'] = x__parse_message__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_11'] = x__parse_message__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_12'] = x__parse_message__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_13'] = x__parse_message__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_14'] = x__parse_message__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_15'] = x__parse_message__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_16'] = x__parse_message__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_17'] = x__parse_message__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_18'] = x__parse_message__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_19'] = x__parse_message__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_20'] = x__parse_message__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_21'] = x__parse_message__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_22'] = x__parse_message__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_23'] = x__parse_message__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_24'] = x__parse_message__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_25'] = x__parse_message__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_26'] = x__parse_message__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_27'] = x__parse_message__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_28'] = x__parse_message__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_29'] = x__parse_message__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_30'] = x__parse_message__mutmut_30 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_31'] = x__parse_message__mutmut_31 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_32'] = x__parse_message__mutmut_32 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_33'] = x__parse_message__mutmut_33 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_34'] = x__parse_message__mutmut_34 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_35'] = x__parse_message__mutmut_35 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_36'] = x__parse_message__mutmut_36 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_37'] = x__parse_message__mutmut_37 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_38'] = x__parse_message__mutmut_38 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_39'] = x__parse_message__mutmut_39 # type: ignore # mutmut generated
mutants_x__parse_message__mutmut['x__parse_message__mutmut_40'] = x__parse_message__mutmut_40 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_level__mutmut)
def _detect_level(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_orig(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_1(message: str) -> str:
    upper = None
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_2(message: str) -> str:
    upper = message.lower()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_3(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword not in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_4(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "XXERRORXX" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_5(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "error" if keyword == "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_6(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword != "FATAL" else keyword
    return "INFO"


def x__detect_level__mutmut_7(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "XXFATALXX" else keyword
    return "INFO"


def x__detect_level__mutmut_8(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "fatal" else keyword
    return "INFO"


def x__detect_level__mutmut_9(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "XXINFOXX"


def x__detect_level__mutmut_10(message: str) -> str:
    upper = message.upper()
    for keyword in _LEVEL_KEYWORDS:
        if keyword in upper:
            return "ERROR" if keyword == "FATAL" else keyword
    return "info"

mutants_x__detect_level__mutmut['_mutmut_orig'] = x__detect_level__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_1'] = x__detect_level__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_2'] = x__detect_level__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_3'] = x__detect_level__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_4'] = x__detect_level__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_5'] = x__detect_level__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_6'] = x__detect_level__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_7'] = x__detect_level__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_8'] = x__detect_level__mutmut_8 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_9'] = x__detect_level__mutmut_9 # type: ignore # mutmut generated
mutants_x__detect_level__mutmut['x__detect_level__mutmut_10'] = x__detect_level__mutmut_10 # type: ignore # mutmut generated
