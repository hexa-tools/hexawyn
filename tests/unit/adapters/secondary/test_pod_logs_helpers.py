from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
    _detect_level,
    _parse_message,
    _split_timestamp,
    _translate_error,
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


class TestSplitTimestamp:
    def test_iso_timestamp(self) -> None:
        ts, msg = _split_timestamp("2024-01-01T00:00:00.000Z hello world")
        assert ts == "2024-01-01T00:00:00.000Z"
        assert msg == "hello world"

    def test_no_timestamp(self) -> None:
        ts, msg = _split_timestamp("hello world")
        assert ts == ""
        assert msg == "hello world"

    def test_short_timestamp_ignored(self) -> None:
        ts, msg = _split_timestamp("2024-01-01T00Z hi")
        assert ts == ""
        assert msg == "2024-01-01T00Z hi"


class TestParseMessage:
    def test_json_with_msg_field(self) -> None:
        import json

        is_json, msg, level = _parse_message(json.dumps({"msg": "hello", "level": "error"}))
        assert is_json is True
        assert msg == "hello"
        assert level == "ERROR"

    def test_json_with_message_field(self) -> None:
        import json

        _, msg, _ = _parse_message(json.dumps({"message": "test"}))
        assert msg == "test"

    def test_json_with_error_field(self) -> None:
        import json

        _, msg, _ = _parse_message(json.dumps({"error": "oops"}))
        assert msg == "oops"

    def test_plain_text(self) -> None:
        is_json, msg, level = _parse_message("ERROR something went wrong")
        assert is_json is False
        assert msg == "ERROR something went wrong"
        assert level == "ERROR"

    def test_invalid_json(self) -> None:
        is_json, msg, _ = _parse_message("{invalid")
        assert is_json is False


class TestDetectLevel:
    def test_fatal_becomes_error(self) -> None:
        assert _detect_level("FATAL: crash") == "ERROR"

    def test_error(self) -> None:
        assert _detect_level("ERROR: fail") == "ERROR"

    def test_warn(self) -> None:
        assert _detect_level("WARN: something") == "WARN"

    def test_warning(self) -> None:
        assert _detect_level("WARNING: be careful") == "WARN"

    def test_info(self) -> None:
        assert _detect_level("INFO: all good") == "INFO"

    def test_debug(self) -> None:
        assert _detect_level("DEBUG: trace") == "DEBUG"

    def test_default_is_info(self) -> None:
        assert _detect_level("hello world") == "INFO"

    def test_case_insensitive(self) -> None:
        assert _detect_level("Error: fail") == "ERROR"


class TestTranslateErrorPodLogs:
    def test_not_found(self) -> None:
        req = _mk(pod_name="p", namespace="n")
        assert isinstance(_translate_error(_mk(status=404), req), ResourceNotFoundError)

    def test_forbidden(self) -> None:
        req = _mk(pod_name="p", namespace="n")
        assert isinstance(_translate_error(_mk(status=403), req), InsufficientPermissionsError)

    def test_other(self) -> None:
        req = _mk(pod_name="p", namespace="n")
        assert isinstance(_translate_error(Exception("err"), req), ClusterUnreachableError)
