from __future__ import annotations

from hexawyn.domain.models.pod_security import ViolationType

_FIXES: dict[ViolationType, str] = {
    "privileged": "Set privileged: false in the container's securityContext.",
    "host_pid": "Set hostPID: false in the pod spec (unless this is a legitimate system DaemonSet).",  # noqa: E501
    "host_network": "Set hostNetwork: false in the pod spec.",
    "host_ipc": "Set hostIPC: false in the pod spec.",
    "run_as_root": "Set runAsNonRoot: true (and a non-zero runAsUser) in the securityContext.",
    "allow_privilege_escalation": "Set allowPrivilegeEscalation: false in the container's securityContext.",  # noqa: E501
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_recommend_fix__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_recommend_fix__mutmut)
def recommend_fix(violation_type: ViolationType, capability: str | None = None) -> str:
    if violation_type == "dangerous_capability":
        return (
            f"Remove the '{capability}' capability from securityContext.capabilities.add "
            "(drop ALL and add back only what's required)."
        )
    return _FIXES[violation_type]


def x_recommend_fix__mutmut_orig(violation_type: ViolationType, capability: str | None = None) -> str:
    if violation_type == "dangerous_capability":
        return (
            f"Remove the '{capability}' capability from securityContext.capabilities.add "
            "(drop ALL and add back only what's required)."
        )
    return _FIXES[violation_type]


def x_recommend_fix__mutmut_1(violation_type: ViolationType, capability: str | None = None) -> str:
    if violation_type != "dangerous_capability":
        return (
            f"Remove the '{capability}' capability from securityContext.capabilities.add "
            "(drop ALL and add back only what's required)."
        )
    return _FIXES[violation_type]


def x_recommend_fix__mutmut_2(violation_type: ViolationType, capability: str | None = None) -> str:
    if violation_type == "XXdangerous_capabilityXX":
        return (
            f"Remove the '{capability}' capability from securityContext.capabilities.add "
            "(drop ALL and add back only what's required)."
        )
    return _FIXES[violation_type]


def x_recommend_fix__mutmut_3(violation_type: ViolationType, capability: str | None = None) -> str:
    if violation_type == "DANGEROUS_CAPABILITY":
        return (
            f"Remove the '{capability}' capability from securityContext.capabilities.add "
            "(drop ALL and add back only what's required)."
        )
    return _FIXES[violation_type]


def x_recommend_fix__mutmut_4(violation_type: ViolationType, capability: str | None = None) -> str:
    if violation_type == "dangerous_capability":
        return (
            f"Remove the '{capability}' capability from securityContext.capabilities.add "
            "XX(drop ALL and add back only what's required).XX"
        )
    return _FIXES[violation_type]


def x_recommend_fix__mutmut_5(violation_type: ViolationType, capability: str | None = None) -> str:
    if violation_type == "dangerous_capability":
        return (
            f"Remove the '{capability}' capability from securityContext.capabilities.add "
            "(drop all and add back only what's required)."
        )
    return _FIXES[violation_type]


def x_recommend_fix__mutmut_6(violation_type: ViolationType, capability: str | None = None) -> str:
    if violation_type == "dangerous_capability":
        return (
            f"Remove the '{capability}' capability from securityContext.capabilities.add "
            "(DROP ALL AND ADD BACK ONLY WHAT'S REQUIRED)."
        )
    return _FIXES[violation_type]

mutants_x_recommend_fix__mutmut['_mutmut_orig'] = x_recommend_fix__mutmut_orig # type: ignore # mutmut generated
mutants_x_recommend_fix__mutmut['x_recommend_fix__mutmut_1'] = x_recommend_fix__mutmut_1 # type: ignore # mutmut generated
mutants_x_recommend_fix__mutmut['x_recommend_fix__mutmut_2'] = x_recommend_fix__mutmut_2 # type: ignore # mutmut generated
mutants_x_recommend_fix__mutmut['x_recommend_fix__mutmut_3'] = x_recommend_fix__mutmut_3 # type: ignore # mutmut generated
mutants_x_recommend_fix__mutmut['x_recommend_fix__mutmut_4'] = x_recommend_fix__mutmut_4 # type: ignore # mutmut generated
mutants_x_recommend_fix__mutmut['x_recommend_fix__mutmut_5'] = x_recommend_fix__mutmut_5 # type: ignore # mutmut generated
mutants_x_recommend_fix__mutmut['x_recommend_fix__mutmut_6'] = x_recommend_fix__mutmut_6 # type: ignore # mutmut generated
