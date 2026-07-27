"""Tests for K8s adapter internal helpers."""

from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
    _pod_status,
    _to_deployment_status,
    _to_hpa_status,
    _to_pod_status,
    _translate_namespace_error,
    _waiting_reason,
)
from hexawyn.domain.errors import (
    ClusterUnreachableError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)


def _mk(**attrs: object) -> Mock:
    m = Mock()
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestPodStatus:
    def test_running(self) -> None:
        pod = _mk(
            status=_mk(phase="Running", container_statuses=[]),
        )
        assert _pod_status(pod) == "Running"

    def test_waiting_crashloop(self) -> None:
        cs = _mk(state=_mk(waiting=_mk(reason="CrashLoopBackOff")))
        pod = _mk(status=_mk(phase="Running", container_statuses=[cs]))
        assert _pod_status(pod) == "CrashLoopBackOff"

    def test_no_phase(self) -> None:
        pod = _mk(status=_mk(phase=None, container_statuses=[]))
        assert _pod_status(pod) == "Unknown"


class TestWaitingReason:
    def test_found(self) -> None:
        cs = _mk(state=_mk(waiting=_mk(reason="ImagePullBackOff")))
        pod = _mk(status=_mk(container_statuses=[cs]))
        assert _waiting_reason(pod) == "ImagePullBackOff"

    def test_no_waiting(self) -> None:
        cs = _mk(state=_mk(waiting=None))
        pod = _mk(status=_mk(container_statuses=[cs]))
        assert _waiting_reason(pod) is None

    def test_no_container_statuses(self) -> None:
        pod = _mk(status=_mk(container_statuses=None))
        assert _waiting_reason(pod) is None


class TestToPodStatus:
    def test_creates_status(self) -> None:
        pod = _mk(
            metadata=_mk(name="my-pod"),
            status=_mk(phase="Running", container_statuses=[]),
        )
        result = _to_pod_status(pod)
        assert result["name"] == "my-pod"
        assert result["status"] == "Running"


class TestToDeploymentStatus:
    def test_creates(self) -> None:
        d = _mk(
            metadata=_mk(name="my-deploy"),
            status=_mk(ready_replicas=3),
            spec=_mk(replicas=3),
        )
        result = _to_deployment_status(d)
        assert result["name"] == "my-deploy"
        assert result["ready_replicas"] == 3  # noqa: PLR2004

    def test_defaults(self) -> None:
        d = _mk(
            metadata=_mk(name="d"),
            status=_mk(ready_replicas=None),
            spec=_mk(replicas=None),
        )
        result = _to_deployment_status(d)
        assert result["ready_replicas"] == 0


class TestToHpaStatus:
    def test_creates(self) -> None:
        h = _mk(
            metadata=_mk(name="my-hpa"),
            status=_mk(current_replicas=5),
            spec=_mk(max_replicas=10),
        )
        result = _to_hpa_status(h)
        assert result["name"] == "my-hpa"
        assert result["max_replicas"] == 10  # noqa: PLR2004


class TestTranslateNamespaceError:
    def test_not_found(self) -> None:
        exc = _mk(status=404)
        result = _translate_namespace_error(exc, "ns")
        assert isinstance(result, ResourceNotFoundError)

    def test_forbidden(self) -> None:
        exc = _mk(status=403)
        result = _translate_namespace_error(exc, "ns")
        assert isinstance(result, InsufficientPermissionsError)

    def test_other(self) -> None:
        exc = _mk(status=500)
        result = _translate_namespace_error(exc, "ns")
        assert isinstance(result, ClusterUnreachableError)
