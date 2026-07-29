from hexawyn.domain.models.optimization_roi import OptimizationRoiReport


class TestComputeOptimizationRoiResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.use_case.finops.compute_optimization_roi.response import (  # noqa: E501
            ComputeOptimizationRoiResponse,
        )

        report = OptimizationRoiReport(monthly_saving_eur=350.0)
        response = ComputeOptimizationRoiResponse(result=report)

        assert response.result is report
        assert response.result.monthly_saving_eur == 350.0  # noqa: PLR2004
