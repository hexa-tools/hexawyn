from __future__ import annotations

from hexawyn.domain.models.pod_security import (
    ContainerSecurityContext,
    PodSecuritySpec,
    SecurityViolation,
    ViolationType,
)
from hexawyn.domain.services.pod_security.fix_recommender import recommend_fix
from hexawyn.domain.services.pod_security.security_context_parser import (
    allows_privilege_escalation,
    is_privileged,
    resolves_to_root,
)
from hexawyn.domain.services.pod_security.violation_classifier import (
    classify_pss_level,
    classify_severity,
)


def scan_pod(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def scan_container(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def build_violation(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )
