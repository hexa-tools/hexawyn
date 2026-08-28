from __future__ import annotations

from abc import ABC

from hexawyn.application.ports.driven.cilium_hubble_port import CiliumHubblePort
from hexawyn.domain.models.cilium import CiliumFlowQuery, CiliumFlowsResult


class _FakeHubblePort(CiliumHubblePort):
    def get_flows(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        return CiliumFlowsResult(
            installed=False,
            status="not_installed",
            total_flows=0,
            flows=[],
            note=None,
        )


class TestCiliumHubblePort:
    def test_is_abstract(self) -> None:
        assert issubclass(CiliumHubblePort, ABC)

    def test_get_flows_is_abstract_method(self) -> None:
        assert "get_flows" in CiliumHubblePort.__abstractmethods__

    def test_subclass_can_be_instantiated(self) -> None:
        assert _FakeHubblePort().get_flows(CiliumFlowQuery()).status == "not_installed"
