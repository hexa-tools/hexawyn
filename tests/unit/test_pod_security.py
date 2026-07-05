"""Unit tests for the Pod Security Standards Audit domain models."""

from __future__ import annotations

import dataclasses

import pytest


class TestContainerSecurityContext:
    def test_creates_context_with_expected_fields(self) -> None:
        from hexawyn.domain.models.pod_security import ContainerSecurityContext

        context = ContainerSecurityContext(
            container_name="app",
            container_kind="container",
            privileged=True,
            allow_privilege_escalation=True,
            run_as_non_root=None,
            added_capabilities=["SYS_ADMIN"],
        )

        assert context.container_name == "app"
        assert context.container_kind == "container"
        assert context.privileged is True
        assert context.allow_privilege_escalation is True
        assert context.run_as_non_root is None
        assert context.added_capabilities == ["SYS_ADMIN"]

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.pod_security import ContainerSecurityContext

        context = ContainerSecurityContext(
            container_name="app",
            container_kind="init",
            privileged=None,
            allow_privilege_escalation=None,
            run_as_non_root=None,
            added_capabilities=[],
        )

        with pytest.raises(dataclasses.FrozenInstanceError):
            context.privileged = True  # type: ignore[misc]


class TestPodSecuritySpec:
    def test_creates_spec_with_expected_fields(self) -> None:
        from hexawyn.domain.models.pod_security import ContainerSecurityContext, PodSecuritySpec

        container = ContainerSecurityContext(
            container_name="app",
            container_kind="container",
            privileged=False,
            allow_privilege_escalation=False,
            run_as_non_root=True,
            added_capabilities=[],
        )
        spec = PodSecuritySpec(
            pod_name="payment-pod-abc",
            namespace="production",
            owner_kind="ReplicaSet",
            pod_run_as_non_root=None,
            host_pid=False,
            host_network=False,
            host_ipc=False,
            containers=[container],
        )

        assert spec.pod_name == "payment-pod-abc"
        assert spec.namespace == "production"
        assert spec.owner_kind == "ReplicaSet"
        assert spec.pod_run_as_non_root is None
        assert spec.host_pid is False
        assert spec.containers == [container]

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.pod_security import PodSecuritySpec

        spec = PodSecuritySpec(
            pod_name="p",
            namespace="n",
            owner_kind=None,
            pod_run_as_non_root=None,
            host_pid=False,
            host_network=False,
            host_ipc=False,
            containers=[],
        )

        with pytest.raises(dataclasses.FrozenInstanceError):
            spec.host_pid = True  # type: ignore[misc]


class TestSecurityViolation:
    def test_creates_violation_with_expected_fields(self) -> None:
        from hexawyn.domain.models.pod_security import SecurityViolation

        violation = SecurityViolation(
            violation_type="privileged",
            severity="critical",
            pss_level="Baseline",
            container_name="app",
            recommendation="Set privileged: false in the container's securityContext.",
        )

        assert violation.violation_type == "privileged"
        assert violation.severity == "critical"
        assert violation.pss_level == "Baseline"
        assert violation.container_name == "app"
        assert violation.recommendation.startswith("Set privileged")

    def test_pod_level_violation_has_no_container_name(self) -> None:
        from hexawyn.domain.models.pod_security import SecurityViolation

        violation = SecurityViolation(
            violation_type="host_pid",
            severity="critical",
            pss_level="Baseline",
            container_name=None,
            recommendation="Set hostPID: false in the pod spec.",
        )

        assert violation.container_name is None

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.pod_security import SecurityViolation

        violation = SecurityViolation(
            violation_type="privileged",
            severity="critical",
            pss_level="Baseline",
            container_name=None,
            recommendation="x",
        )

        with pytest.raises(dataclasses.FrozenInstanceError):
            violation.severity = "high"  # type: ignore[misc]


class TestPodSecurityFinding:
    def test_creates_finding_with_expected_fields(self) -> None:
        from hexawyn.domain.models.pod_security import PodSecurityFinding, SecurityViolation

        violation = SecurityViolation(
            violation_type="host_pid",
            severity="critical",
            pss_level="Baseline",
            container_name=None,
            recommendation="Set hostPID: false in the pod spec.",
        )
        finding = PodSecurityFinding(
            pod_name="node-exporter-abc",
            namespace="monitoring",
            violations=[violation],
            note="expected system workload (known system DaemonSet)",
            namespace_psa_enforce_level="restricted",
        )

        assert finding.pod_name == "node-exporter-abc"
        assert finding.namespace == "monitoring"
        assert finding.violations == [violation]
        assert finding.note == "expected system workload (known system DaemonSet)"
        assert finding.namespace_psa_enforce_level == "restricted"

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.pod_security import PodSecurityFinding

        finding = PodSecurityFinding(
            pod_name="p",
            namespace="n",
            violations=[],
            note=None,
            namespace_psa_enforce_level=None,
        )

        with pytest.raises(dataclasses.FrozenInstanceError):
            finding.note = "x"  # type: ignore[misc]


class TestPodSecurityAuditReport:
    def test_creates_report_with_expected_fields(self) -> None:
        from hexawyn.domain.models.pod_security import (
            PodSecurityAuditReport,
            PodSecurityFinding,
            SecurityViolation,
        )

        violation = SecurityViolation(
            violation_type="privileged",
            severity="critical",
            pss_level="Baseline",
            container_name="app",
            recommendation="x",
        )
        finding = PodSecurityFinding(
            pod_name="data-processor-abc",
            namespace="production",
            violations=[violation],
            note=None,
            namespace_psa_enforce_level=None,
        )
        report = PodSecurityAuditReport(
            findings=[finding],
            compliant_pod_count=8,
            total_pods_checked=9,
            summary="1 pod violating Pod Security Standards across 1 namespace.",
        )

        assert report.findings == [finding]
        assert report.compliant_pod_count == 8
        assert report.total_pods_checked == 9
        assert "1 pod violating" in report.summary
