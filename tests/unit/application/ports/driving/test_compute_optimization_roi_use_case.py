from unittest.mock import MagicMock

from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_command import (  # noqa: E501
    ComputeOptimizationRoiCommand,
)
from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_response import (  # noqa: E501
    ComputeOptimizationRoiResponse,
)
from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_service_port import (  # noqa: E501
    ComputeOptimizationRoiServicePort,
)
from hexawyn.domain.models.optimization_roi import OptimizationRoiReport


class TestComputeOptimizationRoiUseCase:
    def test_execute_delegates_to_service(self) -> None:
        from hexawyn.application.use_case.compute_optimization_roi.compute_optimization_roi_use_case import (  # noqa: E501
            ComputeOptimizationRoiUseCase,
        )

        service = MagicMock(spec=ComputeOptimizationRoiServicePort)
        expected = ComputeOptimizationRoiResponse(
            result=OptimizationRoiReport(monthly_saving_eur=350.0)
        )
        service.compute.return_value = expected
        use_case = ComputeOptimizationRoiUseCase(service=service)
        command = ComputeOptimizationRoiCommand(sprint_id="s1")

        response = use_case.execute(command)

        service.compute.assert_called_once_with(command)
        assert response is expected
