from unittest.mock import MagicMock

from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_command import (  # noqa: E501
    ComputePredictionRoiCommand,
)
from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_response import (  # noqa: E501
    ComputePredictionRoiResponse,
)
from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_service_port import (  # noqa: E501
    ComputePredictionRoiServicePort,
)
from hexawyn.domain.models.prediction_roi import PredictionRoiReport


class TestComputePredictionRoiUseCase:
    def test_execute_delegates_to_service(self) -> None:
        from hexawyn.application.use_case.compute_prediction_roi.compute_prediction_roi_use_case import (  # noqa: E501
            ComputePredictionRoiUseCase,
        )

        service = MagicMock(spec=ComputePredictionRoiServicePort)
        expected = ComputePredictionRoiResponse(result=PredictionRoiReport(period_label="2026-06"))
        service.compute.return_value = expected
        use_case = ComputePredictionRoiUseCase(service=service)

        response = use_case.execute(ComputePredictionRoiCommand(period="2026-06"))

        service.compute.assert_called_once_with(ComputePredictionRoiCommand(period="2026-06"))
        assert response is expected
