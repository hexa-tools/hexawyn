from datetime import UTC, datetime

from hexawyn.domain.models.cluster import (
    CloudProvider,
    ClusterContext,
    ClusterHealth,
    ClusterScore,
)


class TestClusterContext:
    def test_default_values(self):
        ctx = ClusterContext(name="prod-cluster")
        assert ctx.name == "prod-cluster"
        assert ctx.namespace == "default"
        assert ctx.provider == CloudProvider.VANILLA
        assert ctx.api_server == ""

    def test_custom_values(self):
        ctx = ClusterContext(
            name="eks-prod",
            namespace="kube-system",
            provider=CloudProvider.AWS,
            api_server="https://api.eks.amazonaws.com",
        )
        assert ctx.provider == CloudProvider.AWS
        assert ctx.namespace == "kube-system"

    def test_is_dataclass(self):
        ctx = ClusterContext(name="test")
        ctx2 = ClusterContext(name="test")
        assert ctx == ctx2


class TestClusterScore:
    def test_defaults(self):
        score = ClusterScore(
            overall=85, health=ClusterHealth.HEALTHY, cluster_name="prod"
        )
        assert score.overall == 85
        assert score.health == ClusterHealth.HEALTHY
        assert score.breakdown == {}
        assert score.issues == []
        assert score.recommendations == []

    def test_timestamp_is_utc(self):
        score = ClusterScore(
            overall=50, health=ClusterHealth.DEGRADED, cluster_name="staging"
        )
        assert score.timestamp.tzinfo is not None
        assert score.timestamp.tzinfo == UTC

    def test_with_breakdown_and_issues(self):
        score = ClusterScore(
            overall=30,
            health=ClusterHealth.CRITICAL,
            cluster_name="dev",
            breakdown={"cpu": 10, "memory": 20},
            issues=["OOMKill", "CrashLoopBackOff"],
            recommendations=["Increase memory limit"],
        )
        assert len(score.issues) == 2
        assert len(score.recommendations) == 1
        assert score.breakdown["cpu"] == 10


class TestClusterHealth:
    def test_values(self):
        assert ClusterHealth.HEALTHY.value == "healthy"
        assert ClusterHealth.DEGRADED.value == "degraded"
        assert ClusterHealth.CRITICAL.value == "critical"
        assert ClusterHealth.UNKNOWN.value == "unknown"


class TestCloudProvider:
    def test_values(self):
        assert CloudProvider.VANILLA.value == "vanilla"
        assert CloudProvider.AWS.value == "aws"
        assert CloudProvider.AZURE.value == "azure"
        assert CloudProvider.GCP.value == "gcp"
        assert CloudProvider.DEMO.value == "demo"
