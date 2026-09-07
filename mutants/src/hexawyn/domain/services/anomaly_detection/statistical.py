import statistics
from dataclasses import dataclass, field

from hexawyn.domain.models.constants import EventAnalysisConstants

_cfg = EventAnalysisConstants()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class AnomalyDetectionResult:
    """Output of a statistical anomaly detection run."""

    anomalies_detected: bool = False
    anomaly_count: int = 0
    anomalies: list[dict[str, float | int | str]] = field(default_factory=list)
    threshold: float = _cfg.temporal_anomaly_zscore_threshold
    mean: float = 0.0
    std_dev: float = 0.0
mutants_xǁZScoreAnomalyDetectorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut: MutantDict = {}  # type: ignore


class ZScoreAnomalyDetector:
    """Detects anomalies using Z-score method on a univariate data series.

    Z-score = |value - mean| / std_dev. Values exceeding the threshold
    are flagged as anomalies. Requires at least min_data_points samples.
    """

    @_mutmut_mutated(mutants_xǁZScoreAnomalyDetectorǁ__init____mutmut)
    def __init__(
        self,
        threshold: float | None = None,
        min_data_points: int | None = None,
    ) -> None:
        self.threshold = threshold or _cfg.temporal_anomaly_zscore_threshold
        self.min_data_points = min_data_points or _cfg.min_data_points_for_anomaly

    def xǁZScoreAnomalyDetectorǁ__init____mutmut_orig(
        self,
        threshold: float | None = None,
        min_data_points: int | None = None,
    ) -> None:
        self.threshold = threshold or _cfg.temporal_anomaly_zscore_threshold
        self.min_data_points = min_data_points or _cfg.min_data_points_for_anomaly

    def xǁZScoreAnomalyDetectorǁ__init____mutmut_1(
        self,
        threshold: float | None = None,
        min_data_points: int | None = None,
    ) -> None:
        self.threshold = None
        self.min_data_points = min_data_points or _cfg.min_data_points_for_anomaly

    def xǁZScoreAnomalyDetectorǁ__init____mutmut_2(
        self,
        threshold: float | None = None,
        min_data_points: int | None = None,
    ) -> None:
        self.threshold = threshold and _cfg.temporal_anomaly_zscore_threshold
        self.min_data_points = min_data_points or _cfg.min_data_points_for_anomaly

    def xǁZScoreAnomalyDetectorǁ__init____mutmut_3(
        self,
        threshold: float | None = None,
        min_data_points: int | None = None,
    ) -> None:
        self.threshold = threshold or _cfg.temporal_anomaly_zscore_threshold
        self.min_data_points = None

    def xǁZScoreAnomalyDetectorǁ__init____mutmut_4(
        self,
        threshold: float | None = None,
        min_data_points: int | None = None,
    ) -> None:
        self.threshold = threshold or _cfg.temporal_anomaly_zscore_threshold
        self.min_data_points = min_data_points and _cfg.min_data_points_for_anomaly

    @_mutmut_mutated(mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut)
    def detect(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_orig(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_1(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) <= self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_2(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=None,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_3(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=None,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_4(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_5(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_6(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=True,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_7(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = None
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_8(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(None)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_9(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = None

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_10(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(None) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_11(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) >= 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_12(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 2 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_13(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 1.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_14(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev != 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_15(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 1.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_16(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=None,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_17(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=None,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_18(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=None,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_19(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=None,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_20(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_21(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_22(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_23(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_24(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=True,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_25(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = None
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_26(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(None):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_27(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = None
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_28(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) * std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_29(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(None) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_30(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value + mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_31(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score >= self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_32(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = None
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_33(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "XXindexXX": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_34(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "INDEX": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_35(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "XXvalueXX": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_36(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "VALUE": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_37(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "XXz_scoreXX": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_38(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "Z_SCORE": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_39(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(None, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_40(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, None),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_41(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_42(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, ),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_43(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 5),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_44(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context or i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_45(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i <= len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_46(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = None
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_47(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["XXcontextXX"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_48(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["CONTEXT"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_49(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(None)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_50(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=None,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_51(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=None,
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_52(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=None,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_53(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=None,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_54(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=None,
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_55(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=None,
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_56(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_57(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_58(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_59(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_60(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_61(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_62(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) >= 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_63(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 1,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_64(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(None, 4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_65(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, None),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_66(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(4),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_67(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, ),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_68(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 5),
            std_dev=round(std_dev, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_69(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(None, 4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_70(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, None),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_71(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(4),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_72(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, ),
        )

    def xǁZScoreAnomalyDetectorǁdetect__mutmut_73(
        self,
        data_points: list[float],
        context: list[str] | None = None,
    ) -> AnomalyDetectionResult:
        if len(data_points) < self.min_data_points:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
            )

        mean_val = statistics.mean(data_points)
        std_dev = statistics.stdev(data_points) if len(data_points) > 1 else 0.0

        if std_dev == 0.0:
            return AnomalyDetectionResult(
                anomalies_detected=False,
                threshold=self.threshold,
                mean=mean_val,
                std_dev=std_dev,
            )

        anomalies: list[dict[str, float | int | str]] = []
        for i, value in enumerate(data_points):
            z_score = abs(value - mean_val) / std_dev
            if z_score > self.threshold:
                entry: dict[str, float | int | str] = {
                    "index": i,
                    "value": value,
                    "z_score": round(z_score, 4),
                }
                if context and i < len(context):
                    entry["context"] = context[i]
                anomalies.append(entry)

        return AnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
            threshold=self.threshold,
            mean=round(mean_val, 4),
            std_dev=round(std_dev, 5),
        )

mutants_xǁZScoreAnomalyDetectorǁ__init____mutmut['_mutmut_orig'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁ__init____mutmut['xǁZScoreAnomalyDetectorǁ__init____mutmut_1'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁ__init____mutmut['xǁZScoreAnomalyDetectorǁ__init____mutmut_2'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁ__init____mutmut['xǁZScoreAnomalyDetectorǁ__init____mutmut_3'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁ__init____mutmut['xǁZScoreAnomalyDetectorǁ__init____mutmut_4'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['_mutmut_orig'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_1'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_2'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_3'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_4'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_5'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_6'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_7'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_7 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_8'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_8 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_9'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_9 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_10'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_10 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_11'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_11 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_12'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_12 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_13'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_13 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_14'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_14 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_15'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_15 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_16'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_16 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_17'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_17 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_18'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_18 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_19'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_19 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_20'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_20 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_21'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_21 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_22'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_22 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_23'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_23 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_24'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_24 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_25'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_25 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_26'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_26 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_27'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_27 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_28'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_28 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_29'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_29 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_30'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_30 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_31'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_31 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_32'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_32 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_33'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_33 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_34'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_34 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_35'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_35 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_36'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_36 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_37'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_37 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_38'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_38 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_39'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_39 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_40'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_40 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_41'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_41 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_42'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_42 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_43'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_43 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_44'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_44 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_45'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_45 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_46'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_46 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_47'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_47 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_48'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_48 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_49'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_49 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_50'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_50 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_51'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_51 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_52'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_52 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_53'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_53 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_54'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_54 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_55'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_55 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_56'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_56 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_57'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_57 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_58'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_58 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_59'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_59 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_60'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_60 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_61'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_61 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_62'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_62 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_63'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_63 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_64'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_64 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_65'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_65 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_66'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_66 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_67'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_67 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_68'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_68 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_69'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_69 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_70'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_70 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_71'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_71 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_72'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_72 # type: ignore # mutmut generated
mutants_xǁZScoreAnomalyDetectorǁdetect__mutmut['xǁZScoreAnomalyDetectorǁdetect__mutmut_73'] = ZScoreAnomalyDetector.xǁZScoreAnomalyDetectorǁdetect__mutmut_73 # type: ignore # mutmut generated
