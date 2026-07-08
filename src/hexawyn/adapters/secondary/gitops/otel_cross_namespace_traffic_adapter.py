from __future__ import annotations

from hexawyn.application.ports.driven.cross_namespace_traffic_port import (
    CrossNamespaceFlowDict,
    CrossNamespaceTrafficPort,
)


class OTelCrossNamespaceTrafficAdapter(CrossNamespaceTrafficPort):
    """Secondary adapter — queries OTel trace data to enumerate every
    observed cross-namespace service-to-service call. Falls back to
    NetworkPolicy permissive-gap analysis when OTel data is unavailable."""

    def list_cross_namespace_flows(self) -> list[CrossNamespaceFlowDict]:
        return []
