"""Unit tests for classify_risk_level — reconciles the ticket's own Test
Data literally: postgres-svc (LoadBalancer, production, critical port) ->
critical; redis-svc (NodePort, staging, critical/cache port) -> high.

NodePort exposure and non-production-namespace-for-LoadBalancer are
modeled as *alternative* single downgrades, not stacked — stacking both
would overshoot redis-svc to "medium," contradicting the ticket's own
literal Test Data. loadBalancerSourceRanges is a separate, independently
stacking downgrade (Edge Case 1 / Checker case 5)."""

from __future__ import annotations

_PRODUCTION = "production"


class TestClassifyRiskLevel:
    def test_tc1_postgres_loadbalancer_production_stays_critical(self) -> None:
        from hexawyn.domain.services.external_exposure.risk_scorer import classify_risk_level

        result = classify_risk_level(
            base_severity="critical",
            service_type="LoadBalancer",
            namespace="production",
            production_namespace=_PRODUCTION,
            has_source_ranges=False,
        )

        assert result == "critical"

    def test_tc3_redis_nodeport_staging_is_high_not_critical_or_medium(self) -> None:
        """Reproduces the ticket's own Test Data row exactly: NodePort
        downgrades one tier regardless of namespace."""
        from hexawyn.domain.services.external_exposure.risk_scorer import classify_risk_level

        result = classify_risk_level(
            base_severity="critical",
            service_type="NodePort",
            namespace="staging",
            production_namespace=_PRODUCTION,
            has_source_ranges=False,
        )

        assert result == "high"

    def test_nodeport_in_production_is_still_downgraded(self) -> None:
        """The NodePort downgrade applies regardless of namespace — it's an
        alternative to the namespace downgrade, not conditional on it."""
        from hexawyn.domain.services.external_exposure.risk_scorer import classify_risk_level

        result = classify_risk_level(
            base_severity="critical",
            service_type="NodePort",
            namespace="production",
            production_namespace=_PRODUCTION,
            has_source_ranges=False,
        )

        assert result == "high"

    def test_edge_case_4_loadbalancer_in_dev_is_downgraded(self) -> None:
        """Edge Case 4: dev namespace = lower risk than production."""
        from hexawyn.domain.services.external_exposure.risk_scorer import classify_risk_level

        result = classify_risk_level(
            base_severity="critical",
            service_type="LoadBalancer",
            namespace="dev",
            production_namespace=_PRODUCTION,
            has_source_ranges=False,
        )

        assert result == "high"

    def test_edge_case_1_source_ranges_downgrades_one_more_tier(self) -> None:
        """Edge Case 1 / Checker case 5: loadBalancerSourceRanges reduces
        risk, and must never be silently ignored."""
        from hexawyn.domain.services.external_exposure.risk_scorer import classify_risk_level

        result = classify_risk_level(
            base_severity="critical",
            service_type="LoadBalancer",
            namespace="production",
            production_namespace=_PRODUCTION,
            has_source_ranges=True,
        )

        assert result == "high"

    def test_downgrade_never_goes_below_low(self) -> None:
        from hexawyn.domain.services.external_exposure.risk_scorer import classify_risk_level

        result = classify_risk_level(
            base_severity="low",
            service_type="NodePort",
            namespace="dev",
            production_namespace=_PRODUCTION,
            has_source_ranges=True,
        )

        assert result == "low"

    def test_medium_base_in_production_loadbalancer_stays_medium(self) -> None:
        from hexawyn.domain.services.external_exposure.risk_scorer import classify_risk_level

        result = classify_risk_level(
            base_severity="medium",
            service_type="LoadBalancer",
            namespace="production",
            production_namespace=_PRODUCTION,
            has_source_ranges=False,
        )

        assert result == "medium"
