from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.correlate_error_latency_spikes.command import (
    CorrelateErrorLatencySpikesUseCaseCommand,
)
from hexawyn.application.use_case.observability.correlate_error_latency_spikes.correlate_error_latency_spikes_use_case import (  # noqa: E501
    CorrelateErrorLatencySpikesUseCase,
)
from hexawyn.application.use_case.observability.correlate_error_latency_spikes.response import (
    CorrelateErrorLatencySpikesUseCaseResponse,
)


class TestCorrelateErrorLatencySpikesUseCase:
    def test_execute_returns_response(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = CorrelateErrorLatencySpikesUseCase(k8s_port=k8s)
        result = use_case.execute(CorrelateErrorLatencySpikesUseCaseCommand())

        assert isinstance(result, CorrelateErrorLatencySpikesUseCaseResponse)

    def test_execute_empty_namespace(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = CorrelateErrorLatencySpikesUseCase(k8s_port=k8s)
        result = use_case.execute(CorrelateErrorLatencySpikesUseCaseCommand(namespace="empty"))

        assert result.total_pods == 0
