from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
    _is_daemonset,
    _node_allocatable,
)
from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
    _detect_level,
)
from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
    _parse_message,
    _split_timestamp,
)


class TestSplitTimestamp:
    def test_valid_iso(self) -> None:
        ts, msg = _split_timestamp("2026-01-01T00:00:00Z hello world")
        assert ts == "2026-01-01T00:00:00Z"
        assert msg == "hello world"

    def test_no_timestamp(self) -> None:
        ts, msg = _split_timestamp("hello world")
        assert ts == ""
        assert msg == "hello world"

    def test_short_token(self) -> None:
        ts, msg = _split_timestamp("abc def")
        assert ts == ""


class TestParseMessage:
    def test_plain(self) -> None:
        is_json, msg, level = _parse_message("hello")
        assert not is_json
        assert msg == "hello"
        assert level == "INFO"

    def test_json(self) -> None:
        is_json, msg, level = _parse_message('{"msg":"error occurred","level":"ERROR"}')
        assert is_json
        assert msg == "error occurred"
        assert level == "ERROR"

    def test_json_fallback(self) -> None:
        is_json, msg, level = _parse_message('{"not_msg":"x"}')
        assert is_json
        assert msg == '{"not_msg":"x"}'
        assert level == "INFO"

    def test_invalid_json(self) -> None:
        is_json, msg, level = _parse_message("{invalid}")
        assert not is_json
        assert msg == "{invalid}"


class TestDetectLevel:
    def test_error(self) -> None:
        assert _detect_level("ERROR: something happened") == "ERROR"

    def test_warn(self) -> None:
        assert _detect_level("WARNING: low memory") == "WARN"

    def test_info_default(self) -> None:
        assert _detect_level("all good") == "INFO"

    def test_fatal(self) -> None:
        assert _detect_level("FATAL: crash") == "ERROR"


class TestIsDaemonSet:
    def test_daemonset(self) -> None:
        ref = Mock(kind="DaemonSet")
        pod = Mock(metadata=Mock(owner_references=[ref]))
        assert _is_daemonset(pod) is True

    def test_not_daemonset(self) -> None:
        ref = Mock(kind="Deployment")
        pod = Mock(metadata=Mock(owner_references=[ref]))
        assert _is_daemonset(pod) is False

    def test_no_owners(self) -> None:
        pod = Mock(metadata=Mock(owner_references=None))
        assert _is_daemonset(pod) is False


class TestNodeAllocatable:
    def test_with_data(self) -> None:
        node = Mock(status=Mock(allocatable={"cpu": "4", "memory": "16Gi"}))
        assert _node_allocatable(node) == {"cpu": "4", "memory": "16Gi"}

    def test_no_allocatable(self) -> None:
        node = Mock(status=None)
        assert _node_allocatable(node) == {}
