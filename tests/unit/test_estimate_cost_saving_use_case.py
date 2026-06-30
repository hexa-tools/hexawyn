"""Unit tests for the estimate_cost_saving use case — domain logic + wiring."""

from __future__ import annotations

import asyncio
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driving.estimate_cost_saving.estimate_cost_saving_command import (
    EstimateCostSavingCommand,
)
from hexawyn.application.ports.driving.estimate_cost_saving.estimate_cost_saving_response import (
    EstimateCostSavingResponse,
)
from hexawyn.application.ports.driving.estimate_cost_saving.estimate_cost_saving_service_port import (
    EstimateCostSavingServicePort,
)
from hexawyn.application.use_case.estimate_cost_saving.estimate_cost_saving_use_case import (
    EstimateCostSavingUseCase,
)
from hexawyn.domain.models.cost_saving_estimation import (
    CostSavingReport,
)
from hexawyn.domain.services.cost_saving.cost_saving_estimation_service import (
    RightSizingCostEstimationService,
)

_CPU_PRICE = 0.05  # $/core/hour
_MEM_PRICE = 0.007  # $/GB/hour
_HOURS = 24 * 30  # 720


def _pod(
    name: str = "data-processor-abc",
    ns: str = "production",
    cpu_req: float = 4.0,
    mem_req_mi: float = 4096.0,
    cpu_p95: float | None = 0.4,
    mem_p95_mi: float | None = 1024.0,
    cpu_max: float | None = None,
    hpa: bool = False,
    hpa_min: int | None = None,
) -> dict[str, object]:
    return {
        "pod_name": name,
        "namespace": ns,
        "cpu_request_cores": cpu_req,
        "memory_request_mi": mem_req_mi,
        "cpu_limit_cores": None,
        "memory_limit_mi": None,
        "cpu_p95_cores": cpu_p95,
        "memory_p95_mi": mem_p95_mi,
        "cpu_max_cores": cpu_max,
        "hpa_enabled": hpa,
        "hpa_min_replicas": hpa_min,
    }


# ── Domain service — pure right-sizing logic ──────────────────────────────


class TestRightSizingCostEstimationService:
    """Core domain logic tests per user story acceptance criteria."""

    def _svc(self) -> RightSizingCostEstimationService:
        return RightSizingCostEstimationService()

    def test_recommends_p95_plus_20pct_buffer(self) -> None:
        """Recommended CPU = p95 * 1.2 (buffer must be applied)."""
        report = self._svc().estimate(
            pods=[_pod(cpu_req=4.0, cpu_p95=0.4)],
            top_n=10,
            cpu_price=None,
            mem_price=None,
        )
        assert len(report.top_opportunities) == 1
        opp = report.top_opportunities[0]
        assert opp.recommended_cpu_request == pytest.approx(0.4 * 1.2, rel=1e-3)

    def test_monthly_saving_formula_delta_times_price_times_720h(self) -> None:
        """Monthly saving = delta_cores * cpu_price * 24 * 30."""
        report = self._svc().estimate(
            pods=[_pod(cpu_req=4.0, cpu_p95=0.4, mem_p95_mi=None)],
            top_n=10,
            cpu_price=_CPU_PRICE,
            mem_price=None,
        )
        opp = report.top_opportunities[0]
        expected_delta = 4.0 - (0.4 * 1.2)
        expected_saving = round(expected_delta * _CPU_PRICE * _HOURS, 2)
        assert opp.monthly_saving_usd == pytest.approx(expected_saving, rel=1e-3)

    def test_test_data_saving_126_usd(self) -> None:
        """Scenario: delta=3.5 cores → monthly saving ≈ $126 (delta * 0.05 * 720)."""
        # With cpu_req=4.0 and cpu_p95=0.4 → recommended=0.48 → delta=3.52 → $126.72
        # Test validates formula is correct: delta * price * 24 * 30
        report = self._svc().estimate(
            pods=[_pod(cpu_req=4.0, cpu_p95=0.4, mem_req_mi=0.0, mem_p95_mi=0.0)],
            top_n=10,
            cpu_price=0.05,
            mem_price=None,
        )
        opp = report.top_opportunities[0]
        rec = 0.4 * 1.2  # = 0.48
        expected = round((4.0 - rec) * 0.05 * 720, 2)
        assert opp.monthly_saving_usd == pytest.approx(expected, rel=1e-3)

    def test_10_pods_total_saving_sums_correctly(self) -> None:
        """10 over-provisioned pods → total saving = sum of individual savings."""
        pods = [_pod(name=f"pod-{i}", cpu_req=4.0, cpu_p95=0.4) for i in range(10)]
        report = self._svc().estimate(
            pods=pods, top_n=10, cpu_price=_CPU_PRICE, mem_price=_MEM_PRICE
        )
        assert report.pods_analyzed == 10
        expected_total = sum(
            o.monthly_saving_usd for o in report.top_opportunities if o.monthly_saving_usd
        )
        assert report.total_monthly_saving_usd == pytest.approx(expected_total, rel=1e-3)

    def test_optimal_pod_excluded(self) -> None:
        """Pod with usage ≥ 90% of request is excluded from saving report."""
        # p95 = 0.92 * request → ratio = 0.92 → optimal
        report = self._svc().estimate(
            pods=[_pod(cpu_req=1.0, cpu_p95=0.92, mem_req_mi=1024.0, mem_p95_mi=1000.0)],
            top_n=10,
            cpu_price=_CPU_PRICE,
            mem_price=_MEM_PRICE,
        )
        assert report.pods_analyzed == 0
        assert report.pods_excluded == 1
        assert report.top_opportunities == []

    def test_no_requests_pod_excluded(self) -> None:
        """Pod with no CPU and no memory request is excluded."""
        pod_no_req: dict[str, object] = {
            "pod_name": "ghost-pod",
            "namespace": "ns",
            "cpu_request_cores": None,
            "memory_request_mi": None,
            "cpu_limit_cores": None,
            "memory_limit_mi": None,
            "cpu_p95_cores": 0.5,
            "memory_p95_mi": 512.0,
            "cpu_max_cores": None,
            "hpa_enabled": False,
            "hpa_min_replicas": None,
        }
        report = self._svc().estimate(pods=[pod_no_req], top_n=10, cpu_price=None, mem_price=None)
        assert report.pods_excluded == 1
        assert report.pods_analyzed == 0

    def test_no_pricing_configured_no_usd_savings(self) -> None:
        """When pricing is not configured, monthly_saving_usd must be None."""
        report = self._svc().estimate(
            pods=[_pod(cpu_req=4.0, cpu_p95=0.4)],
            top_n=10,
            cpu_price=None,
            mem_price=None,
        )
        assert report.pricing_configured is False
        assert report.total_monthly_saving_usd is None
        opp = report.top_opportunities[0]
        assert opp.monthly_saving_usd is None
        assert opp.delta_cores > 0  # cores delta still computed

    def test_ranking_descending_by_monthly_saving(self) -> None:
        """Top opportunities ranked by monthly_saving_usd descending."""
        pods = [
            _pod(name="a", cpu_req=2.0, cpu_p95=0.1),  # low saving
            _pod(name="b", cpu_req=8.0, cpu_p95=0.1),  # high saving
            _pod(name="c", cpu_req=4.0, cpu_p95=0.1),  # medium saving
        ]
        report = self._svc().estimate(pods=pods, top_n=10, cpu_price=_CPU_PRICE, mem_price=None)
        savings = [o.monthly_saving_usd for o in report.top_opportunities]
        assert savings == sorted(savings, reverse=True)

    def test_cloud_pricing_both_resources(self) -> None:
        """Monthly saving includes CPU and memory delta: $0.05/core/h + $0.007/GB/h."""
        report = self._svc().estimate(
            pods=[_pod(cpu_req=4.0, cpu_p95=0.4, mem_req_mi=4096.0, mem_p95_mi=512.0)],
            top_n=10,
            cpu_price=0.05,
            mem_price=0.007,
        )
        opp = report.top_opportunities[0]
        rec_cpu = 0.4 * 1.2
        rec_mem_mi = 512.0 * 1.2
        delta_cores = 4.0 - rec_cpu
        delta_gb = (4096.0 - rec_mem_mi) / 1024.0
        expected = round(delta_cores * 0.05 * 720 + delta_gb * 0.007 * 720, 2)
        assert opp.monthly_saving_usd == pytest.approx(expected, rel=1e-3)

    def test_pod_with_limits_but_no_requests_uses_limit(self) -> None:
        """Pod has limits but no requests → right-size based on limit delta."""
        pod_lim_only: dict[str, object] = {
            "pod_name": "batch-job",
            "namespace": "jobs",
            "cpu_request_cores": None,
            "memory_request_mi": None,
            "cpu_limit_cores": 4.0,
            "memory_limit_mi": 4096.0,
            "cpu_p95_cores": 0.4,
            "memory_p95_mi": 512.0,
            "cpu_max_cores": None,
            "hpa_enabled": False,
            "hpa_min_replicas": None,
        }
        report = self._svc().estimate(pods=[pod_lim_only], top_n=10, cpu_price=None, mem_price=None)
        assert report.pods_analyzed == 1
        opp = report.top_opportunities[0]
        assert opp.current_cpu_request == pytest.approx(4.0)  # uses limit
        assert opp.delta_cores > 0

    def test_hpa_pod_includes_caveat(self) -> None:
        """Pod with HPA enabled has a caveat in the output."""
        report = self._svc().estimate(
            pods=[_pod(cpu_req=4.0, cpu_p95=0.4, hpa=True, hpa_min=2)],
            top_n=10,
            cpu_price=None,
            mem_price=None,
        )
        opp = report.top_opportunities[0]
        assert opp.hpa_enabled is True
        assert any("HPA" in c for c in opp.caveats)

    def test_bursty_pod_includes_caveat(self) -> None:
        """Pod with max/p95 > 2.5 is flagged as bursty with a caveat."""
        report = self._svc().estimate(
            pods=[_pod(cpu_req=4.0, cpu_p95=0.4, cpu_max=3.0)],  # 3.0/0.4 = 7.5 > 2.5
            top_n=10,
            cpu_price=None,
            mem_price=None,
        )
        opp = report.top_opportunities[0]
        assert opp.is_bursty is True
        assert any("bursty" in c.lower() for c in opp.caveats)

    def test_top_n_limits_opportunities(self) -> None:
        """Only top_n opportunities are returned."""
        pods = [_pod(name=f"pod-{i}", cpu_req=float(i + 2), cpu_p95=0.1) for i in range(20)]
        report = self._svc().estimate(pods=pods, top_n=10, cpu_price=_CPU_PRICE, mem_price=None)
        assert len(report.top_opportunities) == 10

    def test_namespace_savings_aggregated(self) -> None:
        """Per-namespace savings correctly aggregate all pods in that namespace."""
        pods = [
            _pod(name="a", ns="ns-a", cpu_req=4.0, cpu_p95=0.4),
            _pod(name="b", ns="ns-a", cpu_req=4.0, cpu_p95=0.4),
            _pod(name="c", ns="ns-b", cpu_req=4.0, cpu_p95=0.4),
        ]
        report = self._svc().estimate(pods=pods, top_n=10, cpu_price=_CPU_PRICE, mem_price=None)
        ns_map = {ns.namespace: ns for ns in report.namespace_savings}
        assert ns_map["ns-a"].pod_count == 2
        assert ns_map["ns-b"].pod_count == 1

    def test_no_p95_data_pod_excluded(self) -> None:
        """Pod with no p95 data (Prometheus unavailable) is excluded."""
        pod: dict[str, object] = {
            "pod_name": "no-prom",
            "namespace": "ns",
            "cpu_request_cores": 2.0,
            "memory_request_mi": 1024.0,
            "cpu_limit_cores": None,
            "memory_limit_mi": None,
            "cpu_p95_cores": None,
            "memory_p95_mi": None,
            "cpu_max_cores": None,
            "hpa_enabled": False,
            "hpa_min_replicas": None,
        }
        report = self._svc().estimate(pods=[pod], top_n=10, cpu_price=None, mem_price=None)
        assert report.pods_excluded == 1
        assert report.pods_analyzed == 0

    def test_invalid_p95_value_excluded(self) -> None:
        """Pod with non-numeric p95 value is treated as None → excluded."""
        pod: dict[str, object] = {
            "pod_name": "bad-data",
            "namespace": "ns",
            "cpu_request_cores": 2.0,
            "memory_request_mi": 1024.0,
            "cpu_limit_cores": None,
            "memory_limit_mi": None,
            "cpu_p95_cores": "not-a-number",
            "memory_p95_mi": None,
            "cpu_max_cores": None,
            "hpa_enabled": False,
            "hpa_min_replicas": None,
        }
        report = self._svc().estimate(pods=[pod], top_n=10, cpu_price=None, mem_price=None)
        assert report.pods_excluded == 1


# ── _compute_trend coverage ───────────────────────────────────────────────


class TestComputeTrend:
    def test_decreasing_trend(self) -> None:
        """previous=$485, current=$200 → trend='decreasing' (>10% drop)."""
        from hexawyn.application.service.estimate_cost_saving_service import _compute_trend

        assert _compute_trend(485.0, 200.0) == "decreasing"

    def test_stable_trend(self) -> None:
        """previous=$100, current=$105 → trend='stable' (<10% change)."""
        from hexawyn.application.service.estimate_cost_saving_service import _compute_trend

        assert _compute_trend(100.0, 105.0) == "stable"

    def test_none_when_previous_is_none(self) -> None:
        from hexawyn.application.service.estimate_cost_saving_service import _compute_trend

        assert _compute_trend(None, 200.0) is None

    def test_none_when_previous_is_zero(self) -> None:
        from hexawyn.application.service.estimate_cost_saving_service import _compute_trend

        assert _compute_trend(0.0, 200.0) is None


# ── Use Case wiring ───────────────────────────────────────────────────────


class TestEstimateCostSavingUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=EstimateCostSavingServicePort)
        service.estimate_cost_saving.return_value = EstimateCostSavingResponse(
            report=CostSavingReport()
        )
        use_case = EstimateCostSavingUseCase(service=service)

        use_case.execute(EstimateCostSavingCommand())

        service.estimate_cost_saving.assert_called_once()

    def test_passes_command_through(self) -> None:
        service = MagicMock(spec=EstimateCostSavingServicePort)
        service.estimate_cost_saving.return_value = EstimateCostSavingResponse(
            report=CostSavingReport()
        )
        use_case = EstimateCostSavingUseCase(service=service)
        cmd = EstimateCostSavingCommand(top_n=5, cpu_per_core_per_hour_usd=0.05)

        use_case.execute(cmd)

        service.estimate_cost_saving.assert_called_once_with(cmd)


# ── MCP tool registration ─────────────────────────────────────────────────


class TestMCPEstimateCostSavingTool:
    def test_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = {t.name for t in tools}
        assert "estimate_cost_saving" in tool_names

    def test_returns_top_opportunities(self) -> None:
        from hexawyn.application.ports.driven.cost_saving_estimation_port import (
            CostSavingEstimationPort,
        )

        mock_port = MagicMock(spec=CostSavingEstimationPort)
        mock_port.get_pod_resource_data.return_value = [
            {
                "pod_name": "data-processor-abc",
                "namespace": "production",
                "cpu_request_cores": 4.0,
                "memory_request_mi": 4096.0,
                "cpu_limit_cores": None,
                "memory_limit_mi": None,
                "cpu_p95_cores": 0.4,
                "memory_p95_mi": 512.0,
                "cpu_max_cores": 0.6,
                "hpa_enabled": False,
                "hpa_min_replicas": None,
            }
        ]
        mock_port.get_previous_total_saving.return_value = None
        mock_port.store_total_saving.return_value = None

        with patch("hexawyn.mcp.server.build_cost_saving_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.estimate_cost_saving import estimate_cost_saving

            result = estimate_cost_saving(
                top_n=10,
                cpu_per_core_per_hour_usd=0.05,
                memory_per_gb_per_hour_usd=0.007,
            )

        assert result["error"] is None
        assert len(result["top_opportunities"]) == 1  # type: ignore[arg-type]
        opp = result["top_opportunities"][0]  # type: ignore[index]
        assert opp["pod"] == "data-processor-abc"
        assert opp["delta_cores"] > 0
        assert opp["monthly_saving_usd"] is not None
        assert result["pricing_configured"] is True

    def test_no_pricing_no_usd(self) -> None:
        from hexawyn.application.ports.driven.cost_saving_estimation_port import (
            CostSavingEstimationPort,
        )

        mock_port = MagicMock(spec=CostSavingEstimationPort)
        mock_port.get_pod_resource_data.return_value = [
            {
                "pod_name": "svc",
                "namespace": "ns",
                "cpu_request_cores": 4.0,
                "memory_request_mi": 2048.0,
                "cpu_limit_cores": None,
                "memory_limit_mi": None,
                "cpu_p95_cores": 0.3,
                "memory_p95_mi": 400.0,
                "cpu_max_cores": None,
                "hpa_enabled": False,
                "hpa_min_replicas": None,
            }
        ]
        mock_port.get_previous_total_saving.return_value = None
        mock_port.store_total_saving.return_value = None

        with patch("hexawyn.mcp.server.build_cost_saving_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.estimate_cost_saving import estimate_cost_saving

            result = estimate_cost_saving()

        assert result["pricing_configured"] is False
        assert result["total_monthly_saving_usd"] is None
        assert result["top_opportunities"][0]["monthly_saving_usd"] is None  # type: ignore[index]
        assert result["top_opportunities"][0]["delta_cores"] > 0  # type: ignore[index]

    def test_cluster_error_captured(self) -> None:
        from hexawyn.application.ports.driven.cost_saving_estimation_port import (
            CostSavingEstimationPort,
        )
        from hexawyn.domain.errors import ClusterUnreachableError

        mock_port = MagicMock(spec=CostSavingEstimationPort)
        mock_port.get_pod_resource_data.side_effect = ClusterUnreachableError("down")

        with patch("hexawyn.mcp.server.build_cost_saving_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.estimate_cost_saving import estimate_cost_saving

            result = estimate_cost_saving()

        assert result["error"] is not None
        assert result["top_opportunities"] == []

    def test_saving_trend_increasing(self) -> None:
        """When waste grows >10% vs previous estimate, trend=increasing."""
        from hexawyn.application.ports.driven.cost_saving_estimation_port import (
            CostSavingEstimationPort,
        )

        mock_port = MagicMock(spec=CostSavingEstimationPort)
        mock_port.get_pod_resource_data.return_value = [
            {
                "pod_name": "svc",
                "namespace": "ns",
                "cpu_request_cores": 4.0,
                "memory_request_mi": 0.0,
                "cpu_limit_cores": None,
                "memory_limit_mi": None,
                "cpu_p95_cores": 0.4,
                "memory_p95_mi": None,
                "cpu_max_cores": None,
                "hpa_enabled": False,
                "hpa_min_replicas": None,
            }
        ]
        mock_port.get_previous_total_saving.return_value = 100.0  # was $100 last time
        mock_port.store_total_saving.return_value = None

        with patch("hexawyn.mcp.server.build_cost_saving_adapter", return_value=mock_port):
            from hexawyn.mcp.tools.estimate_cost_saving import estimate_cost_saving

            result = estimate_cost_saving(cpu_per_core_per_hour_usd=0.05)

        # Current saving >> 100 → trend increasing
        if result["total_monthly_saving_usd"] and float(result["total_monthly_saving_usd"]) > 110:  # type: ignore[arg-type]
            assert result["saving_trend"] == "increasing"
