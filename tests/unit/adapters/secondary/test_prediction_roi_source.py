from __future__ import annotations

from unittest.mock import patch


class TestConfigPredictionRoiSource:
    def test_reads_revenue_from_config(self) -> None:
        from hexawyn.adapters.secondary.gitops.prediction_roi_source import (
            ConfigPredictionRoiSource,
        )

        with patch(
            "hexawyn.adapters.secondary.gitops.prediction_roi_source.load_config",
            return_value={"business": {"revenue_per_minute": 500.0}},
        ):
            data = ConfigPredictionRoiSource().fetch_prediction_roi_data("2026-06")

        assert data["revenue_per_minute"] == 500.0

    def test_missing_business_config_returns_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.prediction_roi_source import (
            ConfigPredictionRoiSource,
        )

        with patch(
            "hexawyn.adapters.secondary.gitops.prediction_roi_source.load_config",
            return_value={},
        ):
            data = ConfigPredictionRoiSource().fetch_prediction_roi_data("2026-06")

        assert data["revenue_per_minute"] is None

    def test_non_numeric_revenue_is_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.prediction_roi_source import (
            ConfigPredictionRoiSource,
        )

        with patch(
            "hexawyn.adapters.secondary.gitops.prediction_roi_source.load_config",
            return_value={"business": {"revenue_per_minute": "not-a-number"}},
        ):
            data = ConfigPredictionRoiSource().fetch_prediction_roi_data("2026-06")

        assert data["revenue_per_minute"] is None

    def test_boolean_revenue_is_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.prediction_roi_source import (
            ConfigPredictionRoiSource,
        )

        with patch(
            "hexawyn.adapters.secondary.gitops.prediction_roi_source.load_config",
            return_value={"business": {"revenue_per_minute": True}},
        ):
            data = ConfigPredictionRoiSource().fetch_prediction_roi_data("2026-06")

        assert data["revenue_per_minute"] is None
