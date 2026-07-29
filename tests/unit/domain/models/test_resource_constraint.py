from __future__ import annotations

from hexawyn.domain.models.resource_constraint import (
    ContainerResourceEntry,
    ResourceConstraintReport,
    RiskLevel,
)


class TestRiskLevel:
    def test_values(self) -> None:
        assert RiskLevel.CRITICAL.value == "CRITICAL"
        assert RiskLevel.NO_LIMITS.value == "NO_LIMITS"
        assert RiskLevel.OK.value == "OK"

    def test_is_str_enum(self) -> None:
        assert isinstance(RiskLevel.CRITICAL, str)


class TestContainerResourceEntry:
    def test_create(self) -> None:
        entry = ContainerResourceEntry(
            container_name="app",
            pod_name="app-abc",
            namespace="default",
            cpu_usage_millicores=500,
            cpu_limit_millicores=1000,
            memory_usage_bytes=256_000_000,
            memory_limit_bytes=512_000_000,
            cpu_pct=50.0,
            memory_pct=50.0,
            risk_level=RiskLevel.OK,
        )
        assert entry.container_name == "app"
        assert entry.risk_level == RiskLevel.OK
        assert not entry.is_init_container
        assert entry.tags == []

    def test_with_tags(self) -> None:
        entry = ContainerResourceEntry(
            container_name="init",
            pod_name="p",
            namespace="ns",
            cpu_usage_millicores=0,
            cpu_limit_millicores=None,
            memory_usage_bytes=0,
            memory_limit_bytes=None,
            cpu_pct=None,
            memory_pct=None,
            risk_level=RiskLevel.NO_LIMITS,
            is_init_container=True,
            tags=["throttled"],
        )
        assert entry.is_init_container
        assert entry.tags == ["throttled"]
        assert entry.cpu_limit_millicores is None


class TestResourceConstraintReport:
    def test_create(self) -> None:
        r = ResourceConstraintReport(namespace="ns", total_pods_scanned=10, total_containers=20)
        assert r.namespace == "ns"
        assert r.total_pods_scanned == 10  # noqa: PLR2004
        assert r.total_containers == 20  # noqa: PLR2004
        assert r.critical_count == 0
        assert r.containers == []
        assert r.generated_at is not None

    def test_with_containers(self) -> None:
        entry = ContainerResourceEntry(
            container_name="c",
            pod_name="p",
            namespace="ns",
            cpu_usage_millicores=0,
            cpu_limit_millicores=None,
            memory_usage_bytes=0,
            memory_limit_bytes=None,
            cpu_pct=None,
            memory_pct=None,
            risk_level=RiskLevel.CRITICAL,
        )
        r = ResourceConstraintReport(
            namespace="ns",
            total_pods_scanned=1,
            total_containers=1,
            critical_count=1,
            containers=[entry],
        )
        assert r.critical_count == 1
        assert len(r.containers) == 1
