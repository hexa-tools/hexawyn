from __future__ import annotations

from hexawyn.domain.models.configuration_drift import DriftSeverity

_FIELD_SEVERITY: dict[str, DriftSeverity] = {
    "image": "critical",
    "replicas": "warning",
    "resource_limits": "warning",
    "env_vars": "warning",
    "configmap_data": "warning",
    "labels": "info",
}
_DEFAULT_SEVERITY: DriftSeverity = "warning"

_ALWAYS_CRITICAL_KINDS = frozenset(
    {"Role", "ClusterRole", "RoleBinding", "ClusterRoleBinding", "Secret"}
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_classify_severity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_severity__mutmut)
def classify_severity(field_name: str, resource_kind: str) -> DriftSeverity:
    """RBAC/Secret kinds are always critical regardless of which field
    drifted; otherwise severity is determined by which kind of field it is."""
    if resource_kind in _ALWAYS_CRITICAL_KINDS:
        return "critical"
    return _FIELD_SEVERITY.get(field_name, _DEFAULT_SEVERITY)


def x_classify_severity__mutmut_orig(field_name: str, resource_kind: str) -> DriftSeverity:
    """RBAC/Secret kinds are always critical regardless of which field
    drifted; otherwise severity is determined by which kind of field it is."""
    if resource_kind in _ALWAYS_CRITICAL_KINDS:
        return "critical"
    return _FIELD_SEVERITY.get(field_name, _DEFAULT_SEVERITY)


def x_classify_severity__mutmut_1(field_name: str, resource_kind: str) -> DriftSeverity:
    """RBAC/Secret kinds are always critical regardless of which field
    drifted; otherwise severity is determined by which kind of field it is."""
    if resource_kind not in _ALWAYS_CRITICAL_KINDS:
        return "critical"
    return _FIELD_SEVERITY.get(field_name, _DEFAULT_SEVERITY)


def x_classify_severity__mutmut_2(field_name: str, resource_kind: str) -> DriftSeverity:
    """RBAC/Secret kinds are always critical regardless of which field
    drifted; otherwise severity is determined by which kind of field it is."""
    if resource_kind in _ALWAYS_CRITICAL_KINDS:
        return "XXcriticalXX"
    return _FIELD_SEVERITY.get(field_name, _DEFAULT_SEVERITY)


def x_classify_severity__mutmut_3(field_name: str, resource_kind: str) -> DriftSeverity:
    """RBAC/Secret kinds are always critical regardless of which field
    drifted; otherwise severity is determined by which kind of field it is."""
    if resource_kind in _ALWAYS_CRITICAL_KINDS:
        return "CRITICAL"
    return _FIELD_SEVERITY.get(field_name, _DEFAULT_SEVERITY)


def x_classify_severity__mutmut_4(field_name: str, resource_kind: str) -> DriftSeverity:
    """RBAC/Secret kinds are always critical regardless of which field
    drifted; otherwise severity is determined by which kind of field it is."""
    if resource_kind in _ALWAYS_CRITICAL_KINDS:
        return "critical"
    return _FIELD_SEVERITY.get(None, _DEFAULT_SEVERITY)


def x_classify_severity__mutmut_5(field_name: str, resource_kind: str) -> DriftSeverity:
    """RBAC/Secret kinds are always critical regardless of which field
    drifted; otherwise severity is determined by which kind of field it is."""
    if resource_kind in _ALWAYS_CRITICAL_KINDS:
        return "critical"
    return _FIELD_SEVERITY.get(field_name, None)


def x_classify_severity__mutmut_6(field_name: str, resource_kind: str) -> DriftSeverity:
    """RBAC/Secret kinds are always critical regardless of which field
    drifted; otherwise severity is determined by which kind of field it is."""
    if resource_kind in _ALWAYS_CRITICAL_KINDS:
        return "critical"
    return _FIELD_SEVERITY.get(_DEFAULT_SEVERITY)


def x_classify_severity__mutmut_7(field_name: str, resource_kind: str) -> DriftSeverity:
    """RBAC/Secret kinds are always critical regardless of which field
    drifted; otherwise severity is determined by which kind of field it is."""
    if resource_kind in _ALWAYS_CRITICAL_KINDS:
        return "critical"
    return _FIELD_SEVERITY.get(field_name, )

mutants_x_classify_severity__mutmut['_mutmut_orig'] = x_classify_severity__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_1'] = x_classify_severity__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_2'] = x_classify_severity__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_3'] = x_classify_severity__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_4'] = x_classify_severity__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_5'] = x_classify_severity__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_6'] = x_classify_severity__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_severity__mutmut['x_classify_severity__mutmut_7'] = x_classify_severity__mutmut_7 # type: ignore # mutmut generated
