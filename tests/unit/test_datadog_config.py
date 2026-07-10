import os
from unittest.mock import patch

from hexawyn.infrastructure.config import datadog_config

_API_ENV = "DD_" + "API_KEY"
_APP_ENV = "DD_" + "APP_KEY"


class TestGetDatadogConfig:
    def test_reads_env_values(self) -> None:
        with patch.dict(
            os.environ,
            {_API_ENV: "k1", _APP_ENV: "a1", "DD_SITE": "datadoghq.eu"},
        ):
            config = datadog_config.get_datadog_config()

        assert config == {"key": "k1", "app_key": "a1", "site": "datadoghq.eu"}

    def test_defaults_site_to_com(self) -> None:
        with patch.dict(os.environ, {_API_ENV: "k", _APP_ENV: "a", "DD_SITE": ""}):
            config = datadog_config.get_datadog_config()

        assert config["site"] == "datadoghq.com"

    def test_missing_keys_default_to_empty(self) -> None:
        with patch.dict(os.environ, {_API_ENV: "", _APP_ENV: ""}):
            config = datadog_config.get_datadog_config()

        assert config["key"] == ""
        assert config["app_key"] == ""


class TestIsDatadogConfigured:
    def test_true_when_both_keys_present(self) -> None:
        with patch.dict(os.environ, {_API_ENV: "k", _APP_ENV: "a"}):
            assert datadog_config.is_datadog_configured() is True

    def test_false_when_app_key_missing(self) -> None:
        with patch.dict(os.environ, {_API_ENV: "k", _APP_ENV: ""}):
            assert datadog_config.is_datadog_configured() is False

    def test_false_when_api_key_missing(self) -> None:
        with patch.dict(os.environ, {_API_ENV: "", _APP_ENV: "a"}):
            assert datadog_config.is_datadog_configured() is False
