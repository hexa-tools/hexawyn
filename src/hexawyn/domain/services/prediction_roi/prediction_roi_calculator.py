from __future__ import annotations

from hexawyn.application.ports.driven.prediction_roi_port import (
    PredictionRoiData,
    PreventedIncidentRaw,
)
from hexawyn.domain.models.prediction_roi import (
    PredictionRoiReport,
    PreventedIncident,
)


def compute_prediction_roi(data: PredictionRoiData, period: str) -> PredictionRoiReport:
    """Compute the ROI of prediction-based prevention.

    Only detections flagged ``prevented`` back a reported saving, and each
    saving is traceable to its historical event reference. Without
    ``revenue_per_minute`` no avoided-cost figure is produced.
    """
    revenue = data["revenue_per_minute"]
    detections = data["detections"]
    prevented = [detection for detection in detections if detection["prevented"]]
    detected_count = len(detections)

    if revenue is None:
        return _unconfigured_report(detected_count, len(prevented), period)

    prevented_items = [_to_prevented(detection, revenue) for detection in prevented]
    total_avoided = sum(item.avoided_cost_eur for item in prevented_items)
    total_downtime = sum(item.avoided_downtime_minutes for item in prevented_items)
    infra = data["infrastructure_cost_eur"]
    roi = round(total_avoided - infra, 2)

    return PredictionRoiReport(
        period_label=period,
        detected_count=detected_count,
        prevented_incident_count=len(prevented_items),
        avoided_downtime_minutes=total_downtime,
        total_avoided_cost_eur=total_avoided,
        infrastructure_cost_eur=infra,
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def _unconfigured_report(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = (
        f"{detected} saturations detectees dont {prevented} incidents evites. "
        f"Configurez 'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
    )
    return PredictionRoiReport(
        period_label=period,
        detected_count=detected,
        prevented_incident_count=prevented,
        config_available=False,
        explanation=explanation,
    )


def _to_prevented(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )
