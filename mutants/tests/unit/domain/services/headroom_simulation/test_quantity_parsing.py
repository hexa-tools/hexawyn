"""Unit tests for parse_cpu_quantity / parse_memory_quantity — pure K8s
quantity-string parsing (human-typed strings, no client objects involved)."""

from __future__ import annotations

import pytest
from hexawyn.domain.services.headroom_simulation.quantity_parsing import (
    parse_cpu_quantity,
    parse_memory_quantity,
)


class TestParseCpuQuantity:
    def test_millicore_suffix(self) -> None:
        assert parse_cpu_quantity("500m") == pytest.approx(0.5)

    def test_bare_core_value(self) -> None:
        assert parse_cpu_quantity("2") == pytest.approx(2.0)

    def test_microcore_suffix(self) -> None:
        assert parse_cpu_quantity("500000u") == pytest.approx(0.5)

    def test_nanocore_suffix(self) -> None:
        assert parse_cpu_quantity("500000000n") == pytest.approx(0.5)

    def test_unparseable_value_returns_zero(self) -> None:
        assert parse_cpu_quantity("not-a-number") == 0.0

    def test_nanocore_exact_value(self) -> None:
        assert parse_cpu_quantity("1000000000n") == pytest.approx(1.0)

    def test_single_nanocore_exact(self) -> None:
        assert parse_cpu_quantity("1n") == 1e-9  # noqa: PLR2004

    def test_microcore_exact_value(self) -> None:
        assert parse_cpu_quantity("1000000u") == pytest.approx(1.0)

    def test_single_microcore_exact(self) -> None:
        assert parse_cpu_quantity("1u") == 1e-6  # noqa: PLR2004

    def test_uppercase_suffix_not_parsed_as_nano(self) -> None:
        assert parse_cpu_quantity("500N") == 0.0

    def test_uppercase_suffix_not_parsed_as_micro(self) -> None:
        assert parse_cpu_quantity("500U") == 0.0

    def test_uppercase_suffix_not_parsed_as_milli(self) -> None:
        assert parse_cpu_quantity("500M") == 0.0

    def test_decimal_core_value(self) -> None:
        assert parse_cpu_quantity("1.5") == pytest.approx(1.5)


class TestParseMemoryQuantity:
    def test_mebibyte_suffix_converted_to_gb(self) -> None:
        assert parse_memory_quantity("512Mi") == pytest.approx(512 / 1024)

    def test_gibibyte_suffix(self) -> None:
        assert parse_memory_quantity("2Gi") == pytest.approx(2.0)

    def test_kibibyte_suffix(self) -> None:
        assert parse_memory_quantity("1048576Ki") == pytest.approx(1.0)

    def test_bare_bytes_value(self) -> None:
        assert parse_memory_quantity(str(1024**3)) == pytest.approx(1.0)

    def test_unparseable_value_returns_zero(self) -> None:
        assert parse_memory_quantity("garbage") == 0.0

    def test_tebibyte_suffix(self) -> None:
        assert parse_memory_quantity("1Ti") == pytest.approx(1024.0)

    def test_multi_tibibyte_suffix(self) -> None:
        assert parse_memory_quantity("2Ti") == pytest.approx(2048.0)

    def test_uppercase_gi_suffix(self) -> None:
        assert parse_memory_quantity("2GI") == 0.0

    def test_mebibyte_fractional(self) -> None:
        assert parse_memory_quantity("1536Mi") == pytest.approx(1.5)

    def test_negative_quantity_parsed(self) -> None:
        assert parse_memory_quantity("-1Gi") == pytest.approx(-1.0)
