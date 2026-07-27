"""RED → GREEN — Layer 1: Team Cost domain models."""

from hexawyn.domain.models.team_cost import TeamCost, TeamCostReport


class TestTeamCost:
    def test_is_frozen(self) -> None:
        import pytest

        t = TeamCost(
            team_name="payments",
            total_cost=500.0,
            cpu_cost=300.0,
            memory_cost=150.0,
            storage_cost=50.0,
            namespace_count=3,
            days_active=31,
            is_prorated=False,
        )
        with pytest.raises(Exception):
            t.total_cost = 100.0  # type: ignore[misc]


class TestTeamCostReport:
    def test_default_values(self) -> None:
        report = TeamCostReport()
        assert report.month == ""
        assert report.teams == []
        assert report.total_cost == 0.0

    def test_can_populate(self) -> None:
        report = TeamCostReport(month="2026-07", total_cost=2500.0, unattributed_cost=300.0)
        assert report.total_cost == 2500.0  # noqa: PLR2004
        assert report.unattributed_cost == 300.0  # noqa: PLR2004
