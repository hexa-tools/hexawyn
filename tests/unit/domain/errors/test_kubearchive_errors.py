from __future__ import annotations

from hexawyn.domain.errors import (
    HexawynError,
    HistoricalDataWindowExpiredError,
    KubeArchiveUnavailableError,
)


class TestKubeArchiveUnavailableError:
    def test_inherits_from_hexawyn_error(self) -> None:
        error = KubeArchiveUnavailableError()
        assert isinstance(error, HexawynError)

    def test_has_sensible_message(self) -> None:
        error = KubeArchiveUnavailableError()
        message = str(error)
        assert "KubeArchive" in message
        assert len(message) > 10  # noqa: PLR2004

    def test_accepts_context(self) -> None:
        error = KubeArchiveUnavailableError(context={"url": "http://localhost:8081"})
        assert error.context["url"] == "http://localhost:8081"


class TestHistoricalDataWindowExpiredError:
    def test_inherits_from_hexawyn_error(self) -> None:
        queried = "2024-01-01T00:00:00Z"
        retention = "30d"
        error = HistoricalDataWindowExpiredError(
            queried_timestamp=queried, retention_window=retention
        )
        assert isinstance(error, HexawynError)

    def test_message_includes_timestamp_and_retention(self) -> None:
        error = HistoricalDataWindowExpiredError(
            queried_timestamp="2024-01-01T00:00:00Z",
            retention_window="90d",
        )
        message = str(error)
        assert "2024-01-01T00:00:00Z" in message
        assert "90d" in message

    def test_stores_queried_timestamp(self) -> None:
        error = HistoricalDataWindowExpiredError(
            queried_timestamp="2024-06-01T12:00:00Z",
            retention_window="30d",
        )
        assert error.queried_timestamp == "2024-06-01T12:00:00Z"
        assert error.retention_window == "30d"

    def test_null_queried_data(self) -> None:
        error = HistoricalDataWindowExpiredError(
            queried_timestamp="2023-01-01T00:00:00Z",
            retention_window="365d",
        )
        assert error.queried_timestamp == "2023-01-01T00:00:00Z"
        assert error.retention_window == "365d"
