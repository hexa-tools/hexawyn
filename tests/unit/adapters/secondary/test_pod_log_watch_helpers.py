from __future__ import annotations

from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
    _detect_level,
    _parse_line,
    _parse_message,
    _split_timestamp,
)


class TestWatchParseLine:
    def test_produces_pod_log_line(self) -> None:
        import json

        line = json.dumps({"msg": "test", "level": "INFO"})
        result = _parse_line(f"2024-01-01T00:00:00.000000000Z {line}")
        assert result.message == "test"
        assert result.level == "INFO"
        assert result.run_index == 0

    def test_plain_line(self) -> None:
        result = _parse_line("2024-01-01T00:00:00.000000000Z ERROR: boom")
        assert result.level == "ERROR"
        assert result.run_index == 0


class TestWatchSplitTimestamp:
    def test_iso_timestamp(self) -> None:
        ts, msg = _split_timestamp("2024-01-01T00:00:00.000Z hello")
        assert ts == "2024-01-01T00:00:00.000Z"
        assert msg == "hello"

    def test_no_timestamp(self) -> None:
        ts, msg = _split_timestamp("plain text")
        assert ts == ""
        assert msg == "plain text"


class TestWatchParseMessage:
    def test_json_message(self) -> None:
        import json

        is_json, msg, level = _parse_message(json.dumps({"msg": "hello"}))
        assert is_json is True
        assert msg == "hello"

    def test_plain_message(self) -> None:
        is_json, msg, level = _parse_message("INFO all good")
        assert is_json is False
        assert level == "INFO"


class TestWatchDetectLevel:
    def test_error(self) -> None:
        assert _detect_level("ERROR: fail") == "ERROR"

    def test_info_default(self) -> None:
        assert _detect_level("nothing special") == "INFO"
