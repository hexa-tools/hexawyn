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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_to_domain_spec__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_domain_spec__mutmut)
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


def x_to_domain_spec__mutmut_orig(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
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


def x_to_domain_spec__mutmut_1(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=None,
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_2(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=None,
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_3(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=None,
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_4(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=None,
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_5(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=None,
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_6(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=None,
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_7(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=None,
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_8(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=None,
    )


def x_to_domain_spec__mutmut_9(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_10(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_11(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_12(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_13(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_14(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_15(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_16(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        )


def x_to_domain_spec__mutmut_17(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["XXpod_nameXX"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_18(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["POD_NAME"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_19(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["XXnamespaceXX"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_20(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["NAMESPACE"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_21(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["XXowner_kindXX"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_22(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["OWNER_KIND"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_23(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["XXpod_run_as_non_rootXX"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_24(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["POD_RUN_AS_NON_ROOT"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_25(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["XXhost_pidXX"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_26(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["HOST_PID"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_27(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["XXhost_networkXX"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_28(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["HOST_NETWORK"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_29(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["XXhost_ipcXX"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_30(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["HOST_IPC"],
        containers=[_to_domain_container(c) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_31(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(None) for c in raw["containers"]],
    )


def x_to_domain_spec__mutmut_32(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["XXcontainersXX"]],
    )


def x_to_domain_spec__mutmut_33(raw: PodSecuritySpecRaw) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=raw["pod_name"],
        namespace=raw["namespace"],
        owner_kind=raw["owner_kind"],
        pod_run_as_non_root=raw["pod_run_as_non_root"],
        host_pid=raw["host_pid"],
        host_network=raw["host_network"],
        host_ipc=raw["host_ipc"],
        containers=[_to_domain_container(c) for c in raw["CONTAINERS"]],
    )

mutants_x_to_domain_spec__mutmut['_mutmut_orig'] = x_to_domain_spec__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_1'] = x_to_domain_spec__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_2'] = x_to_domain_spec__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_3'] = x_to_domain_spec__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_4'] = x_to_domain_spec__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_5'] = x_to_domain_spec__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_6'] = x_to_domain_spec__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_7'] = x_to_domain_spec__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_8'] = x_to_domain_spec__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_9'] = x_to_domain_spec__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_10'] = x_to_domain_spec__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_11'] = x_to_domain_spec__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_12'] = x_to_domain_spec__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_13'] = x_to_domain_spec__mutmut_13 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_14'] = x_to_domain_spec__mutmut_14 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_15'] = x_to_domain_spec__mutmut_15 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_16'] = x_to_domain_spec__mutmut_16 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_17'] = x_to_domain_spec__mutmut_17 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_18'] = x_to_domain_spec__mutmut_18 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_19'] = x_to_domain_spec__mutmut_19 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_20'] = x_to_domain_spec__mutmut_20 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_21'] = x_to_domain_spec__mutmut_21 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_22'] = x_to_domain_spec__mutmut_22 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_23'] = x_to_domain_spec__mutmut_23 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_24'] = x_to_domain_spec__mutmut_24 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_25'] = x_to_domain_spec__mutmut_25 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_26'] = x_to_domain_spec__mutmut_26 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_27'] = x_to_domain_spec__mutmut_27 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_28'] = x_to_domain_spec__mutmut_28 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_29'] = x_to_domain_spec__mutmut_29 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_30'] = x_to_domain_spec__mutmut_30 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_31'] = x_to_domain_spec__mutmut_31 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_32'] = x_to_domain_spec__mutmut_32 # type: ignore # mutmut generated
mutants_x_to_domain_spec__mutmut['x_to_domain_spec__mutmut_33'] = x_to_domain_spec__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_domain_container__mutmut)
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


def x__to_domain_container__mutmut_orig(
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


def x__to_domain_container__mutmut_1(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=None,
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_2(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=None,
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_3(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=None,
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_4(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=None,
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_5(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=None,
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_6(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=None,
    )


def x__to_domain_container__mutmut_7(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_8(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_9(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_10(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_11(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_12(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        )


def x__to_domain_container__mutmut_13(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["XXcontainer_nameXX"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_14(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["CONTAINER_NAME"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_15(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["XXcontainer_kindXX"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_16(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["CONTAINER_KIND"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_17(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["XXprivilegedXX"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_18(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["PRIVILEGED"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_19(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["XXallow_privilege_escalationXX"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_20(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["ALLOW_PRIVILEGE_ESCALATION"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_21(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["XXrun_as_non_rootXX"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_22(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["RUN_AS_NON_ROOT"],
        added_capabilities=raw["added_capabilities"],
    )


def x__to_domain_container__mutmut_23(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["XXadded_capabilitiesXX"],
    )


def x__to_domain_container__mutmut_24(
    raw: ContainerSecurityContextRaw,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=raw["container_name"],
        container_kind=raw["container_kind"],
        privileged=raw["privileged"],
        allow_privilege_escalation=raw["allow_privilege_escalation"],
        run_as_non_root=raw["run_as_non_root"],
        added_capabilities=raw["ADDED_CAPABILITIES"],
    )

mutants_x__to_domain_container__mutmut['_mutmut_orig'] = x__to_domain_container__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_1'] = x__to_domain_container__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_2'] = x__to_domain_container__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_3'] = x__to_domain_container__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_4'] = x__to_domain_container__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_5'] = x__to_domain_container__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_6'] = x__to_domain_container__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_7'] = x__to_domain_container__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_8'] = x__to_domain_container__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_9'] = x__to_domain_container__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_10'] = x__to_domain_container__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_11'] = x__to_domain_container__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_12'] = x__to_domain_container__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_13'] = x__to_domain_container__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_14'] = x__to_domain_container__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_15'] = x__to_domain_container__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_16'] = x__to_domain_container__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_17'] = x__to_domain_container__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_18'] = x__to_domain_container__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_19'] = x__to_domain_container__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_20'] = x__to_domain_container__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_21'] = x__to_domain_container__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_22'] = x__to_domain_container__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_23'] = x__to_domain_container__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_domain_container__mutmut['x__to_domain_container__mutmut_24'] = x__to_domain_container__mutmut_24 # type: ignore # mutmut generated
mutants_x_to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_response__mutmut)
def to_response(report: PodSecurityAuditReport) -> dict[str, object]:
    return {
        "findings": [_to_finding_dict(f) for f in report.findings],
        "compliant_pod_count": report.compliant_pod_count,
        "total_pods_checked": report.total_pods_checked,
        "summary": report.summary,
    }


def x_to_response__mutmut_orig(report: PodSecurityAuditReport) -> dict[str, object]:
    return {
        "findings": [_to_finding_dict(f) for f in report.findings],
        "compliant_pod_count": report.compliant_pod_count,
        "total_pods_checked": report.total_pods_checked,
        "summary": report.summary,
    }


def x_to_response__mutmut_1(report: PodSecurityAuditReport) -> dict[str, object]:
    return {
        "XXfindingsXX": [_to_finding_dict(f) for f in report.findings],
        "compliant_pod_count": report.compliant_pod_count,
        "total_pods_checked": report.total_pods_checked,
        "summary": report.summary,
    }


def x_to_response__mutmut_2(report: PodSecurityAuditReport) -> dict[str, object]:
    return {
        "FINDINGS": [_to_finding_dict(f) for f in report.findings],
        "compliant_pod_count": report.compliant_pod_count,
        "total_pods_checked": report.total_pods_checked,
        "summary": report.summary,
    }


def x_to_response__mutmut_3(report: PodSecurityAuditReport) -> dict[str, object]:
    return {
        "findings": [_to_finding_dict(None) for f in report.findings],
        "compliant_pod_count": report.compliant_pod_count,
        "total_pods_checked": report.total_pods_checked,
        "summary": report.summary,
    }


def x_to_response__mutmut_4(report: PodSecurityAuditReport) -> dict[str, object]:
    return {
        "findings": [_to_finding_dict(f) for f in report.findings],
        "XXcompliant_pod_countXX": report.compliant_pod_count,
        "total_pods_checked": report.total_pods_checked,
        "summary": report.summary,
    }


def x_to_response__mutmut_5(report: PodSecurityAuditReport) -> dict[str, object]:
    return {
        "findings": [_to_finding_dict(f) for f in report.findings],
        "COMPLIANT_POD_COUNT": report.compliant_pod_count,
        "total_pods_checked": report.total_pods_checked,
        "summary": report.summary,
    }


def x_to_response__mutmut_6(report: PodSecurityAuditReport) -> dict[str, object]:
    return {
        "findings": [_to_finding_dict(f) for f in report.findings],
        "compliant_pod_count": report.compliant_pod_count,
        "XXtotal_pods_checkedXX": report.total_pods_checked,
        "summary": report.summary,
    }


def x_to_response__mutmut_7(report: PodSecurityAuditReport) -> dict[str, object]:
    return {
        "findings": [_to_finding_dict(f) for f in report.findings],
        "compliant_pod_count": report.compliant_pod_count,
        "TOTAL_PODS_CHECKED": report.total_pods_checked,
        "summary": report.summary,
    }


def x_to_response__mutmut_8(report: PodSecurityAuditReport) -> dict[str, object]:
    return {
        "findings": [_to_finding_dict(f) for f in report.findings],
        "compliant_pod_count": report.compliant_pod_count,
        "total_pods_checked": report.total_pods_checked,
        "XXsummaryXX": report.summary,
    }


def x_to_response__mutmut_9(report: PodSecurityAuditReport) -> dict[str, object]:
    return {
        "findings": [_to_finding_dict(f) for f in report.findings],
        "compliant_pod_count": report.compliant_pod_count,
        "total_pods_checked": report.total_pods_checked,
        "SUMMARY": report.summary,
    }

mutants_x_to_response__mutmut['_mutmut_orig'] = x_to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_1'] = x_to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_2'] = x_to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_3'] = x_to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_4'] = x_to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_5'] = x_to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_6'] = x_to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_7'] = x_to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_8'] = x_to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_9'] = x_to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_finding_dict__mutmut)
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


def x__to_finding_dict__mutmut_orig(finding: PodSecurityFinding) -> PodSecurityFindingDict:
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


def x__to_finding_dict__mutmut_1(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=None,
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


def x__to_finding_dict__mutmut_2(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=None,
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


def x__to_finding_dict__mutmut_3(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=None,
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_4(finding: PodSecurityFinding) -> PodSecurityFindingDict:
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
        note=None,
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_5(finding: PodSecurityFinding) -> PodSecurityFindingDict:
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
        namespace_psa_enforce_level=None,
    )


def x__to_finding_dict__mutmut_6(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
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


def x__to_finding_dict__mutmut_7(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
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


def x__to_finding_dict__mutmut_8(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_9(finding: PodSecurityFinding) -> PodSecurityFindingDict:
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
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_10(finding: PodSecurityFinding) -> PodSecurityFindingDict:
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
        )


def x__to_finding_dict__mutmut_11(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
                violation_type=None,
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


def x__to_finding_dict__mutmut_12(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
                violation_type=v.violation_type,
                severity=None,
                pss_level=v.pss_level,
                container_name=v.container_name or "",
                recommendation=v.recommendation,
            )
            for v in finding.violations
        ],
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_13(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
                violation_type=v.violation_type,
                severity=v.severity,
                pss_level=None,
                container_name=v.container_name or "",
                recommendation=v.recommendation,
            )
            for v in finding.violations
        ],
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_14(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
                violation_type=v.violation_type,
                severity=v.severity,
                pss_level=v.pss_level,
                container_name=None,
                recommendation=v.recommendation,
            )
            for v in finding.violations
        ],
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_15(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
                violation_type=v.violation_type,
                severity=v.severity,
                pss_level=v.pss_level,
                container_name=v.container_name or "",
                recommendation=None,
            )
            for v in finding.violations
        ],
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_16(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
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


def x__to_finding_dict__mutmut_17(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
                violation_type=v.violation_type,
                pss_level=v.pss_level,
                container_name=v.container_name or "",
                recommendation=v.recommendation,
            )
            for v in finding.violations
        ],
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_18(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
                violation_type=v.violation_type,
                severity=v.severity,
                container_name=v.container_name or "",
                recommendation=v.recommendation,
            )
            for v in finding.violations
        ],
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_19(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
                violation_type=v.violation_type,
                severity=v.severity,
                pss_level=v.pss_level,
                recommendation=v.recommendation,
            )
            for v in finding.violations
        ],
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_20(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
                violation_type=v.violation_type,
                severity=v.severity,
                pss_level=v.pss_level,
                container_name=v.container_name or "",
                )
            for v in finding.violations
        ],
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_21(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
                violation_type=v.violation_type,
                severity=v.severity,
                pss_level=v.pss_level,
                container_name=v.container_name and "",
                recommendation=v.recommendation,
            )
            for v in finding.violations
        ],
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_22(finding: PodSecurityFinding) -> PodSecurityFindingDict:
    return PodSecurityFindingDict(
        pod_name=finding.pod_name,
        namespace=finding.namespace,
        violations=[
            SecurityViolationDict(
                violation_type=v.violation_type,
                severity=v.severity,
                pss_level=v.pss_level,
                container_name=v.container_name or "XXXX",
                recommendation=v.recommendation,
            )
            for v in finding.violations
        ],
        note=finding.note or "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_23(finding: PodSecurityFinding) -> PodSecurityFindingDict:
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
        note=finding.note and "",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )


def x__to_finding_dict__mutmut_24(finding: PodSecurityFinding) -> PodSecurityFindingDict:
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
        note=finding.note or "XXXX",
        namespace_psa_enforce_level=finding.namespace_psa_enforce_level,
    )

mutants_x__to_finding_dict__mutmut['_mutmut_orig'] = x__to_finding_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_1'] = x__to_finding_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_2'] = x__to_finding_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_3'] = x__to_finding_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_4'] = x__to_finding_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_5'] = x__to_finding_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_6'] = x__to_finding_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_7'] = x__to_finding_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_8'] = x__to_finding_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_9'] = x__to_finding_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_10'] = x__to_finding_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_11'] = x__to_finding_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_12'] = x__to_finding_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_13'] = x__to_finding_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_14'] = x__to_finding_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_15'] = x__to_finding_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_16'] = x__to_finding_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_17'] = x__to_finding_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_18'] = x__to_finding_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_19'] = x__to_finding_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_20'] = x__to_finding_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_21'] = x__to_finding_dict__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_22'] = x__to_finding_dict__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_23'] = x__to_finding_dict__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_finding_dict__mutmut['x__to_finding_dict__mutmut_24'] = x__to_finding_dict__mutmut_24 # type: ignore # mutmut generated
