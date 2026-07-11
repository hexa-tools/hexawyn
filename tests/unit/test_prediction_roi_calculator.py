from __future__ import annotations

from hexawyn.application.ports.driven.prediction_roi_port import (
    PredictionRoiData,
    PreventedIncidentRaw,
)


def _detection(
    ref: str = "PRED-1",
    downtime: int = 120,
    confidence: float = 90.0,
    prevented: bool = True,
    service: str = "Service Paiement",
) -> PreventedIncidentRaw:
    return PreventedIncidentRaw(
        incident_ref=ref,
        business_service_name=service,
        detected_at="2026-06-10",
        avoided_downtime_minutes=downtime,
        confidence_pct=confidence,
        prevented=prevented,
    )


def _data(
    detections: list[PreventedIncidentRaw] | None = None,
    infra_cost: float = 2000.0,
    revenue: float | None = 500.0,
) -> PredictionRoiData:
    return PredictionRoiData(
        detections=detections if detections is not None else [],
        infrastructure_cost_eur=infra_cost,
        revenue_per_minute=revenue,
    )


class TestAvoidedCost:
    def test_prevented_incident_avoided_cost(self) -> None:
        from hexawyn.domain.services.prediction_roi.prediction_roi_calculator import (
            compute_prediction_roi,
        )

        # 120 min avoided x 500/min = 60 000 €.
        report = compute_prediction_roi(
            _data(detections=[_detection(downtime=120)], revenue=500.0), period="2026-06"
        )

        assert report.total_avoided_cost_eur == 60000.0
        assert report.prevented_incidents[0].avoided_cost_eur == 60000.0

    def test_detected_vs_prevented_counts(self) -> None:
        from hexawyn.domain.services.prediction_roi.prediction_roi_calculator import (
            compute_prediction_roi,
        )

        report = compute_prediction_roi(
            _data(
                detections=[
                    _detection("a", prevented=True),
                    _detection("b", prevented=False),
                    _detection("c", prevented=False),
                    _detection("d", prevented=False),
                ]
            ),
            period="2026-06",
        )

        assert report.detected_count == 4
        assert report.prevented_incident_count == 1


class TestRoi:
    def test_roi_is_avoided_minus_infra(self) -> None:
        from hexawyn.domain.services.prediction_roi.prediction_roi_calculator import (
            compute_prediction_roi,
        )

        report = compute_prediction_roi(
            _data(detections=[_detection(downtime=120)], infra_cost=2000.0, revenue=500.0),
            period="2026-06",
        )

        assert report.roi_eur == 60000.0 - 2000.0


class TestTraceability:
    def test_only_prevented_detections_back_savings(self) -> None:
        from hexawyn.domain.services.prediction_roi.prediction_roi_calculator import (
            compute_prediction_roi,
        )

        report = compute_prediction_roi(
            _data(
                detections=[
                    _detection("a", downtime=100, prevented=True),
                    _detection("b", prevented=False),
                ]
            ),
            period="2026-06",
        )

        assert len(report.prevented_incidents) == 1
        assert report.prevented_incidents[0].incident_ref == "a"

    def test_no_prevented_incidents_zero_avoided(self) -> None:
        from hexawyn.domain.services.prediction_roi.prediction_roi_calculator import (
            compute_prediction_roi,
        )

        report = compute_prediction_roi(
            _data(detections=[_detection(prevented=False)], revenue=500.0), period="2026-06"
        )

        assert report.total_avoided_cost_eur == 0.0
        assert report.prevented_incidents == []


class TestMissingConfig:
    def test_no_revenue_no_euro_amount(self) -> None:
        from hexawyn.domain.services.prediction_roi.prediction_roi_calculator import (
            compute_prediction_roi,
        )

        report = compute_prediction_roi(
            _data(detections=[_detection(downtime=120)], revenue=None), period="2026-06"
        )

        assert report.config_available is False
        assert report.total_avoided_cost_eur is None
        assert report.roi_eur is None

    def test_no_revenue_returns_explanation_and_counts(self) -> None:
        from hexawyn.domain.services.prediction_roi.prediction_roi_calculator import (
            compute_prediction_roi,
        )

        report = compute_prediction_roi(
            _data(
                detections=[_detection(prevented=True), _detection("b", prevented=False)],
                revenue=None,
            ),
            period="2026-06",
        )

        assert "revenue_per_minute" in report.explanation
        assert report.detected_count == 2
        assert report.prevented_incident_count == 1
