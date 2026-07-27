from __future__ import annotations

from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
    _merge,
    _parse_cpu,
    _parse_memory,
)


class TestParseCpu:
    def test_empty(self) -> None:
        assert _parse_cpu(None) is None
        assert _parse_cpu("") is None

    def test_millicores(self) -> None:
        assert _parse_cpu("500m") == 500  # noqa: PLR2004

    def test_cores_float(self) -> None:
        assert _parse_cpu("0.5") == 500  # noqa: PLR2004

    def test_cores_int(self) -> None:
        assert _parse_cpu("2") == 2000  # noqa: PLR2004

    def test_invalid(self) -> None:
        assert _parse_cpu("abc") is None


class TestParseMemory:
    def test_empty(self) -> None:
        assert _parse_memory(None) is None
        assert _parse_memory("") is None

    def test_mi(self) -> None:
        assert _parse_memory("256Mi") == 256 * 1024 * 1024

    def test_gi(self) -> None:
        assert _parse_memory("1Gi") == 1024**3

    def test_bytes(self) -> None:
        assert _parse_memory("128974848") == 128974848  # noqa: PLR2004

    def test_invalid(self) -> None:
        assert _parse_memory("xyz") is None


class TestMerge:
    def test_empty(self) -> None:
        result = _merge({}, {}, "ns")
        assert result == []

    def test_with_data(self) -> None:
        limits = {
            "pod-1": [("app", 500, 256 * 1024 * 1024, False)],
        }
        usage = {"pod-1": {"app": (200, 100 * 1024 * 1024)}}
        result = _merge(limits, usage, "default")
        assert len(result) == 1
        assert result[0]["container_name"] == "app"
        assert result[0]["pod_name"] == "pod-1"
        assert result[0]["cpu_limit_millicores"] == 500  # noqa: PLR2004
        assert result[0]["cpu_usage_millicores"] == 200  # noqa: PLR2004

    def test_missing_usage_defaults_to_zero(self) -> None:
        limits = {"pod-1": [("app", 1000, 512 * 1024 * 1024, True)]}
        result = _merge(limits, {}, "ns")
        assert len(result) == 1
        assert result[0]["cpu_usage_millicores"] == 0
        assert result[0]["memory_usage_bytes"] == 0
        assert result[0]["is_init_container"] is True
