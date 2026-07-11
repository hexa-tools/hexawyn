from abc import ABC


class TestPredictionRoiPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.prediction_roi_port import (
            PredictionRoiPort,
        )

        assert issubclass(PredictionRoiPort, ABC)

    def test_declares_get_prediction_roi_data(self) -> None:
        from hexawyn.application.ports.driven.prediction_roi_port import (
            PredictionRoiPort,
        )

        assert "get_prediction_roi_data" in PredictionRoiPort.__abstractmethods__


class TestRawTypedDicts:
    def test_prevented_incident_raw_shape(self) -> None:
        from hexawyn.application.ports.driven.prediction_roi_port import (
            PreventedIncidentRaw,
        )

        raw: PreventedIncidentRaw = {
            "incident_ref": "PRED-42",
            "business_service_name": "Service Paiement",
            "detected_at": "2026-06-10",
            "avoided_downtime_minutes": 120,
            "confidence_pct": 90.0,
            "prevented": True,
        }

        assert raw["incident_ref"] == "PRED-42"
        assert raw["prevented"] is True

    def test_prediction_roi_data_shape(self) -> None:
        from hexawyn.application.ports.driven.prediction_roi_port import (
            PredictionRoiData,
        )

        data: PredictionRoiData = {
            "detections": [],
            "infrastructure_cost_eur": 2000.0,
            "revenue_per_minute": 500.0,
        }

        assert data["infrastructure_cost_eur"] == 2000.0
        assert data["revenue_per_minute"] == 500.0
