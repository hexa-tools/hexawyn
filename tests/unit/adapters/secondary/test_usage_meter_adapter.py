from __future__ import annotations

from hexawyn.adapters.secondary.usage_meter_adapter import UsageMeterAdapter
from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort


class TestUsageMeterAdapter:
    def test_get_default_zero(self) -> None:
        adapter = UsageMeterAdapter()
        assert adapter.get_usage("investigations") == 0

    def test_set_and_get(self) -> None:
        adapter = UsageMeterAdapter()
        adapter.set_usage("investigations", 42)
        assert adapter.get_usage("investigations") == 42  # noqa: PLR2004

    def test_overwrite(self) -> None:
        adapter = UsageMeterAdapter()
        adapter.set_usage("a", 10)
        adapter.set_usage("a", 20)
        assert adapter.get_usage("a") == 20  # noqa: PLR2004

    def test_unknown_resource_zero(self) -> None:
        adapter = UsageMeterAdapter()
        assert adapter.get_usage("unknown") == 0

    def test_implements_port(self) -> None:
        assert isinstance(UsageMeterAdapter(), UsageMeterPort)
