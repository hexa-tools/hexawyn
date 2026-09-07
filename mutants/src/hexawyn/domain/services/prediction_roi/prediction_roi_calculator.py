from __future__ import annotations

from hexawyn.application.ports.driven.prediction_roi_port import (
    PredictionRoiData,
    PreventedIncidentRaw,
)
from hexawyn.domain.models.prediction_roi import (
    PredictionRoiReport,
    PreventedIncident,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_prediction_roi__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_prediction_roi__mutmut)
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


def x_compute_prediction_roi__mutmut_orig(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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


def x_compute_prediction_roi__mutmut_1(data: PredictionRoiData, period: str) -> PredictionRoiReport:
    """Compute the ROI of prediction-based prevention.

    Only detections flagged ``prevented`` back a reported saving, and each
    saving is traceable to its historical event reference. Without
    ``revenue_per_minute`` no avoided-cost figure is produced.
    """
    revenue = None
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


def x_compute_prediction_roi__mutmut_2(data: PredictionRoiData, period: str) -> PredictionRoiReport:
    """Compute the ROI of prediction-based prevention.

    Only detections flagged ``prevented`` back a reported saving, and each
    saving is traceable to its historical event reference. Without
    ``revenue_per_minute`` no avoided-cost figure is produced.
    """
    revenue = data["XXrevenue_per_minuteXX"]
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


def x_compute_prediction_roi__mutmut_3(data: PredictionRoiData, period: str) -> PredictionRoiReport:
    """Compute the ROI of prediction-based prevention.

    Only detections flagged ``prevented`` back a reported saving, and each
    saving is traceable to its historical event reference. Without
    ``revenue_per_minute`` no avoided-cost figure is produced.
    """
    revenue = data["REVENUE_PER_MINUTE"]
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


def x_compute_prediction_roi__mutmut_4(data: PredictionRoiData, period: str) -> PredictionRoiReport:
    """Compute the ROI of prediction-based prevention.

    Only detections flagged ``prevented`` back a reported saving, and each
    saving is traceable to its historical event reference. Without
    ``revenue_per_minute`` no avoided-cost figure is produced.
    """
    revenue = data["revenue_per_minute"]
    detections = None
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


def x_compute_prediction_roi__mutmut_5(data: PredictionRoiData, period: str) -> PredictionRoiReport:
    """Compute the ROI of prediction-based prevention.

    Only detections flagged ``prevented`` back a reported saving, and each
    saving is traceable to its historical event reference. Without
    ``revenue_per_minute`` no avoided-cost figure is produced.
    """
    revenue = data["revenue_per_minute"]
    detections = data["XXdetectionsXX"]
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


def x_compute_prediction_roi__mutmut_6(data: PredictionRoiData, period: str) -> PredictionRoiReport:
    """Compute the ROI of prediction-based prevention.

    Only detections flagged ``prevented`` back a reported saving, and each
    saving is traceable to its historical event reference. Without
    ``revenue_per_minute`` no avoided-cost figure is produced.
    """
    revenue = data["revenue_per_minute"]
    detections = data["DETECTIONS"]
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


def x_compute_prediction_roi__mutmut_7(data: PredictionRoiData, period: str) -> PredictionRoiReport:
    """Compute the ROI of prediction-based prevention.

    Only detections flagged ``prevented`` back a reported saving, and each
    saving is traceable to its historical event reference. Without
    ``revenue_per_minute`` no avoided-cost figure is produced.
    """
    revenue = data["revenue_per_minute"]
    detections = data["detections"]
    prevented = None
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


def x_compute_prediction_roi__mutmut_8(data: PredictionRoiData, period: str) -> PredictionRoiReport:
    """Compute the ROI of prediction-based prevention.

    Only detections flagged ``prevented`` back a reported saving, and each
    saving is traceable to its historical event reference. Without
    ``revenue_per_minute`` no avoided-cost figure is produced.
    """
    revenue = data["revenue_per_minute"]
    detections = data["detections"]
    prevented = [detection for detection in detections if detection["XXpreventedXX"]]
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


def x_compute_prediction_roi__mutmut_9(data: PredictionRoiData, period: str) -> PredictionRoiReport:
    """Compute the ROI of prediction-based prevention.

    Only detections flagged ``prevented`` back a reported saving, and each
    saving is traceable to its historical event reference. Without
    ``revenue_per_minute`` no avoided-cost figure is produced.
    """
    revenue = data["revenue_per_minute"]
    detections = data["detections"]
    prevented = [detection for detection in detections if detection["PREVENTED"]]
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


def x_compute_prediction_roi__mutmut_10(data: PredictionRoiData, period: str) -> PredictionRoiReport:
    """Compute the ROI of prediction-based prevention.

    Only detections flagged ``prevented`` back a reported saving, and each
    saving is traceable to its historical event reference. Without
    ``revenue_per_minute`` no avoided-cost figure is produced.
    """
    revenue = data["revenue_per_minute"]
    detections = data["detections"]
    prevented = [detection for detection in detections if detection["prevented"]]
    detected_count = None

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


def x_compute_prediction_roi__mutmut_11(data: PredictionRoiData, period: str) -> PredictionRoiReport:
    """Compute the ROI of prediction-based prevention.

    Only detections flagged ``prevented`` back a reported saving, and each
    saving is traceable to its historical event reference. Without
    ``revenue_per_minute`` no avoided-cost figure is produced.
    """
    revenue = data["revenue_per_minute"]
    detections = data["detections"]
    prevented = [detection for detection in detections if detection["prevented"]]
    detected_count = len(detections)

    if revenue is not None:
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


def x_compute_prediction_roi__mutmut_12(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        return _unconfigured_report(None, len(prevented), period)

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


def x_compute_prediction_roi__mutmut_13(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        return _unconfigured_report(detected_count, None, period)

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


def x_compute_prediction_roi__mutmut_14(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        return _unconfigured_report(detected_count, len(prevented), None)

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


def x_compute_prediction_roi__mutmut_15(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        return _unconfigured_report(len(prevented), period)

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


def x_compute_prediction_roi__mutmut_16(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        return _unconfigured_report(detected_count, period)

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


def x_compute_prediction_roi__mutmut_17(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        return _unconfigured_report(detected_count, len(prevented), )

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


def x_compute_prediction_roi__mutmut_18(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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

    prevented_items = None
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


def x_compute_prediction_roi__mutmut_19(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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

    prevented_items = [_to_prevented(None, revenue) for detection in prevented]
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


def x_compute_prediction_roi__mutmut_20(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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

    prevented_items = [_to_prevented(detection, None) for detection in prevented]
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


def x_compute_prediction_roi__mutmut_21(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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

    prevented_items = [_to_prevented(revenue) for detection in prevented]
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


def x_compute_prediction_roi__mutmut_22(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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

    prevented_items = [_to_prevented(detection, ) for detection in prevented]
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


def x_compute_prediction_roi__mutmut_23(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    total_avoided = None
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


def x_compute_prediction_roi__mutmut_24(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    total_avoided = sum(None)
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


def x_compute_prediction_roi__mutmut_25(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    total_downtime = None
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


def x_compute_prediction_roi__mutmut_26(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    total_downtime = sum(None)
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


def x_compute_prediction_roi__mutmut_27(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    infra = None
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


def x_compute_prediction_roi__mutmut_28(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    infra = data["XXinfrastructure_cost_eurXX"]
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


def x_compute_prediction_roi__mutmut_29(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    infra = data["INFRASTRUCTURE_COST_EUR"]
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


def x_compute_prediction_roi__mutmut_30(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    roi = None

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


def x_compute_prediction_roi__mutmut_31(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    roi = round(None, 2)

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


def x_compute_prediction_roi__mutmut_32(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    roi = round(total_avoided - infra, None)

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


def x_compute_prediction_roi__mutmut_33(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    roi = round(2)

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


def x_compute_prediction_roi__mutmut_34(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    roi = round(total_avoided - infra, )

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


def x_compute_prediction_roi__mutmut_35(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    roi = round(total_avoided + infra, 2)

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


def x_compute_prediction_roi__mutmut_36(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
    roi = round(total_avoided - infra, 3)

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


def x_compute_prediction_roi__mutmut_37(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        period_label=None,
        detected_count=detected_count,
        prevented_incident_count=len(prevented_items),
        avoided_downtime_minutes=total_downtime,
        total_avoided_cost_eur=total_avoided,
        infrastructure_cost_eur=infra,
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_38(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        detected_count=None,
        prevented_incident_count=len(prevented_items),
        avoided_downtime_minutes=total_downtime,
        total_avoided_cost_eur=total_avoided,
        infrastructure_cost_eur=infra,
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_39(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        prevented_incident_count=None,
        avoided_downtime_minutes=total_downtime,
        total_avoided_cost_eur=total_avoided,
        infrastructure_cost_eur=infra,
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_40(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        avoided_downtime_minutes=None,
        total_avoided_cost_eur=total_avoided,
        infrastructure_cost_eur=infra,
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_41(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        total_avoided_cost_eur=None,
        infrastructure_cost_eur=infra,
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_42(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        infrastructure_cost_eur=None,
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_43(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        roi_eur=None,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_44(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        prevented_incidents=None,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_45(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        config_available=None,
    )


def x_compute_prediction_roi__mutmut_46(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        detected_count=detected_count,
        prevented_incident_count=len(prevented_items),
        avoided_downtime_minutes=total_downtime,
        total_avoided_cost_eur=total_avoided,
        infrastructure_cost_eur=infra,
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_47(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        prevented_incident_count=len(prevented_items),
        avoided_downtime_minutes=total_downtime,
        total_avoided_cost_eur=total_avoided,
        infrastructure_cost_eur=infra,
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_48(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        avoided_downtime_minutes=total_downtime,
        total_avoided_cost_eur=total_avoided,
        infrastructure_cost_eur=infra,
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_49(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        total_avoided_cost_eur=total_avoided,
        infrastructure_cost_eur=infra,
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_50(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        infrastructure_cost_eur=infra,
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_51(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        roi_eur=roi,
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_52(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        prevented_incidents=prevented_items,
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_53(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        config_available=True,
    )


def x_compute_prediction_roi__mutmut_54(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        )


def x_compute_prediction_roi__mutmut_55(data: PredictionRoiData, period: str) -> PredictionRoiReport:
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
        config_available=False,
    )

mutants_x_compute_prediction_roi__mutmut['_mutmut_orig'] = x_compute_prediction_roi__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_1'] = x_compute_prediction_roi__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_2'] = x_compute_prediction_roi__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_3'] = x_compute_prediction_roi__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_4'] = x_compute_prediction_roi__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_5'] = x_compute_prediction_roi__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_6'] = x_compute_prediction_roi__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_7'] = x_compute_prediction_roi__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_8'] = x_compute_prediction_roi__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_9'] = x_compute_prediction_roi__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_10'] = x_compute_prediction_roi__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_11'] = x_compute_prediction_roi__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_12'] = x_compute_prediction_roi__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_13'] = x_compute_prediction_roi__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_14'] = x_compute_prediction_roi__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_15'] = x_compute_prediction_roi__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_16'] = x_compute_prediction_roi__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_17'] = x_compute_prediction_roi__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_18'] = x_compute_prediction_roi__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_19'] = x_compute_prediction_roi__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_20'] = x_compute_prediction_roi__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_21'] = x_compute_prediction_roi__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_22'] = x_compute_prediction_roi__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_23'] = x_compute_prediction_roi__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_24'] = x_compute_prediction_roi__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_25'] = x_compute_prediction_roi__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_26'] = x_compute_prediction_roi__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_27'] = x_compute_prediction_roi__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_28'] = x_compute_prediction_roi__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_29'] = x_compute_prediction_roi__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_30'] = x_compute_prediction_roi__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_31'] = x_compute_prediction_roi__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_32'] = x_compute_prediction_roi__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_33'] = x_compute_prediction_roi__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_34'] = x_compute_prediction_roi__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_35'] = x_compute_prediction_roi__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_36'] = x_compute_prediction_roi__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_37'] = x_compute_prediction_roi__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_38'] = x_compute_prediction_roi__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_39'] = x_compute_prediction_roi__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_40'] = x_compute_prediction_roi__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_41'] = x_compute_prediction_roi__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_42'] = x_compute_prediction_roi__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_43'] = x_compute_prediction_roi__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_44'] = x_compute_prediction_roi__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_45'] = x_compute_prediction_roi__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_46'] = x_compute_prediction_roi__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_47'] = x_compute_prediction_roi__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_48'] = x_compute_prediction_roi__mutmut_48 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_49'] = x_compute_prediction_roi__mutmut_49 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_50'] = x_compute_prediction_roi__mutmut_50 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_51'] = x_compute_prediction_roi__mutmut_51 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_52'] = x_compute_prediction_roi__mutmut_52 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_53'] = x_compute_prediction_roi__mutmut_53 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_54'] = x_compute_prediction_roi__mutmut_54 # type: ignore # mutmut generated
mutants_x_compute_prediction_roi__mutmut['x_compute_prediction_roi__mutmut_55'] = x_compute_prediction_roi__mutmut_55 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__unconfigured_report__mutmut)
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


def x__unconfigured_report__mutmut_orig(detected: int, prevented: int, period: str) -> PredictionRoiReport:
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


def x__unconfigured_report__mutmut_1(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = None
    return PredictionRoiReport(
        period_label=period,
        detected_count=detected,
        prevented_incident_count=prevented,
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_2(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = (
        f"{detected} saturations detectees dont {prevented} incidents evites. "
        f"Configurez 'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
    )
    return PredictionRoiReport(
        period_label=None,
        detected_count=detected,
        prevented_incident_count=prevented,
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_3(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = (
        f"{detected} saturations detectees dont {prevented} incidents evites. "
        f"Configurez 'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
    )
    return PredictionRoiReport(
        period_label=period,
        detected_count=None,
        prevented_incident_count=prevented,
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_4(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = (
        f"{detected} saturations detectees dont {prevented} incidents evites. "
        f"Configurez 'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
    )
    return PredictionRoiReport(
        period_label=period,
        detected_count=detected,
        prevented_incident_count=None,
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_5(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = (
        f"{detected} saturations detectees dont {prevented} incidents evites. "
        f"Configurez 'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
    )
    return PredictionRoiReport(
        period_label=period,
        detected_count=detected,
        prevented_incident_count=prevented,
        config_available=None,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_6(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = (
        f"{detected} saturations detectees dont {prevented} incidents evites. "
        f"Configurez 'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
    )
    return PredictionRoiReport(
        period_label=period,
        detected_count=detected,
        prevented_incident_count=prevented,
        config_available=False,
        explanation=None,
    )


def x__unconfigured_report__mutmut_7(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = (
        f"{detected} saturations detectees dont {prevented} incidents evites. "
        f"Configurez 'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
    )
    return PredictionRoiReport(
        detected_count=detected,
        prevented_incident_count=prevented,
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_8(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = (
        f"{detected} saturations detectees dont {prevented} incidents evites. "
        f"Configurez 'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
    )
    return PredictionRoiReport(
        period_label=period,
        prevented_incident_count=prevented,
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_9(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = (
        f"{detected} saturations detectees dont {prevented} incidents evites. "
        f"Configurez 'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
    )
    return PredictionRoiReport(
        period_label=period,
        detected_count=detected,
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_10(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = (
        f"{detected} saturations detectees dont {prevented} incidents evites. "
        f"Configurez 'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
    )
    return PredictionRoiReport(
        period_label=period,
        detected_count=detected,
        prevented_incident_count=prevented,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_11(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = (
        f"{detected} saturations detectees dont {prevented} incidents evites. "
        f"Configurez 'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
    )
    return PredictionRoiReport(
        period_label=period,
        detected_count=detected,
        prevented_incident_count=prevented,
        config_available=False,
        )


def x__unconfigured_report__mutmut_12(detected: int, prevented: int, period: str) -> PredictionRoiReport:
    explanation = (
        f"{detected} saturations detectees dont {prevented} incidents evites. "
        f"Configurez 'revenue_per_minute' pour obtenir l'estimation des pertes evitees."
    )
    return PredictionRoiReport(
        period_label=period,
        detected_count=detected,
        prevented_incident_count=prevented,
        config_available=True,
        explanation=explanation,
    )

mutants_x__unconfigured_report__mutmut['_mutmut_orig'] = x__unconfigured_report__mutmut_orig # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_1'] = x__unconfigured_report__mutmut_1 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_2'] = x__unconfigured_report__mutmut_2 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_3'] = x__unconfigured_report__mutmut_3 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_4'] = x__unconfigured_report__mutmut_4 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_5'] = x__unconfigured_report__mutmut_5 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_6'] = x__unconfigured_report__mutmut_6 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_7'] = x__unconfigured_report__mutmut_7 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_8'] = x__unconfigured_report__mutmut_8 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_9'] = x__unconfigured_report__mutmut_9 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_10'] = x__unconfigured_report__mutmut_10 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_11'] = x__unconfigured_report__mutmut_11 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_12'] = x__unconfigured_report__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_prevented__mutmut)
def _to_prevented(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_orig(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_1(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=None,
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_2(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=None,
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_3(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=None,
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_4(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=None,
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_5(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=None,
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_6(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=None,
    )


def x__to_prevented__mutmut_7(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_8(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_9(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_10(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_11(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_12(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        )


def x__to_prevented__mutmut_13(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["XXincident_refXX"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_14(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["INCIDENT_REF"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_15(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["XXbusiness_service_nameXX"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_16(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["BUSINESS_SERVICE_NAME"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_17(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["XXdetected_atXX"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_18(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["DETECTED_AT"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_19(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["XXavoided_downtime_minutesXX"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_20(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["AVOIDED_DOWNTIME_MINUTES"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_21(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["XXconfidence_pctXX"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_22(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["CONFIDENCE_PCT"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 2),
    )


def x__to_prevented__mutmut_23(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(None, 2),
    )


def x__to_prevented__mutmut_24(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, None),
    )


def x__to_prevented__mutmut_25(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(2),
    )


def x__to_prevented__mutmut_26(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, ),
    )


def x__to_prevented__mutmut_27(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] / revenue, 2),
    )


def x__to_prevented__mutmut_28(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["XXavoided_downtime_minutesXX"] * revenue, 2),
    )


def x__to_prevented__mutmut_29(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["AVOIDED_DOWNTIME_MINUTES"] * revenue, 2),
    )


def x__to_prevented__mutmut_30(detection: PreventedIncidentRaw, revenue: float) -> PreventedIncident:
    return PreventedIncident(
        incident_ref=detection["incident_ref"],
        business_service_name=detection["business_service_name"],
        detected_at=detection["detected_at"],
        avoided_downtime_minutes=detection["avoided_downtime_minutes"],
        confidence_pct=detection["confidence_pct"],
        avoided_cost_eur=round(detection["avoided_downtime_minutes"] * revenue, 3),
    )

mutants_x__to_prevented__mutmut['_mutmut_orig'] = x__to_prevented__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_1'] = x__to_prevented__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_2'] = x__to_prevented__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_3'] = x__to_prevented__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_4'] = x__to_prevented__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_5'] = x__to_prevented__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_6'] = x__to_prevented__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_7'] = x__to_prevented__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_8'] = x__to_prevented__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_9'] = x__to_prevented__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_10'] = x__to_prevented__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_11'] = x__to_prevented__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_12'] = x__to_prevented__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_13'] = x__to_prevented__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_14'] = x__to_prevented__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_15'] = x__to_prevented__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_16'] = x__to_prevented__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_17'] = x__to_prevented__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_18'] = x__to_prevented__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_19'] = x__to_prevented__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_20'] = x__to_prevented__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_21'] = x__to_prevented__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_22'] = x__to_prevented__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_23'] = x__to_prevented__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_24'] = x__to_prevented__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_25'] = x__to_prevented__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_26'] = x__to_prevented__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_27'] = x__to_prevented__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_28'] = x__to_prevented__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_29'] = x__to_prevented__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_prevented__mutmut['x__to_prevented__mutmut_30'] = x__to_prevented__mutmut_30 # type: ignore # mutmut generated
