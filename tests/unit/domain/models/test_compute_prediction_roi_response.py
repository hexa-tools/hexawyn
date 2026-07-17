from hexawyn.domain.models.prediction_roi import PredictionRoiReport


class TestComputePredictionRoiResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.ports.driving.compute_prediction_roi.compute_prediction_roi_response import (  # noqa: E501
            ComputePredictionRoiResponse,
        )

        report = PredictionRoiReport(period_label="2026-06")
        response = ComputePredictionRoiResponse(result=report)

        assert response.result is report
        assert response.result.period_label == "2026-06"
