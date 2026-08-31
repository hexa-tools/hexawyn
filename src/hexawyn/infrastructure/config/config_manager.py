import os
from pathlib import Path

import yaml

from hexawyn.domain.errors import HexawynError
from hexawyn.infrastructure.config.llm_providers import LLM_PROVIDERS

CONFIG_PATH = Path.home() / ".hexawyn" / "config.yaml"
DEFAULT_RUNTIME_ENDPOINT = "https://api.hexawyn.com"
RUNTIME_ENDPOINT_ENV_VAR = "HEXAWYN_RUNTIME_ENDPOINT"
RUNTIME_MODE_ENV_VAR = "HEXAWYN_RUNTIME_MODE"


class ConfigCorruptedError(HexawynError):
    """Raised when ~/.hexawyn/config.yaml exists but cannot be parsed as YAML."""

    def __init__(self, path: Path) -> None:
        super().__init__(
            f"config.yaml is corrupted, see {path} — fix or delete it to reset the config."
        )


def load_config() -> dict[str, object]:
    """Load config from ~/.hexawyn/config.yaml.

    Returns an empty dict when the file is absent. Raises ConfigCorruptedError
    when the file exists but is not valid YAML (never silently drops config).
    """
    if not CONFIG_PATH.exists():
        return {}
    try:
        with open(CONFIG_PATH) as f:
            content: object = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        raise ConfigCorruptedError(CONFIG_PATH) from exc
    if isinstance(content, dict):
        return content
    return {}


def save_config(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def _env_key_for_provider(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["name"] == provider:
            return provider_entry["env_key"]
    keyed_entry = LLM_PROVIDERS.get(provider)
    if keyed_entry is not None:
        return keyed_entry["env_key"]
    return None


def get_api_key() -> str | None:
    """
    Get the LLM API key for the *configured* provider.

    Priority:
      1. env var dedicated to the configured provider (e.g. OPENAI_API_KEY).
      2. LLM_API_KEY as a voluntary universal override.
      3. api_key stored in config.yaml.
    A leftover env var for a different provider (e.g. DEEPSEEK_API_KEY while
    llm_provider is OpenAI) is intentionally ignored.
    """
    config = load_config()
    provider = config.get("llm_provider")
    if isinstance(provider, str):
        provider_env = _env_key_for_provider(provider)
        if provider_env is not None:
            provider_key = os.environ.get(provider_env)
            if provider_key:
                return provider_key
    llm_override = os.environ.get("LLM_API_KEY")
    if llm_override:
        return llm_override
    config_key = config.get("api_key")
    if isinstance(config_key, str):
        return config_key
    return None


def get_llm_config() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = config.get("llm_base_url")
    api_key = get_api_key()
    result: dict[str, str] = {}
    if isinstance(provider, str):
        result["provider"] = provider
    if isinstance(base_url, str):
        result["base_url"] = base_url
    if api_key:
        result["api_key"] = api_key
    return result


def save_llm_config(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["llm_provider"] = provider
    config["llm_base_url"] = base_url
    config["api_key"] = api_key
    save_config(config)


def get_runtime_mode() -> str:
    """
    Get the runtime mode from environment or config.yaml.
    Returns "remote" by default (production), "embedded" if explicitly configured.
    """
    env_mode = os.environ.get(RUNTIME_MODE_ENV_VAR)
    if env_mode in ("embedded", "remote"):
        return env_mode
    if _get_runtime_endpoint_from_env() is not None:
        return "remote"
    config = load_config()
    runtime_section = config.get("runtime")
    if isinstance(runtime_section, dict):
        mode = runtime_section.get("mode")
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def get_runtime_endpoint() -> str | None:
    """
    Get the remote runtime endpoint from environment or config.yaml.
    Falls back to production API URL.
    """
    env_endpoint = _get_runtime_endpoint_from_env()
    if env_endpoint is not None:
        return env_endpoint
    config = load_config()
    runtime_section = config.get("runtime")
    if isinstance(runtime_section, dict):
        endpoint = runtime_section.get("endpoint")
        if isinstance(endpoint, str):
            return endpoint
    return DEFAULT_RUNTIME_ENDPOINT


def _get_runtime_endpoint_from_env() -> str | None:
    endpoint = os.environ.get(RUNTIME_ENDPOINT_ENV_VAR)
    if endpoint:
        return endpoint
    return None
