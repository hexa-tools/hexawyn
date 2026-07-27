from __future__ import annotations

from hexawyn.domain.models.cluster_diff import ClusterDiffReport, PromotionChecklist, ResourceDiff
from hexawyn.domain.models.cost_forecast import BillingEvent, CostForecast, ResourceCost
from hexawyn.domain.models.mcp_tool import MCPToolRegistry, MCPToolSchema
from hexawyn.domain.models.security_audit import SecurityAudit
from hexawyn.domain.models.zombie_detection import ZombieCandidate, ZombieDetectionResult


class TestCostForecast:
    def test_resource_cost(self) -> None:
        rc = ResourceCost(name="ec2", kind="compute", monthly_cost_usd=500.0, percentage=50.0)
        assert rc.kind == "compute"
        assert rc.monthly_cost_usd == 500.0  # noqa: PLR2004

    def test_billing_event(self) -> None:
        be = BillingEvent(
            date="2026-07",
            description="Reserved instance purchase",
            cost_impact_usd=-200.0,
            provider="AWS",
        )
        assert be.provider == "AWS"

    def test_forecast(self) -> None:
        f = CostForecast(
            cluster_name="prod",
            month="2026-07",
            days_elapsed=15,
            days_remaining=16,
            current_spend_usd=500.0,
            projected_total_usd=1000.0,
            previous_month_usd=800.0,
            month_over_month_delta=200.0,
            trend_factor=1.2,
            top_cost_drivers=[],
            billing_events=[],
            forecast_confidence="medium",
            historical_days_used=30,
            data_source="prometheus",
        )
        assert f.cluster_name == "prod"
        assert f.forecast_confidence == "medium"


class TestClusterDiff:
    def test_resource_diff(self) -> None:
        rd = ResourceDiff(
            resource="deploy-1",
            namespace="ns",
            reason="missing",
            priority="HIGH",
            staging_value="v2",
            prod_value="v1",
            detail="not promoted",
        )
        assert rd.resource == "deploy-1"
        assert rd.priority == "HIGH"

    def test_checklist(self) -> None:
        pc = PromotionChecklist(ready_to_promote=True, requires_review=False)
        assert pc.ready_to_promote is True

    def test_report(self) -> None:
        r = ClusterDiffReport(
            source_cluster="stage",
            target_cluster="prod",
            in_staging_not_prod=[],
            version_mismatches=[],
            prod_only=[],
            promotion_checklist=PromotionChecklist(True, False),
            sync_status="behind",
            total_differences=5,
            has_data=True,
            warning=None,
        )
        assert r.source_cluster == "stage"
        assert r.sync_status == "behind"


class TestSecurityAudit:
    def test(self) -> None:
        sa = SecurityAudit(cluster_name="prod", severity="HIGH", findings=[])
        assert sa.cluster_name == "prod"
        assert sa.severity == "HIGH"


class TestMCPTool:
    def test_schema(self) -> None:
        s = MCPToolSchema(name="list_pods", description="List pods", input_schema={})
        assert s.name == "list_pods"

    def test_registry(self) -> None:
        r = MCPToolRegistry(tools=[])
        assert r.tools == []


class TestZombieDetection:
    def test_candidate(self) -> None:
        zc = ZombieCandidate(
            pod_name="pod-1",
            namespace="ns",
            age_days=10,
            traffic_rps=0.0,
            cpu_cores=0.5,
            memory_gb=1.0,
            risk="safe_to_remove",
            reason="zero traffic",
        )
        assert zc.pod_name == "pod-1"
        assert zc.risk == "safe_to_remove"

    def test_result(self) -> None:
        r = ZombieDetectionResult(
            analysis_window_hours=24,
            zombie_candidates=[],
            total_wasted_cores=0.0,
            total_wasted_gb=0.0,
            prometheus_available=True,
            data_source="prometheus",
        )
        assert r.analysis_window_hours == 24  # noqa: PLR2004
        assert r.prometheus_available is True
