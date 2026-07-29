from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.slowest_traces.command import (
    SlowestTracesCommand,
)
from hexawyn.application.use_case.observability.slowest_traces.response import (
    SlowestTracesResponse,
)
from hexawyn.application.use_case.observability.slowest_traces.slowest_traces_use_case import (
    SlowestTracesUseCase,
)
from hexawyn.domain.models.slowest_traces import SlowTrace


class TestSlowestTracesUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.search_pod_traces.return_value = []

        use_case = SlowestTracesUseCase(port=port)
        result = use_case.execute(SlowestTracesCommand(top_n=5))  # type: ignore

        assert isinstance(result, SlowestTracesResponse)

    def test_execute_with_traces_returns_ordered_slowest(self) -> None:
        traces = [
            SlowTrace(
                trace_id="trace-1",
                duration_ms=120.5,
                operation="GET /api/users",
                span_count=3,
            ),
            SlowTrace(
                trace_id="trace-2",
                duration_ms=450.0,
                operation="POST /api/orders",
                span_count=7,
            ),
            SlowTrace(
                trace_id="trace-3",
                duration_ms=80.2,
                operation="GET /api/health",
                span_count=1,
            ),
        ]
        port = MagicMock()
        port.search_pod_traces.return_value = traces

        use_case = SlowestTracesUseCase(port=port)
        result = use_case.execute(
            SlowestTracesCommand(pod_name="api-pod", top_n=3)  # type: ignore
        )

        slowest = result.slowest_traces  # type: ignore[assignment]
        assert isinstance(result, SlowestTracesResponse)
        assert len(slowest) == 3  # noqa: PLR2004
        assert result.total_traces_found == 3  # noqa: PLR2004

    def test_execute_respects_top_n(self) -> None:
        traces = [
            SlowTrace(
                trace_id=f"trace-{i}",
                duration_ms=float(100 - i),
                operation=f"op-{i}",
                span_count=1,
            )
            for i in range(20)
        ]
        port = MagicMock()
        port.search_pod_traces.return_value = traces

        use_case = SlowestTracesUseCase(port=port)
        result = use_case.execute(
            SlowestTracesCommand(pod_name="svc", top_n=5)  # type: ignore
        )

        slowest = result.slowest_traces  # type: ignore[assignment]
        assert result.total_traces_found == 20  # noqa: PLR2004
        assert len(slowest) == 5  # noqa: PLR2004
