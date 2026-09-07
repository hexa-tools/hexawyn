from __future__ import annotations

from typing import Literal

from hexawyn.domain.models.namespace_overview import NamespaceHealthStatus, UnhealthyResource

_UNHEALTHY_POD_STATUSES = frozenset(
    {
        "CrashLoop",
        "CrashLoopBackOff",
        "Error",
        "ImagePullBackOff",
        "Pending",
        "Unknown",
        "Terminating",
        "Failed",
    }
)

DeploymentClassification = Literal["degraded", "critical"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_pod_unhealthy__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_pod_unhealthy__mutmut)
def is_pod_unhealthy(status: str) -> bool:
    return status in _UNHEALTHY_POD_STATUSES


def x_is_pod_unhealthy__mutmut_orig(status: str) -> bool:
    return status in _UNHEALTHY_POD_STATUSES


def x_is_pod_unhealthy__mutmut_1(status: str) -> bool:
    return status not in _UNHEALTHY_POD_STATUSES

mutants_x_is_pod_unhealthy__mutmut['_mutmut_orig'] = x_is_pod_unhealthy__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_pod_unhealthy__mutmut['x_is_pod_unhealthy__mutmut_1'] = x_is_pod_unhealthy__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_deployment__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_classify_deployment__mutmut)
def classify_deployment(ready: int, desired: int) -> DeploymentClassification | None:
    """A deployment intentionally scaled to 0 (desired=0) is never an issue."""
    if desired == 0:
        return None
    if ready == 0:
        return "critical"
    if ready < desired:
        return "degraded"
    return None


def x_classify_deployment__mutmut_orig(ready: int, desired: int) -> DeploymentClassification | None:
    """A deployment intentionally scaled to 0 (desired=0) is never an issue."""
    if desired == 0:
        return None
    if ready == 0:
        return "critical"
    if ready < desired:
        return "degraded"
    return None


def x_classify_deployment__mutmut_1(ready: int, desired: int) -> DeploymentClassification | None:
    """A deployment intentionally scaled to 0 (desired=0) is never an issue."""
    if desired != 0:
        return None
    if ready == 0:
        return "critical"
    if ready < desired:
        return "degraded"
    return None


def x_classify_deployment__mutmut_2(ready: int, desired: int) -> DeploymentClassification | None:
    """A deployment intentionally scaled to 0 (desired=0) is never an issue."""
    if desired == 1:
        return None
    if ready == 0:
        return "critical"
    if ready < desired:
        return "degraded"
    return None


def x_classify_deployment__mutmut_3(ready: int, desired: int) -> DeploymentClassification | None:
    """A deployment intentionally scaled to 0 (desired=0) is never an issue."""
    if desired == 0:
        return None
    if ready != 0:
        return "critical"
    if ready < desired:
        return "degraded"
    return None


def x_classify_deployment__mutmut_4(ready: int, desired: int) -> DeploymentClassification | None:
    """A deployment intentionally scaled to 0 (desired=0) is never an issue."""
    if desired == 0:
        return None
    if ready == 1:
        return "critical"
    if ready < desired:
        return "degraded"
    return None


def x_classify_deployment__mutmut_5(ready: int, desired: int) -> DeploymentClassification | None:
    """A deployment intentionally scaled to 0 (desired=0) is never an issue."""
    if desired == 0:
        return None
    if ready == 0:
        return "XXcriticalXX"
    if ready < desired:
        return "degraded"
    return None


def x_classify_deployment__mutmut_6(ready: int, desired: int) -> DeploymentClassification | None:
    """A deployment intentionally scaled to 0 (desired=0) is never an issue."""
    if desired == 0:
        return None
    if ready == 0:
        return "CRITICAL"
    if ready < desired:
        return "degraded"
    return None


def x_classify_deployment__mutmut_7(ready: int, desired: int) -> DeploymentClassification | None:
    """A deployment intentionally scaled to 0 (desired=0) is never an issue."""
    if desired == 0:
        return None
    if ready == 0:
        return "critical"
    if ready <= desired:
        return "degraded"
    return None


def x_classify_deployment__mutmut_8(ready: int, desired: int) -> DeploymentClassification | None:
    """A deployment intentionally scaled to 0 (desired=0) is never an issue."""
    if desired == 0:
        return None
    if ready == 0:
        return "critical"
    if ready < desired:
        return "XXdegradedXX"
    return None


def x_classify_deployment__mutmut_9(ready: int, desired: int) -> DeploymentClassification | None:
    """A deployment intentionally scaled to 0 (desired=0) is never an issue."""
    if desired == 0:
        return None
    if ready == 0:
        return "critical"
    if ready < desired:
        return "DEGRADED"
    return None

mutants_x_classify_deployment__mutmut['_mutmut_orig'] = x_classify_deployment__mutmut_orig # type: ignore # mutmut generated
mutants_x_classify_deployment__mutmut['x_classify_deployment__mutmut_1'] = x_classify_deployment__mutmut_1 # type: ignore # mutmut generated
mutants_x_classify_deployment__mutmut['x_classify_deployment__mutmut_2'] = x_classify_deployment__mutmut_2 # type: ignore # mutmut generated
mutants_x_classify_deployment__mutmut['x_classify_deployment__mutmut_3'] = x_classify_deployment__mutmut_3 # type: ignore # mutmut generated
mutants_x_classify_deployment__mutmut['x_classify_deployment__mutmut_4'] = x_classify_deployment__mutmut_4 # type: ignore # mutmut generated
mutants_x_classify_deployment__mutmut['x_classify_deployment__mutmut_5'] = x_classify_deployment__mutmut_5 # type: ignore # mutmut generated
mutants_x_classify_deployment__mutmut['x_classify_deployment__mutmut_6'] = x_classify_deployment__mutmut_6 # type: ignore # mutmut generated
mutants_x_classify_deployment__mutmut['x_classify_deployment__mutmut_7'] = x_classify_deployment__mutmut_7 # type: ignore # mutmut generated
mutants_x_classify_deployment__mutmut['x_classify_deployment__mutmut_8'] = x_classify_deployment__mutmut_8 # type: ignore # mutmut generated
mutants_x_classify_deployment__mutmut['x_classify_deployment__mutmut_9'] = x_classify_deployment__mutmut_9 # type: ignore # mutmut generated


def compute_health_status(has_critical: bool, has_degraded: bool) -> NamespaceHealthStatus:
    if has_critical:
        return NamespaceHealthStatus.CRITICAL
    if has_degraded:
        return NamespaceHealthStatus.DEGRADED
    return NamespaceHealthStatus.HEALTHY
mutants_x_build_root_cause__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_root_cause__mutmut)
def build_root_cause(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "Deployment"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_orig(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "Deployment"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_1(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "Deployment"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_2(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return "XXXX"

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "Deployment"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_3(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = None
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_4(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind != "Deployment"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_5(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "XXDeploymentXX"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_6(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "deployment"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_7(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "DEPLOYMENT"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_8(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "Deployment"
    ]
    primary = None

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_9(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "Deployment"
    ]
    primary = deployment_issues[1] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_10(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "Deployment"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[1]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_11(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "Deployment"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) != 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_12(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "Deployment"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 2:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 1} more issue(s))"


def x_build_root_cause__mutmut_13(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "Deployment"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) + 1} more issue(s))"


def x_build_root_cause__mutmut_14(unhealthy_resources: list[UnhealthyResource]) -> str:
    """One-line summary — deployment issues are more systemic than a single
    pod's, so they're preferred as the stated primary cause when both exist."""
    if not unhealthy_resources:
        return ""

    deployment_issues = [
        resource for resource in unhealthy_resources if resource.kind == "Deployment"
    ]
    primary = deployment_issues[0] if deployment_issues else unhealthy_resources[0]

    if len(unhealthy_resources) == 1:
        return f"{primary.name}: {primary.reason}"
    return f"{primary.name}: {primary.reason} (+{len(unhealthy_resources) - 2} more issue(s))"

mutants_x_build_root_cause__mutmut['_mutmut_orig'] = x_build_root_cause__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_1'] = x_build_root_cause__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_2'] = x_build_root_cause__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_3'] = x_build_root_cause__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_4'] = x_build_root_cause__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_5'] = x_build_root_cause__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_6'] = x_build_root_cause__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_7'] = x_build_root_cause__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_8'] = x_build_root_cause__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_9'] = x_build_root_cause__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_10'] = x_build_root_cause__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_11'] = x_build_root_cause__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_12'] = x_build_root_cause__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_13'] = x_build_root_cause__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_root_cause__mutmut['x_build_root_cause__mutmut_14'] = x_build_root_cause__mutmut_14 # type: ignore # mutmut generated
