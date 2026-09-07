"""Unit tests for provider_config — CLI-set cloud provider credentials."""

from __future__ import annotations

import os
from unittest.mock import patch

from hexawyn.infrastructure.config.provider_config import (
    apply_provider_env,
    clear_provider_credentials,
    credential_fields,
    get_provider_credentials,
    list_provider_credentials,
    set_provider_credentials,
)


def _cfg(data: dict[str, object] | None = None) -> dict[str, object]:
    return data if data is not None else {}


class TestProviderConfig:
    def test_set_then_get(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.provider_config.load_config",
            return_value=_cfg(),
        ):
            set_provider_credentials("aws", {"access_key": "AKIA", "secret_key": "s3cr3t"})
            creds = get_provider_credentials("aws")

        assert creds == {"access_key": "AKIA", "secret_key": "s3cr3t"}

    def test_get_empty_when_missing(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.provider_config.load_config",
            return_value=_cfg(),
        ):
            assert get_provider_credentials("gcp") == {}

    def test_clear_removes_provider(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.provider_config.load_config",
            return_value=_cfg({"providers": {"aws": {"access_key": "AKIA"}}}),
        ):
            clear_provider_credentials("aws")
            assert get_provider_credentials("aws") == {}

    def test_list_providers_with_credentials(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.provider_config.load_config",
            return_value=_cfg(
                {"providers": {"aws": {"access_key": "AKIA"}, "datadog": {"api_key": "k"}}}
            ),
        ):
            listing = list_provider_credentials()

        assert listing == {"aws": {"access_key": "AKIA"}, "datadog": {"api_key": "k"}}


class TestApplyProviderEnv:
    def test_aws_sets_sdk_env_vars(self) -> None:
        values = {"access_key": "AKIA", "secret_key": "s3cr3t", "region": "eu-west-3"}
        with patch(
            "hexawyn.infrastructure.config.provider_config.load_config",
            return_value=_cfg({"providers": {"aws": values}}),
        ):
            apply_provider_env("aws")

        assert os.environ["AWS_ACCESS_KEY_ID"] == "AKIA"
        assert os.environ["AWS_SECRET_ACCESS_KEY"] == "s3cr3t"
        assert os.environ["AWS_DEFAULT_REGION"] == "eu-west-3"

    def test_datadog_sets_env_vars(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.provider_config.load_config",
            return_value=_cfg(
                {"providers": {"datadog": {"api_key": "k", "app_key": "ak", "site": "eu"}}}
            ),
        ):
            apply_provider_env("datadog")

        assert os.environ["DD_API_KEY"] == "k"
        assert os.environ["DD_APP_KEY"] == "ak"
        assert os.environ["DD_SITE"] == "eu"

    def test_gcp_sets_credentials_file(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.provider_config.load_config",
            return_value=_cfg({"providers": {"gcp": {"credentials_file": "/tmp/key.json"}}}),
        ):
            apply_provider_env("gcp")

        assert os.environ["GOOGLE_APPLICATION_CREDENTIALS"] == "/tmp/key.json"

    def test_unknown_provider_noop(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.provider_config.load_config",
            return_value=_cfg(),
        ):
            result = apply_provider_env("oyh")

        assert result == {}

    def test_credential_fields_for_provider(self) -> None:
        assert credential_fields("aws") == [
            ("access_key", "Access Key"),
            ("secret_key", "Secret Key"),
            ("region", "Region"),
        ]

    def test_credential_fields_unknown(self) -> None:
        assert credential_fields("oyh") == []
