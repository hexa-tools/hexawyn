from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
    _to_container,
    _to_containers,
    _to_pod_spec,
    _translate_error,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _mk(**attrs: object) -> Mock:
    m = Mock()
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestToPodSpec:
    def test_full_pod_spec(self) -> None:
        pod = _mk(
            metadata=_mk(
                name="my-pod", namespace="default", owner_references=[_mk(kind="Deployment")]
            ),
            spec=_mk(
                security_context=_mk(run_as_non_root=True),
                host_pid=False,
                host_network=False,
                host_ipc=False,
                init_containers=[],
                containers=[_mk(name="main", security_context=None)],
                ephemeral_containers=[],
            ),
        )
        result = _to_pod_spec(pod)
        assert result["pod_name"] == "my-pod"
        assert result["namespace"] == "default"
        assert result["owner_kind"] == "Deployment"
        assert result["pod_run_as_non_root"] is True
        assert result["host_pid"] is False
        assert result["host_network"] is False
        assert result["host_ipc"] is False

    def test_no_owner(self) -> None:
        pod = _mk(
            metadata=_mk(name="p", namespace="n", owner_references=[]),
            spec=_mk(
                security_context=None,
                host_pid=None,
                host_network=None,
                host_ipc=None,
                init_containers=[],
                containers=[],
                ephemeral_containers=[],
            ),
        )
        result = _to_pod_spec(pod)
        assert result["owner_kind"] is None
        assert result["pod_run_as_non_root"] is None


class TestToContainers:
    def test_returns_empty_for_none(self) -> None:
        assert _to_containers(None, "container") == []

    def test_returns_converted(self) -> None:
        containers = [
            _mk(name="c1", security_context=_mk(privileged=True)),
        ]
        result = _to_containers(containers, "container")
        assert len(result) == 1
        assert result[0]["container_name"] == "c1"


class TestToContainer:
    def test_no_security_context(self) -> None:
        c = _mk(name="main", security_context=None)
        result = _to_container(c, "container")
        assert result["container_name"] == "main"
        assert result["container_kind"] == "container"
        assert result["privileged"] is None
        assert result["allow_privilege_escalation"] is None
        assert result["run_as_non_root"] is None
        assert result["added_capabilities"] == []

    def test_with_security_context(self) -> None:
        c = _mk(
            name="main",
            security_context=_mk(
                privileged=True,
                allow_privilege_escalation=True,
                run_as_non_root=False,
                capabilities=_mk(add=["NET_ADMIN"]),
            ),
        )
        result = _to_container(c, "container")
        assert result["privileged"] is True
        assert result["allow_privilege_escalation"] is True
        assert result["run_as_non_root"] is False
        assert result["added_capabilities"] == ["NET_ADMIN"]

    def test_capabilities_is_none(self) -> None:
        c = _mk(
            name="main",
            security_context=_mk(
                privileged=False,
                allow_privilege_escalation=False,
                run_as_non_root=True,
                capabilities=None,
            ),
        )
        result = _to_container(c, "container")
        assert result["added_capabilities"] == []

    def test_capabilities_add_is_none(self) -> None:
        c = _mk(
            name="main",
            security_context=_mk(
                privileged=False,
                allow_privilege_escalation=False,
                run_as_non_root=True,
                capabilities=_mk(add=None),
            ),
        )
        result = _to_container(c, "container")
        assert result["added_capabilities"] == []


class TestSecurityTranslateError:
    def test_forbidden(self) -> None:
        assert isinstance(_translate_error(_mk(status=403)), InsufficientPermissionsError)

    def test_other(self) -> None:
        assert isinstance(_translate_error(Exception("err")), ClusterUnreachableError)
