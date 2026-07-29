from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
    _pod_ready,
    _to_non_pod_raw,
    _to_pod_raw,
)


def _mk(**attrs: object) -> Mock:
    m = Mock()
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestToPodRaw:
    def test_converts_pod_to_matched_resource(self) -> None:
        item = _mk(
            metadata=_mk(name="my-pod", namespace="default", labels={"app": "nginx"}),
            spec=_mk(node_name="node-1"),
            status=_mk(phase="Running", container_statuses=[_mk(ready=True)]),
        )
        result = _to_pod_raw(item)
        assert result["name"] == "my-pod"
        assert result["namespace"] == "default"
        assert result["kind"] == "pod"
        assert result["node"] == "node-1"
        assert result["phase"] == "Running"
        assert result["ready"] is True
        assert result["labels"] == {"app": "nginx"}

    def test_phase_unknown_when_none(self) -> None:
        item = _mk(
            metadata=_mk(name="p", namespace="n", labels={}),
            spec=_mk(node_name=None),
            status=_mk(phase=None, container_statuses=[]),
        )
        result = _to_pod_raw(item)
        assert result["phase"] == "Unknown"


class TestPodReady:
    def test_all_containers_ready(self) -> None:
        item = _mk(status=_mk(container_statuses=[_mk(ready=True), _mk(ready=True)]))
        assert _pod_ready(item) is True

    def test_one_container_not_ready(self) -> None:
        item = _mk(status=_mk(container_statuses=[_mk(ready=True), _mk(ready=False)]))
        assert _pod_ready(item) is False

    def test_no_statuses_returns_false(self) -> None:
        item = _mk(status=_mk(container_statuses=[]))
        assert _pod_ready(item) is False

    def test_none_statuses_returns_false(self) -> None:
        item = _mk(status=_mk(container_statuses=None))
        assert _pod_ready(item) is False


class TestToNonPodRaw:
    def test_converts_deployment_to_matched_resource(self) -> None:
        item = _mk(
            metadata=_mk(name="my-deploy", namespace="default", labels={"app": "web"}),
        )
        result = _to_non_pod_raw(item, "deployment")
        assert result["name"] == "my-deploy"
        assert result["namespace"] == "default"
        assert result["kind"] == "deployment"
        assert result["node"] is None
        assert result["phase"] is None
        assert result["ready"] is None
        assert result["labels"] == {"app": "web"}

    def test_converts_service(self) -> None:
        item = _mk(metadata=_mk(name="svc", namespace="ns", labels={}))
        result = _to_non_pod_raw(item, "service")
        assert result["kind"] == "service"
