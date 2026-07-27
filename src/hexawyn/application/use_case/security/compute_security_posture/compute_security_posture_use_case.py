from __future__ import annotations

from hexawyn.application.ports.driven.security_posture_port import SecurityPosturePort
from hexawyn.application.use_case.security.compute_security_posture.command import (  # noqa: E501
    ComputeSecurityPostureCommand,
)
from hexawyn.application.use_case.security.compute_security_posture.response import (  # noqa: E501
    ComputeSecurityPostureResponse,
)
from hexawyn.domain.services.security_posture.security_posture_service import (
    SecurityPostureService,
)


class ComputeSecurityPostureUseCase:
    def __init__(self, posture_port: SecurityPosturePort) -> None:
        self._port = posture_port
        self._engine = SecurityPostureService()

    def execute(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=records,
            defined_categories=defined_categories,
            partial=partial,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=result)
