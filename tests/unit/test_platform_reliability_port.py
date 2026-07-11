from abc import ABC


class TestPlatformReliabilityPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.platform_reliability_port import (
            PlatformReliabilityPort,
        )

        assert issubclass(PlatformReliabilityPort, ABC)

    def test_declares_get_reliability_data(self) -> None:
        from hexawyn.application.ports.driven.platform_reliability_port import (
            PlatformReliabilityPort,
        )

        assert "get_reliability_data" in PlatformReliabilityPort.__abstractmethods__


class TestRawTypedDicts:
    def test_reliability_incident_raw_shape(self) -> None:
        from hexawyn.application.ports.driven.platform_reliability_port import (
            ReliabilityIncidentRaw,
        )

        raw: ReliabilityIncidentRaw = {
            "date": "2026-06-14",
            "severity": "major",
            "downtime_minutes": 120,
            "resolution_minutes": 120,
            "root_cause": "Database outage",
            "resolved": True,
            "planned_maintenance": False,
        }

        assert raw["severity"] == "major"
        assert raw["downtime_minutes"] == 120

    def test_reliability_data_shape(self) -> None:
        from hexawyn.application.ports.driven.platform_reliability_port import (
            ReliabilityData,
        )

        data: ReliabilityData = {
            "period_minutes": 43200,
            "incidents": [],
            "previous_avg_resolution_minutes": 14,
            "cost_per_downtime_minute_eur": None,
        }

        assert data["period_minutes"] == 43200
        assert data["cost_per_downtime_minute_eur"] is None
