"""CLI-set cloud provider credentials, stored in ~/.hexawyn/config.yaml.

Cloud adapters authenticate through their SDK credential chain (env vars /
credential files). This module lets a user store those credentials once via
``hexa config provider set`` and re-inject them as the SDK-recognised env vars
(``apply_provider_env``) so the cloud adapters pick them up without the user
touching each SDK's auth setup.
"""

from __future__ import annotations

import os
from typing import cast

from hexawyn.infrastructure.config.config_manager import load_config, save_config

_PROVIDERS_KEY = "providers"

# canonical credential key -> SDK-recognised env var, per cloud provider
_ENV_BY_PROVIDER: dict[str, dict[str, str]] = {
    "aws": {
        "access_key": "AWS_ACCESS_KEY_ID",
        "secret_key": "AWS_SECRET_ACCESS_KEY",
        "region": "AWS_DEFAULT_REGION",
    },
    "gcp": {"credentials_file": "GOOGLE_APPLICATION_CREDENTIALS"},
    "azure": {
        "client_id": "AZURE_CLIENT_ID",
        "client_secret": "AZURE_CLIENT_SECRET",
        "tenant_id": "AZURE_TENANT_ID",
        "subscription_id": "AZURE_SUBSCRIPTION_ID",
    },
    "datadog": {
        "api_key": "DD_API_KEY",
        "app_key": "DD_APP_KEY",
        "site": "DD_SITE",
    },
}


def _providers_from(config: dict[str, object]) -> dict[str, dict[str, str]]:
    raw = config.get(_PROVIDERS_KEY)
    if not isinstance(raw, dict):
        return {}
    return cast(dict[str, dict[str, str]], raw)


def _providers() -> dict[str, dict[str, str]]:
    return _providers_from(load_config())


def get_provider_credentials(provider: str) -> dict[str, str]:
    """Return the stored credentials for a provider (empty when unset)."""
    return _providers().get(provider, {})


def set_provider_credentials(provider: str, values: dict[str, str]) -> None:
    """Persist a provider's credentials (empty values are dropped)."""
    config = load_config()
    providers = _providers_from(config)
    providers[provider] = {key: value for key, value in values.items() if value}
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def clear_provider_credentials(provider: str) -> None:
    """Remove a provider's stored credentials."""
    config = load_config()
    providers = _providers_from(config)
    providers.pop(provider, None)
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def list_provider_credentials() -> dict[str, dict[str, str]]:
    """All providers that have stored credentials."""
    return _providers()


def credential_fields(provider: str) -> list[tuple[str, str]]:
    """Ordered (credential key, human label) pairs a provider needs.

    Used by the TUI to render the credential form for a provider. Returns an
    empty list for an unknown provider.
    """
    mapping = _ENV_BY_PROVIDER.get(provider)
    if mapping is None:
        return []
    return [(key, _human_label(key)) for key in mapping]


def _human_label(key: str) -> str:
    return key.replace("_", " ").title()


def apply_provider_env(provider: str) -> dict[str, str]:
    """Inject stored credentials as the SDK-recognised env vars.

    Returns the env vars that were set (empty when the provider is unknown or
    has no stored credentials).
    """
    mapping = _ENV_BY_PROVIDER.get(provider)
    if mapping is None:
        return {}
    credentials = get_provider_credentials(provider)
    applied: dict[str, str] = {}
    for key, env_name in mapping.items():
        if key in credentials:
            os.environ[env_name] = credentials[key]
            applied[env_name] = credentials[key]
    return applied
