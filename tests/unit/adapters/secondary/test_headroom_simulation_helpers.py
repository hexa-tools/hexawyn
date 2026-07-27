from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
    KubernetesHeadroomSimulationAdapter,
    _cpu_to_cores,
    _float_prefix,
    _memory_to_bytes,
    _node_allocatable,
    _node_allocatable_cpu,
    _node_allocatable_memory_gb,
    _safe_float,
    _translate_error,
)
from hexawyn.application.ports.driven.headroom_simulation_port import (
    HeadroomSimulationPort,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _mk(**attrs: object) -> Mock:
    m = Mock()
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestKubernetesHeadroomSimulationAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesHeadroomSimulationAdapter(), HeadroomSimulationPort)


class TestHeadroomCpuToCores:
    def test_nano_cores(self) -> None:
        assert _cpu_to_cores("500n") == 500 / 1_000_000_000

    def test_micro_cores(self) -> None:
        assert _cpu_to_cores("500u") == 500 / 1_000_000

    def test_milli_cores(self) -> None:
        assert _cpu_to_cores("500m") == 0.5  # noqa: PLR2004

    def test_plain_number(self) -> None:
        assert _cpu_to_cores("2") == 2.0  # noqa: PLR2004


class TestHeadroomMemoryToBytes:
    def test_ki(self) -> None:
        assert _memory_to_bytes("1Ki") == 1024.0  # noqa: PLR2004

    def test_mi(self) -> None:
        assert _memory_to_bytes("1Mi") == 1024.0**2

    def test_gi(self) -> None:
        assert _memory_to_bytes("1Gi") == 1024.0**3

    def test_ti(self) -> None:
        assert _memory_to_bytes("1Ti") == 1024.0**4


class TestHeadroomFloatPrefix:
    def test_strips_suffix(self) -> None:
        assert _float_prefix("500m", "m") == 500.0  # noqa: PLR2004


class TestHeadroomSafeFloat:
    def test_valid_number(self) -> None:
        assert _safe_float("3.14") == 3.14  # noqa: PLR2004

    def test_invalid_string_returns_zero(self) -> None:
        assert _safe_float("not-a-number") == 0.0


class TestHeadroomNodeAllocatable:
    def test_returns_empty_dict_when_none(self) -> None:
        node = _mk(status=None)
        assert _node_allocatable(node) == {}


class TestHeadroomNodeAllocatableCpu:
    def test_parses_cpu(self) -> None:
        node = _mk(status=_mk(allocatable={"cpu": "4000m"}))
        assert _node_allocatable_cpu(node) == 4.0  # noqa: PLR2004


class TestHeadroomNodeAllocatableMemoryGb:
    def test_parses_memory(self) -> None:
        node = _mk(status=_mk(allocatable={"memory": "4Gi"}))
        assert _node_allocatable_memory_gb(node) == 4.0  # noqa: PLR2004


class TestHeadroomTranslateError:
    def test_forbidden(self) -> None:
        exc = _mk(status=403)
        result = _translate_error(exc)
        assert isinstance(result, InsufficientPermissionsError)

    def test_cluster_unreachable_no_status(self) -> None:
        exc = Exception("timeout")
        result = _translate_error(exc)
        assert isinstance(result, ClusterUnreachableError)
