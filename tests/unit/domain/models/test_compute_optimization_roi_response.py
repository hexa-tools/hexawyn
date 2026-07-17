from hexawyn.domain.models.optimization_roi import OptimizationRoiReport


class TestComputeOptimizationRoiResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_response import (  # noqa: E501
            ComputeOptimizationRoiResponse,
        )

        report = OptimizationRoiReport(monthly_saving_eur=350.0)
        response = ComputeOptimizationRoiResponse(result=report)

        assert response.result is report
        assert response.result.monthly_saving_eur == 350.0
