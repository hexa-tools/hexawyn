from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cilium.get_cilium_flows.command import (
    GetCiliumFlowsCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_flows.get_cilium_flows_use_case import (
    GetCiliumFlowsUseCase,
)
from hexawyn.application.use_case.cilium.get_cilium_flows.response import (
    GetCiliumFlowsResponse,
)
from hexawyn.domain.models.cilium import CiliumFlowEntry, CiliumFlowsResult


class TestGetCiliumFlowsUseCase:
    def test_execute_returns_flows(self) -> None:
        result = CiliumFlowsResult(
            installed=True,
            status="present",
            total_flows=1,
            flows=[
                CiliumFlowEntry(
                    timestamp="2026-08-28T10:00:00Z",
                    source="web-0",
                    destination="db-0",
                    source_namespace="payments",
                    destination_namespace="payments",
                    source_identity="100",
                    destination_identity="200",
                    verdict="FORWARDED",
                    drop_reason=None,
                    protocol="tcp",
                    destination_port="443",
                    l7_protocol="http",
                    direction="ingress",
                )
            ],
            note=None,
        )
        port = MagicMock()
        port.get_flows.return_value = result

        response = GetCiliumFlowsUseCase(port=port).execute(
            GetCiliumFlowsCommand(namespace="payments")
        )

        assert isinstance(response, GetCiliumFlowsResponse)
        assert response.status == "present"
        assert response.flows == [
            {
                "timestamp": "2026-08-28T10:00:00Z",
                "source": "web-0",
                "destination": "db-0",
                "source_namespace": "payments",
                "destination_namespace": "payments",
                "source_identity": "100",
                "destination_identity": "200",
                "verdict": "FORWARDED",
                "drop_reason": None,
                "protocol": "tcp",
                "destination_port": "443",
                "l7_protocol": "http",
                "direction": "ingress",
            }
        ]

    def test_execute_not_installed(self) -> None:
        result = CiliumFlowsResult(
            installed=False,
            status="not_installed",
            total_flows=0,
            flows=[],
            note="Hubble relay is not available in this cluster",
        )
        port = MagicMock()
        port.get_flows.return_value = result

        response = GetCiliumFlowsUseCase(port=port).execute(GetCiliumFlowsCommand())

        assert response.installed is False
        assert response.status == "not_installed"
        assert response.flows == []
