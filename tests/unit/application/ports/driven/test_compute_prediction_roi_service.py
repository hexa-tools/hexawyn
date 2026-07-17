from unittest.mock import MagicMock

from hexawyn.application.ports.driven.prediction_roi_port import (
    PredictionRoiData,
    PredictionRoiPort,
    PreventedIncidentRaw,
)
from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_command import (  # noqa: E501
    ComputePredictionRoiCommand,
)


def _detection(prevented: bool = True) -> PreventedIncidentRaw:
    return PreventedIncidentRaw(
        incident_ref="PRED-1",
        business_service_name="Service Paiement",
        detected_at="2026-06-10",
        avoided_downtime_minutes=120,
        confidence_pct=90.0,
        prevented=prevented,
    )


def _data(revenue: float | None = 500.0) -> PredictionRoiData:
    return PredictionRoiData(
        detections=[_detection(), _detection(prevented=False)],
        infrastructure_cost_eur=2000.0,
        revenue_per_minute=revenue,
    )


class TestComputePredictionRoiService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_service_port import (  # noqa: E501
            ComputePredictionRoiServicePort,
        )
        from hexawyn.application.service.compute_prediction_roi_service import (
            ComputePredictionRoiService,
        )

        service = ComputePredictionRoiService(prediction_roi_port=MagicMock(spec=PredictionRoiPort))

        assert isinstance(service, ComputePredictionRoiServicePort)

    def test_compute_returns_roi(self) -> None:
        from hexawyn.application.service.compute_prediction_roi_service import (
            ComputePredictionRoiService,
        )

        port = MagicMock(spec=PredictionRoiPort)
        port.get_prediction_roi_data.return_value = _data()
        service = ComputePredictionRoiService(prediction_roi_port=port)

        response = service.compute(ComputePredictionRoiCommand(period="2026-06"))

        assert response.result.roi_eur == 60000.0 - 2000.0
        assert response.result.prevented_incident_count == 1

    def test_compute_lets_error_propagate(self) -> None:
        import pytest
        from hexawyn.application.service.compute_prediction_roi_service import (
            ComputePredictionRoiService,
        )
        from hexawyn.domain.errors import ClusterUnreachableError

        port = MagicMock(spec=PredictionRoiPort)
        port.get_prediction_roi_data.side_effect = ClusterUnreachableError("down")
        service = ComputePredictionRoiService(prediction_roi_port=port)

        with pytest.raises(ClusterUnreachableError):
            service.compute(ComputePredictionRoiCommand(period="2026-06"))
