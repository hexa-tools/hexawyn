"""RED tests — domain/models/rightsizing.py"""

import pytest
from hexawyn.domain.models.rightsizing import (
    RightsizingRecommendation,
    RightsizingReport,
    RightsizingType,
)


class TestRightsizingType:
    def test_over_provisioned_value(self) -> None:
        assert RightsizingType.OVER_PROVISIONED.value == "over_provisioned"

    def test_under_provisioned_value(self) -> None:
        assert RightsizingType.UNDER_PROVISIONED.value == "under_provisioned"

    def test_optimal_value(self) -> None:
        assert RightsizingType.OPTIMAL.value == "optimal"


class TestRightsizingRecommendation:
    def _make(self, **kwargs: object) -> RightsizingRecommendation:
        defaults: dict[str, object] = {
            "resource_name": "ml-worker",
            "namespace": "production",
            "kind": "Deployment",
            "rightsizing_type": RightsizingType.OVER_PROVISIONED,
            "current_cpu_cores": 4.0,
            "recommended_cpu_cores": 1.0,
            "current_memory_mi": 8192.0,
            "recommended_memory_mi": 3072.0,
            "monthly_savings_usd": 71.0,
            "waste_percentage": 80.0,
            "reason": "CPU usage 20% of requests",
            "priority": "high",
        }
        defaults.update(kwargs)
        return RightsizingRecommendation(**defaults)  # type: ignore[arg-type]

    def test_fields_stored_correctly(self) -> None:
        rec = self._make()
        assert rec.resource_name == "ml-worker"
        assert rec.namespace == "production"
        assert rec.kind == "Deployment"
        assert rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
        assert rec.current_cpu_cores == 4.0
        assert rec.recommended_cpu_cores == 1.0
        assert rec.current_memory_mi == 8192.0
        assert rec.recommended_memory_mi == 3072.0
        assert rec.monthly_savings_usd == 71.0
        assert rec.waste_percentage == 80.0
        assert rec.reason == "CPU usage 20% of requests"
        assert rec.priority == "high"

    def test_is_frozen(self) -> None:
        rec = self._make()
        with pytest.raises((AttributeError, TypeError)):
            rec.resource_name = "changed"  # type: ignore[misc]

    def test_negative_savings_for_under_provisioned(self) -> None:
        rec = self._make(
            rightsizing_type=RightsizingType.UNDER_PROVISIONED,
            monthly_savings_usd=-2.0,
        )
        assert rec.monthly_savings_usd < 0


class TestRightsizingReport:
    def test_empty_report(self) -> None:
        report = RightsizingReport(
            recommendations=[],
            skipped_count=0,
            total_monthly_savings_usd=0.0,
        )
        assert report.recommendations == []
        assert report.skipped_count == 0
        assert report.total_monthly_savings_usd == 0.0

    def test_recommendations_list_mutable(self) -> None:
        report = RightsizingReport(
            recommendations=[],
            skipped_count=2,
            total_monthly_savings_usd=0.0,
        )
        report.recommendations.append(
            RightsizingRecommendation(
                resource_name="x",
                namespace="ns",
                kind="Deployment",
                rightsizing_type=RightsizingType.OPTIMAL,
                current_cpu_cores=1.0,
                recommended_cpu_cores=1.0,
                current_memory_mi=512.0,
                recommended_memory_mi=512.0,
                monthly_savings_usd=0.0,
                waste_percentage=0.0,
                reason="optimal",
                priority="low",
            )
        )
        assert len(report.recommendations) == 1
