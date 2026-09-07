from __future__ import annotations

from hexawyn.domain.models.constants import PodSecurityConstants
from hexawyn.domain.models.pod_security import PSSLevel, Severity, ViolationType

_cfg = PodSecurityConstants()
_CRITICAL_VIOLATION_TYPES = frozenset({"privileged", "host_pid", "host_network", "host_ipc"})
_HIGH_SEVERITY_CAPABILITIES = frozenset(_cfg.high_severity_capabilities)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_severity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_severity__mutmut)
def classify_severity(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_orig(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_1(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type not in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_2(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "XXcriticalXX"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_3(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "CRITICAL"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_4(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type != "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_5(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "XXrun_as_rootXX":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_6(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "RUN_AS_ROOT":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_7(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "XXhighXX"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_8(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "HIGH"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_9(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type != "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_10(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "XXdangerous_capabilityXX":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_11(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "DANGEROUS_CAPABILITY":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_12(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "XXhighXX" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_13(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "HIGH" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_14(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability not in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "medium"


def x_classify_severity__mutmut_15(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "XXmediumXX"
    return "medium"


def x_classify_severity__mutmut_16(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "MEDIUM"
    return "medium"


def x_classify_severity__mutmut_17(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "XXmediumXX"


def x_classify_severity__mutmut_18(violation_type: ViolationType, capability: str | None = None) -> Severity:
    if violation_type in _CRITICAL_VIOLATION_TYPES:
        return "critical"
    if violation_type == "run_as_root":
        return "high"
    if violation_type == "dangerous_capability":
        return "high" if capability in _HIGH_SEVERITY_CAPABILITIES else "medium"
    return "MEDIUM"

mutants_x_classify_severity__mutmut['_mutmut_orig'] = x_classify_severity__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_1'] = x_classify_severity__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_2'] = x_classify_severity__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_3'] = x_classify_severity__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_4'] = x_classify_severity__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_5'] = x_classify_severity__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_6'] = x_classify_severity__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_7'] = x_classify_severity__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_8'] = x_classify_severity__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_9'] = x_classify_severity__mutmut_9 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_10'] = x_classify_severity__mutmut_10 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_11'] = x_classify_severity__mutmut_11 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_12'] = x_classify_severity__mutmut_12 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_13'] = x_classify_severity__mutmut_13 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_14'] = x_classify_severity__mutmut_14 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_15'] = x_classify_severity__mutmut_15 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_16'] = x_classify_severity__mutmut_16 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_17'] = x_classify_severity__mutmut_17 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_18'] = x_classify_severity__mutmut_18 # type: ignore # mutmut generated
mutants_x_classify_pss_level__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_pss_level__mutmut)
def classify_pss_level(violation_type: ViolationType) -> PSSLevel:
    return "Baseline" if violation_type in _CRITICAL_VIOLATION_TYPES else "Restricted"


def x_classify_pss_level__mutmut_orig(violation_type: ViolationType) -> PSSLevel:
    return "Baseline" if violation_type in _CRITICAL_VIOLATION_TYPES else "Restricted"


def x_classify_pss_level__mutmut_1(violation_type: ViolationType) -> PSSLevel:
    return "XXBaselineXX" if violation_type in _CRITICAL_VIOLATION_TYPES else "Restricted"


def x_classify_pss_level__mutmut_2(violation_type: ViolationType) -> PSSLevel:
    return "baseline" if violation_type in _CRITICAL_VIOLATION_TYPES else "Restricted"


def x_classify_pss_level__mutmut_3(violation_type: ViolationType) -> PSSLevel:
    return "BASELINE" if violation_type in _CRITICAL_VIOLATION_TYPES else "Restricted"


def x_classify_pss_level__mutmut_4(violation_type: ViolationType) -> PSSLevel:
    return "Baseline" if violation_type not in _CRITICAL_VIOLATION_TYPES else "Restricted"


def x_classify_pss_level__mutmut_5(violation_type: ViolationType) -> PSSLevel:
    return "Baseline" if violation_type in _CRITICAL_VIOLATION_TYPES else "XXRestrictedXX"


def x_classify_pss_level__mutmut_6(violation_type: ViolationType) -> PSSLevel:
    return "Baseline" if violation_type in _CRITICAL_VIOLATION_TYPES else "restricted"


def x_classify_pss_level__mutmut_7(violation_type: ViolationType) -> PSSLevel:
    return "Baseline" if violation_type in _CRITICAL_VIOLATION_TYPES else "RESTRICTED"

mutants_x_classify_pss_level__mutmut['_mutmut_orig'] = x_classify_pss_level__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_pss_level__mutmut['x_classify_pss_level__mutmut_1'] = x_classify_pss_level__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_pss_level__mutmut['x_classify_pss_level__mutmut_2'] = x_classify_pss_level__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_pss_level__mutmut['x_classify_pss_level__mutmut_3'] = x_classify_pss_level__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_pss_level__mutmut['x_classify_pss_level__mutmut_4'] = x_classify_pss_level__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_pss_level__mutmut['x_classify_pss_level__mutmut_5'] = x_classify_pss_level__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_pss_level__mutmut['x_classify_pss_level__mutmut_6'] = x_classify_pss_level__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_pss_level__mutmut['x_classify_pss_level__mutmut_7'] = x_classify_pss_level__mutmut_7 # type: ignore # mutmut generated
