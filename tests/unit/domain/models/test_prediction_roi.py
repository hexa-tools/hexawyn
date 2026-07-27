from dataclasses import fields


class TestPreventedIncident:
    def test_fields(self) -> None:
        from hexawyn.domain.models.prediction_roi import PreventedIncident

        names = {f.name for f in fields(PreventedIncident)}
        assert names == {
            "incident_ref",
            "business_service_name",
            "detected_at",
            "avoided_downtime_minutes",
            "confidence_pct",
            "avoided_cost_eur",
        }

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.prediction_roi import PreventedIncident

        prevented = PreventedIncident(
            incident_ref="PRED-42",
            business_service_name="Service Paiement",
            detected_at="2026-06-10",
            avoided_downtime_minutes=120,
            confidence_pct=90.0,
            avoided_cost_eur=60000.0,
        )

        assert prevented.incident_ref == "PRED-42"
        assert prevented.avoided_cost_eur == 60000.0  # noqa: PLR2004


class TestPredictionRoiReport:
    def test_defaults(self) -> None:
        from hexawyn.domain.models.prediction_roi import PredictionRoiReport

        report = PredictionRoiReport(period_label="2026-06")

        assert report.period_label == "2026-06"
        assert report.detected_count == 0
        assert report.prevented_incident_count == 0
        assert report.avoided_downtime_minutes == 0
        assert report.total_avoided_cost_eur is None
        assert report.infrastructure_cost_eur == 0.0
        assert report.roi_eur is None
        assert report.prevented_incidents == []
        assert report.config_available is False
        assert report.explanation == ""

    def test_holds_summary(self) -> None:
        from hexawyn.domain.models.prediction_roi import PredictionRoiReport

        report = PredictionRoiReport(
            period_label="2026-06",
            detected_count=4,
            prevented_incident_count=1,
            avoided_downtime_minutes=360,
            total_avoided_cost_eur=198000.0,
            infrastructure_cost_eur=2000.0,
            roi_eur=196000.0,
            config_available=True,
        )

        assert report.total_avoided_cost_eur == 198000.0  # noqa: PLR2004
        assert report.roi_eur == 196000.0  # noqa: PLR2004
