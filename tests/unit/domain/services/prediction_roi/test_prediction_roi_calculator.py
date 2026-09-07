from __future__ import annotations

from hexawyn.application.ports.driven.prediction_roi_port import (
    PredictionRoiData,
    PreventedIncidentRaw,
)
from hexawyn.domain.models.prediction_roi import (
    PredictionRoiReport,
    PreventedIncident,
)
from hexawyn.domain.services.prediction_roi.prediction_roi_calculator import (
    _to_prevented,
    _unconfigured_report,
    compute_prediction_roi,
)


def _detection(  # noqa: PLR0913
    incident_ref: str = "inc-001",
    business_service_name: str = "payments-api",
    detected_at: str = "2026-06-15T14:00:00Z",
    avoided_downtime_minutes: int = 30,
    confidence_pct: float = 85.0,
    prevented: bool = True,
) -> PreventedIncidentRaw:
    return PreventedIncidentRaw(
        incident_ref=incident_ref,
        business_service_name=business_service_name,
        detected_at=detected_at,
        avoided_downtime_minutes=avoided_downtime_minutes,
        confidence_pct=confidence_pct,
        prevented=prevented,
    )


class TestToPrevented:
    def test_computes_avoided_cost(self) -> None:
        detection = _detection(avoided_downtime_minutes=30)
        result = _to_prevented(detection, 1000.0)
        assert result.avoided_cost_eur == 30000.0  # noqa: PLR2004

    def test_preserves_all_fields(self) -> None:
        detection = _detection(
            incident_ref="ref-42",
            business_service_name="orders-api",
            detected_at="2026-07-01T08:00:00Z",
            avoided_downtime_minutes=15,
            confidence_pct=92.0,
        )
        result = _to_prevented(detection, 500.0)
        assert result.incident_ref == "ref-42"
        assert result.business_service_name == "orders-api"
        assert result.detected_at == "2026-07-01T08:00:00Z"
        assert result.avoided_downtime_minutes == 15  # noqa: PLR2004
        assert result.confidence_pct == 92.0  # noqa: PLR2004
        assert result.avoided_cost_eur == 7500.0  # noqa: PLR2004

    def test_zero_minutes(self) -> None:
        detection = _detection(avoided_downtime_minutes=0)
        result = _to_prevented(detection, 1000.0)
        assert result.avoided_cost_eur == 0.0

    def test_zero_revenue(self) -> None:
        detection = _detection(avoided_downtime_minutes=10)
        result = _to_prevented(detection, 0.0)
        assert result.avoided_cost_eur == 0.0


class TestUnconfiguredReport:
    def test_returns_report_with_explanation(self) -> None:
        report = _unconfigured_report(50, 10, "2026-06")
        assert report.period_label == "2026-06"
        assert report.detected_count == 50  # noqa: PLR2004
        assert report.prevented_incident_count == 10  # noqa: PLR2004
        assert report.config_available is False
        assert "revenue_per_minute" in report.explanation

    def test_zero_detections(self) -> None:
        report = _unconfigured_report(0, 0, "2026-01")
        assert report.detected_count == 0
        assert report.prevented_incident_count == 0

    def test_no_revenue_fields_are_none(self) -> None:
        report = _unconfigured_report(10, 3, "2026-06")
        assert report.total_avoided_cost_eur is None
        assert report.roi_eur is None


class TestComputePredictionRoi:
    def test_unconfigured_when_no_revenue(self) -> None:
        detections = [_detection()]
        data: PredictionRoiData = {
            "detections": detections,
            "infrastructure_cost_eur": 1000.0,
            "revenue_per_minute": None,
        }
        report = compute_prediction_roi(data, "2026-06")
        assert report.config_available is False
        assert report.detected_count == 1
        assert report.prevented_incident_count == 1

    def test_configured_with_revenue(self) -> None:
        detections = [
            _detection(incident_ref="inc-1", avoided_downtime_minutes=30),
            _detection(incident_ref="inc-2", avoided_downtime_minutes=15),
        ]
        data: PredictionRoiData = {
            "detections": detections,
            "infrastructure_cost_eur": 5000.0,
            "revenue_per_minute": 1000.0,
        }
        report = compute_prediction_roi(data, "2026-06")
        assert report.config_available is True
        assert report.detected_count == 2  # noqa: PLR2004
        assert report.prevented_incident_count == 2  # noqa: PLR2004
        assert report.total_avoided_cost_eur == 45000.0  # noqa: PLR2004
        assert report.avoided_downtime_minutes == 45  # noqa: PLR2004
        assert report.infrastructure_cost_eur == 5000.0  # noqa: PLR2004
        assert report.roi_eur == 40000.0  # noqa: PLR2004

    def test_only_prevented_counted(self) -> None:
        detections = [
            _detection(incident_ref="inc-1", prevented=True),
            _detection(incident_ref="inc-2", prevented=False),
            _detection(incident_ref="inc-3", prevented=False),
        ]
        data: PredictionRoiData = {
            "detections": detections,
            "infrastructure_cost_eur": 0.0,
            "revenue_per_minute": 100.0,
        }
        report = compute_prediction_roi(data, "2026-06")
        assert report.detected_count == 3  # noqa: PLR2004
        assert report.prevented_incident_count == 1

    def test_period_label_preserved(self) -> None:
        data: PredictionRoiData = {
            "detections": [],
            "infrastructure_cost_eur": 0.0,
            "revenue_per_minute": None,
        }
        report = compute_prediction_roi(data, "Q2-2026")
        assert report.period_label == "Q2-2026"

    def test_empty_detections(self) -> None:
        data: PredictionRoiData = {
            "detections": [],
            "infrastructure_cost_eur": 500.0,
            "revenue_per_minute": 1000.0,
        }
        report = compute_prediction_roi(data, "2026-07")
        assert report.detected_count == 0
        assert report.prevented_incident_count == 0
        assert report.total_avoided_cost_eur == 0.0

    def test_negative_roi_possible(self) -> None:
        detections = [_detection(avoided_downtime_minutes=1)]
        data: PredictionRoiData = {
            "detections": detections,
            "infrastructure_cost_eur": 10000.0,
            "revenue_per_minute": 1000.0,
        }
        report = compute_prediction_roi(data, "2026-06")
        assert report.roi_eur == -9000.0  # noqa: PLR2004


class TestExactPayloads:
    def test_configured_report_full_payload(self) -> None:
        data: PredictionRoiData = {
            "revenue_per_minute": 0.05,
            "detections": [
                {
                    "incident_ref": "INC-1",
                    "business_service_name": "pay",
                    "detected_at": "2026-07-01T10:00:00Z",
                    "avoided_downtime_minutes": 33,
                    "confidence_pct": 80.0,
                    "prevented": True,
                },
                {
                    "incident_ref": "INC-2",
                    "business_service_name": "auth",
                    "detected_at": "2026-07-02T11:00:00Z",
                    "avoided_downtime_minutes": 10,
                    "confidence_pct": 60.0,
                    "prevented": True,
                },
                {
                    "incident_ref": "INC-3",
                    "business_service_name": "web",
                    "detected_at": "2026-07-03T12:00:00Z",
                    "avoided_downtime_minutes": 5,
                    "confidence_pct": 70.0,
                    "prevented": False,
                },
            ],
            "infrastructure_cost_eur": 2.123,
        }

        report = compute_prediction_roi(data, "2026-07")

        assert report == PredictionRoiReport(
            period_label="2026-07",
            detected_count=3,
            prevented_incident_count=2,
            avoided_downtime_minutes=43,
            total_avoided_cost_eur=2.15,
            infrastructure_cost_eur=2.123,
            roi_eur=0.03,
            prevented_incidents=[
                PreventedIncident(
                    incident_ref="INC-1",
                    business_service_name="pay",
                    detected_at="2026-07-01T10:00:00Z",
                    avoided_downtime_minutes=33,
                    confidence_pct=80.0,
                    avoided_cost_eur=1.65,
                ),
                PreventedIncident(
                    incident_ref="INC-2",
                    business_service_name="auth",
                    detected_at="2026-07-02T11:00:00Z",
                    avoided_downtime_minutes=10,
                    confidence_pct=60.0,
                    avoided_cost_eur=0.5,
                ),
            ],
            config_available=True,
            explanation="",
        )

    def test_unconfigured_report_full_payload(self) -> None:
        data: PredictionRoiData = {
            "revenue_per_minute": None,
            "detections": [
                {
                    "incident_ref": "INC-1",
                    "business_service_name": "pay",
                    "detected_at": "2026-07-01T10:00:00Z",
                    "avoided_downtime_minutes": 33,
                    "confidence_pct": 80.0,
                    "prevented": True,
                },
                {
                    "incident_ref": "INC-2",
                    "business_service_name": "auth",
                    "detected_at": "2026-07-02T11:00:00Z",
                    "avoided_downtime_minutes": 10,
                    "confidence_pct": 60.0,
                    "prevented": False,
                },
            ],
            "infrastructure_cost_eur": 1.0,
        }

        report = compute_prediction_roi(data, "2026-07")

        assert report == PredictionRoiReport(
            period_label="2026-07",
            detected_count=2,
            prevented_incident_count=1,
            avoided_downtime_minutes=0,
            total_avoided_cost_eur=None,
            infrastructure_cost_eur=0.0,
            roi_eur=None,
            prevented_incidents=[],
            config_available=False,
            explanation=(
                "2 saturations detectees dont 1 incidents evites. Configurez "
                "'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
            ),
        )

    def test_avoided_cost_rounds_to_two_decimals(self) -> None:
        detection = _detection(avoided_downtime_minutes=31)
        result = _to_prevented(detection, 0.055)

        assert result.avoided_cost_eur == 1.71  # noqa: PLR2004
