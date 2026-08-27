"""Unit tests for adapters/secondary/pypi/pypi_version_adapter.py.

Covers index resolution (env var > persisted config > auto-detected fallback)
and the JSON fetch behaviour.
"""

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

    def test_default_index_points_to_prod_pypi(self) -> None:
        """Without env or config, the adapter queries pypi.org."""
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"info": {"version": "0.1.0b16"}}

        with patch.dict("os.environ", {}, clear=True):
            with patch(
                "hexawyn.adapters.secondary.pypi.pypi_version_adapter.load_config",
                return_value={},
            ):
                with patch("httpx.get", return_value=response) as mock_get:
                    PyPIVersionAdapter().fetch_latest_version()

        called_url = mock_get.call_args.args[0]
        assert called_url == "https://pypi.org/pypi/hexawyn/json"

    def test_env_index_overrides_url(self) -> None:
        """HEXAWYN_PYPI_INDEX_URL redirects the query (e.g. TestPyPI for dev)."""
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"info": {"version": "0.1.0b16"}}

        with patch.dict("os.environ", {"HEXAWYN_PYPI_INDEX_URL": "https://test.pypi.org"}):
            with patch(
                "hexawyn.adapters.secondary.pypi.pypi_version_adapter.load_config",
                return_value={},
            ):
                with patch("httpx.get", return_value=response) as mock_get:
                    PyPIVersionAdapter().fetch_latest_version()

        called_url = mock_get.call_args.args[0]
        assert called_url == "https://test.pypi.org/pypi/hexawyn/json"

    def test_env_index_trailing_slash_stripped(self) -> None:
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"info": {"version": "0.1.0b16"}}

        with patch.dict("os.environ", {"HEXAWYN_PYPI_INDEX_URL": "https://test.pypi.org/"}):
            with patch(
                "hexawyn.adapters.secondary.pypi.pypi_version_adapter.load_config",
                return_value={},
            ):
                with patch("httpx.get", return_value=response) as mock_get:
                    PyPIVersionAdapter().fetch_latest_version()

        called_url = mock_get.call_args.args[0]
        assert called_url == "https://test.pypi.org/pypi/hexawyn/json"

    def test_persisted_config_used_when_no_env(self) -> None:
        """A previously persisted pypi_index_url in config is honoured."""
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"info": {"version": "0.1.0b16"}}

        with patch.dict("os.environ", {}, clear=True):
            with patch(
                "hexawyn.adapters.secondary.pypi.pypi_version_adapter.load_config",
                return_value={"pypi_index_url": "https://test.pypi.org"},
            ):
                with patch("httpx.get", return_value=response) as mock_get:
                    PyPIVersionAdapter().fetch_latest_version()

        called_url = mock_get.call_args.args[0]
        assert called_url == "https://test.pypi.org/pypi/hexawyn/json"

    def test_env_overrides_persisted_config(self) -> None:
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"info": {"version": "0.1.0b16"}}

        with patch.dict("os.environ", {"HEXAWYN_PYPI_INDEX_URL": "https://pypi.org"}):
            with patch(
                "hexawyn.adapters.secondary.pypi.pypi_version_adapter.load_config",
                return_value={"pypi_index_url": "https://test.pypi.org"},
            ):
                with patch("httpx.get", return_value=response) as mock_get:
                    PyPIVersionAdapter().fetch_latest_version()

        called_url = mock_get.call_args.args[0]
        assert called_url == "https://pypi.org/pypi/hexawyn/json"

    def test_auto_detects_testpypi_when_prod_missing_and_persists(self) -> None:
        """When prod 404s, fall back to TestPyPI and persist the choice."""
        response_404 = MagicMock()
        response_404.status_code = 404
        response_ok = MagicMock()
        response_ok.status_code = 200
        response_ok.json.return_value = {"info": {"version": "0.1.0b16"}}

        with patch.dict("os.environ", {}, clear=True):
            with patch(
                "hexawyn.adapters.secondary.pypi.pypi_version_adapter.load_config",
                return_value={},
            ):
                with patch(
                    "hexawyn.adapters.secondary.pypi.pypi_version_adapter.save_config"
                ) as mock_save:
                    with patch(
                        "httpx.get",
                        side_effect=[response_404, response_ok],
                    ) as mock_get:
                        result = PyPIVersionAdapter().fetch_latest_version()

        assert result == "0.1.0b16"
        assert mock_get.call_count == 2  # noqa: PLR2004
        # First call to prod, then to TestPyPI
        assert mock_get.call_args_list[0].args[0] == "https://pypi.org/pypi/hexawyn/json"
        assert mock_get.call_args_list[1].args[0] == ("https://test.pypi.org/pypi/hexawyn/json")
        mock_save.assert_called_once()
        assert mock_save.call_args.args[0]["pypi_index_url"] == "https://test.pypi.org"

    def test_no_fallback_when_prod_available(self) -> None:
        """Prod answering 200 means no TestPyPI fallback and no config write."""
        response_ok = MagicMock()
        response_ok.status_code = 200
        response_ok.json.return_value = {"info": {"version": "0.1.0b16"}}

        with patch.dict("os.environ", {}, clear=True):
            with patch(
                "hexawyn.adapters.secondary.pypi.pypi_version_adapter.load_config",
                return_value={},
            ):
                with patch(
                    "hexawyn.adapters.secondary.pypi.pypi_version_adapter.save_config"
                ) as mock_save:
                    with patch("httpx.get", return_value=response_ok) as mock_get:
                        result = PyPIVersionAdapter().fetch_latest_version()

        assert result == "0.1.0b16"
        assert mock_get.call_count == 1
        mock_save.assert_not_called()

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

    def test_no_fallback_when_explicit_env_index_404(self) -> None:
        """An explicit env index that 404s must NOT trigger a TestPyPI fallback."""
        response_404 = MagicMock()
        response_404.status_code = 404

        with patch.dict("os.environ", {"HEXAWYN_PYPI_INDEX_URL": "https://custom.example"}):
            with patch(
                "hexawyn.adapters.secondary.pypi.pypi_version_adapter.load_config",
                return_value={},
            ):
                with patch(
                    "hexawyn.adapters.secondary.pypi.pypi_version_adapter.save_config"
                ) as mock_save:
                    with patch("httpx.get", return_value=response_404) as mock_get:
                        result = PyPIVersionAdapter().fetch_latest_version()

        assert result == ""
        assert mock_get.call_count == 1
        mock_save.assert_not_called()

    def test_connect_error_tries_fallback_persists_not(self) -> None:
        """A prod connect error falls back to TestPyPI (best-effort discovery)."""
        response_ok = MagicMock()
        response_ok.status_code = 200
        response_ok.json.return_value = {"info": {"version": "0.1.0b16"}}

        with patch.dict("os.environ", {}, clear=True):
            with patch(
                "hexawyn.adapters.secondary.pypi.pypi_version_adapter.load_config",
                return_value={},
            ):
                with patch(
                    "hexawyn.adapters.secondary.pypi.pypi_version_adapter.save_config"
                ) as mock_save:
                    with patch(
                        "httpx.get",
                        side_effect=[httpx.ConnectError("down"), response_ok],
                    ):
                        result = PyPIVersionAdapter().fetch_latest_version()

        assert result == "0.1.0b16"
        mock_save.assert_called_once()

    def test_fetch_version_non_dict_info_returns_none(self) -> None:
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"info": "not-a-dict"}

        with patch("httpx.get", return_value=response):
            result = PyPIVersionAdapter().fetch_latest_version()

        assert result == ""

    def test_persist_index_swallows_save_error(self) -> None:
        from hexawyn.adapters.secondary.pypi.pypi_version_adapter import (
            PyPIVersionAdapter,
        )

        with patch(
            "hexawyn.adapters.secondary.pypi.pypi_version_adapter.load_config",
            return_value={},
        ):
            with patch(
                "hexawyn.adapters.secondary.pypi.pypi_version_adapter.save_config",
                side_effect=OSError("read-only fs"),
            ):
                with patch(
                    "hexawyn.adapters.secondary.pypi.pypi_version_adapter.logger.warning"
                ) as mock_warn:
                    PyPIVersionAdapter._persist_index("https://test.pypi.org")

        assert mock_warn.call_count == 1
