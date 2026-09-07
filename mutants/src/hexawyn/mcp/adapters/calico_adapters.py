"""Calico adapter builders — the chosen collaborators for the Calico series."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.calico_port import CalicoPort

if TYPE_CHECKING:
    from hexawyn.infrastructure.adapters.secondary.calico.calico_prometheus_adapter import (
        CalicoPrometheusAdapter,
    )


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_calico_metrics_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_calico_metrics_adapter__mutmut)
def build_calico_metrics_adapter() -> CalicoPrometheusAdapter:
    """Build the metrics-backed Calico collaborator (Felix metrics via Prometheus)."""
    from hexawyn.infrastructure.adapters.secondary.calico.calico_prometheus_adapter import (
        CalicoPrometheusAdapter,
    )
    from hexawyn.mcp.adapters.observability_adapters import build_metrics_query_adapter

    return CalicoPrometheusAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_calico_metrics_adapter__mutmut_orig() -> CalicoPrometheusAdapter:
    """Build the metrics-backed Calico collaborator (Felix metrics via Prometheus)."""
    from hexawyn.infrastructure.adapters.secondary.calico.calico_prometheus_adapter import (
        CalicoPrometheusAdapter,
    )
    from hexawyn.mcp.adapters.observability_adapters import build_metrics_query_adapter

    return CalicoPrometheusAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_calico_metrics_adapter__mutmut_1() -> CalicoPrometheusAdapter:
    """Build the metrics-backed Calico collaborator (Felix metrics via Prometheus)."""
    from hexawyn.infrastructure.adapters.secondary.calico.calico_prometheus_adapter import (
        CalicoPrometheusAdapter,
    )
    from hexawyn.mcp.adapters.observability_adapters import build_metrics_query_adapter

    return CalicoPrometheusAdapter(metrics_query_port=None)

mutants_x_build_calico_metrics_adapter__mutmut['_mutmut_orig'] = x_build_calico_metrics_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_calico_metrics_adapter__mutmut['x_build_calico_metrics_adapter__mutmut_1'] = x_build_calico_metrics_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_calico_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_calico_adapter__mutmut)
def build_calico_adapter() -> CalicoPort:
    """Build the primary Calico port (K8s CRD/agent detection)."""
    from hexawyn.infrastructure.adapters.secondary.calico.calico_k8s_adapter import CalicoK8sAdapter

    return CalicoK8sAdapter(metrics_source=build_calico_metrics_adapter())


def x_build_calico_adapter__mutmut_orig() -> CalicoPort:
    """Build the primary Calico port (K8s CRD/agent detection)."""
    from hexawyn.infrastructure.adapters.secondary.calico.calico_k8s_adapter import CalicoK8sAdapter

    return CalicoK8sAdapter(metrics_source=build_calico_metrics_adapter())


def x_build_calico_adapter__mutmut_1() -> CalicoPort:
    """Build the primary Calico port (K8s CRD/agent detection)."""
    from hexawyn.infrastructure.adapters.secondary.calico.calico_k8s_adapter import CalicoK8sAdapter

    return CalicoK8sAdapter(metrics_source=None)

mutants_x_build_calico_adapter__mutmut['_mutmut_orig'] = x_build_calico_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_calico_adapter__mutmut['x_build_calico_adapter__mutmut_1'] = x_build_calico_adapter__mutmut_1 # type: ignore # mutmut generated
