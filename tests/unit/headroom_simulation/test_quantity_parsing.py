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
