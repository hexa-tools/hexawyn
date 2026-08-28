from __future__ import annotations

from abc import ABC

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.ports.driving.cilium_detect.cilium_detect_service_port import (
    CiliumDetectServicePort,
)
from hexawyn.domain.models.cilium import (
    CiliumDetectionResult,
    CiliumIdentitiesResult,
    CiliumNetworkPoliciesResult,
    CiliumNetworkPolicyDetail,
    CiliumPolicyAuditResult,
    CiliumSegmentationAuditResult,
    CiliumStatusResult,
)


class _FakeCiliumPort(CiliumPort):
    def detect(self) -> CiliumDetectionResult:
        return CiliumDetectionResult(
            installed=False,
            status="not_installed",
            version=None,
            mode="UNKNOWN",
            namespace=None,
            total_agents=0,
            ready_agents=0,
            degraded_summary=None,
            agents=[],
            note=None,
        )

    def status(self) -> CiliumStatusResult:
        return CiliumStatusResult(
            installed=False,
            status="not_installed",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=[],
            note=None,
        )

    def list_network_policies(self) -> CiliumNetworkPoliciesResult:
        return CiliumNetworkPoliciesResult(
            installed=False,
            status="not_installed",
            total_policies=0,
            namespaced_count=0,
            clusterwide_count=0,
            policies=[],
            note=None,
        )

    def get_network_policy(self, name: str, namespace: str | None) -> CiliumNetworkPolicyDetail:
        return CiliumNetworkPolicyDetail(
            installed=False,
            status="not_installed",
            kind="",
            name="",
            namespace=None,
            endpoint_selector="",
            ingress_rules=(),
            egress_rules=(),
            l7_protocols=(),
            spec={},
            note=None,
        )

    def audit_policies(self) -> CiliumPolicyAuditResult:
        return CiliumPolicyAuditResult(
            installed=False,
            status="not_installed",
            view="vanilla",
            total_workloads=0,
            uncovered_count=0,
            findings=[],
            summary="",
            note=None,
        )

    def list_identities(self) -> CiliumIdentitiesResult:
        return CiliumIdentitiesResult(
            installed=False,
            status="not_installed",
            total_identities=0,
            identities=[],
            note=None,
        )

    def segmentation_audit(self) -> CiliumSegmentationAuditResult:
        return CiliumSegmentationAuditResult(
            installed=False,
            status="not_installed",
            view="vanilla",
            total_identities=0,
            total_paths=0,
            uncovered_paths=0,
            findings=[],
            summary="",
            note=None,
        )


class _FakeCiliumDetectServicePort(CiliumDetectServicePort):
    def detect(self, command: object) -> object:
        return command


class TestCiliumPort:
    def test_is_abstract(self) -> None:
        assert issubclass(CiliumPort, ABC)

    def test_detect_is_abstract_method(self) -> None:
        assert "detect" in CiliumPort.__abstractmethods__

    def test_subclass_must_implement_detect(self) -> None:
        port = _FakeCiliumPort()
        result = port.detect()
        assert result.installed is False

    def test_status_is_abstract_method(self) -> None:
        assert "status" in CiliumPort.__abstractmethods__

    def test_subclass_must_implement_status(self) -> None:
        assert _FakeCiliumPort().status().status == "not_installed"

    def test_list_network_policies_is_abstract_method(self) -> None:
        assert "list_network_policies" in CiliumPort.__abstractmethods__

    def test_subclass_must_implement_list_network_policies(self) -> None:
        assert _FakeCiliumPort().list_network_policies().status == "not_installed"

    def test_get_network_policy_is_abstract_method(self) -> None:
        assert "get_network_policy" in CiliumPort.__abstractmethods__

    def test_subclass_must_implement_get_network_policy(self) -> None:
        detail = _FakeCiliumPort().get_network_policy("p", "ns")
        assert detail.status == "not_installed"

    def test_audit_policies_is_abstract_method(self) -> None:
        assert "audit_policies" in CiliumPort.__abstractmethods__

    def test_subclass_must_implement_audit_policies(self) -> None:
        assert _FakeCiliumPort().audit_policies().view == "vanilla"

    def test_list_identities_is_abstract_method(self) -> None:
        assert "list_identities" in CiliumPort.__abstractmethods__

    def test_subclass_must_implement_list_identities(self) -> None:
        assert _FakeCiliumPort().list_identities().status == "not_installed"

    def test_segmentation_audit_is_abstract_method(self) -> None:
        assert "segmentation_audit" in CiliumPort.__abstractmethods__

    def test_subclass_must_implement_segmentation_audit(self) -> None:
        assert _FakeCiliumPort().segmentation_audit().view == "vanilla"


class TestCiliumDetectServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(CiliumDetectServicePort, ABC)

    def test_subclass_can_be_instantiated(self) -> None:
        port = _FakeCiliumDetectServicePort()
        assert port.detect(command="ping") == "ping"
