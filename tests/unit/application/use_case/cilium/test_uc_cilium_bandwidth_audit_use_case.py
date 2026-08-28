from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.cilium_bandwidth_audit_use_case import (  # noqa: E501
    CiliumBandwidthAuditUseCase,
)
from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.command import (
    CiliumBandwidthAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_bandwidth_audit.response import (
    CiliumBandwidthAuditResponse,
)
from hexawyn.domain.models.cilium import CiliumBandwidthAuditResult, CiliumBandwidthEntry


class TestCiliumBandwidthAuditUseCase:
    def test_execute_returns_entries(self) -> None:
        result = CiliumBandwidthAuditResult(
            installed=True,
            status="anomalies",
            total_pods=1,
            entries=[
                CiliumBandwidthEntry(
                    namespace="payments",
                    pod="db-0",
                    ingress_limit="10M",
                    egress_limit="20M",
                    usage_ratio=0.95,
                    state="near_limit",
                    note="Pod at 95% of its bandwidth limit",
                )
            ],
            note=None,
        )
        port = MagicMock()
        port.bandwidth_audit.return_value = result

        response = CiliumBandwidthAuditUseCase(port=port).execute(CiliumBandwidthAuditCommand())

        assert isinstance(response, CiliumBandwidthAuditResponse)
        assert response.status == "anomalies"
        assert response.entries == [
            {
                "namespace": "payments",
                "pod": "db-0",
                "ingress_limit": "10M",
                "egress_limit": "20M",
                "usage_ratio": 0.95,
                "state": "near_limit",
                "note": "Pod at 95% of its bandwidth limit",
            }
        ]

    def test_execute_not_available(self) -> None:
        result = CiliumBandwidthAuditResult(
            installed=True,
            status="not_available",
            total_pods=0,
            entries=[],
            note="Cilium bandwidth manager is disabled (no bandwidth annotations found)",
        )
        port = MagicMock()
        port.bandwidth_audit.return_value = result

        response = CiliumBandwidthAuditUseCase(port=port).execute(CiliumBandwidthAuditCommand())

        assert response.status == "not_available"
        assert response.entries == []
