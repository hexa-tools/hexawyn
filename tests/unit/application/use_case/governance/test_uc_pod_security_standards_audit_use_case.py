from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.governance.pod_security_standards_audit.command import (
    PodSecurityStandardsAuditCommand,
)
from hexawyn.application.use_case.governance.pod_security_standards_audit.pod_security_standards_audit_use_case import (  # noqa: E501
    PodSecurityStandardsAuditUseCase,
)
from hexawyn.application.use_case.governance.pod_security_standards_audit.response import (
    PodSecurityStandardsAuditResponse,
)


class TestPodSecurityStandardsAuditUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = []
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        assert isinstance(result, PodSecurityStandardsAuditResponse)
        assert result.total_pods_checked == 0
        assert result.compliant_pod_count == 0

    def test_execute_finds_privileged_container(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "bad-pod",
                "namespace": "default",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": False,
                "host_network": False,
                "host_ipc": False,
                "containers": [
                    {
                        "container_name": "main",
                        "container_kind": "container",
                        "privileged": True,
                        "allow_privilege_escalation": False,
                        "run_as_non_root": True,
                        "added_capabilities": [],
                    },
                ],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        assert result.total_pods_checked == 1
        assert result.compliant_pod_count == 0
        assert len(result.findings) == 1
        finding = result.findings[0]
        assert finding["pod_name"] == "bad-pod"
        assert any(v["violation_type"] == "privileged" for v in finding["violations"])

    def test_execute_finds_host_pid(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "host-pid-pod",
                "namespace": "default",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": True,
                "host_network": False,
                "host_ipc": False,
                "containers": [],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        assert len(result.findings) == 1
        violations = result.findings[0]["violations"]
        assert any(v["violation_type"] == "host_pid" for v in violations)

    def test_execute_finds_host_network(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "host-net-pod",
                "namespace": "default",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": False,
                "host_network": True,
                "host_ipc": False,
                "containers": [],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        violations = result.findings[0]["violations"]
        assert any(v["violation_type"] == "host_network" for v in violations)

    def test_execute_finds_host_ipc(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "host-ipc-pod",
                "namespace": "default",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": False,
                "host_network": False,
                "host_ipc": True,
                "containers": [],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        violations = result.findings[0]["violations"]
        assert any(v["violation_type"] == "host_ipc" for v in violations)

    def test_execute_finds_run_as_root(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "root-pod",
                "namespace": "default",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": False,
                "host_network": False,
                "host_ipc": False,
                "containers": [
                    {
                        "container_name": "main",
                        "container_kind": "container",
                        "privileged": False,
                        "allow_privilege_escalation": False,
                        "run_as_non_root": None,
                        "added_capabilities": [],
                    },
                ],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        violations = result.findings[0]["violations"]
        assert any(v["violation_type"] == "run_as_root" for v in violations)

    def test_execute_finds_allow_privilege_escalation(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "esc-pod",
                "namespace": "default",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": False,
                "host_network": False,
                "host_ipc": False,
                "containers": [
                    {
                        "container_name": "main",
                        "container_kind": "container",
                        "privileged": False,
                        "allow_privilege_escalation": True,
                        "run_as_non_root": True,
                        "added_capabilities": [],
                    },
                ],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        violations = result.findings[0]["violations"]
        assert any(v["violation_type"] == "allow_privilege_escalation" for v in violations)

    def test_execute_finds_dangerous_capability(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "cap-pod",
                "namespace": "default",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": False,
                "host_network": False,
                "host_ipc": False,
                "containers": [
                    {
                        "container_name": "main",
                        "container_kind": "container",
                        "privileged": False,
                        "allow_privilege_escalation": False,
                        "run_as_non_root": True,
                        "added_capabilities": ["SYS_ADMIN"],
                    },
                ],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        violations = result.findings[0]["violations"]
        assert any(v["violation_type"] == "dangerous_capability" for v in violations)

    def test_execute_compliant_pod(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "good-pod",
                "namespace": "default",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": True,
                "host_pid": False,
                "host_network": False,
                "host_ipc": False,
                "containers": [
                    {
                        "container_name": "main",
                        "container_kind": "container",
                        "privileged": False,
                        "allow_privilege_escalation": False,
                        "run_as_non_root": True,
                        "added_capabilities": [],
                    },
                ],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        assert result.total_pods_checked == 1
        assert result.compliant_pod_count == 1
        assert len(result.findings) == 0

    def test_execute_system_workload_gets_note(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "node-exporter-abc123",
                "namespace": "kube-system",
                "owner_kind": "DaemonSet",
                "pod_run_as_non_root": None,
                "host_pid": True,
                "host_network": False,
                "host_ipc": False,
                "containers": [],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        finding = result.findings[0]
        assert finding["note"] is not None
        assert "system workload" in finding["note"]

    def test_execute_namespace_filtering(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "pod-a",
                "namespace": "ns-a",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": True,
                "host_network": False,
                "host_ipc": False,
                "containers": [],
            },
            {
                "pod_name": "pod-b",
                "namespace": "ns-b",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": True,
                "host_network": False,
                "host_ipc": False,
                "containers": [],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand(namespaces=["ns-a"]))

        assert result.total_pods_checked == 1
        assert result.findings[0]["namespace"] == "ns-a"

    def test_execute_with_psa_enforce_levels(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "bad-pod",
                "namespace": "default",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": True,
                "host_network": False,
                "host_ipc": False,
                "containers": [],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {"default": "restricted"}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        finding = result.findings[0]
        assert finding["namespace_psa_enforce_level"] == "restricted"

    def test_execute_no_namespace_psa_level(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "bad-pod",
                "namespace": "unknown-ns",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": True,
                "host_network": False,
                "host_ipc": False,
                "containers": [],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        finding = result.findings[0]
        assert finding["namespace_psa_enforce_level"] is None

    def test_execute_low_severity_capability(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "cap-pod",
                "namespace": "default",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": False,
                "host_network": False,
                "host_ipc": False,
                "containers": [
                    {
                        "container_name": "main",
                        "container_kind": "container",
                        "privileged": False,
                        "allow_privilege_escalation": False,
                        "run_as_non_root": True,
                        "added_capabilities": ["NET_RAW"],
                    },
                ],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        violations = result.findings[0]["violations"]
        vio = next(v for v in violations if v["violation_type"] == "dangerous_capability")
        assert vio["severity"] == "medium"

    def test_execute_multiple_violations_per_pod(self) -> None:
        port = MagicMock()
        port.list_pod_security_specs.return_value = [
            {
                "pod_name": "multi-violation-pod",
                "namespace": "default",
                "owner_kind": "Deployment",
                "pod_run_as_non_root": None,
                "host_pid": True,
                "host_network": True,
                "host_ipc": False,
                "containers": [
                    {
                        "container_name": "main",
                        "container_kind": "container",
                        "privileged": True,
                        "allow_privilege_escalation": True,
                        "run_as_non_root": None,
                        "added_capabilities": ["SYS_ADMIN"],
                    },
                ],
            },
        ]
        port.get_namespace_psa_enforce_levels.return_value = {}

        use_case = PodSecurityStandardsAuditUseCase(pod_security_port=port)
        result = use_case.audit_pod_security(PodSecurityStandardsAuditCommand())

        violations = result.findings[0]["violations"]
        violation_types = {v["violation_type"] for v in violations}
        assert "host_pid" in violation_types
        assert "host_network" in violation_types
        assert "privileged" in violation_types
        assert "allow_privilege_escalation" in violation_types
        assert "run_as_root" in violation_types
        assert "dangerous_capability" in violation_types
