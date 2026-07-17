from unittest.mock import MagicMock

from hexawyn.application.ports.driven.optimization_roi_port import (
    OptimizationRoiPort,
    SprintRoiData,
)
from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_command import (  # noqa: E501
    ComputeOptimizationRoiCommand,
)


def _data(has_baseline: bool = True) -> SprintRoiData:
    return SprintRoiData(
        has_baseline=has_baseline,
        baseline_monthly_eur=500.0,
        current_monthly_eur=150.0,
        optimizations=[
            {
                "name": "right-size",
                "category": "right_sizing",
                "monthly_saving_eur": 350.0,
                "description": "",
            }
        ],
        performance_metrics=[],
    )


class TestComputeOptimizationRoiService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.compute_optimization_roi.compute_optimization_roi_service_port import (  # noqa: E501
            ComputeOptimizationRoiServicePort,
        )
        from hexawyn.application.service.compute_optimization_roi_service import (
            ComputeOptimizationRoiService,
        )

        service = ComputeOptimizationRoiService(roi_port=MagicMock(spec=OptimizationRoiPort))

        assert isinstance(service, ComputeOptimizationRoiServicePort)

    def test_compute_returns_report(self) -> None:
        from hexawyn.application.service.compute_optimization_roi_service import (
            ComputeOptimizationRoiService,
        )

        port = MagicMock(spec=OptimizationRoiPort)
        port.get_sprint_roi_data.return_value = _data()
        service = ComputeOptimizationRoiService(roi_port=port)

        response = service.compute(ComputeOptimizationRoiCommand(sprint_id="s1"))

        port.get_sprint_roi_data.assert_called_once_with("s1")
        assert response.result.monthly_saving_eur == 350.0

    def test_compute_passes_traffic_growth(self) -> None:
        from hexawyn.application.service.compute_optimization_roi_service import (
            ComputeOptimizationRoiService,
        )

        port = MagicMock(spec=OptimizationRoiPort)
        port.get_sprint_roi_data.return_value = _data()
        service = ComputeOptimizationRoiService(roi_port=port)

        response = service.compute(
            ComputeOptimizationRoiCommand(sprint_id="s1", traffic_growth_pct=20.0)
        )

        assert response.result.traffic_normalized is True
        assert response.result.monthly_saving_eur == 375.0

    def test_no_baseline_propagated(self) -> None:
        from hexawyn.application.service.compute_optimization_roi_service import (
            ComputeOptimizationRoiService,
        )

        port = MagicMock(spec=OptimizationRoiPort)
        port.get_sprint_roi_data.return_value = _data(has_baseline=False)
        service = ComputeOptimizationRoiService(roi_port=port)

        response = service.compute(ComputeOptimizationRoiCommand(sprint_id="s1"))

        assert response.result.has_baseline is False

    def test_lets_error_propagate(self) -> None:
        import pytest
        from hexawyn.application.service.compute_optimization_roi_service import (
            ComputeOptimizationRoiService,
        )
        from hexawyn.domain.errors import ClusterUnreachableError

        port = MagicMock(spec=OptimizationRoiPort)
        port.get_sprint_roi_data.side_effect = ClusterUnreachableError("down")
        service = ComputeOptimizationRoiService(roi_port=port)

        with pytest.raises(ClusterUnreachableError):
            service.compute(ComputeOptimizationRoiCommand(sprint_id="s1"))
