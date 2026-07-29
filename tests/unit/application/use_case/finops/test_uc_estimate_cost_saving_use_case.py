from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.estimate_cost_saving.command import (
    EstimateCostSavingCommand,
)
from hexawyn.application.use_case.finops.estimate_cost_saving.estimate_cost_saving_use_case import (  # noqa: E501
    EstimateCostSavingUseCase,
)
from hexawyn.application.use_case.finops.estimate_cost_saving.response import (
    EstimateCostSavingResponse,
)


class TestEstimateCostSavingUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_pod_resource_data.return_value = []

        use_case = EstimateCostSavingUseCase(
            cost_saving_port=port,
        )
        result = use_case.estimate_cost_saving(EstimateCostSavingCommand())

        assert isinstance(result, EstimateCostSavingResponse)

    def test_execute_with_previous_saving_computes_trend(self) -> None:
        port = MagicMock()
        port.get_pod_resource_data.return_value = [
            {
                "pod_name": "wasteful-app",
                "namespace": "default",
                "cpu_request_cores": 4.0,
                "memory_request_mi": 4096.0,
                "cpu_limit_cores": None,
                "memory_limit_mi": None,
                "cpu_p95_cores": 1.0,
                "memory_p95_mi": 512.0,
                "cpu_max_cores": None,
                "hpa_enabled": False,
                "hpa_min_replicas": None,
            },
        ]
        port.get_previous_total_saving.return_value = 100.0

        use_case = EstimateCostSavingUseCase(cost_saving_port=port)
        result = use_case.estimate_cost_saving(
            EstimateCostSavingCommand(cpu_per_core_per_hour_usd=0.04)
        )

        assert isinstance(result, EstimateCostSavingResponse)
        assert result.saving_trend == "decreasing"
        port.store_total_saving.assert_called_once()

    def test_compute_trend(self) -> None:
        from hexawyn.application.use_case.finops.estimate_cost_saving.estimate_cost_saving_use_case import (  # noqa: E501
            _compute_trend,
        )

        assert _compute_trend(100.0, 120.0) == "increasing"
        assert _compute_trend(100.0, 80.0) == "decreasing"
        assert _compute_trend(100.0, 105.0) == "stable"
        assert _compute_trend(None, 100.0) is None
        assert _compute_trend(0.0, 100.0) is None
