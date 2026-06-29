from unittest.mock import MagicMock

from hexawyn.application.ports.driven.k8s_port import NamespaceInfo
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_command import (
    ListNamespacesCommand,
)
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_service_port import (
    ListNamespacesServicePort,
)
from hexawyn.application.service.list_namespaces_service import ListNamespacesService


class TestListNamespacesService:
    def test_implements_service_port(self) -> None:
        service = ListNamespacesService(k8s_port=MagicMock())
        assert isinstance(service, ListNamespacesServicePort)

    def test_returns_namespaces_from_port(self) -> None:
        k8s = MagicMock()
        ns = NamespaceInfo(name="default", status="Active", age="30d")
        k8s.list_namespaces.return_value = [ns]
        service = ListNamespacesService(k8s_port=k8s)

        result = service.list_namespaces(ListNamespacesCommand())

        assert len(result.namespaces) == 1
        assert result.namespaces[0]["name"] == "default"
        k8s.list_namespaces.assert_called_once()

    def test_empty_cluster(self) -> None:
        k8s = MagicMock()
        k8s.list_namespaces.return_value = []
        service = ListNamespacesService(k8s_port=k8s)

        result = service.list_namespaces(ListNamespacesCommand())

        assert result.namespaces == []
