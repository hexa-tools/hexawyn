from __future__ import annotations

from hexawyn.application.ports.driven.prediction_roi_port import (
    PredictionRoiData,
)
from hexawyn.infrastructure.config.config_manager import load_config


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut: MutantDict = {}  # type: ignore


class ConfigPredictionRoiSource:
    @_mutmut_mutated(mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut)
    def fetch_prediction_roi_data(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_orig(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_1(self, period: str) -> PredictionRoiData:
        config = None
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_2(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = None
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_3(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get(None)
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_4(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("XXbusinessXX")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_5(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("BUSINESS")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_6(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = ""
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_7(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = None
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_8(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(None)
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_9(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get(None))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_10(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("XXrevenue_per_minuteXX"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_11(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("REVENUE_PER_MINUTE"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_12(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=None,
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_13(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=None,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_14(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            revenue_per_minute=None,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_15(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            infrastructure_cost_eur=0.0,
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_16(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            revenue_per_minute=revenue,
        )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_17(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=0.0,
            )
    def xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_18(self, period: str) -> PredictionRoiData:
        config = load_config()
        business = config.get("business")
        revenue: float | None = None
        if isinstance(business, dict):
            revenue = _as_float(business.get("revenue_per_minute"))
        return PredictionRoiData(
            detections=[],
            infrastructure_cost_eur=1.0,
            revenue_per_minute=revenue,
        )

mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['_mutmut_orig'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_1'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_2'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_3'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_4'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_5'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_6'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_7'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_8'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_9'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_10'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_11'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_11 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_12'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_12 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_13'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_13 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_14'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_14 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_15'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_15 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_16'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_16 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_17'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_17 # type: ignore # mutmut generated
mutants_xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut['xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_18'] = ConfigPredictionRoiSource.xǁConfigPredictionRoiSourceǁfetch_prediction_roi_data__mutmut_18 # type: ignore # mutmut generated
mutants_x__as_float__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_float__mutmut)
def _as_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value)
    return None


def x__as_float__mutmut_orig(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value)
    return None


def x__as_float__mutmut_1(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(None)
    return None

mutants_x__as_float__mutmut['_mutmut_orig'] = x__as_float__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_1'] = x__as_float__mutmut_1 # type: ignore # mutmut generated
