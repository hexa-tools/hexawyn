from __future__ import annotations

from hexawyn.domain.models.pod_security import (
    ContainerSecurityContext,
    PodSecuritySpec,
    SecurityViolation,
)
from hexawyn.domain.services.pod_security.scanner import (
    build_violation,
    scan_container,
    scan_pod,
)


def _container(
    name: str = "app",
    privileged: bool | None = False,
    allow_privilege_escalation: bool | None = False,
    run_as_non_root: bool | None = True,
    added_capabilities: list[str] | None = None,
) -> ContainerSecurityContext:
    return ContainerSecurityContext(
        container_name=name,
        container_kind="container",
        privileged=privileged,
        allow_privilege_escalation=allow_privilege_escalation,
        run_as_non_root=run_as_non_root,
        added_capabilities=added_capabilities or [],
    )


def _spec(  # noqa: PLR0913
    pod_name: str = "test-pod",
    namespace: str = "default",
    containers: list[ContainerSecurityContext] | None = None,
    host_pid: bool = False,
    host_network: bool = False,
    host_ipc: bool = False,
    pod_run_as_non_root: bool | None = None,
) -> PodSecuritySpec:
    return PodSecuritySpec(
        pod_name=pod_name,
        namespace=namespace,
        owner_kind=None,
        pod_run_as_non_root=pod_run_as_non_root,
        host_pid=host_pid,
        host_network=host_network,
        host_ipc=host_ipc,
        containers=containers or [_container()],
    )


class TestBuildViolation:
    def test_returns_security_violation(self) -> None:
        result = build_violation("privileged", "app")
        assert isinstance(result, SecurityViolation)
        assert result.violation_type == "privileged"
        assert result.container_name == "app"
        assert result.severity == "critical"
        assert result.pss_level == "Baseline"

    def test_dangerous_capability_medium(self) -> None:
        result = build_violation("dangerous_capability", "app", "NET_RAW")
        assert result.violation_type == "dangerous_capability"
        assert result.severity == "medium"

    def test_dangerous_capability_high(self) -> None:
        result = build_violation("dangerous_capability", "app", "SYS_ADMIN")
        assert result.violation_type == "dangerous_capability"
        assert result.severity == "high"

    def test_run_as_root(self) -> None:
        result = build_violation("run_as_root", "worker")
        assert result.violation_type == "run_as_root"
        assert result.severity == "high"
        assert result.pss_level == "Restricted"

    def test_allow_privilege_escalation(self) -> None:
        result = build_violation("allow_privilege_escalation", "sidecar")
        assert result.violation_type == "allow_privilege_escalation"
        assert result.severity == "medium"

    def test_host_violations_are_critical(self) -> None:
        for vt in ("host_pid", "host_network", "host_ipc"):
            result = build_violation(vt, None)
            assert result.severity == "critical"
            assert result.pss_level == "Baseline"


class TestScanContainer:
    def test_no_violations_for_safe_container(self) -> None:
        c = _container()
        violations = scan_container(c, None)
        assert violations == []

    def test_privileged_detected(self) -> None:
        c = _container(privileged=True)
        violations = scan_container(c, None)
        assert len(violations) == 1
        assert violations[0].violation_type == "privileged"

    def test_run_as_root_detected(self) -> None:
        c = _container(run_as_non_root=False)
        violations = scan_container(c, None)
        assert any(v.violation_type == "run_as_root" for v in violations)

    def test_run_as_root_pod_level_missing(self) -> None:
        c = _container(run_as_non_root=None)
        violations = scan_container(c, None)
        assert any(v.violation_type == "run_as_root" for v in violations)

    def test_run_as_root_pod_level_true_container_none(self) -> None:
        c = _container(run_as_non_root=None)
        violations = scan_container(c, True)
        assert not any(v.violation_type == "run_as_root" for v in violations)

    def test_privilege_escalation_detected(self) -> None:
        c = _container(allow_privilege_escalation=True)
        violations = scan_container(c, None)
        assert any(v.violation_type == "allow_privilege_escalation" for v in violations)

    def test_privilege_escalation_none_is_allowed(self) -> None:
        c = _container(allow_privilege_escalation=None)
        violations = scan_container(c, None)
        assert any(v.violation_type == "allow_privilege_escalation" for v in violations)

    def test_dangerous_capabilities_detected(self) -> None:
        c = _container(added_capabilities=["SYS_ADMIN", "NET_RAW"])
        violations = scan_container(c, None)
        caps = [v for v in violations if v.violation_type == "dangerous_capability"]
        assert len(caps) == 2  # noqa: PLR2004

    def test_multiple_violations(self) -> None:
        c = _container(privileged=True, allow_privilege_escalation=True, run_as_non_root=False)
        violations = scan_container(c, None)
        assert len(violations) >= 3  # noqa: PLR2004

    def test_run_as_non_root_true_no_violation(self) -> None:
        c = _container(run_as_non_root=True)
        violations = scan_container(c, None)
        assert not any(v.violation_type == "run_as_root" for v in violations)

    def test_privilege_escalation_false_no_violation(self) -> None:
        c = _container(allow_privilege_escalation=False)
        violations = scan_container(c, None)
        assert not any(v.violation_type == "allow_privilege_escalation" for v in violations)


class TestScanPod:
    def test_safe_pod_no_violations(self) -> None:
        spec = _spec()
        violations = scan_pod(spec)
        assert violations == []

    def test_host_pid_detected(self) -> None:
        spec = _spec(host_pid=True)
        violations = scan_pod(spec)
        assert any(v.violation_type == "host_pid" for v in violations)

    def test_host_network_detected(self) -> None:
        spec = _spec(host_network=True)
        violations = scan_pod(spec)
        assert any(v.violation_type == "host_network" for v in violations)

    def test_host_ipc_detected(self) -> None:
        spec = _spec(host_ipc=True)
        violations = scan_pod(spec)
        assert any(v.violation_type == "host_ipc" for v in violations)

    def test_all_host_features_detected(self) -> None:
        spec = _spec(host_pid=True, host_network=True, host_ipc=True)
        violations = scan_pod(spec)
        assert len(violations) == 3  # noqa: PLR2004

    def test_multiple_containers_scanned(self) -> None:
        spec = _spec(
            containers=[
                _container(name="app", privileged=True),
                _container(name="sidecar", allow_privilege_escalation=True),
            ]
        )
        violations = scan_pod(spec)
        assert len(violations) == 2  # noqa: PLR2004
        names = {v.container_name for v in violations}
        assert names == {"app", "sidecar"}

    def test_host_and_container_violations_combined(self) -> None:
        spec = _spec(host_pid=True, containers=[_container(privileged=True)])
        violations = scan_pod(spec)
        assert len(violations) == 2  # noqa: PLR2004
        types = {v.violation_type for v in violations}
        assert types == {"host_pid", "privileged"}
