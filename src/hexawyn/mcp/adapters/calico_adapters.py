"""Calico adapter builders — the chosen collaborators for the Calico series."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.calico_port import CalicoPort

if TYPE_CHECKING:
    from hexawyn.adapters.secondary.calico.calico_prometheus_adapter import (
        CalicoPrometheusAdapter,
    )


def build_calico_metrics_adapter() -> CalicoPrometheusAdapter:
    """Build the metrics-backed Calico collaborator (Felix metrics via Prometheus)."""
    from hexawyn.adapters.secondary.calico.calico_prometheus_adapter import (
        CalicoPrometheusAdapter,
    )
    from hexawyn.mcp.adapters.observability_adapters import build_metrics_query_adapter

    return CalicoPrometheusAdapter(metrics_query_port=build_metrics_query_adapter())


def build_calico_adapter() -> CalicoPort:
    """Build the primary Calico port (K8s CRD/agent detection)."""
    from hexawyn.adapters.secondary.calico.calico_k8s_adapter import CalicoK8sAdapter

    return CalicoK8sAdapter(metrics_source=build_calico_metrics_adapter())
