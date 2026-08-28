from __future__ import annotations

from abc import ABC

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.ports.driving.cilium_detect.cilium_detect_service_port import (
    CiliumDetectServicePort,
)
from hexawyn.domain.models.cilium import CiliumDetectionResult, CiliumStatusResult


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


class TestCiliumDetectServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(CiliumDetectServicePort, ABC)

    def test_subclass_can_be_instantiated(self) -> None:
        port = _FakeCiliumDetectServicePort()
        assert port.detect(command="ping") == "ping"
