"""CiliumHubbleAdapter — queries Cilium flow logs via a Hubble Relay HTTP client."""

from __future__ import annotations

from hexawyn.adapters.secondary.cilium.hubble_client import (
    fetch_hubble_flows,
    hubble_available,
)
from hexawyn.application.ports.driven.cilium_hubble_port import CiliumHubblePort
from hexawyn.domain.errors import AdapterTimeoutError, ClusterUnreachableError
from hexawyn.domain.models.cilium import CiliumFlowQuery, CiliumFlowsResult
from hexawyn.domain.services.cilium.flow_builder import (
    build_flows,
    not_installed_flows_result,
)


class CiliumHubbleAdapter(CiliumHubblePort):
    """Real Hubble adapter using the HTTP flow client."""

    def get_flows(self, query: CiliumFlowQuery) -> CiliumFlowsResult:
        if not hubble_available():
            return not_installed_flows_result()
        try:
            raw = fetch_hubble_flows(
                namespace=query.namespace,
                pod=query.pod,
                direction=query.direction,
                verdict=query.verdict,
                window_minutes=query.window_minutes,
                limit=query.limit,
            )
        except TimeoutError as exc:
            raise AdapterTimeoutError(f"Hubble request timed out: {exc}") from exc
        except Exception as exc:
            raise ClusterUnreachableError(f"Hubble Relay is unreachable: {exc}") from exc
        return build_flows(raw, query)
