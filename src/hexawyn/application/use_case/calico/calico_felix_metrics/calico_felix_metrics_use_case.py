"""CalicoFelixMetricsUseCase — per-policy Felix allow/deny counters."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_felix_metrics.command import (
    CalicoFelixMetricsCommand,
)
from hexawyn.application.use_case.calico.calico_felix_metrics.response import (
    CalicoFelixMetricsResponse,
)
from hexawyn.domain.services.calico.felix_metrics_service import (
    build_calico_felix_metrics_result,
)


class CalicoFelixMetricsUseCase:
    """Orchestrates Felix metrics — depends only on ``CalicoPort``."""

    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def execute(self, command: CalicoFelixMetricsCommand) -> CalicoFelixMetricsResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoFelixMetricsResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                metrics_available=False,
                error=detection.error,
            )
        counters = self._port.felix_policy_counters()
        result = build_calico_felix_metrics_result(detection=detection, counters=counters)
        return CalicoFelixMetricsResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            metrics_available=result.metrics_available,
            metrics_message=result.metrics_message,
            total_denies=result.total_denies,
            total_allows=result.total_allows,
            deny_policy_count=result.deny_policy_count,
            policies=list(result.policies),
            error=result.error,
        )
