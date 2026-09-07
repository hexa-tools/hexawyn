from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.troubleshooting.memory_saturation.command import (
    MemorySaturationCommand,
)
from hexawyn.application.use_case.troubleshooting.memory_saturation.memory_saturation_use_case import (  # noqa: E501
    MemorySaturationUseCase,
)
from hexawyn.application.use_case.troubleshooting.memory_saturation.response import (
    MemorySaturationResponse,
)


def _raw_pod(
    name: str,
    namespace: str,
    current_mb: float,
    limit_mb: float | None = None,
    growth_rate: float = 0.0,
) -> dict[str, object]:
    pod: dict[str, object] = {
        "name": name,
        "namespace": namespace,
        "current_mb": current_mb,
        "growth_rate_mb_per_min": growth_rate,
    }
    if limit_mb is not None:
        pod["limit_mb"] = limit_mb
    return pod


class TestMemorySaturationUseCase:
    def test_execute_returns_memory_saturation_response(self) -> None:
        port = MagicMock()
        port.fetch_memory_metrics.return_value = []
        port.correlate_with_otel.return_value = None

        use_case = MemorySaturationUseCase(port=port)
        result = use_case.execute(MemorySaturationCommand())

        assert isinstance(result, MemorySaturationResponse)

    def test_execute_safe_pods_counted_correctly(self) -> None:
        stable_pod = _raw_pod(
            name="stable-app",
            namespace="default",
            current_mb=1000.0,
            limit_mb=4096.0,
            growth_rate=0.0,
        )
        port = MagicMock()
        port.fetch_memory_metrics.return_value = [stable_pod]
        port.correlate_with_otel.return_value = None

        use_case = MemorySaturationUseCase(port=port)
        result = use_case.execute(MemorySaturationCommand())

        assert result.safe_pod_count == 1
        assert len(result.critical_pods) == 0

    def test_execute_critical_pods_identified(self) -> None:
        critical_pod = _raw_pod(
            name="leaky-app",
            namespace="production",
            current_mb=5000.0,
            limit_mb=5120.0,
            growth_rate=10.0,
        )
        port = MagicMock()
        port.fetch_memory_metrics.return_value = [critical_pod]
        port.correlate_with_otel.return_value = None

        use_case = MemorySaturationUseCase(port=port)
        result = use_case.execute(MemorySaturationCommand())

        assert len(result.critical_pods) > 0

    def test_execute_passes_prediction_window(self) -> None:
        port = MagicMock()
        port.fetch_memory_metrics.return_value = []
        port.correlate_with_otel.return_value = None

        use_case = MemorySaturationUseCase(port=port)
        result = use_case.execute(MemorySaturationCommand(prediction_window_minutes=60))

        assert result.prediction_window_minutes == 60  # noqa: PLR2004

    def test_execute_otel_correlation_applied(self) -> None:
        critical_pod = _raw_pod(
            name="leaky-app",
            namespace="production",
            current_mb=5000.0,
            limit_mb=5120.0,
            growth_rate=10.0,
        )
        port = MagicMock()
        port.fetch_memory_metrics.return_value = [critical_pod]
        port.correlate_with_otel.return_value = "memory_leak_in_worker"

        use_case = MemorySaturationUseCase(port=port)
        result = use_case.execute(MemorySaturationCommand())

        pod_dict = result.critical_pods[0]
        assert pod_dict["otel_root_cause"] == "memory_leak_in_worker"

    def test_execute_no_otel_correlation_when_none(self) -> None:
        critical_pod = _raw_pod(
            name="leaky-app",
            namespace="production",
            current_mb=5000.0,
            limit_mb=5120.0,
            growth_rate=10.0,
        )
        port = MagicMock()
        port.fetch_memory_metrics.return_value = [critical_pod]
        port.correlate_with_otel.return_value = None

        use_case = MemorySaturationUseCase(port=port)
        result = use_case.execute(MemorySaturationCommand())

        pod_dict = result.critical_pods[0]
        assert pod_dict["otel_root_cause"] is None

    def test_execute_all_pods_safe_no_critical(self) -> None:
        stable_pod = _raw_pod(
            name="stable",
            namespace="default",
            current_mb=100.0,
            limit_mb=4096.0,
            growth_rate=0.0,
        )
        port = MagicMock()
        port.fetch_memory_metrics.return_value = [stable_pod]
        port.correlate_with_otel.return_value = None

        use_case = MemorySaturationUseCase(port=port)
        result = use_case.execute(MemorySaturationCommand())

        assert len(result.critical_pods) == 0
        assert result.safe_pod_count == 1
