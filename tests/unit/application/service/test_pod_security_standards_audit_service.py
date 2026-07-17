"""Unit tests for PodSecurityStandardsAuditService (mocks PodSecurityContextAuditPort).

Covers the ticket's five Test Scenarios (TC1-TC5) and its five Edge Cases by
name in the test names.
"""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_command import (
    DetectPrivilegedPodsCommand,
)
from hexawyn.application.service.pod_security_standards_audit_service import (
    PodSecurityStandardsAuditService,
)


def _container(
    name: str,
    kind: str = "container",
    privileged: bool | None = None,
    escalation: bool | None = None,
    run_as_non_root: bool | None = None,
    capabilities: list[str] | None = None,
) -> dict:
    return {
        "container_name": name,
        "container_kind": kind,
        "privileged": privileged,
        "allow_privilege_escalation": escalation,
        "run_as_non_root": run_as_non_root,
        "added_capabilities": capabilities or [],
    }


def _pod(
    name: str,
    namespace: str = "production",
    owner_kind: str | None = None,
    pod_run_as_non_root: bool | None = None,
    host_pid: bool = False,
    host_network: bool = False,
    host_ipc: bool = False,
    containers: list[dict] | None = None,
) -> dict:
    return {
        "pod_name": name,
        "namespace": namespace,
        "owner_kind": owner_kind,
        "pod_run_as_non_root": pod_run_as_non_root,
        "host_pid": host_pid,
        "host_network": host_network,
        "host_ipc": host_ipc,
        "containers": containers or [],
    }


def _make_service(
    pod_specs: list[dict] | None = None, psa_levels: dict[str, str] | None = None
) -> tuple[PodSecurityStandardsAuditService, MagicMock]:
    port = MagicMock()
    port.list_pod_security_specs.return_value = pod_specs or []
    port.get_namespace_psa_enforce_levels.return_value = psa_levels or {}
    service = PodSecurityStandardsAuditService(pod_security_port=port)
    return service, port


class TestPrivilegedContainer:
    def test_tc1_privileged_true_is_critical_baseline(self) -> None:
        service, _ = _make_service(
            pod_specs=[_pod("data-processor-abc", containers=[_container("app", privileged=True)])]
        )

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        finding = response.findings[0]
        violation = next(v for v in finding["violations"] if v["violation_type"] == "privileged")
        assert violation["severity"] == "critical"
        assert violation["pss_level"] == "Baseline"


class TestRunAsRoot:
    def test_tc2_run_as_non_root_false_is_high_restricted(self) -> None:
        service, _ = _make_service(
            pod_specs=[
                _pod(
                    "reader-pod",
                    containers=[_container("app", privileged=False, run_as_non_root=False)],
                )
            ]
        )

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        finding = response.findings[0]
        violation = next(v for v in finding["violations"] if v["violation_type"] == "run_as_root")
        assert violation["severity"] == "high"
        assert violation["pss_level"] == "Restricted"


class TestAllowPrivilegeEscalation:
    def test_tc3_allow_privilege_escalation_true_is_medium(self) -> None:
        service, _ = _make_service(
            pod_specs=[
                _pod(
                    "escalating-pod",
                    containers=[
                        _container("app", privileged=False, escalation=True, run_as_non_root=True)
                    ],
                )
            ]
        )

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        finding = response.findings[0]
        violation_types = {v["violation_type"] for v in finding["violations"]}
        assert violation_types == {"allow_privilege_escalation"}
        assert finding["violations"][0]["severity"] == "medium"


class TestAllPodsCompliant:
    def test_tc4_all_pods_compliant_produces_no_violations(self) -> None:
        service, _ = _make_service(
            pod_specs=[
                _pod(
                    "compliant-pod",
                    containers=[
                        _container("app", privileged=False, escalation=False, run_as_non_root=True)
                    ],
                )
            ]
        )

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        assert response.findings == []
        assert response.compliant_pod_count == 1


class TestTenViolatingPodsAcrossThreeNamespaces:
    def test_tc5_ten_violating_pods_across_three_namespaces_all_listed(self) -> None:
        namespaces = ["production", "staging", "monitoring"]
        pods = [
            _pod(
                f"pod-{i}",
                namespace=namespaces[i % 3],
                containers=[_container("app", privileged=True)],
            )
            for i in range(10)
        ]
        service, _ = _make_service(pod_specs=pods)

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        assert len(response.findings) == 10
        assert {f["namespace"] for f in response.findings} == set(namespaces)


class TestDaemonSetLegitimateHostPid:
    def test_edge_case_known_system_daemonset_shown_with_note(self) -> None:
        service, _ = _make_service(
            pod_specs=[
                _pod(
                    "node-exporter-xyz",
                    namespace="monitoring",
                    owner_kind="DaemonSet",
                    host_pid=True,
                    containers=[
                        _container(
                            "node-exporter",
                            privileged=False,
                            escalation=False,
                            run_as_non_root=True,
                        )
                    ],
                )
            ]
        )

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        finding = response.findings[0]
        assert finding["note"] == "expected system workload (known system DaemonSet)"
        violation = next(v for v in finding["violations"] if v["violation_type"] == "host_pid")
        assert violation["severity"] == "critical"


class TestInitContainerCheckedIndependently:
    def test_edge_case_init_container_with_different_security_context_is_checked(self) -> None:
        init_container = _container("init-setup", kind="init", privileged=True)
        main_container = _container(
            "app", kind="container", privileged=False, escalation=False, run_as_non_root=True
        )
        service, _ = _make_service(
            pod_specs=[_pod("p", containers=[init_container, main_container])]
        )

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        finding = response.findings[0]
        flagged_containers = {v["container_name"] for v in finding["violations"]}
        assert flagged_containers == {"init-setup"}


class TestNoSecurityContextDefaults:
    def test_edge_case_no_security_context_defaults_to_root_and_escalation_allowed(self) -> None:
        service, _ = _make_service(pod_specs=[_pod("p", containers=[_container("app")])])

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        finding = response.findings[0]
        violation_types = {v["violation_type"] for v in finding["violations"]}
        assert "run_as_root" in violation_types
        assert "allow_privilege_escalation" in violation_types
        assert "privileged" not in violation_types


class TestHostNetworkAndHostIpc:
    def test_host_network_true_is_flagged_critical_baseline(self) -> None:
        service, _ = _make_service(
            pod_specs=[
                _pod(
                    "p",
                    host_network=True,
                    containers=[
                        _container("app", privileged=False, escalation=False, run_as_non_root=True)
                    ],
                )
            ]
        )

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        finding = response.findings[0]
        violation = next(v for v in finding["violations"] if v["violation_type"] == "host_network")
        assert violation["severity"] == "critical"
        assert violation["pss_level"] == "Baseline"

    def test_host_ipc_true_is_flagged_critical_baseline(self) -> None:
        service, _ = _make_service(
            pod_specs=[
                _pod(
                    "p",
                    host_ipc=True,
                    containers=[
                        _container("app", privileged=False, escalation=False, run_as_non_root=True)
                    ],
                )
            ]
        )

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        finding = response.findings[0]
        violation = next(v for v in finding["violations"] if v["violation_type"] == "host_ipc")
        assert violation["severity"] == "critical"
        assert violation["pss_level"] == "Baseline"


class TestNamespacePsaCrossReference:
    def test_edge_case_namespace_psa_enforce_restricted_is_cross_referenced(self) -> None:
        service, _ = _make_service(
            pod_specs=[
                _pod("p", namespace="production", containers=[_container("app", privileged=True)])
            ],
            psa_levels={"production": "restricted"},
        )

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        assert response.findings[0]["namespace_psa_enforce_level"] == "restricted"


class TestNetBindServiceCapability:
    def test_edge_case_net_bind_service_capability_is_medium_not_critical(self) -> None:
        service, _ = _make_service(
            pod_specs=[
                _pod(
                    "p",
                    containers=[
                        _container(
                            "app",
                            privileged=False,
                            escalation=False,
                            run_as_non_root=True,
                            capabilities=["NET_BIND_SERVICE"],
                        )
                    ],
                )
            ]
        )

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        finding = response.findings[0]
        violation = next(
            v for v in finding["violations"] if v["violation_type"] == "dangerous_capability"
        )
        assert violation["severity"] == "medium"


class TestNamespacesFilter:
    def test_namespaces_filter_narrows_scan_to_requested_namespaces(self) -> None:
        pods = [
            _pod("a", namespace="production", containers=[_container("app", privileged=True)]),
            _pod("b", namespace="staging", containers=[_container("app", privileged=True)]),
        ]
        service, _ = _make_service(pod_specs=pods)

        response = service.audit_pod_security(
            DetectPrivilegedPodsCommand(namespaces=["production"])
        )

        assert len(response.findings) == 1
        assert response.findings[0]["namespace"] == "production"


class TestTotalPodsChecked:
    def test_total_pods_checked_reflects_all_scanned_pods(self) -> None:
        service, _ = _make_service(
            pod_specs=[
                _pod("a", containers=[_container("app", privileged=True)]),
                _pod(
                    "b",
                    containers=[
                        _container("app", privileged=False, escalation=False, run_as_non_root=True)
                    ],
                ),
            ]
        )

        response = service.audit_pod_security(DetectPrivilegedPodsCommand())

        assert response.total_pods_checked == 2
