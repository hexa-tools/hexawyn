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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_scan_pod__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_scan_pod__mutmut)
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


def x_scan_pod__mutmut_orig(spec: PodSecuritySpec) -> list[SecurityViolation]:
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


def x_scan_pod__mutmut_1(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = None
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_2(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(None)
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_3(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation(None, None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_4(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation(None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_5(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", ))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_6(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("XXhost_pidXX", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_7(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("HOST_PID", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_8(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(None)
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_9(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation(None, None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_10(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation(None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_11(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", ))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_12(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("XXhost_networkXX", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_13(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("HOST_NETWORK", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_14(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(None)
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_15(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation(None, None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_16(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation(None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_17(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", ))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_18(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("XXhost_ipcXX", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_19(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("HOST_IPC", None))
    for container in spec.containers:
        violations.extend(scan_container(container, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_20(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(None)
    return violations


def x_scan_pod__mutmut_21(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(None, spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_22(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, None))
    return violations


def x_scan_pod__mutmut_23(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(spec.pod_run_as_non_root))
    return violations


def x_scan_pod__mutmut_24(spec: PodSecuritySpec) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if spec.host_pid:
        violations.append(build_violation("host_pid", None))
    if spec.host_network:
        violations.append(build_violation("host_network", None))
    if spec.host_ipc:
        violations.append(build_violation("host_ipc", None))
    for container in spec.containers:
        violations.extend(scan_container(container, ))
    return violations

mutants_x_scan_pod__mutmut['_mutmut_orig'] = x_scan_pod__mutmut_orig # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_1'] = x_scan_pod__mutmut_1 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_2'] = x_scan_pod__mutmut_2 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_3'] = x_scan_pod__mutmut_3 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_4'] = x_scan_pod__mutmut_4 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_5'] = x_scan_pod__mutmut_5 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_6'] = x_scan_pod__mutmut_6 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_7'] = x_scan_pod__mutmut_7 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_8'] = x_scan_pod__mutmut_8 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_9'] = x_scan_pod__mutmut_9 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_10'] = x_scan_pod__mutmut_10 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_11'] = x_scan_pod__mutmut_11 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_12'] = x_scan_pod__mutmut_12 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_13'] = x_scan_pod__mutmut_13 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_14'] = x_scan_pod__mutmut_14 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_15'] = x_scan_pod__mutmut_15 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_16'] = x_scan_pod__mutmut_16 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_17'] = x_scan_pod__mutmut_17 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_18'] = x_scan_pod__mutmut_18 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_19'] = x_scan_pod__mutmut_19 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_20'] = x_scan_pod__mutmut_20 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_21'] = x_scan_pod__mutmut_21 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_22'] = x_scan_pod__mutmut_22 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_23'] = x_scan_pod__mutmut_23 # type: ignore # mutmut generated
mutants_x_scan_pod__mutmut['x_scan_pod__mutmut_24'] = x_scan_pod__mutmut_24 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_scan_container__mutmut)
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


def x_scan_container__mutmut_orig(
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


def x_scan_container__mutmut_1(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = None
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


def x_scan_container__mutmut_2(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(None):
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


def x_scan_container__mutmut_3(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(None)
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_4(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation(None, container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_5(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", None))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_6(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation(container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_7(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", ))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_8(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("XXprivilegedXX", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_9(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("PRIVILEGED", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_10(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(None, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_11(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, None):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_12(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_13(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, ):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_14(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(None)
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_15(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation(None, container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_16(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", None))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_17(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation(container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_18(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", ))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_19(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("XXrun_as_rootXX", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_20(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("RUN_AS_ROOT", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_21(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(None):
        violations.append(build_violation("allow_privilege_escalation", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_22(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(None)
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_23(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation(None, container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_24(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", None))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_25(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation(container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_26(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("allow_privilege_escalation", ))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_27(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("XXallow_privilege_escalationXX", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_28(
    container: ContainerSecurityContext, pod_run_as_non_root: bool | None
) -> list[SecurityViolation]:
    violations: list[SecurityViolation] = []
    if is_privileged(container.privileged):
        violations.append(build_violation("privileged", container.container_name))
    if resolves_to_root(container.run_as_non_root, pod_run_as_non_root):
        violations.append(build_violation("run_as_root", container.container_name))
    if allows_privilege_escalation(container.allow_privilege_escalation):
        violations.append(build_violation("ALLOW_PRIVILEGE_ESCALATION", container.container_name))
    for capability in container.added_capabilities:
        violations.append(
            build_violation("dangerous_capability", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_29(
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
            None
        )
    return violations


def x_scan_container__mutmut_30(
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
            build_violation(None, container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_31(
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
            build_violation("dangerous_capability", None, capability)
        )
    return violations


def x_scan_container__mutmut_32(
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
            build_violation("dangerous_capability", container.container_name, None)
        )
    return violations


def x_scan_container__mutmut_33(
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
            build_violation(container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_34(
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
            build_violation("dangerous_capability", capability)
        )
    return violations


def x_scan_container__mutmut_35(
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
            build_violation("dangerous_capability", container.container_name, )
        )
    return violations


def x_scan_container__mutmut_36(
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
            build_violation("XXdangerous_capabilityXX", container.container_name, capability)
        )
    return violations


def x_scan_container__mutmut_37(
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
            build_violation("DANGEROUS_CAPABILITY", container.container_name, capability)
        )
    return violations

mutants_x_scan_container__mutmut['_mutmut_orig'] = x_scan_container__mutmut_orig # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_1'] = x_scan_container__mutmut_1 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_2'] = x_scan_container__mutmut_2 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_3'] = x_scan_container__mutmut_3 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_4'] = x_scan_container__mutmut_4 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_5'] = x_scan_container__mutmut_5 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_6'] = x_scan_container__mutmut_6 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_7'] = x_scan_container__mutmut_7 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_8'] = x_scan_container__mutmut_8 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_9'] = x_scan_container__mutmut_9 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_10'] = x_scan_container__mutmut_10 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_11'] = x_scan_container__mutmut_11 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_12'] = x_scan_container__mutmut_12 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_13'] = x_scan_container__mutmut_13 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_14'] = x_scan_container__mutmut_14 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_15'] = x_scan_container__mutmut_15 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_16'] = x_scan_container__mutmut_16 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_17'] = x_scan_container__mutmut_17 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_18'] = x_scan_container__mutmut_18 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_19'] = x_scan_container__mutmut_19 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_20'] = x_scan_container__mutmut_20 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_21'] = x_scan_container__mutmut_21 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_22'] = x_scan_container__mutmut_22 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_23'] = x_scan_container__mutmut_23 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_24'] = x_scan_container__mutmut_24 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_25'] = x_scan_container__mutmut_25 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_26'] = x_scan_container__mutmut_26 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_27'] = x_scan_container__mutmut_27 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_28'] = x_scan_container__mutmut_28 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_29'] = x_scan_container__mutmut_29 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_30'] = x_scan_container__mutmut_30 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_31'] = x_scan_container__mutmut_31 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_32'] = x_scan_container__mutmut_32 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_33'] = x_scan_container__mutmut_33 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_34'] = x_scan_container__mutmut_34 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_35'] = x_scan_container__mutmut_35 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_36'] = x_scan_container__mutmut_36 # type: ignore # mutmut generated
mutants_x_scan_container__mutmut['x_scan_container__mutmut_37'] = x_scan_container__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_violation__mutmut)
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


def x_build_violation__mutmut_orig(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_1(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=None,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_2(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=None,
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_3(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=None,
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_4(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=None,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_5(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=None,
    )


def x_build_violation__mutmut_6(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_7(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_8(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_9(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_10(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        )


def x_build_violation__mutmut_11(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(None, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_12(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, None),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_13(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_14(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, ),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_15(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(None),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, capability),
    )


def x_build_violation__mutmut_16(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(None, capability),
    )


def x_build_violation__mutmut_17(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, None),
    )


def x_build_violation__mutmut_18(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(capability),
    )


def x_build_violation__mutmut_19(
    violation_type: ViolationType, container_name: str | None, capability: str | None = None
) -> SecurityViolation:
    return SecurityViolation(
        violation_type=violation_type,
        severity=classify_severity(violation_type, capability),
        pss_level=classify_pss_level(violation_type),
        container_name=container_name,
        recommendation=recommend_fix(violation_type, ),
    )

mutants_x_build_violation__mutmut['_mutmut_orig'] = x_build_violation__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_1'] = x_build_violation__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_2'] = x_build_violation__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_3'] = x_build_violation__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_4'] = x_build_violation__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_5'] = x_build_violation__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_6'] = x_build_violation__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_7'] = x_build_violation__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_8'] = x_build_violation__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_9'] = x_build_violation__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_10'] = x_build_violation__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_11'] = x_build_violation__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_12'] = x_build_violation__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_13'] = x_build_violation__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_14'] = x_build_violation__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_15'] = x_build_violation__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_16'] = x_build_violation__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_17'] = x_build_violation__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_18'] = x_build_violation__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_violation__mutmut['x_build_violation__mutmut_19'] = x_build_violation__mutmut_19 # type: ignore # mutmut generated
