from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
    _to_container,
    _to_containers,
)


class TestToContainer:
    def test_no_security_context(self) -> None:
        container = Mock()
        container.name = "app"
        container.security_context = None
        result = _to_container(container, "container")
        assert result["container_name"] == "app"
        assert result["container_kind"] == "container"
        assert result["privileged"] is None
        assert result["added_capabilities"] == []

    def test_with_security_context(self) -> None:
        caps = Mock()
        caps.add = ["NET_ADMIN"]
        sc = Mock()
        sc.privileged = True
        sc.allow_privilege_escalation = False
        sc.run_as_non_root = False
        sc.capabilities = caps
        container = Mock()
        container.name = "db"
        container.security_context = sc
        result = _to_container(container, "init")
        assert result["privileged"] is True
        assert result["container_kind"] == "init"
        assert result["added_capabilities"] == ["NET_ADMIN"]

    def test_no_capabilities_add(self) -> None:
        caps = Mock()
        caps.add = None
        sc = Mock()
        sc.privileged = False
        sc.allow_privilege_escalation = False
        sc.run_as_non_root = True
        sc.capabilities = caps
        container = Mock()
        container.name = "c"
        container.security_context = sc
        result = _to_container(container, "ephemeral")
        assert result["added_capabilities"] == []

    def test_capabilities_none(self) -> None:
        sc = Mock()
        sc.privileged = None
        sc.allow_privilege_escalation = None
        sc.run_as_non_root = None
        sc.capabilities = None
        container = Mock()
        container.name = "c"
        container.security_context = sc
        result = _to_container(container, "container")
        assert result["added_capabilities"] == []


class TestToContainers:
    def test_empty(self) -> None:
        assert _to_containers(None, "container") == []
        assert _to_containers([], "init") == []

    def test_with_items(self) -> None:
        c = Mock()
        c.name = "app"
        c.security_context = None
        result = _to_containers([c], "container")
        assert len(result) == 1
        assert result[0]["container_name"] == "app"
