import statistics
from dataclasses import dataclass, field

from hexawyn.domain.models.constants import EventAnalysisConstants

_cfg = EventAnalysisConstants()


@dataclass
class AnomalyDetectionResult:
    """Output of a statistical anomaly detection run."""

    anomalies_detected: bool = False
    anomaly_count: int = 0
    anomalies: list[dict[str, float | int | str]] = field(default_factory=list)
    threshold: float = _cfg.temporal_anomaly_zscore_threshold
    mean: float = 0.0
    std_dev: float = 0.0


class ZScoreAnomalyDetector:
    """Detects anomalies using Z-score method on a univariate data series.

    Z-score = |value - mean| / std_dev. Values exceeding the threshold
    are flagged as anomalies. Requires at least min_data_points samples.
    """

    def __init__(
        self,
        threshold: float | None = None,
        min_data_points: int | None = None,
    ) -> None:
        self.threshold = threshold or _cfg.temporal_anomaly_zscore_threshold
        self.min_data_points = min_data_points or _cfg.min_data_points_for_anomaly

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
