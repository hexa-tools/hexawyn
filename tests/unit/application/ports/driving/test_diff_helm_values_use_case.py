from unittest.mock import MagicMock

from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_command import (
    DiffHelmValuesCommand,
)
from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_response import (
    DiffHelmValuesResponse,
)
from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_service_port import (
    DiffHelmValuesServicePort,
)
from hexawyn.domain.models.helm_values_diff import HelmValuesDiffReport


class TestDiffHelmValuesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        from hexawyn.application.use_case.diff_helm_values.diff_helm_values_use_case import (
            DiffHelmValuesUseCase,
        )

        service = MagicMock(spec=DiffHelmValuesServicePort)
        expected = DiffHelmValuesResponse(
            result=HelmValuesDiffReport(
                release="payment-service", source_env="staging", target_env="production"
            )
        )
        service.diff.return_value = expected
        use_case = DiffHelmValuesUseCase(service=service)
        command = DiffHelmValuesCommand(
            release="payment-service",
            source_namespace="staging",
            target_namespace="production",
        )

        response = use_case.execute(command)

        service.diff.assert_called_once_with(command)
        assert response is expected
