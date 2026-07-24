"""Unit tests for ListNamespacesUseCase (post-refacto)."""

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.k8s_port import NamespaceInfo
from hexawyn.application.use_case.list_namespaces.command import ListNamespacesCommand
from hexawyn.application.use_case.list_namespaces.list_namespaces_use_case import (
    ListNamespacesUseCase,
)
from hexawyn.application.use_case.list_namespaces.response import ListNamespacesResponse


class TestListNamespacesUseCase:
    def test_returns_namespaces_from_port(self) -> None:
        k8s = MagicMock()
        ns = NamespaceInfo(name="default", status="Active", age="30d")
        k8s.list_namespaces.return_value = [ns]
        use_case = ListNamespacesUseCase(k8s_port=k8s)

        result = use_case.execute(ListNamespacesCommand())

        assert isinstance(result, ListNamespacesResponse)
        assert len(result.namespaces) == 1
        assert result.namespaces[0]["name"] == "default"
        k8s.list_namespaces.assert_called_once()

    def test_empty_cluster(self) -> None:
        k8s = MagicMock()
        k8s.list_namespaces.return_value = []
        use_case = ListNamespacesUseCase(k8s_port=k8s)

        result = use_case.execute(ListNamespacesCommand())

        assert result.namespaces == []

    def test_k8s_port_failure_propagates(self) -> None:
        k8s = MagicMock()
        k8s.list_namespaces.side_effect = RuntimeError("connection refused")
        use_case = ListNamespacesUseCase(k8s_port=k8s)

        with pytest.raises(RuntimeError, match="connection refused"):
            use_case.execute(ListNamespacesCommand())
