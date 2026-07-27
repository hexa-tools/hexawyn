from __future__ import annotations

from hexawyn.application.ports.driven.pod_security_context_audit_port import (
    ContainerSecurityContextRaw,
    PodSecuritySpecRaw,
)
from hexawyn.application.use_case.security.detect_privileged_pods.response import (
    PodSecurityFindingDict,
    SecurityViolationDict,
)
from hexawyn.domain.models.pod_security import (
    ContainerSecurityContext,
    PodSecurityAuditReport,
    PodSecurityFinding,
    PodSecuritySpec,
)


def to_domain_spec(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def _to_domain_container(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def to_response(report: PodSecurityAuditReport) -> dict[str, object]:
    return {
        "findings": [_to_finding_dict(f) for f in report.findings],
        "compliant_pod_count": report.compliant_pod_count,
        "total_pods_checked": report.total_pods_checked,
        "summary": report.summary,
    }


def _to_finding_dict(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
                violation_type=v.violation_type,
                severity=v.severity,
                pss_level=v.pss_level,
                container_name=v.container_name or "",
                recommendation=v.recommendation,
            )
            for v in finding.violations
        ],
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )
