from __future__ import annotations

from unittest.mock import patch


class TestConfigBudgetIntelligenceSource:
    def test_reads_budget_from_config(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_intelligence_source import (
            ConfigBudgetIntelligenceSource,
        )

        with patch(
            "hexawyn.adapters.secondary.gitops.budget_intelligence_source.load_config",
            return_value={"business": {"cloud_budget_monthly": 12000.0}},
        ):
            data = ConfigBudgetIntelligenceSource().fetch_budget_intelligence_data("current")

        assert data["budget_monthly_eur"] == 12000.0  # noqa: PLR2004

    def test_missing_config_returns_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_intelligence_source import (
            ConfigBudgetIntelligenceSource,
        )

        with patch(
            "hexawyn.adapters.secondary.gitops.budget_intelligence_source.load_config",
            return_value={},
        ):
            data = ConfigBudgetIntelligenceSource().fetch_budget_intelligence_data("current")

        assert data["budget_monthly_eur"] is None

    def test_non_numeric_is_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_intelligence_source import (
            ConfigBudgetIntelligenceSource,
        )

        with patch(
            "hexawyn.adapters.secondary.gitops.budget_intelligence_source.load_config",
            return_value={"business": {"cloud_budget_monthly": True}},
        ):
            data = ConfigBudgetIntelligenceSource().fetch_budget_intelligence_data("current")

        assert data["budget_monthly_eur"] is None

    def test_string_budget_is_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.budget_intelligence_source import (
            ConfigBudgetIntelligenceSource,
        )

        with patch(
            "hexawyn.adapters.secondary.gitops.budget_intelligence_source.load_config",
            return_value={"business": {"cloud_budget_monthly": "12000"}},
        ):
            data = ConfigBudgetIntelligenceSource().fetch_budget_intelligence_data("current")

        assert data["budget_monthly_eur"] is None
