from unittest.mock import MagicMock, patch

from hexawyn.infrastructure.config.telemetry import (
    is_telemetry_enabled,
    send_investigation_telemetry,
    send_startup_telemetry,
)


class TestIsTelemetryEnabled:
    def test_enabled_when_env_is_true(self) -> None:
        with patch.dict("os.environ", {"HEXAWYN_TELEMETRY": "true"}):
            assert is_telemetry_enabled() is True

    def test_disabled_when_env_not_set(self) -> None:
        with patch.dict("os.environ", {}, clear=True):
            assert is_telemetry_enabled() is False

    def test_disabled_when_env_is_false(self) -> None:
        with patch.dict("os.environ", {"HEXAWYN_TELEMETRY": "false"}):
            assert is_telemetry_enabled() is False

    def test_case_insensitive_true(self) -> None:
        with patch.dict("os.environ", {"HEXAWYN_TELEMETRY": "TRUE"}):
            assert is_telemetry_enabled() is True


class TestSendTelemetry:
    def test_startup_skips_when_disabled(self) -> None:
        with patch.dict("os.environ", {"HEXAWYN_TELEMETRY": "false"}):
            with patch("threading.Thread.start") as mock_start:
                send_startup_telemetry()
                mock_start.assert_not_called()

    def test_startup_sends_when_enabled(self) -> None:
        with patch.dict("os.environ", {"HEXAWYN_TELEMETRY": "true"}):
            with patch(
                "hexawyn.infrastructure.config.telemetry.get_license_tier",
                return_value=MagicMock(value="starter"),
            ):
                with patch("threading.Thread.start") as mock_start:
                    send_startup_telemetry()
                    mock_start.assert_called_once()

    def test_investigation_skips_when_disabled(self) -> None:
        with patch.dict("os.environ", {"HEXAWYN_TELEMETRY": "false"}):
            with patch("threading.Thread.start") as mock_start:
                send_investigation_telemetry(investigation_count=23)
                mock_start.assert_not_called()

    def test_investigation_sends_when_enabled(self) -> None:
        with patch.dict("os.environ", {"HEXAWYN_TELEMETRY": "true"}):
            with patch(
                "hexawyn.infrastructure.config.telemetry.get_license_tier",
                return_value=MagicMock(value="dev"),
            ):
                with patch("threading.Thread.start") as mock_start:
                    send_investigation_telemetry(investigation_count=45)
                    mock_start.assert_called_once()

    def test_payload_includes_tier_and_count(self) -> None:
        with patch.dict("os.environ", {"HEXAWYN_TELEMETRY": "true"}):
            with patch(
                "hexawyn.infrastructure.config.telemetry.get_license_tier",
                return_value=MagicMock(value="team"),
            ):
                with patch("threading.Thread") as mock_thread_cls:
                    send_investigation_telemetry(investigation_count=300)
                    args = mock_thread_cls.call_args[1]["args"]
                    payload = args[0]
                    assert payload["event"] == "investigation"
                    assert payload["tier"] == "team"
                    assert payload["monthly_count"] == 300
                    assert payload["version"] == "0.1.0"
