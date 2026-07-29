from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.get_pod_logs.command import (
    GetPodLogsUseCaseCommand,
)
from hexawyn.application.use_case.observability.get_pod_logs.get_pod_logs_use_case import (
    GetPodLogsUseCase,
)
from hexawyn.application.use_case.observability.get_pod_logs.response import (
    GetPodLogsUseCaseResponse,
)


class TestGetPodLogsUseCase:
    def test_execute_returns_response(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = GetPodLogsUseCase(k8s_port=k8s)
        result = use_case.execute(GetPodLogsUseCaseCommand())

        assert isinstance(result, GetPodLogsUseCaseResponse)

    def test_execute_empty_namespace(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = GetPodLogsUseCase(k8s_port=k8s)
        result = use_case.execute(GetPodLogsUseCaseCommand(namespace="empty"))

        assert result.total_pods == 0
