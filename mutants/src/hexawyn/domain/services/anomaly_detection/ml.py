from dataclasses import dataclass, field

import numpy as np
from hexawyn.domain.models.constants import LogAnomalyDetectionConstants
from hexawyn.domain.services.anomaly_detection.log_features import extract_log_features
from sklearn.ensemble import IsolationForest

_cfg = LogAnomalyDetectionConstants()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class MLAnomalyDetectionResult:
    """Output of an Isolation Forest semantic anomaly detection run."""

    anomalies_detected: bool = False
    anomaly_count: int = 0
    anomalies: list[dict[str, float | int | str]] = field(default_factory=list)
mutants_xǁIsolationForestAnomalyDetectorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut: MutantDict = {}  # type: ignore


class IsolationForestAnomalyDetector:
    """Detects semantic outliers in log lines using scikit-learn's Isolation Forest.

    No K8s dependency — operates purely on numeric features extracted from
    log line text (log_features.extract_log_features), so it catches silent
    failures (e.g. a slow DB query with no "ERROR" keyword) that a keyword
    or regex-based strategy would miss entirely.
    """

    @_mutmut_mutated(mutants_xǁIsolationForestAnomalyDetectorǁ__init____mutmut)
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

    def xǁIsolationForestAnomalyDetectorǁ__init____mutmut_orig(
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

    def xǁIsolationForestAnomalyDetectorǁ__init____mutmut_1(
        self,
        contamination: float | None = None,
        random_state: int | None = None,
        min_samples: int | None = None,
        min_score_deviation: float | None = None,
    ) -> None:
        self.contamination = None
        self.random_state = (
            random_state if random_state is not None else _cfg.isolation_forest_random_state
        )
        self.min_samples = min_samples or _cfg.isolation_forest_min_samples
        self.min_score_deviation = min_score_deviation or _cfg.isolation_forest_min_score_deviation

    def xǁIsolationForestAnomalyDetectorǁ__init____mutmut_2(
        self,
        contamination: float | None = None,
        random_state: int | None = None,
        min_samples: int | None = None,
        min_score_deviation: float | None = None,
    ) -> None:
        self.contamination = contamination and _cfg.isolation_forest_contamination
        self.random_state = (
            random_state if random_state is not None else _cfg.isolation_forest_random_state
        )
        self.min_samples = min_samples or _cfg.isolation_forest_min_samples
        self.min_score_deviation = min_score_deviation or _cfg.isolation_forest_min_score_deviation

    def xǁIsolationForestAnomalyDetectorǁ__init____mutmut_3(
        self,
        contamination: float | None = None,
        random_state: int | None = None,
        min_samples: int | None = None,
        min_score_deviation: float | None = None,
    ) -> None:
        self.contamination = contamination or _cfg.isolation_forest_contamination
        self.random_state = None
        self.min_samples = min_samples or _cfg.isolation_forest_min_samples
        self.min_score_deviation = min_score_deviation or _cfg.isolation_forest_min_score_deviation

    def xǁIsolationForestAnomalyDetectorǁ__init____mutmut_4(
        self,
        contamination: float | None = None,
        random_state: int | None = None,
        min_samples: int | None = None,
        min_score_deviation: float | None = None,
    ) -> None:
        self.contamination = contamination or _cfg.isolation_forest_contamination
        self.random_state = (
            random_state if random_state is None else _cfg.isolation_forest_random_state
        )
        self.min_samples = min_samples or _cfg.isolation_forest_min_samples
        self.min_score_deviation = min_score_deviation or _cfg.isolation_forest_min_score_deviation

    def xǁIsolationForestAnomalyDetectorǁ__init____mutmut_5(
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
        self.min_samples = None
        self.min_score_deviation = min_score_deviation or _cfg.isolation_forest_min_score_deviation

    def xǁIsolationForestAnomalyDetectorǁ__init____mutmut_6(
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
        self.min_samples = min_samples and _cfg.isolation_forest_min_samples
        self.min_score_deviation = min_score_deviation or _cfg.isolation_forest_min_score_deviation

    def xǁIsolationForestAnomalyDetectorǁ__init____mutmut_7(
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
        self.min_score_deviation = None

    def xǁIsolationForestAnomalyDetectorǁ__init____mutmut_8(
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
        self.min_score_deviation = min_score_deviation and _cfg.isolation_forest_min_score_deviation

    @_mutmut_mutated(mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut)
    def detect(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_orig(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_1(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) <= self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_2(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = None
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_3(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array(None)
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_4(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(None) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_5(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = None

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_6(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(None, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_7(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, None, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_8(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key=None)

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_9(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_10(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_11(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, )

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_12(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="XXlineXX")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_13(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="LINE")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_14(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=None,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_15(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=None,
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_16(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=None,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_17(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_18(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_19(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_20(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) >= 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect__mutmut_21(self, log_lines: list[str]) -> MLAnomalyDetectionResult:
        if len(log_lines) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([extract_log_features(line) for line in log_lines])
        anomalies = self._run(log_lines, features, item_key="line")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 1,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    @_mutmut_mutated(mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut)
    def detect_series(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_orig(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_1(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) <= self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_2(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = None
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_3(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array(None)
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_4(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = None

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_5(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(None, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_6(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, None, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_7(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key=None)

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_8(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_9(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_10(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, )

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_11(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="XXvalueXX")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_12(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="VALUE")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_13(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=None,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_14(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=None,
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_15(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            anomalies=None,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_16(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_17(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_18(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 0,
            anomaly_count=len(anomalies),
            )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_19(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) >= 0,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    def xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_20(self, values: list[float]) -> MLAnomalyDetectionResult:
        """Same Isolation Forest + deviation-filter engine as `detect`, fed raw
        numeric values instead of text-derived features — used by pod-metrics
        anomaly detection to catch both sharp spikes and gradual multi-point
        drift (a drifting tail is numerically distant from the stable bulk,
        so it isolates in fewer random splits even without one extreme point).
        """
        if len(values) < self.min_samples:
            return MLAnomalyDetectionResult()

        features = np.array([[value] for value in values])
        anomalies = self._run(values, features, item_key="value")

        return MLAnomalyDetectionResult(
            anomalies_detected=len(anomalies) > 1,
            anomaly_count=len(anomalies),
            anomalies=anomalies,
        )

    @_mutmut_mutated(mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut)
    def _run(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_orig(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_1(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = None
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_2(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=None,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_3(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=None,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_4(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_5(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_6(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = None
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_7(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(None)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_8(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = None
        return self._select_true_outliers(items, predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_9(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(None)
        return self._select_true_outliers(items, predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_10(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(None, predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_11(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, None, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_12(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, None, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_13(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, scores, None)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_14(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(predictions, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_15(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, scores, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_16(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, item_key)

    def xǁIsolationForestAnomalyDetectorǁ_run__mutmut_17(
        self,
        items: list[str] | list[float],
        features: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        model = IsolationForest(
            contamination=self.contamination,
            random_state=self.random_state,
        )
        predictions = model.fit_predict(features)
        scores = model.decision_function(features)
        return self._select_true_outliers(items, predictions, scores, )

    @_mutmut_mutated(mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut)
    def _select_true_outliers(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_orig(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_1(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        """Filters IsolationForest's fixed-contamination predictions.

        `contamination` forces ~N% of any batch to be flagged even when the
        batch is genuinely uniform (TC3). A point only counts as a real
        anomaly when its score also deviates from the batch's own score
        distribution by min_score_deviation standard deviations — on
        uniform data that deviation never clears the bar.
        """
        score_mean = None
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_2(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        """Filters IsolationForest's fixed-contamination predictions.

        `contamination` forces ~N% of any batch to be flagged even when the
        batch is genuinely uniform (TC3). A point only counts as a real
        anomaly when its score also deviates from the batch's own score
        distribution by min_score_deviation standard deviations — on
        uniform data that deviation never clears the bar.
        """
        score_mean = float(None)
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_3(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        """Filters IsolationForest's fixed-contamination predictions.

        `contamination` forces ~N% of any batch to be flagged even when the
        batch is genuinely uniform (TC3). A point only counts as a real
        anomaly when its score also deviates from the batch's own score
        distribution by min_score_deviation standard deviations — on
        uniform data that deviation never clears the bar.
        """
        score_mean = float(np.mean(None))
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_4(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        """Filters IsolationForest's fixed-contamination predictions.

        `contamination` forces ~N% of any batch to be flagged even when the
        batch is genuinely uniform (TC3). A point only counts as a real
        anomaly when its score also deviates from the batch's own score
        distribution by min_score_deviation standard deviations — on
        uniform data that deviation never clears the bar.
        """
        score_mean = float(np.mean(scores))
        score_std = None
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_5(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        """Filters IsolationForest's fixed-contamination predictions.

        `contamination` forces ~N% of any batch to be flagged even when the
        batch is genuinely uniform (TC3). A point only counts as a real
        anomaly when its score also deviates from the batch's own score
        distribution by min_score_deviation standard deviations — on
        uniform data that deviation never clears the bar.
        """
        score_mean = float(np.mean(scores))
        score_std = float(None)
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_6(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
    ) -> list[dict[str, float | int | str]]:
        """Filters IsolationForest's fixed-contamination predictions.

        `contamination` forces ~N% of any batch to be flagged even when the
        batch is genuinely uniform (TC3). A point only counts as a real
        anomaly when its score also deviates from the batch's own score
        distribution by min_score_deviation standard deviations — on
        uniform data that deviation never clears the bar.
        """
        score_mean = float(np.mean(scores))
        score_std = float(np.std(None))
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_7(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
        if score_std != 0.0:
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_8(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
        if score_std == 1.0:
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_9(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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

        anomalies: list[dict[str, float | int | str]] = None
        for index, (prediction, score) in enumerate(zip(predictions, scores, strict=True)):
            if prediction != -1:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_10(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
        for index, (prediction, score) in enumerate(None):
            if prediction != -1:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_11(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
        for index, (prediction, score) in enumerate(zip(None, scores, strict=True)):
            if prediction != -1:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_12(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
        for index, (prediction, score) in enumerate(zip(predictions, None, strict=True)):
            if prediction != -1:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_13(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
        for index, (prediction, score) in enumerate(zip(predictions, scores, strict=None)):
            if prediction != -1:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_14(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
        for index, (prediction, score) in enumerate(zip(scores, strict=True)):
            if prediction != -1:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_15(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
        for index, (prediction, score) in enumerate(zip(predictions, strict=True)):
            if prediction != -1:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_16(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
        for index, (prediction, score) in enumerate(zip(predictions, scores, )):
            if prediction != -1:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_17(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
        for index, (prediction, score) in enumerate(zip(predictions, scores, strict=False)):
            if prediction != -1:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_18(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
            if prediction == -1:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_19(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
            if prediction != +1:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_20(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
            if prediction != -2:
                continue
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_21(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                break
            deviation = (score_mean - score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_22(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
            deviation = None
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_23(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
            deviation = (score_mean - score) * score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_24(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
            deviation = (score_mean + score) / score_std
            if deviation < self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_25(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
            if deviation <= self.min_score_deviation:
                continue
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_26(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                break
            anomalies.append(
                {
                    "index": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_27(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                None
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_28(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    "XXindexXX": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_29(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    "INDEX": index,
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_30(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    item_key: items[index],
                    "XXanomaly_scoreXX": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_31(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    item_key: items[index],
                    "ANOMALY_SCORE": round(float(-score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_32(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    item_key: items[index],
                    "anomaly_score": round(None, 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_33(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), None),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_34(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    item_key: items[index],
                    "anomaly_score": round(4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_35(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), ),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_36(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    item_key: items[index],
                    "anomaly_score": round(float(None), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_37(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    item_key: items[index],
                    "anomaly_score": round(float(+score), 4),
                }
            )
        return anomalies

    def xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_38(
        self,
        items: list[str] | list[float],
        predictions: np.ndarray,
        scores: np.ndarray,
        item_key: str,
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
                    item_key: items[index],
                    "anomaly_score": round(float(-score), 5),
                }
            )
        return anomalies

mutants_xǁIsolationForestAnomalyDetectorǁ__init____mutmut['_mutmut_orig'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ__init____mutmut['xǁIsolationForestAnomalyDetectorǁ__init____mutmut_1'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ__init____mutmut['xǁIsolationForestAnomalyDetectorǁ__init____mutmut_2'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ__init____mutmut['xǁIsolationForestAnomalyDetectorǁ__init____mutmut_3'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ__init____mutmut['xǁIsolationForestAnomalyDetectorǁ__init____mutmut_4'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ__init____mutmut['xǁIsolationForestAnomalyDetectorǁ__init____mutmut_5'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ__init____mutmut['xǁIsolationForestAnomalyDetectorǁ__init____mutmut_6'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ__init____mutmut['xǁIsolationForestAnomalyDetectorǁ__init____mutmut_7'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ__init____mutmut['xǁIsolationForestAnomalyDetectorǁ__init____mutmut_8'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ__init____mutmut_8 # type: ignore # mutmut generated

mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['_mutmut_orig'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_1'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_2'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_3'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_4'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_5'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_6'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_7'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_8'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_9'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_10'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_11'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_12'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_13'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_14'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_15'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_16'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_17'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_18'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_19'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_20'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect__mutmut['xǁIsolationForestAnomalyDetectorǁdetect__mutmut_21'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect__mutmut_21 # type: ignore # mutmut generated

mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['_mutmut_orig'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_1'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_2'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_3'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_4'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_5'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_6'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_7'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_8'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_9'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_10'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_11'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_12'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_13'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_14'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_15'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_16'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_17'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_18'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_19'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut['xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_20'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁdetect_series__mutmut_20 # type: ignore # mutmut generated

mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['_mutmut_orig'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_1'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_2'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_3'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_4'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_5'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_6'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_7'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_8'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_9'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_10'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_11'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_12'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_13'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_14'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_15'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_16'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_run__mutmut['xǁIsolationForestAnomalyDetectorǁ_run__mutmut_17'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_run__mutmut_17 # type: ignore # mutmut generated

mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['_mutmut_orig'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_orig # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_1'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_1 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_2'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_2 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_3'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_3 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_4'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_4 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_5'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_5 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_6'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_6 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_7'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_7 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_8'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_8 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_9'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_9 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_10'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_10 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_11'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_11 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_12'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_12 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_13'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_13 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_14'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_14 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_15'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_15 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_16'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_16 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_17'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_17 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_18'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_18 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_19'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_19 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_20'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_20 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_21'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_21 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_22'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_22 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_23'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_23 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_24'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_24 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_25'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_25 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_26'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_26 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_27'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_27 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_28'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_28 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_29'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_29 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_30'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_30 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_31'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_31 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_32'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_32 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_33'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_33 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_34'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_34 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_35'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_35 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_36'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_36 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_37'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_37 # type: ignore # mutmut generated
mutants_xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut['xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_38'] = IsolationForestAnomalyDetector.xǁIsolationForestAnomalyDetectorǁ_select_true_outliers__mutmut_38 # type: ignore # mutmut generated
