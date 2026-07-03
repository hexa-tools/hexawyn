"""Unit tests for the log_anomaly_detector domain service.

Covers all 4 acceptance test scenarios (TC1-TC4) and both documented edge
cases for the detect_log_anomalies use case (ECA-14 dependency).
"""

from __future__ import annotations

from hexawyn.domain.models.analyze_pod_logs import PodLogLine
from hexawyn.domain.models.log_anomaly import DetectLogAnomaliesRequest
from hexawyn.domain.services.log_analysis.log_anomaly_detector import detect_log_anomalies


def _line(minute: str, message: str, is_json: bool = False, hour: str = "14") -> PodLogLine:
    return PodLogLine(
        timestamp=f"2024-01-01T{hour}:{minute}:00Z",
        level="INFO",
        message=message,
        run_index=0,
        is_json=is_json,
    )


class TestDetectLogAnomaliesVolumeSpike:
    """TC1: Log volume spike at 14:32 (10x normal) → volume anomaly with Z-score."""

    def test_spike_minute_flagged_as_volume_anomaly(self) -> None:
        lines = []
        for minute in range(10, 30):
            lines += [_line(f"{minute:02d}", "heartbeat ok") for _ in range(5)]
        lines += [_line("32", "heartbeat ok") for _ in range(50)]
        request = DetectLogAnomaliesRequest(pod_name="inventory-service", namespace="prod")

        result = detect_log_anomalies(request, lines)

        volume_anomalies = [a for a in result.anomalies if a.type == "volume"]
        assert len(volume_anomalies) == 1
        assert volume_anomalies[0].timestamp == "2024-01-01T14:32"
        assert volume_anomalies[0].anomaly_score > 3.0


class TestDetectLogAnomaliesSilentError:
    """TC2: Silent slow DB query (no 'ERROR' keyword) → detected by Isolation Forest."""

    def test_silent_slow_query_detected_without_error_keyword(self) -> None:
        lines = []
        for minute in range(20):
            for i in range(5):
                if minute == 10 and i < 3:
                    message = "DB query completed in 8000ms"
                else:
                    message = f"DB query completed in {5 + (i % 3)}ms"
                lines.append(_line(f"{minute:02d}", message, hour="10"))
        request = DetectLogAnomaliesRequest(pod_name="inventory-service", namespace="prod")

        result = detect_log_anomalies(request, lines)

        semantic_anomalies = [a for a in result.anomalies if a.type == "semantic"]
        assert len(semantic_anomalies) >= 1
        assert all("error" not in a.log_line.lower() for a in semantic_anomalies)
        assert any("8000ms" in a.log_line for a in semantic_anomalies)


class TestDetectLogAnomaliesNormalLogs:
    """TC3: Completely normal logs → "no anomalies detected" with baseline stats."""

    def test_normal_logs_return_no_anomalies_with_baseline(self) -> None:
        lines = []
        for minute in range(20):
            lines += [_line(f"{minute:02d}", "heartbeat ok", hour="09") for _ in range(5)]
        request = DetectLogAnomaliesRequest(pod_name="inventory-service", namespace="prod")

        result = detect_log_anomalies(request, lines)

        assert result.anomalies == []
        assert result.summary == "no anomalies detected"
        assert result.baseline_mean_lines_per_minute > 0.0


class TestDetectLogAnomaliesInsufficientData:
    """TC4: Less than 100 log lines → warning "insufficient data for statistical analysis"."""

    def test_fewer_than_100_lines_returns_insufficient_data_warning(self) -> None:
        lines = [_line("00", "heartbeat ok") for _ in range(42)]
        request = DetectLogAnomaliesRequest(pod_name="inventory-service", namespace="prod")

        result = detect_log_anomalies(request, lines)

        assert result.insufficient_data is True
        assert result.summary == "insufficient data for statistical analysis"
        assert result.anomalies == []


class TestDetectLogAnomaliesEdgeCases:
    def test_format_change_mid_window_analyzed_separately(self) -> None:
        """Log format changes mid-window → each format analyzed separately."""
        plain_lines = [_line(f"{minute:02d}", "heartbeat ok") for minute in range(10)]
        json_lines = [
            _line(f"{minute:02d}", '{"event": "heartbeat", "status": "ok"}', is_json=True)
            for minute in range(10, 20)
        ]
        lines = plain_lines * 5 + json_lines * 5
        request = DetectLogAnomaliesRequest(pod_name="inventory-service", namespace="prod")

        result = detect_log_anomalies(request, lines)

        assert result.formats_analyzed_separately == 2

    def test_anomaly_in_first_10_lines_flagged_low_confidence(self) -> None:
        """Anomaly detected in first 10 lines → still returned with low-confidence flag."""
        lines = [_line("00", "DB query completed in 9000ms")]
        lines += [
            _line(f"{minute:02d}", f"DB query completed in {5 + (i % 3)}ms")
            for minute in range(20)
            for i in range(5)
        ][:99]
        request = DetectLogAnomaliesRequest(pod_name="inventory-service", namespace="prod")

        result = detect_log_anomalies(request, lines)

        semantic_anomalies = [a for a in result.anomalies if a.type == "semantic"]
        first_line_anomalies = [a for a in semantic_anomalies if "9000ms" in a.log_line]
        assert len(first_line_anomalies) == 1
        assert first_line_anomalies[0].low_confidence is True
