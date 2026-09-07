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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__providers_from__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__providers_from__mutmut)
def _providers_from(config: dict[str, object]) -> dict[str, dict[str, str]]:
    raw = config.get(_PROVIDERS_KEY)
    if not isinstance(raw, dict):
        return {}
    return cast(dict[str, dict[str, str]], raw)


def x__providers_from__mutmut_orig(config: dict[str, object]) -> dict[str, dict[str, str]]:
    raw = config.get(_PROVIDERS_KEY)
    if not isinstance(raw, dict):
        return {}
    return cast(dict[str, dict[str, str]], raw)


def x__providers_from__mutmut_1(config: dict[str, object]) -> dict[str, dict[str, str]]:
    raw = None
    if not isinstance(raw, dict):
        return {}
    return cast(dict[str, dict[str, str]], raw)


def x__providers_from__mutmut_2(config: dict[str, object]) -> dict[str, dict[str, str]]:
    raw = config.get(None)
    if not isinstance(raw, dict):
        return {}
    return cast(dict[str, dict[str, str]], raw)


def x__providers_from__mutmut_3(config: dict[str, object]) -> dict[str, dict[str, str]]:
    raw = config.get(_PROVIDERS_KEY)
    if isinstance(raw, dict):
        return {}
    return cast(dict[str, dict[str, str]], raw)


def x__providers_from__mutmut_4(config: dict[str, object]) -> dict[str, dict[str, str]]:
    raw = config.get(_PROVIDERS_KEY)
    if not isinstance(raw, dict):
        return {}
    return cast(None, raw)


def x__providers_from__mutmut_5(config: dict[str, object]) -> dict[str, dict[str, str]]:
    raw = config.get(_PROVIDERS_KEY)
    if not isinstance(raw, dict):
        return {}
    return cast(dict[str, dict[str, str]], None)


def x__providers_from__mutmut_6(config: dict[str, object]) -> dict[str, dict[str, str]]:
    raw = config.get(_PROVIDERS_KEY)
    if not isinstance(raw, dict):
        return {}
    return cast(raw)


def x__providers_from__mutmut_7(config: dict[str, object]) -> dict[str, dict[str, str]]:
    raw = config.get(_PROVIDERS_KEY)
    if not isinstance(raw, dict):
        return {}
    return cast(dict[str, dict[str, str]], )

mutants_x__providers_from__mutmut['_mutmut_orig'] = x__providers_from__mutmut_orig # type: ignore # mutmut generated
mutants_x__providers_from__mutmut['x__providers_from__mutmut_1'] = x__providers_from__mutmut_1 # type: ignore # mutmut generated
mutants_x__providers_from__mutmut['x__providers_from__mutmut_2'] = x__providers_from__mutmut_2 # type: ignore # mutmut generated
mutants_x__providers_from__mutmut['x__providers_from__mutmut_3'] = x__providers_from__mutmut_3 # type: ignore # mutmut generated
mutants_x__providers_from__mutmut['x__providers_from__mutmut_4'] = x__providers_from__mutmut_4 # type: ignore # mutmut generated
mutants_x__providers_from__mutmut['x__providers_from__mutmut_5'] = x__providers_from__mutmut_5 # type: ignore # mutmut generated
mutants_x__providers_from__mutmut['x__providers_from__mutmut_6'] = x__providers_from__mutmut_6 # type: ignore # mutmut generated
mutants_x__providers_from__mutmut['x__providers_from__mutmut_7'] = x__providers_from__mutmut_7 # type: ignore # mutmut generated
mutants_x__providers__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__providers__mutmut)
def _providers() -> dict[str, dict[str, str]]:
    return _providers_from(load_config())


def x__providers__mutmut_orig() -> dict[str, dict[str, str]]:
    return _providers_from(load_config())


def x__providers__mutmut_1() -> dict[str, dict[str, str]]:
    return _providers_from(None)

mutants_x__providers__mutmut['_mutmut_orig'] = x__providers__mutmut_orig # type: ignore # mutmut generated
mutants_x__providers__mutmut['x__providers__mutmut_1'] = x__providers__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_provider_credentials__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_provider_credentials__mutmut)
def get_provider_credentials(provider: str) -> dict[str, str]:
    """Return the stored credentials for a provider (empty when unset)."""
    return _providers().get(provider, {})


def x_get_provider_credentials__mutmut_orig(provider: str) -> dict[str, str]:
    """Return the stored credentials for a provider (empty when unset)."""
    return _providers().get(provider, {})


def x_get_provider_credentials__mutmut_1(provider: str) -> dict[str, str]:
    """Return the stored credentials for a provider (empty when unset)."""
    return _providers().get(None, {})


def x_get_provider_credentials__mutmut_2(provider: str) -> dict[str, str]:
    """Return the stored credentials for a provider (empty when unset)."""
    return _providers().get(provider, None)


def x_get_provider_credentials__mutmut_3(provider: str) -> dict[str, str]:
    """Return the stored credentials for a provider (empty when unset)."""
    return _providers().get({})


def x_get_provider_credentials__mutmut_4(provider: str) -> dict[str, str]:
    """Return the stored credentials for a provider (empty when unset)."""
    return _providers().get(provider, )

mutants_x_get_provider_credentials__mutmut['_mutmut_orig'] = x_get_provider_credentials__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_provider_credentials__mutmut['x_get_provider_credentials__mutmut_1'] = x_get_provider_credentials__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_provider_credentials__mutmut['x_get_provider_credentials__mutmut_2'] = x_get_provider_credentials__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_provider_credentials__mutmut['x_get_provider_credentials__mutmut_3'] = x_get_provider_credentials__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_provider_credentials__mutmut['x_get_provider_credentials__mutmut_4'] = x_get_provider_credentials__mutmut_4 # type: ignore # mutmut generated
mutants_x_set_provider_credentials__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_set_provider_credentials__mutmut)
def set_provider_credentials(provider: str, values: dict[str, str]) -> None:
    """Persist a provider's credentials (empty values are dropped)."""
    config = load_config()
    providers = _providers_from(config)
    providers[provider] = {key: value for key, value in values.items() if value}
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_set_provider_credentials__mutmut_orig(provider: str, values: dict[str, str]) -> None:
    """Persist a provider's credentials (empty values are dropped)."""
    config = load_config()
    providers = _providers_from(config)
    providers[provider] = {key: value for key, value in values.items() if value}
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_set_provider_credentials__mutmut_1(provider: str, values: dict[str, str]) -> None:
    """Persist a provider's credentials (empty values are dropped)."""
    config = None
    providers = _providers_from(config)
    providers[provider] = {key: value for key, value in values.items() if value}
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_set_provider_credentials__mutmut_2(provider: str, values: dict[str, str]) -> None:
    """Persist a provider's credentials (empty values are dropped)."""
    config = load_config()
    providers = None
    providers[provider] = {key: value for key, value in values.items() if value}
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_set_provider_credentials__mutmut_3(provider: str, values: dict[str, str]) -> None:
    """Persist a provider's credentials (empty values are dropped)."""
    config = load_config()
    providers = _providers_from(None)
    providers[provider] = {key: value for key, value in values.items() if value}
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_set_provider_credentials__mutmut_4(provider: str, values: dict[str, str]) -> None:
    """Persist a provider's credentials (empty values are dropped)."""
    config = load_config()
    providers = _providers_from(config)
    providers[provider] = None
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_set_provider_credentials__mutmut_5(provider: str, values: dict[str, str]) -> None:
    """Persist a provider's credentials (empty values are dropped)."""
    config = load_config()
    providers = _providers_from(config)
    providers[provider] = {key: value for key, value in values.items() if value}
    config[_PROVIDERS_KEY] = None
    save_config(config)


def x_set_provider_credentials__mutmut_6(provider: str, values: dict[str, str]) -> None:
    """Persist a provider's credentials (empty values are dropped)."""
    config = load_config()
    providers = _providers_from(config)
    providers[provider] = {key: value for key, value in values.items() if value}
    config[_PROVIDERS_KEY] = providers
    save_config(None)

mutants_x_set_provider_credentials__mutmut['_mutmut_orig'] = x_set_provider_credentials__mutmut_orig # type: ignore # mutmut generated
mutants_x_set_provider_credentials__mutmut['x_set_provider_credentials__mutmut_1'] = x_set_provider_credentials__mutmut_1 # type: ignore # mutmut generated
mutants_x_set_provider_credentials__mutmut['x_set_provider_credentials__mutmut_2'] = x_set_provider_credentials__mutmut_2 # type: ignore # mutmut generated
mutants_x_set_provider_credentials__mutmut['x_set_provider_credentials__mutmut_3'] = x_set_provider_credentials__mutmut_3 # type: ignore # mutmut generated
mutants_x_set_provider_credentials__mutmut['x_set_provider_credentials__mutmut_4'] = x_set_provider_credentials__mutmut_4 # type: ignore # mutmut generated
mutants_x_set_provider_credentials__mutmut['x_set_provider_credentials__mutmut_5'] = x_set_provider_credentials__mutmut_5 # type: ignore # mutmut generated
mutants_x_set_provider_credentials__mutmut['x_set_provider_credentials__mutmut_6'] = x_set_provider_credentials__mutmut_6 # type: ignore # mutmut generated
mutants_x_clear_provider_credentials__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_clear_provider_credentials__mutmut)
def clear_provider_credentials(provider: str) -> None:
    """Remove a provider's stored credentials."""
    config = load_config()
    providers = _providers_from(config)
    providers.pop(provider, None)
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_clear_provider_credentials__mutmut_orig(provider: str) -> None:
    """Remove a provider's stored credentials."""
    config = load_config()
    providers = _providers_from(config)
    providers.pop(provider, None)
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_clear_provider_credentials__mutmut_1(provider: str) -> None:
    """Remove a provider's stored credentials."""
    config = None
    providers = _providers_from(config)
    providers.pop(provider, None)
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_clear_provider_credentials__mutmut_2(provider: str) -> None:
    """Remove a provider's stored credentials."""
    config = load_config()
    providers = None
    providers.pop(provider, None)
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_clear_provider_credentials__mutmut_3(provider: str) -> None:
    """Remove a provider's stored credentials."""
    config = load_config()
    providers = _providers_from(None)
    providers.pop(provider, None)
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_clear_provider_credentials__mutmut_4(provider: str) -> None:
    """Remove a provider's stored credentials."""
    config = load_config()
    providers = _providers_from(config)
    providers.pop(None, None)
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_clear_provider_credentials__mutmut_5(provider: str) -> None:
    """Remove a provider's stored credentials."""
    config = load_config()
    providers = _providers_from(config)
    providers.pop(None)
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_clear_provider_credentials__mutmut_6(provider: str) -> None:
    """Remove a provider's stored credentials."""
    config = load_config()
    providers = _providers_from(config)
    providers.pop(provider, )
    config[_PROVIDERS_KEY] = providers
    save_config(config)


def x_clear_provider_credentials__mutmut_7(provider: str) -> None:
    """Remove a provider's stored credentials."""
    config = load_config()
    providers = _providers_from(config)
    providers.pop(provider, None)
    config[_PROVIDERS_KEY] = None
    save_config(config)


def x_clear_provider_credentials__mutmut_8(provider: str) -> None:
    """Remove a provider's stored credentials."""
    config = load_config()
    providers = _providers_from(config)
    providers.pop(provider, None)
    config[_PROVIDERS_KEY] = providers
    save_config(None)

mutants_x_clear_provider_credentials__mutmut['_mutmut_orig'] = x_clear_provider_credentials__mutmut_orig # type: ignore # mutmut generated
mutants_x_clear_provider_credentials__mutmut['x_clear_provider_credentials__mutmut_1'] = x_clear_provider_credentials__mutmut_1 # type: ignore # mutmut generated
mutants_x_clear_provider_credentials__mutmut['x_clear_provider_credentials__mutmut_2'] = x_clear_provider_credentials__mutmut_2 # type: ignore # mutmut generated
mutants_x_clear_provider_credentials__mutmut['x_clear_provider_credentials__mutmut_3'] = x_clear_provider_credentials__mutmut_3 # type: ignore # mutmut generated
mutants_x_clear_provider_credentials__mutmut['x_clear_provider_credentials__mutmut_4'] = x_clear_provider_credentials__mutmut_4 # type: ignore # mutmut generated
mutants_x_clear_provider_credentials__mutmut['x_clear_provider_credentials__mutmut_5'] = x_clear_provider_credentials__mutmut_5 # type: ignore # mutmut generated
mutants_x_clear_provider_credentials__mutmut['x_clear_provider_credentials__mutmut_6'] = x_clear_provider_credentials__mutmut_6 # type: ignore # mutmut generated
mutants_x_clear_provider_credentials__mutmut['x_clear_provider_credentials__mutmut_7'] = x_clear_provider_credentials__mutmut_7 # type: ignore # mutmut generated
mutants_x_clear_provider_credentials__mutmut['x_clear_provider_credentials__mutmut_8'] = x_clear_provider_credentials__mutmut_8 # type: ignore # mutmut generated


def list_provider_credentials() -> dict[str, dict[str, str]]:
    """All providers that have stored credentials."""
    return _providers()
mutants_x_credential_fields__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_credential_fields__mutmut)
def credential_fields(provider: str) -> list[tuple[str, str]]:
    """Ordered (credential key, human label) pairs a provider needs.

    Used by the TUI to render the credential form for a provider. Returns an
    empty list for an unknown provider.
    """
    mapping = _ENV_BY_PROVIDER.get(provider)
    if mapping is None:
        return []
    return [(key, _human_label(key)) for key in mapping]


def x_credential_fields__mutmut_orig(provider: str) -> list[tuple[str, str]]:
    """Ordered (credential key, human label) pairs a provider needs.

    Used by the TUI to render the credential form for a provider. Returns an
    empty list for an unknown provider.
    """
    mapping = _ENV_BY_PROVIDER.get(provider)
    if mapping is None:
        return []
    return [(key, _human_label(key)) for key in mapping]


def x_credential_fields__mutmut_1(provider: str) -> list[tuple[str, str]]:
    """Ordered (credential key, human label) pairs a provider needs.

    Used by the TUI to render the credential form for a provider. Returns an
    empty list for an unknown provider.
    """
    mapping = None
    if mapping is None:
        return []
    return [(key, _human_label(key)) for key in mapping]


def x_credential_fields__mutmut_2(provider: str) -> list[tuple[str, str]]:
    """Ordered (credential key, human label) pairs a provider needs.

    Used by the TUI to render the credential form for a provider. Returns an
    empty list for an unknown provider.
    """
    mapping = _ENV_BY_PROVIDER.get(None)
    if mapping is None:
        return []
    return [(key, _human_label(key)) for key in mapping]


def x_credential_fields__mutmut_3(provider: str) -> list[tuple[str, str]]:
    """Ordered (credential key, human label) pairs a provider needs.

    Used by the TUI to render the credential form for a provider. Returns an
    empty list for an unknown provider.
    """
    mapping = _ENV_BY_PROVIDER.get(provider)
    if mapping is not None:
        return []
    return [(key, _human_label(key)) for key in mapping]


def x_credential_fields__mutmut_4(provider: str) -> list[tuple[str, str]]:
    """Ordered (credential key, human label) pairs a provider needs.

    Used by the TUI to render the credential form for a provider. Returns an
    empty list for an unknown provider.
    """
    mapping = _ENV_BY_PROVIDER.get(provider)
    if mapping is None:
        return []
    return [(key, _human_label(None)) for key in mapping]

mutants_x_credential_fields__mutmut['_mutmut_orig'] = x_credential_fields__mutmut_orig # type: ignore # mutmut generated
mutants_x_credential_fields__mutmut['x_credential_fields__mutmut_1'] = x_credential_fields__mutmut_1 # type: ignore # mutmut generated
mutants_x_credential_fields__mutmut['x_credential_fields__mutmut_2'] = x_credential_fields__mutmut_2 # type: ignore # mutmut generated
mutants_x_credential_fields__mutmut['x_credential_fields__mutmut_3'] = x_credential_fields__mutmut_3 # type: ignore # mutmut generated
mutants_x_credential_fields__mutmut['x_credential_fields__mutmut_4'] = x_credential_fields__mutmut_4 # type: ignore # mutmut generated
mutants_x__human_label__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__human_label__mutmut)
def _human_label(key: str) -> str:
    return key.replace("_", " ").title()


def x__human_label__mutmut_orig(key: str) -> str:
    return key.replace("_", " ").title()


def x__human_label__mutmut_1(key: str) -> str:
    return key.replace(None, " ").title()


def x__human_label__mutmut_2(key: str) -> str:
    return key.replace("_", None).title()


def x__human_label__mutmut_3(key: str) -> str:
    return key.replace(" ").title()


def x__human_label__mutmut_4(key: str) -> str:
    return key.replace("_", ).title()


def x__human_label__mutmut_5(key: str) -> str:
    return key.replace("XX_XX", " ").title()


def x__human_label__mutmut_6(key: str) -> str:
    return key.replace("_", "XX XX").title()

mutants_x__human_label__mutmut['_mutmut_orig'] = x__human_label__mutmut_orig # type: ignore # mutmut generated
mutants_x__human_label__mutmut['x__human_label__mutmut_1'] = x__human_label__mutmut_1 # type: ignore # mutmut generated
mutants_x__human_label__mutmut['x__human_label__mutmut_2'] = x__human_label__mutmut_2 # type: ignore # mutmut generated
mutants_x__human_label__mutmut['x__human_label__mutmut_3'] = x__human_label__mutmut_3 # type: ignore # mutmut generated
mutants_x__human_label__mutmut['x__human_label__mutmut_4'] = x__human_label__mutmut_4 # type: ignore # mutmut generated
mutants_x__human_label__mutmut['x__human_label__mutmut_5'] = x__human_label__mutmut_5 # type: ignore # mutmut generated
mutants_x__human_label__mutmut['x__human_label__mutmut_6'] = x__human_label__mutmut_6 # type: ignore # mutmut generated
mutants_x_apply_provider_env__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_apply_provider_env__mutmut)
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


def x_apply_provider_env__mutmut_orig(provider: str) -> dict[str, str]:
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


def x_apply_provider_env__mutmut_1(provider: str) -> dict[str, str]:
    """Inject stored credentials as the SDK-recognised env vars.

    Returns the env vars that were set (empty when the provider is unknown or
    has no stored credentials).
    """
    mapping = None
    if mapping is None:
        return {}
    credentials = get_provider_credentials(provider)
    applied: dict[str, str] = {}
    for key, env_name in mapping.items():
        if key in credentials:
            os.environ[env_name] = credentials[key]
            applied[env_name] = credentials[key]
    return applied


def x_apply_provider_env__mutmut_2(provider: str) -> dict[str, str]:
    """Inject stored credentials as the SDK-recognised env vars.

    Returns the env vars that were set (empty when the provider is unknown or
    has no stored credentials).
    """
    mapping = _ENV_BY_PROVIDER.get(None)
    if mapping is None:
        return {}
    credentials = get_provider_credentials(provider)
    applied: dict[str, str] = {}
    for key, env_name in mapping.items():
        if key in credentials:
            os.environ[env_name] = credentials[key]
            applied[env_name] = credentials[key]
    return applied


def x_apply_provider_env__mutmut_3(provider: str) -> dict[str, str]:
    """Inject stored credentials as the SDK-recognised env vars.

    Returns the env vars that were set (empty when the provider is unknown or
    has no stored credentials).
    """
    mapping = _ENV_BY_PROVIDER.get(provider)
    if mapping is not None:
        return {}
    credentials = get_provider_credentials(provider)
    applied: dict[str, str] = {}
    for key, env_name in mapping.items():
        if key in credentials:
            os.environ[env_name] = credentials[key]
            applied[env_name] = credentials[key]
    return applied


def x_apply_provider_env__mutmut_4(provider: str) -> dict[str, str]:
    """Inject stored credentials as the SDK-recognised env vars.

    Returns the env vars that were set (empty when the provider is unknown or
    has no stored credentials).
    """
    mapping = _ENV_BY_PROVIDER.get(provider)
    if mapping is None:
        return {}
    credentials = None
    applied: dict[str, str] = {}
    for key, env_name in mapping.items():
        if key in credentials:
            os.environ[env_name] = credentials[key]
            applied[env_name] = credentials[key]
    return applied


def x_apply_provider_env__mutmut_5(provider: str) -> dict[str, str]:
    """Inject stored credentials as the SDK-recognised env vars.

    Returns the env vars that were set (empty when the provider is unknown or
    has no stored credentials).
    """
    mapping = _ENV_BY_PROVIDER.get(provider)
    if mapping is None:
        return {}
    credentials = get_provider_credentials(None)
    applied: dict[str, str] = {}
    for key, env_name in mapping.items():
        if key in credentials:
            os.environ[env_name] = credentials[key]
            applied[env_name] = credentials[key]
    return applied


def x_apply_provider_env__mutmut_6(provider: str) -> dict[str, str]:
    """Inject stored credentials as the SDK-recognised env vars.

    Returns the env vars that were set (empty when the provider is unknown or
    has no stored credentials).
    """
    mapping = _ENV_BY_PROVIDER.get(provider)
    if mapping is None:
        return {}
    credentials = get_provider_credentials(provider)
    applied: dict[str, str] = None
    for key, env_name in mapping.items():
        if key in credentials:
            os.environ[env_name] = credentials[key]
            applied[env_name] = credentials[key]
    return applied


def x_apply_provider_env__mutmut_7(provider: str) -> dict[str, str]:
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
        if key not in credentials:
            os.environ[env_name] = credentials[key]
            applied[env_name] = credentials[key]
    return applied


def x_apply_provider_env__mutmut_8(provider: str) -> dict[str, str]:
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
            os.environ[env_name] = None
            applied[env_name] = credentials[key]
    return applied


def x_apply_provider_env__mutmut_9(provider: str) -> dict[str, str]:
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
            applied[env_name] = None
    return applied

mutants_x_apply_provider_env__mutmut['_mutmut_orig'] = x_apply_provider_env__mutmut_orig # type: ignore # mutmut generated
mutants_x_apply_provider_env__mutmut['x_apply_provider_env__mutmut_1'] = x_apply_provider_env__mutmut_1 # type: ignore # mutmut generated
mutants_x_apply_provider_env__mutmut['x_apply_provider_env__mutmut_2'] = x_apply_provider_env__mutmut_2 # type: ignore # mutmut generated
mutants_x_apply_provider_env__mutmut['x_apply_provider_env__mutmut_3'] = x_apply_provider_env__mutmut_3 # type: ignore # mutmut generated
mutants_x_apply_provider_env__mutmut['x_apply_provider_env__mutmut_4'] = x_apply_provider_env__mutmut_4 # type: ignore # mutmut generated
mutants_x_apply_provider_env__mutmut['x_apply_provider_env__mutmut_5'] = x_apply_provider_env__mutmut_5 # type: ignore # mutmut generated
mutants_x_apply_provider_env__mutmut['x_apply_provider_env__mutmut_6'] = x_apply_provider_env__mutmut_6 # type: ignore # mutmut generated
mutants_x_apply_provider_env__mutmut['x_apply_provider_env__mutmut_7'] = x_apply_provider_env__mutmut_7 # type: ignore # mutmut generated
mutants_x_apply_provider_env__mutmut['x_apply_provider_env__mutmut_8'] = x_apply_provider_env__mutmut_8 # type: ignore # mutmut generated
mutants_x_apply_provider_env__mutmut['x_apply_provider_env__mutmut_9'] = x_apply_provider_env__mutmut_9 # type: ignore # mutmut generated
