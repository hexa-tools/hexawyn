from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.k8s_port import NamespaceInfo
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_command import (
    ListNamespacesCommand,
)
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_response import (
    ListNamespacesResponse,
)
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_service_port import (
    ListNamespacesServicePort,
)
from hexawyn.application.use_case.list_namespaces.list_namespaces_use_case import (
    ListNamespacesUseCase,
)


class TestListNamespacesCommand:
    def test_is_frozen(self) -> None:
        cmd = ListNamespacesCommand()
        with pytest.raises(AttributeError):
            cmd.cluster_name = "other"  # type: ignore[misc]

    def test_default_cluster_name_is_none(self) -> None:
        cmd = ListNamespacesCommand()
        assert cmd.cluster_name is None

    def test_accepts_cluster_name(self) -> None:
        cmd = ListNamespacesCommand(cluster_name="prod-eu")
        assert cmd.cluster_name == "prod-eu"


class TestListNamespacesResponse:
    def test_default_namespaces_is_empty(self) -> None:
        resp = ListNamespacesResponse()
        assert resp.namespaces == []

    def test_accepts_namespaces_list(self) -> None:
        ns = NamespaceInfo(name="default", status="Active", age="30d")
        resp = ListNamespacesResponse(namespaces=[ns])
        assert len(resp.namespaces) == 1
        assert resp.namespaces[0]["name"] == "default"


class TestListNamespacesServicePort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(ListNamespacesServicePort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            ListNamespacesServicePort()  # type: ignore[abstract]


class TestListNamespacesUseCase:
    def test_delegates_to_service_port(self) -> None:
        fake_service = MagicMock(spec=ListNamespacesServicePort)
        ns = NamespaceInfo(name="default", status="Active", age="30d")
        expected = ListNamespacesResponse(namespaces=[ns])
        fake_service.list_namespaces.return_value = expected

        use_case = ListNamespacesUseCase(service=fake_service)
        result = use_case.execute(ListNamespacesCommand())

        assert result.namespaces == [ns]
        fake_service.list_namespaces.assert_called_once()

    def test_returns_empty_when_no_namespaces(self) -> None:
        fake_service = MagicMock(spec=ListNamespacesServicePort)
        fake_service.list_namespaces.return_value = ListNamespacesResponse()

        use_case = ListNamespacesUseCase(service=fake_service)
        result = use_case.execute(ListNamespacesCommand())

        assert result.namespaces == []
