from __future__ import annotations

from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort
from hexawyn.domain.models.slowest_traces import SlowestTracesRequest, SlowTrace


class OTelPodTraceAdapter(SlowTraceSearchPort):
    def search_pod_traces(self, request: SlowestTracesRequest) -> list[SlowTrace]:
        return []
