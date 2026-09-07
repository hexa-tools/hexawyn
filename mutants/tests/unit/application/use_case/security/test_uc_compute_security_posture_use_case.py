from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.compute_security_posture.command import (
    ComputeSecurityPostureCommand,
)
from hexawyn.application.use_case.security.compute_security_posture.compute_security_posture_use_case import (  # noqa: E501
    ComputeSecurityPostureUseCase,
)
from hexawyn.application.use_case.security.compute_security_posture.response import (
    ComputeSecurityPostureResponse,
)


class TestComputeSecurityPostureUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_workload_compliance.return_value = []
        port.get_defined_categories.return_value = []
        port.is_partial.return_value = False

        use_case = ComputeSecurityPostureUseCase(posture_port=port)
        result = use_case.execute(ComputeSecurityPostureCommand())

        assert isinstance(result, ComputeSecurityPostureResponse)

    def test_execute_passes_previous_score_pct(self) -> None:
        port = MagicMock()
        port.list_workload_compliance.return_value = []
        port.get_defined_categories.return_value = []
        port.is_partial.return_value = False

        use_case = ComputeSecurityPostureUseCase(posture_port=port)
        result = use_case.execute(ComputeSecurityPostureCommand(previous_score_pct=85.0))

        assert result.result is not None

    def test_execute_with_partial_data(self) -> None:
        port = MagicMock()
        port.list_workload_compliance.return_value = []
        port.get_defined_categories.return_value = ["network", "rbac"]
        port.is_partial.return_value = True

        use_case = ComputeSecurityPostureUseCase(posture_port=port)
        result = use_case.execute(ComputeSecurityPostureCommand())

        assert isinstance(result, ComputeSecurityPostureResponse)
