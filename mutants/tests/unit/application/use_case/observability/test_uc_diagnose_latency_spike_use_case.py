from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.diagnose_latency_spike.command import (
    DiagnoseLatencySpikeUseCaseCommand,
)
from hexawyn.application.use_case.observability.diagnose_latency_spike.diagnose_latency_spike_use_case import (  # noqa: E501
    DiagnoseLatencySpikeUseCase,
)
from hexawyn.application.use_case.observability.diagnose_latency_spike.response import (
    DiagnoseLatencySpikeUseCaseResponse,
)


class TestDiagnoseLatencySpikeUseCase:
    def test_execute_returns_response(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = DiagnoseLatencySpikeUseCase(k8s_port=k8s)
        result = use_case.execute(DiagnoseLatencySpikeUseCaseCommand())

        assert isinstance(result, DiagnoseLatencySpikeUseCaseResponse)

    def test_execute_empty_namespace(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = DiagnoseLatencySpikeUseCase(k8s_port=k8s)
        result = use_case.execute(DiagnoseLatencySpikeUseCaseCommand(namespace="empty"))

        assert result.total_pods == 0
