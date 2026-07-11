from abc import ABC, abstractmethod
from typing import TypedDict


class PreventedIncidentRaw(TypedDict):
    incident_ref: str
    business_service_name: str
    detected_at: str
    avoided_downtime_minutes: int
    confidence_pct: float
    prevented: bool


class PredictionRoiData(TypedDict):
    detections: list[PreventedIncidentRaw]
    infrastructure_cost_eur: float
    revenue_per_minute: float | None


class PredictionRoiPort(ABC):
    """Driven port — provides the prediction detections for a period (each
    traceable to a historical event), the infrastructure cost, and the
    configured revenue per minute.

    ``revenue_per_minute`` is None when pricing is not configured, so the domain
    never fabricates an avoided-cost figure. Only detections flagged
    ``prevented`` back a reported saving.
    """

    @abstractmethod
    def get_prediction_roi_data(self, period: str) -> PredictionRoiData:
        """Return the ROI inputs for *period* (e.g. ``"2026-06"``).

        Raises ClusterUnreachableError on data-source failures.
        """
