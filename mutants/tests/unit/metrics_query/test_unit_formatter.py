"""Unit tests for format_metric_value — human-readable unit formatting."""

from __future__ import annotations

from hexawyn.domain.services.metrics_query.unit_formatter import format_metric_value


class TestCoresFormatting:
    def test_0_003_cores_formatted_as_3m_cores(self) -> None:
        assert format_metric_value(0.003, "cores") == "3m cores"

    def test_0_0032_cores_formatted_as_3_2m_cores(self) -> None:
        assert format_metric_value(0.0032, "cores") == "3.2m cores"

    def test_value_above_one_core_formatted_as_cores(self) -> None:
        assert format_metric_value(1.5, "cores") == "1.50 cores"

    def test_zero_cores(self) -> None:
        assert format_metric_value(0.0, "cores") == "0m cores"


class TestBytesFormatting:
    def test_bytes_below_kilobyte(self) -> None:
        assert format_metric_value(512, "bytes") == "512 B"

    def test_megabytes(self) -> None:
        assert format_metric_value(52_428_800, "bytes") == "52.43 MB"

    def test_gigabytes(self) -> None:
        assert format_metric_value(2_147_483_648, "bytes") == "2.15 GB"

    def test_kilobytes(self) -> None:
        assert format_metric_value(4_096, "bytes") == "4.10 KB"


class TestPercentFormatting:
    def test_percent_one_decimal(self) -> None:
        assert format_metric_value(87.654, "percent") == "87.7%"


class TestRawFormatting:
    def test_raw_returns_plain_number(self) -> None:
        assert format_metric_value(42.0, "raw") == "42"

    def test_raw_keeps_decimal_when_not_integral(self) -> None:
        assert format_metric_value(42.5, "raw") == "42.5"
