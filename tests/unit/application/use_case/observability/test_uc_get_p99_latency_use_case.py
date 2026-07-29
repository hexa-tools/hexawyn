from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.get_p99_latency.command import (
    GetP99LatencyUseCaseCommand,
)
from hexawyn.application.use_case.observability.get_p99_latency.get_p99_latency_use_case import (
    GetP99LatencyUseCase,
)
from hexawyn.application.use_case.observability.get_p99_latency.response import (
    GetP99LatencyUseCaseResponse,
)


class TestGetP99LatencyUseCase:
    def test_execute_returns_response(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = GetP99LatencyUseCase(k8s_port=k8s)
        result = use_case.execute(GetP99LatencyUseCaseCommand())

        assert isinstance(result, GetP99LatencyUseCaseResponse)

    def test_execute_empty_namespace(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = GetP99LatencyUseCase(k8s_port=k8s)
        result = use_case.execute(GetP99LatencyUseCaseCommand(namespace="empty"))

        assert result.total_pods == 0
