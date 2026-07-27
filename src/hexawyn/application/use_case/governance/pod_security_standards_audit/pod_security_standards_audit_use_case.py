# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.ports.driven.pod_security_context_audit_port import (
    ContainerSecurityContextRaw,
    PodSecuritySpecRaw,
)
from hexawyn.application.use_case.governance.pod_security_standards_audit.command import (
    PodSecurityStandardsAuditCommand,
)
from hexawyn.application.use_case.governance.pod_security_standards_audit.response import (
    PodSecurityStandardsAuditResponse,
)
from hexawyn.application.use_case.security.detect_privileged_pods.response import (
    PodSecurityFindingDict,
    SecurityViolationDict,
)
from hexawyn.domain.models.constants import PodSecurityConstants
from hexawyn.domain.models.pod_security import (
    ContainerSecurityContext,
    PodSecurityAuditReport,
    PodSecurityFinding,
    PodSecuritySpec,
    SecurityViolation,
    ViolationType,
)
from hexawyn.domain.services.pod_security.fix_recommender import recommend_fix
from hexawyn.domain.services.pod_security.pod_security_report_builder import build_report
from hexawyn.domain.services.pod_security.security_context_parser import (
    allows_privilege_escalation,
    is_privileged,
    resolves_to_root,
)
from hexawyn.domain.services.pod_security.system_workload import is_known_system_daemonset
from hexawyn.domain.services.pod_security.violation_classifier import (
    classify_pss_level,
    classify_severity,
)

_cfg = PodSecurityConstants()
_SYSTEM_WORKLOAD_NOTE = "expected system workload (known system DaemonSet)"


class PodSecurityStandardsAuditUseCase:
    def __init__(self, pod_security_port: PodSecurityContextAuditPort) -> None:  # noqa: F821  # type: ignore
        self._pod_security_port = pod_security_port

    def audit_pod_security(
        self, command: PodSecurityStandardsAuditCommand
    ) -> PodSecurityStandardsAuditResponse:
        pod_specs_raw = self._pod_security_port.list_pod_security_specs()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            pod_specs_raw = [raw for raw in pod_specs_raw if raw["namespace"] in allowed_namespaces]
        psa_levels = self._pod_security_port.get_namespace_psa_enforce_levels()

        findings: list[PodSecurityFinding] = []
        compliant_pod_count = 0

        for raw_spec in pod_specs_raw:
            spec = _to_domain_spec(raw_spec)
            violations = _scan_pod(spec)
            if not violations:
                compliant_pod_count += 1
                continue

            note = None
            if is_known_system_daemonset(
                spec.owner_kind, spec.pod_name, _cfg.known_system_daemonset_name_fragments
            ):
                note = _SYSTEM_WORKLOAD_NOTE

            findings.append(
                PodSecurityFinding(
                    pod_name=spec.pod_name,
                    namespace=spec.namespace,
                    violations=violations,
                    note=note,
                    namespace_psa_enforce_level=psa_levels.get(spec.namespace),
                )
            )

        report = build_report(
            findings=findings,
            compliant_pod_count=compliant_pod_count,
            total_pods_checked=len(pod_specs_raw),
        )
        return _to_response(report)


def _scan_pod(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(_build_violation("host_pid", None))
    if spec.host_network:
        violations.append(_build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(_build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(_scan_container(container, spec.pod_run_as_non_root))
    return violations


def _scan_container(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(_build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(_build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(_build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            _build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def _build_violation(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def _to_domain_spec(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(container) for container in raw["containers"]],
    )


def _to_domain_container(raw: ContainerSecurityContextRaw) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def _to_response(report: PodSecurityAuditReport) -> PodSecurityStandardsAuditResponse:
    return PodSecurityStandardsAuditResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        compliant_pod_count=report.compliant_pod_count,
        total_pods_checked=report.total_pods_checked,
        summary=report.summary,
        error=None,
    )


def _to_finding_dict(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[_to_violation_dict(violation) for violation in finding.violations],
        note=finding.note,  # type: ignore
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def _to_violation_dict(violation: SecurityViolation) -> SecurityViolationDict:
    return SecurityViolationDict(
        violation_type=violation.violation_type,
        severity=violation.severity,
        pss_level=violation.pss_level,
        container_name=violation.container_name,  # type: ignore
        recommendation=violation.recommendation,
    )
