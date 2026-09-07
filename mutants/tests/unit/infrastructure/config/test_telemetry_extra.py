"""Additional tests for telemetry.py covering _send_telemetry and payloads."""

from __future__ import annotations

import json
from unittest.mock import patch

from hexawyn.domain.models.quota import LicenseTier
from hexawyn.infrastructure.config import telemetry


class TestSendTelemetryFunction:
    """Cover _send_telemetry function (lines 19-32)."""

    def test_sends_post_with_correct_payload(self) -> None:
        payload: dict[str, str | int] = {"event": "startup", "version": "0.1.0"}
        with patch("urllib.request.urlopen") as mock_urlopen:
            telemetry._send_telemetry(payload)

        mock_urlopen.assert_called_once()
        call_args = mock_urlopen.call_args[0]
        request = call_args[0]
        assert request.get_full_url() == telemetry.TELEMETRY_URL
        assert request.get_method() == "POST"
        data = json.loads(request.data)
        assert data["event"] == "startup"

    def test_handles_http_error_gracefully(self) -> None:
        with patch("urllib.request.urlopen", side_effect=OSError("network down")):
            telemetry._send_telemetry({"event": "test"})

    def test_handles_timeout_gracefully(self) -> None:
        with patch("urllib.request.urlopen", side_effect=Exception("timeout")):
            telemetry._send_telemetry({"event": "test"})


class TestTelemetryPayloadStructure:
    """Verify telemetry payload structure and edge cases."""

    def test_startup_payload_thread_created(self) -> None:
        with patch("os.environ", {"HEXAWYN_TELEMETRY": "true"}):
            with patch.object(telemetry, "get_license_tier", return_value=LicenseTier.STARTER):
                with patch("threading.Thread") as mock_thread:
                    telemetry.send_startup_telemetry()
                    mock_thread.assert_called_once()

    def test_investigation_payload_thread_created(self) -> None:
        with patch("os.environ", {"HEXAWYN_TELEMETRY": "true"}):
            with patch.object(telemetry, "get_license_tier", return_value=LicenseTier.TEAM):
                with patch("threading.Thread") as mock_thread:
                    telemetry.send_investigation_telemetry(42)
                    mock_thread.assert_called_once()

    def test_thread_target_is_send_telemetry(self) -> None:
        with patch("os.environ", {"HEXAWYN_TELEMETRY": "true"}):
            with patch.object(telemetry, "get_license_tier", return_value=LicenseTier.SCALE_UP):
                with patch("threading.Thread") as mock_thread:
                    telemetry.send_investigation_telemetry(100)
                    call_kwargs = mock_thread.call_args[1]
                    assert call_kwargs["target"] == telemetry._send_telemetry
                    assert call_kwargs["daemon"] is True
