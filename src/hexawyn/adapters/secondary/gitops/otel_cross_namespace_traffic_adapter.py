from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import list_jaeger_services
from hexawyn.application.ports.driven.cross_namespace_traffic_port import (
    CrossNamespaceFlowDict,
    CrossNamespaceTrafficPort,
)


class OTelCrossNamespaceTrafficAdapter(CrossNamespaceTrafficPort):
    def list_cross_namespace_flows(self) -> list[CrossNamespaceFlowDict]:
        services = list_jaeger_services()
        result: list[CrossNamespaceFlowDict] = []
        for service in services:
            result.append(
                CrossNamespaceFlowDict(  # type: ignore
                    source_namespace="unknown",
                    target_namespace="unknown",
                    source_service=service,
                    target_service="",
                    call_count=0,
                )
            )
        return result
