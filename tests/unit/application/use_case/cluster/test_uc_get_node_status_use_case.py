from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cluster.get_node_status.command import (
    GetNodeStatusCommand,
)
from hexawyn.application.use_case.cluster.get_node_status.get_node_status_use_case import (  # noqa: E501
    GetNodeStatusUseCase,
)
from hexawyn.application.use_case.cluster.get_node_status.response import (
    GetNodeStatusResponse,
)


class TestGetNodeStatusUseCase:
    def test_execute_returns_response(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = GetNodeStatusUseCase(k8s_port=k8s)
        result = use_case.execute(GetNodeStatusCommand(node_name="worker-1"))

        assert isinstance(result, GetNodeStatusResponse)
        assert result.node_name == "worker-1"

    def test_execute_filters_pods_by_node(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = [
            {
                "name": "app",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "node": "worker-1",
            },
            {
                "name": "db",
                "namespace": "default",
                "status": "Running",
                "restarts": 0,
                "node": "worker-2",
            },
        ]

        use_case = GetNodeStatusUseCase(k8s_port=k8s)
        result = use_case.execute(GetNodeStatusCommand(node_name="worker-1"))

        assert result.total_pods == 1

    def test_execute_node_not_found_returns_unknown_status(self) -> None:
        k8s = MagicMock()
        k8s.list_pods.return_value = []

        use_case = GetNodeStatusUseCase(k8s_port=k8s)
        result = use_case.execute(GetNodeStatusCommand(node_name="nonexistent"))

        assert result.status == "Unknown"
        assert result.total_pods == 0
