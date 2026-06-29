from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.k8s_port import NamespaceInfo
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_command import (
    ListNamespacesCommand,
)
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_response import (
    ListNamespacesResponse,
)
from hexawyn.application.service.list_namespaces_service import ListNamespacesService
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


class TestListNamespacesUseCase:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(ListNamespacesUseCase, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            ListNamespacesUseCase()  # type: ignore[abstract]

    def test_execute_is_abstract(self) -> None:
        assert getattr(ListNamespacesUseCase.execute, "__isabstractmethod__", False)


class TestListNamespacesService:
    def test_implements_use_case(self) -> None:
        service = ListNamespacesService(k8s_port=MagicMock())
        assert isinstance(service, ListNamespacesUseCase)

    def test_delegates_to_port(self) -> None:
        k8s = MagicMock()
        ns = NamespaceInfo(name="default", status="Active", age="30d")
        k8s.list_namespaces.return_value = [ns]

        service = ListNamespacesService(k8s_port=k8s)
        result = service.execute(ListNamespacesCommand())

        k8s.list_namespaces.assert_called_once()
        assert result.namespaces == [ns]

    def test_returns_empty_when_no_namespaces(self) -> None:
        k8s = MagicMock()
        k8s.list_namespaces.return_value = []

        service = ListNamespacesService(k8s_port=k8s)
        result = service.execute(ListNamespacesCommand())

        assert result.namespaces == []
