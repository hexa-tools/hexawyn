from __future__ import annotations

from hexawyn.adapters.secondary.kubernetes_pod_resource_adapter import (
    _merge,
    _parse_cpu,
    _parse_memory,
)


class TestParseCpu:
    def test_millicores(self) -> None:
        assert _parse_cpu("500m") == 500  # noqa: PLR2004

    def test_cores_as_float(self) -> None:
        assert _parse_cpu("0.5") == 500  # noqa: PLR2004

    def test_cores_as_int(self) -> None:
        assert _parse_cpu("2") == 2000  # noqa: PLR2004

    def test_none_returns_none(self) -> None:
        assert _parse_cpu(None) is None

    def test_empty_string_returns_none(self) -> None:
        assert _parse_cpu("") is None

    def test_invalid_string_returns_none(self) -> None:
        assert _parse_cpu("invalid") is None

    def test_strips_whitespace(self) -> None:
        assert _parse_cpu(" 500m ") == 500  # noqa: PLR2004


class TestParseMemory:
    def test_ki(self) -> None:
        assert _parse_memory("1Ki") == 1024  # noqa: PLR2004

    def test_mi(self) -> None:
        assert _parse_memory("1Mi") == 1024**2

    def test_gi(self) -> None:
        assert _parse_memory("1Gi") == 1024**3

    def test_ti(self) -> None:
        assert _parse_memory("1Ti") == 1024**4

    def test_k(self) -> None:
        assert _parse_memory("1K") == 1000  # noqa: PLR2004

    def test_m(self) -> None:
        assert _parse_memory("1M") == 1000**2

    def test_g(self) -> None:
        assert _parse_memory("1G") == 1000**3

    def test_t(self) -> None:
        assert _parse_memory("1T") == 1000**4

    def test_plain_bytes(self) -> None:
        assert _parse_memory("1000") == 1000  # noqa: PLR2004

    def test_none_returns_none(self) -> None:
        assert _parse_memory(None) is None

    def test_empty_returns_none(self) -> None:
        assert _parse_memory("") is None

    def test_invalid_returns_none(self) -> None:
        assert _parse_memory("invalid") is None

    def test_decimal_gi(self) -> None:
        assert _parse_memory("0.5Gi") == 536870912  # int(0.5 * 1024**3)  # noqa: PLR2004


class TestMerge:
    def test_basic_merge(self) -> None:
        limits: dict[str, list[tuple[str, int | None, int | None, bool]]] = {
            "pod-a": [("main", 100, 1024, False)],
        }
        usage: dict[str, dict[str, tuple[int, int]]] = {
            "pod-a": {"main": (50, 512)},
        }
        result = _merge(limits, usage, "default")
        assert len(result) == 1
        assert result[0]["container_name"] == "main"
        assert result[0]["pod_name"] == "pod-a"
        assert result[0]["namespace"] == "default"
        assert result[0]["cpu_usage_millicores"] == 50  # noqa: PLR2004
        assert result[0]["cpu_limit_millicores"] == 100  # noqa: PLR2004
        assert result[0]["memory_usage_bytes"] == 512  # noqa: PLR2004
        assert result[0]["memory_limit_bytes"] == 1024  # noqa: PLR2004
        assert result[0]["is_init_container"] is False

    def test_missing_usage_defaults_to_zero(self) -> None:
        limits = {"pod-a": [("main", 100, 1024, False)]}
        usage: dict[str, dict[str, tuple[int, int]]] = {}
        result = _merge(limits, usage, "ns")
        assert result[0]["cpu_usage_millicores"] == 0
        assert result[0]["memory_usage_bytes"] == 0

    def test_init_container_flag(self) -> None:
        limits = {"pod-a": [("init", 50, 512, True)]}
        usage = {"pod-a": {"init": (10, 100)}}
        result = _merge(limits, usage, "ns")
        assert result[0]["is_init_container"] is True

    def test_multiple_containers(self) -> None:
        limits = {
            "pod-a": [
                ("init", 50, 512, True),
                ("main", 200, 2048, False),
            ],
        }
        usage = {"pod-a": {"init": (10, 100), "main": (150, 1024)}}
        result = _merge(limits, usage, "ns")
        assert len(result) == 2  # noqa: PLR2004
