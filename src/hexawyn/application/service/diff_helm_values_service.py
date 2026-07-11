from __future__ import annotations

from hexawyn.application.ports.driven.helm_values_diff_port import HelmValuesDiffPort
from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_command import (
    DiffHelmValuesCommand,
)
from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_response import (
    DiffHelmValuesResponse,
)
from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_service_port import (
    DiffHelmValuesServicePort,
)
from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
    HelmValuesDiffService,
)


class DiffHelmValuesService(DiffHelmValuesServicePort):
    def __init__(self, helm_values_port: HelmValuesDiffPort) -> None:
        self._port = helm_values_port
        self._engine = HelmValuesDiffService()

    def diff(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)
        target = self._port.get_effective_values(command.release, command.target_namespace)
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,
            target_env=command.target_env,
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)
