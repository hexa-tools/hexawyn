"""MCP tool: check_cluster_certificate_health — full TLS certificate health report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.cluster_certificate_health_port import (
    ClusterCertificateHealthPort,
)
from hexawyn.application.ports.driving.check_cluster_certificate_health.check_cluster_certificate_health_command import (
    CheckClusterCertificateHealthCommand,
)
from hexawyn.application.use_case.check_cluster_certificate_health.check_cluster_certificate_health_use_case import (
    CheckClusterCertificateHealthUseCase,
)
from hexawyn.domain.models.certificate import CertificateEntry

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _build_adapter() -> ClusterCertificateHealthPort:
    from hexawyn.adapters.secondary.kubernetes_cluster_certificate_adapter import (
        KubernetesClusterCertificateAdapter,
    )
    from hexawyn.mcp.server import _k8s_api

    return KubernetesClusterCertificateAdapter(api=_k8s_api)


def _serialize_entry(entry: CertificateEntry) -> dict[str, object]:
    return {
        "secret_name": entry.secret_name,
        "namespace": entry.namespace,
        "subject_cn": entry.info.subject_cn,
        "issuer_cn": entry.info.issuer_cn,
        "days_remaining": entry.days_remaining,
        "status": entry.status.value,
        "expiry": entry.info.not_after.isoformat() if entry.info.not_after else None,
        "ingress_refs": entry.ingress_refs,
        "is_orphan": entry.is_orphan,
        "cert_manager_managed": entry.cert_manager_managed,
        "cert_manager_auto_renewing": entry.cert_manager_auto_renewing,
        "is_wildcard": entry.is_wildcard,
    }


def check_cluster_certificate_health(
    warning_days: int = 30,
    critical_days: int = 7,
    timeout_seconds: float = 10.0,
) -> dict[str, object]:
    """Return a full TLS certificate health report for all namespaces in the cluster.

    Scans every TLS secret across all namespaces, computes expiry dates, maps each
    certificate to the ingresses that reference it, and returns a sorted report:
    critical (≤7d), warning (≤30d), healthy (>30d), expired (<0d).

    Args:
        warning_days: Days threshold for warning status (default: 30).
        critical_days: Days threshold for critical status (default: 7).
        timeout_seconds: Per-namespace K8s API timeout in seconds (default: 10.0).
    """
    from hexawyn.application.service.cluster_certificate_health_service import (
        ClusterCertificateHealthService,
    )
    from hexawyn.mcp.server import context_name

    try:
        adapter = _build_adapter()
        service = ClusterCertificateHealthService(port=adapter, cluster_name=context_name)
        use_case = CheckClusterCertificateHealthUseCase(service=service)
        response = use_case.execute(
            CheckClusterCertificateHealthCommand(
                warning_days=warning_days,
                critical_days=critical_days,
                timeout_seconds=timeout_seconds,
            )
        )
        report = response.report

        return {
            "cluster_name": report.cluster_name,
            "critical": [_serialize_entry(e) for e in report.critical],
            "warning": [_serialize_entry(e) for e in report.warning],
            "healthy": [_serialize_entry(e) for e in report.healthy],
            "expired": [_serialize_entry(e) for e in report.expired],
            "skipped_namespaces": report.skipped_namespaces,
            "total_scanned": report.total_scanned,
            "scanned_at": report.scanned_at.isoformat(),
            "error": None,
        }
    except Exception as exc:
        return {
            "cluster_name": None,
            "critical": [],
            "warning": [],
            "healthy": [],
            "expired": [],
            "skipped_namespaces": [],
            "total_scanned": 0,
            "scanned_at": None,
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(check_cluster_certificate_health)
