from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.k8s_port import NamespaceInfo
from hexawyn.application.use_case.cluster.list_namespaces.command import (
    ListNamespacesCommand,
)
from hexawyn.application.use_case.cluster.list_namespaces.list_namespaces_use_case import (
    ListNamespacesUseCase,
)
from hexawyn.application.use_case.cluster.list_namespaces.response import (
    ListNamespacesResponse,
)


class TestListNamespacesUseCase:
    def test_execute_returns_list_namespaces_response(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = []

        use_case = ListNamespacesUseCase(k8s_port=k8s_port)
        result = use_case.execute(ListNamespacesCommand())

        assert isinstance(result, ListNamespacesResponse)

    def test_execute_returns_namespaces_from_port(self) -> None:
        expected_ns: NamespaceInfo = {"name": "default", "status": "Active", "age": "30d"}
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = [expected_ns]

        use_case = ListNamespacesUseCase(k8s_port=k8s_port)
        result = use_case.execute(ListNamespacesCommand())

        assert len(result.namespaces) == 1
        assert result.namespaces[0]["name"] == "default"

    def test_execute_accepts_cluster_name_in_command(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = []

        use_case = ListNamespacesUseCase(k8s_port=k8s_port)
        result = use_case.execute(ListNamespacesCommand(cluster_name="prod-eu"))

        assert result is not None
        k8s_port.list_namespaces.assert_called_once()

    def test_execute_passes_through_empty_list(self) -> None:
        k8s_port = MagicMock()
        k8s_port.list_namespaces.return_value = []

        use_case = ListNamespacesUseCase(k8s_port=k8s_port)
        result = use_case.execute(ListNamespacesCommand())

        assert result.namespaces == []
