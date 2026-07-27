from __future__ import annotations

from hexawyn.domain.models.cost_saving_estimation import (
    CostSavingReport,
    NamespaceSaving,
    PodSavingOpportunity,
)


class TestPodSavingOpportunity:
    def test_create(self) -> None:
        p = PodSavingOpportunity(
            pod_name="app-abc",
            namespace="default",
            current_cpu_request=2.0,
            recommended_cpu_request=1.0,
            current_memory_request_mi=512.0,
            recommended_memory_request_mi=256.0,
            delta_cores=1.0,
            delta_memory_mi=256.0,
            monthly_saving_usd=12.50,
            hpa_enabled=False,
            is_bursty=False,
            caveats=["estimated"],
        )
        assert p.pod_name == "app-abc"
        assert p.delta_cores == 1.0
        assert p.monthly_saving_usd == 12.50  # noqa: PLR2004
        assert not p.hpa_enabled

    def test_no_pricing(self) -> None:
        p = PodSavingOpportunity(
            pod_name="p",
            namespace="ns",
            current_cpu_request=None,
            recommended_cpu_request=None,
            current_memory_request_mi=None,
            recommended_memory_request_mi=None,
            delta_cores=0.0,
            delta_memory_mi=0.0,
            monthly_saving_usd=None,
            hpa_enabled=True,
            is_bursty=True,
            caveats=[],
        )
        assert p.monthly_saving_usd is None
        assert p.is_bursty


class TestNamespaceSaving:
    def test_create(self) -> None:
        ns = NamespaceSaving(
            namespace="team-a",
            pod_count=5,
            total_delta_cores=3.0,
            total_delta_memory_mi=1024.0,
            total_monthly_saving_usd=37.50,
        )
        assert ns.namespace == "team-a"
        assert ns.pod_count == 5  # noqa: PLR2004
        assert ns.total_monthly_saving_usd == 37.50  # noqa: PLR2004

    def test_no_pricing(self) -> None:
        ns = NamespaceSaving(
            namespace="ns",
            pod_count=1,
            total_delta_cores=0.0,
            total_delta_memory_mi=0.0,
            total_monthly_saving_usd=None,
        )
        assert ns.total_monthly_saving_usd is None


class TestCostSavingReport:
    def test_defaults(self) -> None:
        r = CostSavingReport()
        assert r.top_opportunities == []
        assert r.namespace_savings == []
        assert r.total_monthly_saving_usd is None
        assert r.total_delta_cores == 0.0
        assert r.pods_analyzed == 0
        assert not r.pricing_configured

    def test_with_data(self) -> None:
        pod = PodSavingOpportunity(
            pod_name="p",
            namespace="ns",
            current_cpu_request=1.0,
            recommended_cpu_request=0.5,
            current_memory_request_mi=256.0,
            recommended_memory_request_mi=128.0,
            delta_cores=0.5,
            delta_memory_mi=128.0,
            monthly_saving_usd=5.0,
            hpa_enabled=False,
            is_bursty=False,
            caveats=[],
        )
        ns = NamespaceSaving(
            namespace="ns",
            pod_count=1,
            total_delta_cores=0.5,
            total_delta_memory_mi=128.0,
            total_monthly_saving_usd=5.0,
        )
        r = CostSavingReport(
            top_opportunities=[pod],
            namespace_savings=[ns],
            total_monthly_saving_usd=5.0,
            total_delta_cores=0.5,
            total_delta_memory_mi=128.0,
            pods_analyzed=1,
            pricing_configured=True,
        )
        assert r.pods_analyzed == 1
        assert r.pricing_configured
        assert len(r.top_opportunities) == 1
