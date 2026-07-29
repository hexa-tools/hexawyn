from __future__ import annotations

from hexawyn.application.ports.driven.helm_values_diff_port import HelmValuesDiffPort
from hexawyn.application.use_case.gitops.diff_helm_values.command import (
    DiffHelmValuesCommand,
)
from hexawyn.application.use_case.gitops.diff_helm_values.response import (
    DiffHelmValuesResponse,
)
from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
    HelmValuesDiffService,
)


class DiffHelmValuesUseCase:
    def __init__(self, helm_values_port: HelmValuesDiffPort) -> None:
        self._port = helm_values_port
        self._engine = HelmValuesDiffService()

    def execute(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore
