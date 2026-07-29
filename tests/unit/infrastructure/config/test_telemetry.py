from __future__ import annotations

import os
from unittest.mock import patch

from hexawyn.infrastructure.config.telemetry import (
    is_telemetry_enabled,
    send_investigation_telemetry,
    send_startup_telemetry,
)


class TestIsTelemetryEnabled:
    def test_defaults_to_disabled(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            assert is_telemetry_enabled() is False

    def test_true_enables(self) -> None:
        with patch.dict(os.environ, {"HEXAWYN_TELEMETRY": "true"}, clear=True):
            assert is_telemetry_enabled() is True

    def test_false_disables(self) -> None:
        with patch.dict(os.environ, {"HEXAWYN_TELEMETRY": "false"}, clear=True):
            assert is_telemetry_enabled() is False


class TestSendStartupTelemetry:
    def test_skips_when_disabled(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            with patch("hexawyn.infrastructure.config.telemetry.threading.Thread") as mock_thread:
                send_startup_telemetry()
                mock_thread.assert_not_called()

    def test_sends_when_enabled(self) -> None:
        with patch.dict(os.environ, {"HEXAWYN_TELEMETRY": "true"}, clear=True):
            with patch("hexawyn.infrastructure.config.telemetry.threading.Thread") as mock_thread:
                send_startup_telemetry()
                mock_thread.assert_called_once()


class TestSendInvestigationTelemetry:
    def test_skips_when_disabled(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            with patch("hexawyn.infrastructure.config.telemetry.threading.Thread") as mock_thread:
                send_investigation_telemetry(5)
                mock_thread.assert_not_called()

    def test_sends_when_enabled(self) -> None:
        with patch.dict(os.environ, {"HEXAWYN_TELEMETRY": "true"}, clear=True):
            with patch("hexawyn.infrastructure.config.telemetry.threading.Thread") as mock_thread:
                send_investigation_telemetry(5)
                mock_thread.assert_called_once()
