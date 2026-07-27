from __future__ import annotations

from unittest.mock import patch


class TestConfigBusinessParamsSource:
    def test_reads_business_config_from_config_yaml(self) -> None:
        from hexawyn.adapters.secondary.gitops.incident_cost_source import (
            ConfigIncidentCostSource,
        )

        config = {"business": {"revenue_per_minute": 500, "support_cost_per_hour": 180}}
        with patch(
            "hexawyn.adapters.secondary.gitops.incident_cost_source.load_config",
            return_value=config,
        ):
            data = ConfigIncidentCostSource().fetch_incident_cost_data("yesterday")

        assert data["business_config"]["revenue_per_minute"] == 500.0  # noqa: PLR2004
        assert data["business_config"]["support_cost_per_hour"] == 180.0  # noqa: PLR2004
        assert data["business_config"]["sla_penalty_per_hour"] is None

    def test_missing_business_section_yields_all_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.incident_cost_source import (
            ConfigIncidentCostSource,
        )

        with patch(
            "hexawyn.adapters.secondary.gitops.incident_cost_source.load_config",
            return_value={},
        ):
            data = ConfigIncidentCostSource().fetch_incident_cost_data("yesterday")

        assert data["business_config"]["revenue_per_minute"] is None
        assert data["business_config"]["support_cost_per_hour"] is None
        assert data["business_config"]["sla_penalty_per_hour"] is None

    def test_returns_default_incident_facts(self) -> None:
        from hexawyn.adapters.secondary.gitops.incident_cost_source import (
            ConfigIncidentCostSource,
        )

        with patch(
            "hexawyn.adapters.secondary.gitops.incident_cost_source.load_config",
            return_value={},
        ):
            data = ConfigIncidentCostSource().fetch_incident_cost_data("yesterday")

        assert data["downtime_minutes"] == 0
        assert data["business_service_name"] != ""

    def test_non_numeric_config_value_is_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.incident_cost_source import (
            ConfigIncidentCostSource,
        )

        config = {"business": {"revenue_per_minute": "not-a-number"}}
        with patch(
            "hexawyn.adapters.secondary.gitops.incident_cost_source.load_config",
            return_value=config,
        ):
            data = ConfigIncidentCostSource().fetch_incident_cost_data("yesterday")

        assert data["business_config"]["revenue_per_minute"] is None

    def test_boolean_config_value_is_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.incident_cost_source import (
            ConfigIncidentCostSource,
        )

        config = {"business": {"revenue_per_minute": True}}
        with patch(
            "hexawyn.adapters.secondary.gitops.incident_cost_source.load_config",
            return_value=config,
        ):
            data = ConfigIncidentCostSource().fetch_incident_cost_data("yesterday")

        assert data["business_config"]["revenue_per_minute"] is None
