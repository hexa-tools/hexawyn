"""Tests for CalicoPort ABC contract."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.domain.models.calico import CalicoDetectionResult


class TestCalicoPort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            CalicoPort()  # type: ignore[abstract]

    def test_exposes_detect(self) -> None:
        assert "detect" in CalicoPort.__abstractmethods__

    def test_exposes_required_methods(self) -> None:
        for method in (
            "status",
            "list_network_policies",
            "get_network_policy",
            "list_workloads",
            "audit_policies",
            "list_ip_pools",
            "list_host_endpoints",
            "list_bgp_configurations",
            "list_bgp_peers",
            "bgp_audit",
            "encryption_status",
            "felix_metrics",
            "connectivity_health",
        ):
            assert method in CalicoPort.__abstractmethods__

    def test_subclass_implementing_virtual_methods(self) -> None:  # noqa: C901
        class Fake(CalicoPort):
            def detect(self) -> CalicoDetectionResult:
                raise NotImplementedError

            def status(self) -> CalicoDetectionResult:
                raise NotImplementedError

            def list_network_policies(self, namespace: str | None = None) -> list:
                return []

            def get_network_policy(self, name: str, namespace: str):
                return None

            def list_workloads(self, namespace: str | None = None) -> list:
                return []

            def audit_policies(self) -> dict:
                return {}

            def list_ip_pools(self) -> list:
                return []

            def list_host_endpoints(self) -> list:
                return []

            def list_bgp_configurations(self) -> list:
                return []

            def list_bgp_peers(self) -> list:
                return []

            def bgp_audit(self) -> dict:
                return {}

            def encryption_status(self) -> dict:
                return {}

            def felix_metrics(self) -> dict:
                return {}

            def connectivity_health(self) -> dict:
                return {}

        assert isinstance(Fake(), CalicoPort)
