from __future__ import annotations

from hexawyn.domain.models.cost_profiling import (
    CostProfilingRequest,
    CostProfilingResult,
    EndpointCPUProfile,
)


class TestEndpointCPUProfile:
    def test_create(self) -> None:
        ep = EndpointCPUProfile(
            endpoint="POST /generate-report",
            avg_cpu_ms_per_request=450.0,
            request_count=200,
            total_cpu_ms=90000.0,
        )
        assert ep.avg_cpu_ms_per_request == 450.0  # noqa: PLR2004
        assert ep.request_count == 200  # noqa: PLR2004

    def test_cost_score_high_combined(self) -> None:
        ep = EndpointCPUProfile(
            endpoint="POST /search",
            avg_cpu_ms_per_request=180.0,
            request_count=1500,
            total_cpu_ms=270000.0,
        )
        assert ep.cost_score == round(180.0 * 1500, 2)


class TestCostProfilingRequest:
    def test_defaults(self) -> None:
        req = CostProfilingRequest(time_window_minutes=60, top_n=5)
        assert req.top_n == 5  # noqa: PLR2004
        assert req.time_window_minutes == 60  # noqa: PLR2004


class TestCostProfilingResult:
    def test_ranking_and_candidates(self) -> None:
        endpoints = [
            EndpointCPUProfile(
                endpoint="POST /generate-report",
                avg_cpu_ms_per_request=450.0,
                request_count=200,
                total_cpu_ms=90000.0,
            ),
            EndpointCPUProfile(
                endpoint="POST /search",
                avg_cpu_ms_per_request=180.0,
                request_count=1500,
                total_cpu_ms=270000.0,
            ),
            EndpointCPUProfile(
                endpoint="GET /status",
                avg_cpu_ms_per_request=2.0,
                request_count=10000,
                total_cpu_ms=20000.0,
            ),
        ]
        result = CostProfilingResult.compute(
            request=CostProfilingRequest(time_window_minutes=60, top_n=5), endpoints=endpoints
        )
        assert result.ranked_endpoints[0].endpoint == "POST /search"
        assert len(result.optimisation_candidates) == 2  # noqa: PLR2004
        assert result.optimisation_candidates[0].endpoint == "POST /search"

    def test_empty_endpoints(self) -> None:
        result = CostProfilingResult.compute(
            request=CostProfilingRequest(time_window_minutes=60, top_n=5),
            endpoints=[],
        )
        assert result.ranked_endpoints == []
        assert result.optimisation_candidates == []

    def test_excludes_endpoints_with_no_cpu(self) -> None:
        endpoints = [
            EndpointCPUProfile(
                endpoint="GET /no-cpu",
                avg_cpu_ms_per_request=0.0,
                request_count=100,
                total_cpu_ms=0.0,
            ),
            EndpointCPUProfile(
                endpoint="POST /has-cpu",
                avg_cpu_ms_per_request=50.0,
                request_count=100,
                total_cpu_ms=5000.0,
            ),
        ]
        result = CostProfilingResult.compute(
            request=CostProfilingRequest(time_window_minutes=60, top_n=5),
            endpoints=endpoints,
        )
        assert len(result.ranked_endpoints) == 1
        assert result.ranked_endpoints[0].endpoint == "POST /has-cpu"
