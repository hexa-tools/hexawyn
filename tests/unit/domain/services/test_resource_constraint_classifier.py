from __future__ import annotations

from hexawyn.application.ports.driven.pod_resource_metrics_port import ContainerMetricsRecord
from hexawyn.domain.models.resource_constraint import RiskLevel
from hexawyn.domain.services.resource_constraint.classifier import (
    classify_container,
    sort_key,
)


def _record(  # noqa: PLR0913
    container_name: str = "app",
    pod_name: str = "test-pod",
    namespace: str = "default",
    cpu_usage: int = 100,
    cpu_limit: int | None = 500,
    mem_usage: int = 256 * 1024 * 1024,
    mem_limit: int | None = 512 * 1024 * 1024,
    is_init: bool = False,
) -> ContainerMetricsRecord:
    return ContainerMetricsRecord(
        container_name=container_name,
        pod_name=pod_name,
        namespace=namespace,
        cpu_usage_millicores=cpu_usage,
        cpu_limit_millicores=cpu_limit,
        memory_usage_bytes=mem_usage,
        memory_limit_bytes=mem_limit,
        is_init_container=is_init,
    )


class TestSortKey:
    def test_critical_has_lowest_value(self) -> None:
        assert sort_key(RiskLevel.CRITICAL) == 0

    def test_no_limits_middle_value(self) -> None:
        assert sort_key(RiskLevel.NO_LIMITS) == 1

    def test_ok_has_highest_value(self) -> None:
        assert sort_key(RiskLevel.OK) == 2  # noqa: PLR2004

    def test_ordering_is_critical_first(self) -> None:
        levels = [RiskLevel.OK, RiskLevel.CRITICAL, RiskLevel.NO_LIMITS]
        sorted_levels = sorted(levels, key=sort_key)
        assert sorted_levels[0] == RiskLevel.CRITICAL
        assert sorted_levels[1] == RiskLevel.NO_LIMITS
        assert sorted_levels[2] == RiskLevel.OK


class TestClassifyContainer:
    def test_ok_when_usage_below_thresholds(self) -> None:
        record = _record(
            cpu_usage=100, cpu_limit=500, mem_usage=256 * 1024 * 1024, mem_limit=512 * 1024 * 1024
        )
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.risk_level == RiskLevel.OK
        assert "throttled" not in entry.tags
        assert "oomkill_risk" not in entry.tags

    def test_critical_cpu_throttle(self) -> None:
        record = _record(
            cpu_usage=450, cpu_limit=500, mem_usage=100 * 1024 * 1024, mem_limit=500 * 1024 * 1024
        )
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.risk_level == RiskLevel.CRITICAL
        assert "throttled" in entry.tags

    def test_critical_mem_oomkill_risk(self) -> None:
        record = _record(
            cpu_usage=100, cpu_limit=500, mem_usage=450 * 1024 * 1024, mem_limit=500 * 1024 * 1024
        )
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.risk_level == RiskLevel.CRITICAL
        assert "oomkill_risk" in entry.tags

    def test_critical_both_cpu_and_mem(self) -> None:
        record = _record(
            cpu_usage=450, cpu_limit=500, mem_usage=450 * 1024 * 1024, mem_limit=500 * 1024 * 1024
        )
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.risk_level == RiskLevel.CRITICAL
        assert "throttled" in entry.tags
        assert "oomkill_risk" in entry.tags

    def test_no_limits_cpu(self) -> None:
        record = _record(cpu_limit=None, mem_limit=512 * 1024 * 1024)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.risk_level == RiskLevel.NO_LIMITS

    def test_no_limits_mem(self) -> None:
        record = _record(cpu_limit=500, mem_limit=None)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.risk_level == RiskLevel.NO_LIMITS

    def test_no_limits_both(self) -> None:
        record = _record(cpu_limit=None, mem_limit=None)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.risk_level == RiskLevel.NO_LIMITS

    def test_unlimited_cpu_tags(self) -> None:
        record = _record(
            cpu_limit=0, cpu_usage=100, mem_limit=512 * 1024 * 1024, mem_usage=256 * 1024 * 1024
        )
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.risk_level == RiskLevel.OK
        assert "cpu_unlimited" in entry.tags

    def test_unlimited_mem_tags(self) -> None:
        record = _record(cpu_limit=500, cpu_usage=100, mem_limit=0, mem_usage=256 * 1024 * 1024)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.risk_level == RiskLevel.OK
        assert "memory_unlimited" in entry.tags

    def test_init_container_tagged(self) -> None:
        record = _record(is_init=True)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert "init_container" in entry.tags

    def test_non_init_container_not_tagged(self) -> None:
        record = _record(is_init=False)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert "init_container" not in entry.tags

    def test_cpu_pct_computed_correctly(self) -> None:
        record = _record(cpu_usage=250, cpu_limit=500)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.cpu_pct == 50.0  # noqa: PLR2004

    def test_mem_pct_computed_correctly(self) -> None:
        record = _record(mem_usage=256 * 1024 * 1024, mem_limit=512 * 1024 * 1024)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.memory_pct == 50.0  # noqa: PLR2004

    def test_cpu_pct_none_when_no_limit(self) -> None:
        record = _record(cpu_limit=None)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.cpu_pct is None
        assert entry.risk_level == RiskLevel.NO_LIMITS

    def test_mem_pct_none_when_no_limit(self) -> None:
        record = _record(mem_limit=None)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.memory_pct is None

    def test_cpu_pct_none_when_limit_zero(self) -> None:
        record = _record(
            cpu_limit=0, cpu_usage=100, mem_limit=512 * 1024 * 1024, mem_usage=256 * 1024 * 1024
        )
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.cpu_pct is None

    def test_mem_pct_none_when_limit_zero(self) -> None:
        record = _record(cpu_limit=500, cpu_usage=100, mem_limit=0, mem_usage=256 * 1024 * 1024)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.memory_pct is None

    def test_container_name_preserved(self) -> None:
        record = _record(container_name="nginx")
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.container_name == "nginx"

    def test_pod_name_preserved(self) -> None:
        record = _record(pod_name="web-frontend")
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.pod_name == "web-frontend"

    def test_namespace_preserved(self) -> None:
        record = _record(namespace="production")
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.namespace == "production"

    def test_at_exact_threshold_still_ok(self) -> None:
        record = _record(cpu_usage=400, cpu_limit=500)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.risk_level == RiskLevel.OK

    def test_just_above_threshold_is_critical(self) -> None:
        record = _record(cpu_usage=401, cpu_limit=500)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.risk_level == RiskLevel.CRITICAL

    def test_no_limits_tag_when_none(self) -> None:
        record = _record(cpu_limit=None, mem_limit=None)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert "no_limits" in entry.tags

    def test_no_limits_tag_when_have_limits(self) -> None:
        record = _record(cpu_limit=500, mem_limit=512 * 1024 * 1024)
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert "no_limits" not in entry.tags

    def test_all_original_values_preserved(self) -> None:
        record = _record(
            cpu_usage=100, cpu_limit=500, mem_usage=256 * 1024 * 1024, mem_limit=512 * 1024 * 1024
        )
        entry = classify_container(record, cpu_thr=80.0, mem_thr=80.0)
        assert entry.cpu_usage_millicores == 100  # noqa: PLR2004
        assert entry.cpu_limit_millicores == 500  # noqa: PLR2004
        assert entry.memory_usage_bytes == 256 * 1024 * 1024
        assert entry.memory_limit_bytes == 512 * 1024 * 1024
