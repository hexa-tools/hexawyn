from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
    KubernetesCapacityForecastAdapter,
    _cpu_to_cores,
    _float_prefix,
    _memory_to_bytes,
    _node_allocatable,
    _node_allocatable_cpu,
    _node_allocatable_memory_gb,
    _safe_float,
    _translate_error,
)
from hexawyn.application.ports.driven.capacity_forecast_port import (
    CapacityForecastPort,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _mk(**attrs: object) -> Mock:
    m = Mock()
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestKubernetesCapacityForecastAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesCapacityForecastAdapter(), CapacityForecastPort)


class TestCpuToCores:
    def test_nano_cores(self) -> None:
        assert _cpu_to_cores("500n") == 500 / 1_000_000_000

    def test_micro_cores(self) -> None:
        assert _cpu_to_cores("500u") == 500 / 1_000_000

    def test_milli_cores(self) -> None:
        assert _cpu_to_cores("500m") == 0.5  # noqa: PLR2004

    def test_plain_number(self) -> None:
        assert _cpu_to_cores("2") == 2.0  # noqa: PLR2004

    def test_zero(self) -> None:
        assert _cpu_to_cores("0") == 0.0


class TestMemoryToBytes:
    def test_ki(self) -> None:
        assert _memory_to_bytes("1Ki") == 1024.0  # noqa: PLR2004

    def test_mi(self) -> None:
        assert _memory_to_bytes("1Mi") == 1024.0**2

    def test_gi(self) -> None:
        assert _memory_to_bytes("1Gi") == 1024.0**3

    def test_ti(self) -> None:
        assert _memory_to_bytes("1Ti") == 1024.0**4

    def test_plain_number(self) -> None:
        assert _memory_to_bytes("500") == 500.0  # noqa: PLR2004


class TestFloatPrefix:
    def test_strips_suffix(self) -> None:
        assert _float_prefix("500m", "m") == 500.0  # noqa: PLR2004

    def test_handles_empty(self) -> None:
        assert _float_prefix("m", "m") == 0.0


class TestSafeFloat:
    def test_valid_number(self) -> None:
        assert _safe_float("3.14") == 3.14  # noqa: PLR2004

    def test_invalid_string_returns_zero(self) -> None:
        assert _safe_float("not-a-number") == 0.0

    def test_empty_string_returns_zero(self) -> None:
        assert _safe_float("") == 0.0


class TestNodeAllocatable:
    def test_returns_dict_from_status(self) -> None:
        node = _mk(status=_mk(allocatable={"cpu": "2", "memory": "4Gi"}))
        result = _node_allocatable(node)
        assert result == {"cpu": "2", "memory": "4Gi"}

    def test_returns_empty_dict_when_no_status(self) -> None:
        node = Mock(spec=[])
        assert _node_allocatable(node) == {}

    def test_returns_empty_dict_when_allocatable_not_dict(self) -> None:
        node = _mk(status=_mk(allocatable="bad"))
        assert _node_allocatable(node) == {}


class TestNodeAllocatableCpu:
    def test_parses_cpu_from_node(self) -> None:
        node = _mk(status=_mk(allocatable={"cpu": "2000m"}))
        assert _node_allocatable_cpu(node) == 2.0  # noqa: PLR2004


class TestNodeAllocatableMemoryGb:
    def test_parses_memory_from_node(self) -> None:
        node = _mk(status=_mk(allocatable={"memory": "2Gi"}))
        assert _node_allocatable_memory_gb(node) == 2.0  # noqa: PLR2004


class TestTranslateErrorCapacity:
    def test_forbidden_returns_insufficient_permissions(self) -> None:
        exc = _mk(status=403)
        result = _translate_error(exc)
        assert isinstance(result, InsufficientPermissionsError)

    def test_other_status_returns_cluster_unreachable(self) -> None:
        exc = _mk(status=500)
        result = _translate_error(exc)
        assert isinstance(result, ClusterUnreachableError)

    def test_no_status_returns_cluster_unreachable(self) -> None:
        exc = Exception("network error")
        result = _translate_error(exc)
        assert isinstance(result, ClusterUnreachableError)
