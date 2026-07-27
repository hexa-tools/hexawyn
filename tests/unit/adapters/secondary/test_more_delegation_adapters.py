"""Tests for delegation adapters (source-based) and stubs."""

from __future__ import annotations

from unittest.mock import MagicMock, Mock, patch

from hexawyn.adapters.secondary.gitops.budget_projection_adapter import (
    BudgetProjectionAdapter,
    _month_of,
    _to_monthly_raw,
)
from hexawyn.adapters.secondary.gitops.helm_release_version_adapter import (
    HelmReleaseVersionAdapter,
)
from hexawyn.adapters.secondary.gitops.prediction_roi_adapter import PredictionRoiAdapter
from hexawyn.adapters.secondary.gitops.stale_credentials_adapter import StaleCredentialsAdapter
from hexawyn.adapters.secondary.gitops.unauthorized_access_adapter import (
    UnauthorizedAccessAdapter,
)


class TestBudgetProjectionAdapter:
    def test_get_monthly_cost_history(self) -> None:
        port = Mock()
        port.get_daily_costs.return_value = [
            {"date": "2026-07-01", "total_usd": 10.0},
            {"date": "2026-07-15", "total_usd": 20.0},
        ]
        adapter = BudgetProjectionAdapter(cost_forecast_port=port)
        result = adapter.get_monthly_cost_history(1)
        assert len(result) == 1
        assert result[0]["month"] == "2026-07"
        assert result[0]["total_usd"] == 30.0  # noqa: PLR2004

    def test_empty(self) -> None:
        port = Mock()
        port.get_daily_costs.return_value = []
        adapter = BudgetProjectionAdapter(cost_forecast_port=port)
        assert adapter.get_monthly_cost_history(1) == []


class TestMonthOf:
    def test_valid(self) -> None:
        assert _month_of("2026-07-15") == "2026-07"

    def test_invalid(self) -> None:
        assert _month_of("abc") is None
        assert _month_of("2026") is None

    def test_empty(self) -> None:
        assert _month_of("") is None


class TestToMonthlyRaw:
    def test_compute(self) -> None:
        raw = _to_monthly_raw("2026-07", 100.0)
        assert raw["month"] == "2026-07"
        assert raw["total_usd"] == 100.0  # noqa: PLR2004
        assert raw["compute_usd"] == 60.0  # noqa: PLR2004
        assert raw["storage_usd"] == 25.0  # noqa: PLR2004
        assert raw["network_usd"] == 15.0  # noqa: PLR2004


class TestHelmReleaseVersionAdapter:
    def test_list_releases_empty(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="[]")
            adapter = HelmReleaseVersionAdapter()
            assert adapter.list_releases(None) == []

    def test_fetch_latest_version_empty(self) -> None:
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0, stdout="[]")
            adapter = HelmReleaseVersionAdapter()
            result = adapter.fetch_latest_version("chart")
            assert result["chart_name"] == "chart"
            assert result["latest_version"] == ""


class TestPredictionRoiAdapter:
    def test_delegates(self) -> None:
        source = Mock()
        source.fetch_prediction_roi_data.return_value = {
            "detections": [],
            "infrastructure_cost_eur": 100.0,
            "revenue_per_minute": None,
        }
        adapter = PredictionRoiAdapter(source=source)
        result = adapter.get_prediction_roi_data("30d")
        assert result["infrastructure_cost_eur"] == 100.0  # noqa: PLR2004
        source.fetch_prediction_roi_data.assert_called_once_with("30d")


class TestStaleCredentialsAdapter:
    def test_delegates(self) -> None:
        source = Mock()
        source.fetch_stale_credentials.return_value = []
        adapter = StaleCredentialsAdapter(source=source)
        assert adapter.get_stale_credentials(90) == []


class TestUnauthorizedAccessAdapter:
    def test_delegates(self) -> None:
        source = Mock()
        source.fetch_unauthorized_access_data.return_value = {
            "attempt_count": 5,
            "window_minutes": 60,
            "source_type": "external",
        }
        adapter = UnauthorizedAccessAdapter(source=source)
        result = adapter.get_unauthorized_access_data()
        assert result["attempt_count"] == 5  # noqa: PLR2004
