from datetime import UTC, datetime

from hexawyn.domain.models.cluster import (
    CloudProvider,
    ClusterContext,
    ClusterHealth,
    ClusterScore,
)


class TestClusterHealth:
    def test_values(self):
        assert ClusterHealth.HEALTHY.value == "healthy"
        assert ClusterHealth.DEGRADED.value == "degraded"
        assert ClusterHealth.CRITICAL.value == "critical"
        assert ClusterHealth.UNKNOWN.value == "unknown"


class TestCloudProvider:
    def test_values(self) -> None:
        assert CloudProvider.VANILLA.value == "vanilla"
        assert CloudProvider.AWS.value == "aws"
        assert CloudProvider.AZURE.value == "azure"
        assert CloudProvider.GCP.value == "gcp"
        assert CloudProvider.DEMO.value == "demo"
        assert CloudProvider.OPENSHIFT.value == "openshift"
        assert CloudProvider.DATADOG.value == "datadog"

    def test_all_seven_values(self) -> None:
        values = {p.value for p in CloudProvider}
        assert len(values) == 7

    def test_openshift_membership(self) -> None:
        assert CloudProvider("openshift") == CloudProvider.OPENSHIFT

    def test_datadog_membership(self) -> None:
        assert CloudProvider("datadog") == CloudProvider.DATADOG


class TestClusterContext:
    def test_defaults(self) -> None:
        ctx = ClusterContext(name="unknown")
        assert ctx.name == "unknown"
        assert ctx.namespace == "default"
        assert ctx.api_server == ""

    def test_custom_values(self) -> None:
        ctx = ClusterContext(
            name="prod-eu", namespace="payments", api_server="https://k8s.example.com"
        )
        assert ctx.name == "prod-eu"
        assert ctx.namespace == "payments"
        assert ctx.api_server == "https://k8s.example.com"

    def test_equality_matches_on_name(self) -> None:
        a = ClusterContext(name="prod", namespace="ns1")
        b = ClusterContext(name="prod", namespace="ns1")
        assert a == b

    def test_equality_differs_on_namespace(self) -> None:
        a = ClusterContext(name="prod", namespace="ns1")
        b = ClusterContext(name="prod", namespace="ns2")
        assert a != b

    def test_equality_differs_on_name(self) -> None:
        a = ClusterContext(name="prod")
        b = ClusterContext(name="dev")
        assert a != b

    def test_inequality_on_api_server(self) -> None:
        a = ClusterContext(name="prod", api_server="https://a.com")
        b = ClusterContext(name="prod", api_server="https://b.com")
        assert a != b

    def test_empty_namespace_accepted(self) -> None:
        ctx = ClusterContext(name="unknown", namespace="")
        assert ctx.namespace == ""


class TestClusterScore:
    def test_defaults(self) -> None:
        score = ClusterScore(overall=100, health=ClusterHealth.UNKNOWN, cluster_name="test")
        assert score.overall == 100
        assert score.health == ClusterHealth.UNKNOWN
        assert score.breakdown == {}
        assert score.issues == []
        assert score.recommendations == []

    def test_overall_zero(self) -> None:
        score = ClusterScore(overall=0, health=ClusterHealth.UNKNOWN, cluster_name="test")
        assert score.overall == 0

    def test_overall_hundred(self) -> None:
        score = ClusterScore(overall=100, health=ClusterHealth.UNKNOWN, cluster_name="test")
        assert score.overall == 100

    def test_breakdown_independent_per_instance(self) -> None:
        a = ClusterScore(
            overall=100, health=ClusterHealth.UNKNOWN, cluster_name="test", breakdown={"cpu": 50}
        )
        b = ClusterScore(overall=100, health=ClusterHealth.UNKNOWN, cluster_name="test")
        assert a.breakdown == {"cpu": 50}
        assert b.breakdown == {}

    def test_issues_independent_per_instance(self) -> None:
        a = ClusterScore(
            overall=100, health=ClusterHealth.UNKNOWN, cluster_name="test", issues=["OOM"]
        )
        b = ClusterScore(overall=100, health=ClusterHealth.UNKNOWN, cluster_name="test")
        assert a.issues == ["OOM"]
        assert b.issues == []

    def test_recommendations_independent_per_instance(self) -> None:
        a = ClusterScore(
            overall=100,
            health=ClusterHealth.UNKNOWN,
            cluster_name="test",
            recommendations=["increase memory"],
        )
        b = ClusterScore(overall=100, health=ClusterHealth.UNKNOWN, cluster_name="test")
        assert a.recommendations == ["increase memory"]
        assert b.recommendations == []

    def test_equality(self) -> None:
        now = datetime.now(UTC)
        a = ClusterScore(
            overall=85, health=ClusterHealth.UNKNOWN, cluster_name="test", timestamp=now
        )
        b = ClusterScore(
            overall=85, health=ClusterHealth.UNKNOWN, cluster_name="test", timestamp=now
        )
        assert a == b

    def test_with_health_unknown(self) -> None:
        score = ClusterScore(overall=100, health=ClusterHealth.UNKNOWN, cluster_name="test")
        assert score.health == ClusterHealth.UNKNOWN

    def test_with_health_healthy(self) -> None:
        score = ClusterScore(overall=100, health=ClusterHealth.HEALTHY, cluster_name="test")
        assert score.health == ClusterHealth.HEALTHY

    def test_with_health_degraded(self) -> None:
        score = ClusterScore(overall=100, health=ClusterHealth.DEGRADED, cluster_name="test")
        assert score.health == ClusterHealth.DEGRADED

    def test_with_health_critical(self) -> None:
        score = ClusterScore(overall=100, health=ClusterHealth.CRITICAL, cluster_name="test")
        assert score.health == ClusterHealth.CRITICAL


class TestClusterScoreEdgeCases:
    def test_breakdown_mutable_default_not_shared(self) -> None:
        a = ClusterScore(overall=80, health=ClusterHealth.HEALTHY, cluster_name="a")
        b = ClusterScore(overall=90, health=ClusterHealth.DEGRADED, cluster_name="b")
        a.breakdown["cpu"] = 100
        assert "cpu" not in b.breakdown
        assert b.breakdown == {}

    def test_issues_mutable_default_not_shared(self) -> None:
        a = ClusterScore(overall=80, health=ClusterHealth.HEALTHY, cluster_name="a")
        b = ClusterScore(overall=90, health=ClusterHealth.DEGRADED, cluster_name="b")
        a.issues.append("OOMKilled")
        assert "OOMKilled" not in b.issues
        assert b.issues == []

    def test_recommendations_mutable_default_not_shared(self) -> None:
        a = ClusterScore(overall=80, health=ClusterHealth.HEALTHY, cluster_name="a")
        b = ClusterScore(overall=90, health=ClusterHealth.DEGRADED, cluster_name="b")
        a.recommendations.append("scale up")
        assert "scale up" not in b.recommendations
        assert b.recommendations == []

    def test_overall_boundary_zero(self) -> None:
        score = ClusterScore(overall=0, health=ClusterHealth.CRITICAL, cluster_name="test")
        assert score.overall == 0

    def test_overall_boundary_hundred(self) -> None:
        score = ClusterScore(overall=100, health=ClusterHealth.HEALTHY, cluster_name="test")
        assert score.overall == 100

    def test_overall_negative_accepted(self) -> None:
        score = ClusterScore(overall=-1, health=ClusterHealth.UNKNOWN, cluster_name="test")
        assert score.overall == -1

    def test_timestamp_is_utc_aware(self) -> None:
        score = ClusterScore(overall=50, health=ClusterHealth.UNKNOWN, cluster_name="test")
        assert score.timestamp is not None
        assert score.timestamp.tzinfo is not None
        assert score.timestamp.tzinfo == UTC

    def test_timestamp_is_recent(self) -> None:
        score = ClusterScore(overall=50, health=ClusterHealth.UNKNOWN, cluster_name="test")
        age = (datetime.now(UTC) - score.timestamp).total_seconds()
        assert age < 5

    def test_equality_different_breakdown(self) -> None:
        now = datetime.now(UTC)
        a = ClusterScore(
            overall=85,
            health=ClusterHealth.HEALTHY,
            cluster_name="test",
            timestamp=now,
            breakdown={"cpu": 80},
        )
        b = ClusterScore(
            overall=85,
            health=ClusterHealth.HEALTHY,
            cluster_name="test",
            timestamp=now,
            breakdown={"cpu": 70},
        )
        assert a != b

    def test_equality_different_issues(self) -> None:
        now = datetime.now(UTC)
        a = ClusterScore(
            overall=85,
            health=ClusterHealth.HEALTHY,
            cluster_name="test",
            timestamp=now,
            issues=["issue-a"],
        )
        b = ClusterScore(
            overall=85,
            health=ClusterHealth.HEALTHY,
            cluster_name="test",
            timestamp=now,
            issues=["issue-b"],
        )
        assert a != b

    def test_equality_different_recommendations(self) -> None:
        now = datetime.now(UTC)
        a = ClusterScore(
            overall=85,
            health=ClusterHealth.HEALTHY,
            cluster_name="test",
            timestamp=now,
            recommendations=["rec-a"],
        )
        b = ClusterScore(
            overall=85,
            health=ClusterHealth.HEALTHY,
            cluster_name="test",
            timestamp=now,
            recommendations=["rec-b"],
        )
        assert a != b


class TestClusterContextEdgeCases:
    def test_empty_name_accepted(self) -> None:
        ctx = ClusterContext(name="")
        assert ctx.name == ""
        assert ctx.namespace == "default"

    def test_provider_default_is_vanilla(self) -> None:
        ctx = ClusterContext(name="test")
        assert ctx.provider == CloudProvider.VANILLA

    def test_provider_custom_value(self) -> None:
        ctx = ClusterContext(name="eks-cluster", provider=CloudProvider.AWS)
        assert ctx.provider == CloudProvider.AWS

    def test_empty_api_server_accepted(self) -> None:
        ctx = ClusterContext(name="test", api_server="")
        assert ctx.api_server == ""

    def test_equality_same_provider(self) -> None:
        a = ClusterContext(name="prod", provider=CloudProvider.AWS)
        b = ClusterContext(name="prod", provider=CloudProvider.AWS)
        assert a == b

    def test_equality_different_provider(self) -> None:
        a = ClusterContext(name="prod", provider=CloudProvider.AWS)
        b = ClusterContext(name="prod", provider=CloudProvider.GCP)
        assert a != b
