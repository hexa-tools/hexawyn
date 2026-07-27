"""Tests for fleet_health_adapter internal helpers."""

from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.fleet_health_adapter import (
    _get_failing_pipelines,
    _get_node_counts,
    _get_pod_counts,
    _get_security_violations,
    _items,
    _node_ready,
    _pod_is_crashloop,
    _pod_phase,
)


class MockObj:
    def __init__(self, **kwargs: object) -> None:
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)


class TestItems:
    def test_returns_items(self) -> None:
        obj = MockObj(items=[1, 2, 3])
        assert _items(obj) == [1, 2, 3]

    def test_no_items_returns_empty(self) -> None:
        obj = MockObj()
        assert _items(obj) == []


class TestNodeReady:
    def test_ready(self) -> None:
        node = MockObj(status=MockObj(conditions=[MockObj(type="Ready", status="True")]))
        assert _node_ready(node) is True

    def test_not_ready(self) -> None:
        node = MockObj(status=MockObj(conditions=[MockObj(type="Ready", status="False")]))
        assert _node_ready(node) is False

    def test_no_status(self) -> None:
        node = MockObj()
        assert _node_ready(node) is False


class TestGetNodeCounts:
    def test_healthy(self) -> None:
        api = Mock()
        node = MockObj(status=MockObj(conditions=[MockObj(type="Ready", status="True")]))
        api.list_node.return_value = MockObj(items=[node, node, node])
        total, not_ready = _get_node_counts(api)
        assert total == 3  # noqa: PLR2004
        assert not_ready == 0

    def test_not_ready_nodes(self) -> None:
        api = Mock()
        bad = MockObj(status=MockObj(conditions=[MockObj(type="Ready", status="False")]))
        good = MockObj(status=MockObj(conditions=[MockObj(type="Ready", status="True")]))
        api.list_node.return_value = MockObj(items=[good, bad])
        total, not_ready = _get_node_counts(api)
        assert total == 2  # noqa: PLR2004
        assert not_ready == 1

    def test_exception_returns_zeros(self) -> None:
        api = Mock()
        api.list_node.side_effect = Exception("boom")
        total, not_ready = _get_node_counts(api)
        assert total == 0
        assert not_ready == 0


class TestPodPhase:
    def test_running(self) -> None:
        pod = MockObj(status=MockObj(phase="Running"))
        assert _pod_phase(pod) == "Running"

    def test_no_status(self) -> None:
        pod = MockObj()
        assert _pod_phase(pod) == "Unknown"


class TestPodIsCrashloop:
    def test_crashloop(self) -> None:
        waiting = MockObj(reason="CrashLoopBackOff")
        state = MockObj(waiting=waiting)
        cs = MockObj(state=state)
        pod = MockObj(status=MockObj(container_statuses=[cs]))
        assert _pod_is_crashloop(pod) is True

    def test_not_crashloop(self) -> None:
        pod = MockObj(status=MockObj(container_statuses=[]))
        assert _pod_is_crashloop(pod) is False

    def test_no_status(self) -> None:
        pod = MockObj()
        assert _pod_is_crashloop(pod) is False


class TestGetPodCounts:
    def test_all_running(self) -> None:
        api = Mock()
        pod = MockObj(status=MockObj(phase="Running", container_statuses=[]))
        api.list_pod_for_all_namespaces.return_value = MockObj(items=[pod, pod, pod])
        total, running, crashloop = _get_pod_counts(api)
        assert total == 3  # noqa: PLR2004
        assert running == 3  # noqa: PLR2004
        assert crashloop == 0

    def test_mixed(self) -> None:
        api = Mock()
        running = MockObj(status=MockObj(phase="Running", container_statuses=[]))
        failed = MockObj(status=MockObj(phase="Failed", container_statuses=[]))
        api.list_pod_for_all_namespaces.return_value = MockObj(items=[running, failed])
        total, running_count, crashloop = _get_pod_counts(api)
        assert total == 2  # noqa: PLR2004
        assert running_count == 1

    def test_exception_returns_zeros(self) -> None:
        api = Mock()
        api.list_pod_for_all_namespaces.side_effect = Exception("boom")
        assert _get_pod_counts(api) == (0, 0, 0)


class TestGetSecurityViolations:
    def test_no_privileged(self) -> None:
        api = Mock()
        container = MockObj(security_context=MockObj(privileged=False))
        pod = MockObj(spec=MockObj(containers=[container]))
        api.list_pod_for_all_namespaces.return_value = MockObj(items=[pod])
        assert _get_security_violations(api) == 0

    def test_privileged(self) -> None:
        api = Mock()
        container = MockObj(security_context=MockObj(privileged=True))
        pod = MockObj(spec=MockObj(containers=[container]))
        api.list_pod_for_all_namespaces.return_value = MockObj(items=[pod])
        assert _get_security_violations(api) == 1

    def test_exception_returns_zero(self) -> None:
        api = Mock()
        api.list_pod_for_all_namespaces.side_effect = Exception("boom")
        assert _get_security_violations(api) == 0


class TestGetFailingPipelines:
    def test_no_failures(self) -> None:
        crd = Mock()
        crd.list_cluster_custom_object.return_value = {
            "items": [{"status": {"conditions": [{"type": "Succeeded", "status": "True"}]}}]
        }
        assert _get_failing_pipelines(crd) == 0

    def test_failing(self) -> None:
        crd = Mock()
        crd.list_cluster_custom_object.return_value = {
            "items": [{"status": {"conditions": [{"type": "Succeeded", "status": "False"}]}}]
        }
        assert _get_failing_pipelines(crd) == 1

    def test_exception_returns_zero(self) -> None:
        crd = Mock()
        crd.list_cluster_custom_object.side_effect = Exception("boom")
        assert _get_failing_pipelines(crd) == 0
