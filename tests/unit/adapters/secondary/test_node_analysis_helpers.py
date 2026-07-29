from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
    KubernetesNodeAnalysisAdapter,
    _cpu_to_cores,
    _float_prefix,
    _is_daemonset,
    _memory_to_bytes,
    _node_allocatable,
    _node_allocatable_cpu,
    _node_allocatable_memory_gb,
    _safe_float,
    _translate_error,
)
from hexawyn.application.ports.driven.hot_node_analysis_port import (
    HotNodeAnalysisPort,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _mk(**attrs: object) -> Mock:
    m = Mock()
    for k, v in attrs.items():
        setattr(m, k, v)
    return m


class TestKubernetesNodeAnalysisAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesNodeAnalysisAdapter(), HotNodeAnalysisPort)


class TestIsDaemonSet:
    def test_daemonset_owner_returns_true(self) -> None:
        pod = _mk(metadata=_mk(owner_references=[_mk(kind="DaemonSet")]))
        assert _is_daemonset(pod) is True

    def test_deployment_owner_returns_false(self) -> None:
        pod = _mk(metadata=_mk(owner_references=[_mk(kind="Deployment")]))
        assert _is_daemonset(pod) is False

    def test_no_owner_references_returns_false(self) -> None:
        pod = _mk(metadata=_mk(owner_references=[]))
        assert _is_daemonset(pod) is False

    def test_none_owner_references_returns_false(self) -> None:
        pod = _mk(metadata=_mk(owner_references=None))
        assert _is_daemonset(pod) is False

    def test_no_metadata_returns_false(self) -> None:
        pod = _mk(metadata=None)
        assert _is_daemonset(pod) is False

    def test_owner_refs_not_list_returns_false(self) -> None:
        pod = _mk(metadata=_mk(owner_references="bad"))
        assert _is_daemonset(pod) is False


class TestNodeAnalysisCpuToCores:
    def test_nano(self) -> None:
        assert _cpu_to_cores("1000n") == 1000 / 1_000_000_000

    def test_milli(self) -> None:
        assert _cpu_to_cores("100m") == 0.1  # noqa: PLR2004

    def test_plain(self) -> None:
        assert _cpu_to_cores("1") == 1.0


class TestNodeAnalysisMemoryToBytes:
    def test_ki(self) -> None:
        assert _memory_to_bytes("1Ki") == 1024.0  # noqa: PLR2004

    def test_gi(self) -> None:
        assert _memory_to_bytes("1Gi") == 1024.0**3


class TestNodeAnalysisNodeAllocatable:
    def test_returns_empty_on_none(self) -> None:
        assert _node_allocatable(_mk(status=None)) == {}


class TestNodeAnalysisNodeAllocatableCpu:
    def test_parses(self) -> None:
        node = _mk(status=_mk(allocatable={"cpu": "1000m"}))
        assert _node_allocatable_cpu(node) == 1.0


class TestNodeAnalysisNodeAllocatableMemoryGb:
    def test_parses(self) -> None:
        node = _mk(status=_mk(allocatable={"memory": "1Gi"}))
        assert _node_allocatable_memory_gb(node) == 1.0


class TestNodeAnalysisSafeFloat:
    def test_valid(self) -> None:
        assert _safe_float("1.5") == 1.5  # noqa: PLR2004

    def test_invalid(self) -> None:
        assert _safe_float("bad") == 0.0


class TestNodeAnalysisFloatPrefix:
    def test_strips(self) -> None:
        assert _float_prefix("100m", "m") == 100.0  # noqa: PLR2004


class TestNodeAnalysisTranslateError:
    def test_forbidden(self) -> None:
        assert isinstance(_translate_error(_mk(status=403)), InsufficientPermissionsError)

    def test_other(self) -> None:
        assert isinstance(_translate_error(Exception("err")), ClusterUnreachableError)
