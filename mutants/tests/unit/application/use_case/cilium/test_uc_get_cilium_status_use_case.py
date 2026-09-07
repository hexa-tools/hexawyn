from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cilium.get_cilium_status.command import (
    GetCiliumStatusCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_status.get_cilium_status_use_case import (
    GetCiliumStatusUseCase,
)
from hexawyn.application.use_case.cilium.get_cilium_status.response import (
    GetCiliumStatusResponse,
)
from hexawyn.domain.models.cilium import CiliumAgentHealth, CiliumStatusResult


class TestGetCiliumStatusUseCase:
    def test_execute_returns_healthy_response(self) -> None:
        nodes = [
            CiliumAgentHealth(
                node="node-1",
                pod_name="cilium-a",
                namespace="kube-system",
                ready=True,
                phase="Running",
                restart_count=0,
                image="quay.io/cilium/cilium:v1.16.3",
                message=None,
            )
        ]
        status = CiliumStatusResult(
            installed=True,
            status="healthy",
            ready_agents=1,
            total_agents=1,
            degraded_summary=None,
            controller_errors=0,
            connectivity="ok",
            nodes=nodes,
            note=None,
        )
        port = MagicMock()
        port.status.return_value = status

        result = GetCiliumStatusUseCase(port=port).execute(GetCiliumStatusCommand())

        assert isinstance(result, GetCiliumStatusResponse)
        assert result.status == "healthy"
        assert result.connectivity == "ok"
        assert result.nodes == [
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

    def test_execute_returns_degraded_counts(self) -> None:
        nodes = [
            CiliumAgentHealth(
                node="node-1",
                pod_name="cilium-a",
                namespace="kube-system",
                ready=True,
                phase="Running",
                restart_count=0,
            ),
            CiliumAgentHealth(
                node="node-2",
                pod_name="cilium-b",
                namespace="kube-system",
                ready=False,
                phase="Running",
                restart_count=2,
            ),
        ]
        status = CiliumStatusResult(
            installed=True,
            status="degraded",
            ready_agents=1,
            total_agents=2,
            degraded_summary="1/2 agents ready",
            controller_errors=1,
            connectivity="degraded",
            nodes=nodes,
            note=None,
        )
        port = MagicMock()
        port.status.return_value = status

        result = GetCiliumStatusUseCase(port=port).execute(GetCiliumStatusCommand())

        assert result.status == "degraded"
        assert result.degraded_summary == "1/2 agents ready"
        assert result.controller_errors == 1  # noqa: PLR2004
        assert result.connectivity == "degraded"
        assert result.nodes is not None

    def test_execute_not_installed(self) -> None:
        status = CiliumStatusResult(
            installed=False,
            status="not_installed",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=[],
            note="Cilium is not installed in this cluster",
        )
        port = MagicMock()
        port.status.return_value = status

        result = GetCiliumStatusUseCase(port=port).execute(GetCiliumStatusCommand())

        assert result.installed is False
        assert result.status == "not_installed"
        assert result.nodes == []
