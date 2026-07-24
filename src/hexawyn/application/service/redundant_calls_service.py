from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.redundant_call_detection_port import (
    RedundantCallDetectionPort,
)
from hexawyn.application.use_case.redundant_calls.command import (
    RedundantCallsCommand,
)
from hexawyn.application.use_case.redundant_calls.response import (
    RedundantCallsResponse,
)
from hexawyn.application.ports.driving.redundant_calls.redundant_calls_service_port import (
    RedundantCallsServicePort,
)
from hexawyn.domain.models.redundant_calls import RedundantCallRequest, RedundantCallResult


class RedundantCallsService(RedundantCallsServicePort):
    def __init__(self, port: RedundantCallDetectionPort) -> None:
        self._port = port

    def detect(self, command: RedundantCallsCommand) -> RedundantCallsResponse:
        req = RedundantCallRequest(flow=command.flow, trace_id=command.trace_id)
        spans = self._port.fetch_spans(req)
        r = RedundantCallResult.compute(request=req, spans=spans)
        return RedundantCallsResponse(
            flow=r.flow,
            patterns=[asdict(p) for p in r.patterns],
            total_redundant_calls=r.total_redundant_calls,
            calculated_waste_ms=r.calculated_waste_ms,
        )
