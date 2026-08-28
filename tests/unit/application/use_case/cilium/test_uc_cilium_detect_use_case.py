from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cilium.cilium_detect.cilium_detect_use_case import (
    CiliumDetectUseCase,
)
from hexawyn.application.use_case.cilium.cilium_detect.command import CiliumDetectCommand
from hexawyn.application.use_case.cilium.cilium_detect.response import CiliumDetectResponse


class TestCiliumDetectUseCase:
    def test_execute_returns_response(self) -> None:
        detection = MagicMock()
        detection.installed = True
        detection.status = "installed"
        detection.version = "v1.16.3"
        detection.mode = "tunnel"
        detection.namespace = "kube-system"
        detection.total_agents = 2
        detection.ready_agents = 1
        detection.degraded_summary = "1/2 agents ready"

        a1 = MagicMock()
        a1.node = "node-1"
        a1.pod_name = "cilium-a"
        a1.namespace = "kube-system"
        a1.ready = True
        a1.phase = "Running"
        a1.restart_count = 0
        a1.image = "quay.io/cilium/cilium:v1.16.3"
        a1.message = None
        detection.agents = [a1]
        detection.note = None

        port = MagicMock()
        port.detect.return_value = detection

        use_case = CiliumDetectUseCase(port=port)
        result = use_case.execute(CiliumDetectCommand())

        assert isinstance(result, CiliumDetectResponse)
        assert result.installed is True
        assert result.version == "v1.16.3"
        assert result.mode == "tunnel"
        assert result.degraded_summary == "1/2 agents ready"
        assert result.agents == [
            {
                "node": "node-1",
                "pod_name": "cilium-a",
                "namespace": "kube-system",
                "ready": True,
                "phase": "Running",
                "restart_count": 0,
                "image": "quay.io/cilium/cilium:v1.16.3",
                "message": None,
            }
        ]

    def test_execute_not_installed(self) -> None:
        detection = MagicMock()
        detection.installed = False
        detection.status = "not_installed"
        detection.version = None
        detection.mode = "UNKNOWN"
        detection.namespace = None
        detection.total_agents = 0
        detection.ready_agents = 0
        detection.degraded_summary = None
        detection.agents = []
        detection.note = "Cilium is not installed"

        port = MagicMock()
        port.detect.return_value = detection

        use_case = CiliumDetectUseCase(port=port)
        result = use_case.execute(CiliumDetectCommand())

        assert isinstance(result, CiliumDetectResponse)
        assert result.installed is False
        assert result.status == "not_installed"
        assert result.agents == []
