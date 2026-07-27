from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.deployment_latency.command import (
    DeploymentLatencyCommand,
)
from hexawyn.application.use_case.observability.deployment_latency.deployment_latency_use_case import (  # noqa: E501
    DeploymentLatencyUseCase,
)
from hexawyn.application.use_case.observability.deployment_latency.response import (
    DeploymentLatencyResponse,
)
from hexawyn.domain.models.deployment_latency import WindowLatency


class TestDeploymentLatencyUseCase:
    def test_execute_returns_response(self) -> None:
        window = WindowLatency(
            p50_ms=10.0,
            p95_ms=25.0,
            p99_ms=50.0,
            sample_count=100,
        )
        port = MagicMock()
        port.fetch_pre_deploy_latency.return_value = window
        port.fetch_post_deploy_latency.return_value = window

        use_case = DeploymentLatencyUseCase(port=port)
        result = use_case.execute(DeploymentLatencyCommand(service_name="api"))

        assert isinstance(result, DeploymentLatencyResponse)

    def test_execute_empty_data(self) -> None:
        window = WindowLatency(
            p50_ms=0.0,
            p95_ms=0.0,
            p99_ms=0.0,
            sample_count=0,
        )
        port = MagicMock()
        port.fetch_pre_deploy_latency.return_value = window
        port.fetch_post_deploy_latency.return_value = window

        use_case = DeploymentLatencyUseCase(port=port)
        result = use_case.execute(DeploymentLatencyCommand(service_name="api"))

        assert isinstance(result, DeploymentLatencyResponse)
