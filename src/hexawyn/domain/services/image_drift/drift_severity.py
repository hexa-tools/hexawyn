from __future__ import annotations

from hexawyn.domain.models.image_drift import DriftType, ImageDriftSeverity


def classify_severity(drift_type: DriftType) -> ImageDriftSeverity:
    return "critical"
