from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.vanilla.adapters._helpers import (
    conditions,
    container_statuses,
    cpu_to_cores,
    integer_attr,
    items_from,
    mapping_from,
    mapping_text,
    memory_to_bytes,
    metric_items,
    namespace_age,
    optional_text_attr,
    parse_cpu,
    parse_memory,
    percentage,
    restart_count,
    text_attr,
    waiting_reason,
)


class TestParseCpu:
    def test_milli(self) -> None:
        assert parse_cpu("500m") == 500  # noqa: PLR2004

    def test_cores(self) -> None:
        assert parse_cpu("2") == 2000  # noqa: PLR2004

    def test_empty_string(self) -> None:
        assert parse_cpu("") == 0

    def test_zero(self) -> None:
        assert parse_cpu("0") == 0


class TestParseMemory:
    def test_mi(self) -> None:
        assert parse_memory("512Mi") == 512  # noqa: PLR2004

    def test_gi(self) -> None:
        assert parse_memory("2Gi") == 2048  # noqa: PLR2004

    def test_ki(self) -> None:
        assert parse_memory("1024Ki") == 1

    def test_empty_string(self) -> None:
        assert parse_memory("") == 0


class TestTextAttr:
    def test_returns_value_when_present(self) -> None:
        obj = MagicMock()
        obj.name = "my-pod"
        assert text_attr(obj, "name", "unknown") == "my-pod"

    def test_returns_default_when_none(self) -> None:
        obj = MagicMock()
        obj.name = None
        assert text_attr(obj, "name", "unknown") == "unknown"

    def test_returns_default_when_missing(self) -> None:
        obj = MagicMock(spec=["other"])
        assert text_attr(obj, "name", "unknown") == "unknown"


class TestOptionalTextAttr:
    def test_returns_value(self) -> None:
        obj = MagicMock()
        obj.phase = "Running"
        assert optional_text_attr(obj, "phase") == "Running"

    def test_returns_none_for_empty(self) -> None:
        obj = MagicMock()
        obj.phase = ""
        assert optional_text_attr(obj, "phase") is None

    def test_returns_none_for_none(self) -> None:
        obj = MagicMock()
        obj.phase = None
        assert optional_text_attr(obj, "phase") is None


class TestIntegerAttr:
    def test_returns_integer(self) -> None:
        obj = MagicMock()
        obj.count = 5
        assert integer_attr(obj, "count") == 5  # noqa: PLR2004

    def test_returns_zero_when_missing(self) -> None:
        obj = MagicMock(spec=["other"])
        assert integer_attr(obj, "count") == 0

    def test_returns_zero_when_not_int(self) -> None:
        obj = MagicMock()
        obj.count = "abc"
        assert integer_attr(obj, "count") == 0


class TestItemsFrom:
    def test_returns_items(self) -> None:
        response = MagicMock()
        response.items = [1, 2, 3]
        assert items_from(response) == [1, 2, 3]

    def test_returns_empty_when_no_items(self) -> None:
        response = MagicMock()
        response.items = []
        assert items_from(response) == []


class TestConditions:
    def test_returns_conditions(self) -> None:
        status = MagicMock()
        cond = MagicMock()
        status.conditions = [cond]
        result = conditions(status)
        assert len(result) == 1

    def test_returns_empty(self) -> None:
        status = MagicMock()
        status.conditions = []
        assert conditions(status) == []


class TestContainerStatuses:
    def test_returns_container_statuses(self) -> None:
        status = MagicMock()
        cs = MagicMock()
        status.container_statuses = [cs]
        result = container_statuses(status)
        assert len(result) == 1

    def test_returns_empty(self) -> None:
        status = MagicMock()
        status.container_statuses = []
        assert container_statuses(status) == []


class TestWaitingReason:
    def test_returns_none_when_no_waiting(self) -> None:
        status = MagicMock()
        cs = MagicMock()
        cs.state = MagicMock()
        cs.state.waiting = None
        status.container_statuses = [cs]
        assert waiting_reason(status) is None

    def test_returns_crashloop(self) -> None:
        status = MagicMock()
        cs = MagicMock()
        cs.state = MagicMock()
        cs.state.waiting = MagicMock()
        cs.state.waiting.reason = "CrashLoopBackOff"
        status.container_statuses = [cs]
        assert waiting_reason(status) == "CrashLoop"

    def test_returns_first_reason(self) -> None:
        status = MagicMock()
        cs = MagicMock()
        cs.state = MagicMock()
        cs.state.waiting = MagicMock()
        cs.state.waiting.reason = "ErrImagePull"
        status.container_statuses = [cs]
        assert waiting_reason(status) == "ErrImagePull"


class TestRestartCount:
    def test_sums_restarts(self) -> None:
        status = MagicMock()
        cs1 = MagicMock()
        cs1.restart_count = 3
        cs2 = MagicMock()
        cs2.restart_count = 2
        status.container_statuses = [cs1, cs2]
        assert restart_count(status) == 5  # noqa: PLR2004

    def test_returns_zero_when_empty(self) -> None:
        status = MagicMock()
        status.container_statuses = []
        assert restart_count(status) == 0


class TestNamespaceAge:
    def test_returns_unknown_when_no_timestamp(self) -> None:
        metadata = MagicMock()
        metadata.creation_timestamp = None
        assert namespace_age(metadata) == "unknown"

    def test_returns_days_for_old(self) -> None:
        from datetime import UTC, datetime, timedelta

        metadata = MagicMock()
        metadata.creation_timestamp = datetime.now(UTC) - timedelta(days=5)
        age = namespace_age(metadata)
        assert "d" in age

    def test_returns_minutes_for_recent(self) -> None:
        from datetime import UTC, datetime, timedelta

        metadata = MagicMock()
        metadata.creation_timestamp = datetime.now(UTC) - timedelta(minutes=5)
        age = namespace_age(metadata)
        assert "m" in age


class TestMappingFrom:
    def test_returns_dict(self) -> None:
        d = {"key": "value"}
        assert mapping_from(d) == d

    def test_returns_none_for_list(self) -> None:
        assert mapping_from([1, 2, 3]) is None


class TestMappingText:
    def test_returns_string_value(self) -> None:
        assert mapping_text({"cpu": "100m"}, "cpu") == "100m"

    def test_returns_empty_for_missing(self) -> None:
        assert mapping_text({"cpu": "100m"}, "memory") == ""

    def test_returns_empty_for_non_string(self) -> None:
        assert mapping_text({"count": 5}, "count") == ""


class TestMetricItems:
    def test_returns_items(self) -> None:
        metrics = {"items": [{"usage": {"cpu": "100m"}}]}
        result = metric_items(metrics)
        assert len(result) == 1

    def test_returns_empty_for_non_dict(self) -> None:
        assert metric_items(None) == []

    def test_returns_empty_when_no_items(self) -> None:
        assert metric_items({"other": "data"}) == []


class TestCpuToCores:
    def test_nanocores(self) -> None:
        assert cpu_to_cores("1000000000n") == 1.0

    def test_microcores(self) -> None:
        assert cpu_to_cores("1000000u") == 1.0

    def test_millicores(self) -> None:
        assert cpu_to_cores("1500m") == 1.5  # noqa: PLR2004

    def test_cores(self) -> None:
        assert cpu_to_cores("2") == 2.0  # noqa: PLR2004


class TestMemoryToBytes:
    def test_ki(self) -> None:
        assert memory_to_bytes("1Ki") == 1024.0  # noqa: PLR2004

    def test_mi(self) -> None:
        assert memory_to_bytes("1Mi") == 1048576.0  # noqa: PLR2004

    def test_gi(self) -> None:
        assert memory_to_bytes("1Gi") == 1073741824.0  # noqa: PLR2004

    def test_raw_bytes(self) -> None:
        assert memory_to_bytes("1024") == 1024.0  # noqa: PLR2004


class TestPercentage:
    def test_returns_pct(self) -> None:
        assert percentage(5.0, 10.0) == 50.0  # noqa: PLR2004

    def test_returns_zero_when_capacity_zero(self) -> None:
        assert percentage(5.0, 0.0) == 0.0

    def test_returns_zero_when_capacity_negative(self) -> None:
        assert percentage(5.0, -1.0) == 0.0
