from abc import ABC


class TestIncidentCostPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.incident_cost_port import (
            IncidentCostPort,
        )

        assert issubclass(IncidentCostPort, ABC)

    def test_declares_get_incident_cost_data(self) -> None:
        from hexawyn.application.ports.driven.incident_cost_port import (
            IncidentCostPort,
        )

        assert "get_incident_cost_data" in IncidentCostPort.__abstractmethods__


class TestRawTypedDicts:
    def test_business_config_raw_shape(self) -> None:
        from hexawyn.application.ports.driven.incident_cost_port import (
            BusinessConfigRaw,
        )

        raw: BusinessConfigRaw = {
            "revenue_per_minute": 500.0,
            "support_cost_per_hour": 180.0,
            "sla_penalty_per_hour": 1500.0,
        }

        assert raw["revenue_per_minute"] == 500.0

    def test_incident_cost_data_shape(self) -> None:
        from hexawyn.application.ports.driven.incident_cost_port import (
            IncidentCostData,
        )

        data: IncidentCostData = {
            "business_service_name": "Service Paiement",
            "downtime_minutes": 27,
            "impacted_service_count": 3,
            "resolved_at": "14h23",
            "sla_breached": False,
            "business_config": {
                "revenue_per_minute": 500.0,
                "support_cost_per_hour": None,
                "sla_penalty_per_hour": None,
            },
        }

        assert data["downtime_minutes"] == 27
        assert data["business_config"]["revenue_per_minute"] == 500.0
