"""Unit tests for adapters/secondary/pypi/pypi_version_adapter.py."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import httpx
from hexawyn.adapters.secondary.pypi.pypi_version_adapter import PyPIVersionAdapter


class TestPyPIVersionAdapter:
    def test_returns_version_from_json(self) -> None:
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"info": {"version": "0.1.0b4"}}

        with patch("httpx.get", return_value=response) as mock_get:
            result = PyPIVersionAdapter().fetch_latest_version()

        assert result == "0.1.0b4"
        mock_get.assert_called_once()

    def test_returns_empty_on_http_error(self) -> None:
        response = MagicMock()
        response.status_code = 500

        with patch("httpx.get", return_value=response):
            result = PyPIVersionAdapter().fetch_latest_version()

        assert result == ""

    def test_returns_empty_on_connect_error(self) -> None:
        with patch("httpx.get", side_effect=httpx.ConnectError("network down")):
            result = PyPIVersionAdapter().fetch_latest_version()

        assert result == ""

    def test_returns_empty_on_missing_info(self) -> None:
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {}

        with patch("httpx.get", return_value=response):
            result = PyPIVersionAdapter().fetch_latest_version()

        assert result == ""

    def test_returns_empty_on_invalid_json(self) -> None:
        response = MagicMock()
        response.status_code = 200
        response.json.side_effect = ValueError("invalid json")

        with patch("httpx.get", return_value=response):
            result = PyPIVersionAdapter().fetch_latest_version()

        assert result == ""
