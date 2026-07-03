from dataclasses import dataclass, field

import numpy as np
from hexawyn.domain.models.constants import LogAnomalyDetectionConstants
from hexawyn.domain.services.anomaly_detection.log_features import extract_log_features
from sklearn.ensemble import IsolationForest

_cfg = LogAnomalyDetectionConstants()


@dataclass
class MLAnomalyDetectionResult:
    """Output of an Isolation Forest semantic anomaly detection run."""

    anomalies_detected: bool = False
    anomaly_count: int = 0
    anomalies: list[dict[str, float | int | str]] = field(default_factory=list)


class IsolationForestAnomalyDetector:
    """Detects semantic outliers in log lines using scikit-learn's Isolation Forest.

    No K8s dependency — operates purely on numeric features extracted from
    log line text (log_features.extract_log_features), so it catches silent
    failures (e.g. a slow DB query with no "ERROR" keyword) that a keyword
    or regex-based strategy would miss entirely.
    """

    def __init__(
        self,
        contamination: float | None = None,
        random_state: int | None = None,
        min_samples: int | None = None,
        min_score_deviation: float | None = None,
    ) -> None:
        self.contamination = contamination or _cfg.isolation_forest_contamination
        self.random_state = (
            random_state if random_state is not None else _cfg.isolation_forest_random_state
        )
        self.min_samples = min_samples or _cfg.isolation_forest_min_samples
        self.min_score_deviation = min_score_deviation or _cfg.isolation_forest_min_score_deviation

    def detect(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)

        anomalies = self._select_true_outliers(log_lines, predictions, scores)

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def _select_true_outliers(
        self,
        log_lines: list[str],
        predictions: np.ndarray,
        scores: np.ndarray,
    ) -> list[dict[str, float | int | str]]:
        """Filters IsolationForest's fixed-contamination predictions.

        `contamination` forces ~N% of any batch to be flagged even when the
        batch is genuinely uniform (TC3). A point only counts as a real
        anomaly when its score also deviates from the batch's own score
        distribution by min_score_deviation standard deviations — on
        uniform data that deviation never clears the bar.
        """
        score_mean = float(np.mean(scores))
        score_std = float(np.std(scores))
        if score_std == 0.0:
            return []

        anomalies: list[dict[str, float | int | str]] = []
        for index, (prediction, score) in enumerate(zip(predictions, scores, strict=True)):
            if prediction != -1:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    "line": log_lines[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies
