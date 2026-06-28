import os
from pathlib import Path

import yaml

CONFIG_PATH = Path.home() / ".hexawyn" / "config.yaml"
RUNTIME_ENDPOINT_ENV_VAR = "HEXAWYN_RUNTIME_ENDPOINT"


def load_config() -> dict[str, object]:
    """Load config from ~/.hexawyn/config.yaml. Returns empty dict if not found."""
    if not CONFIG_PATH.exists():
        return {}
    with open(CONFIG_PATH) as f:
        content: object = yaml.safe_load(f)
        if isinstance(content, dict):
            return content
        return {}


def save_config(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml. Creates directory if needed."""
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)


def get_api_key() -> str | None:
    """
    Get LLM API key.
    Priority: LLM_API_KEY env var > DEEPSEEK_API_KEY env var > ANTHROPIC_API_KEY env var > config.yaml
    """
    for env_var in ("LLM_API_KEY", "DEEPSEEK_API_KEY", "ANTHROPIC_API_KEY"):
        env_key = os.environ.get(env_var)
        if env_key:
            return env_key
    config_key = load_config().get("api_key")
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
    Returns "embedded" (default) or "remote".
    """
    if _get_runtime_endpoint_from_env() is not None:
        return "remote"
    config = load_config()
    runtime_section = config.get("runtime")
    if not isinstance(runtime_section, dict):
        return "embedded"
    mode = runtime_section.get("mode")
    if mode in ("embedded", "remote"):
        return str(mode)
    return "embedded"


def get_runtime_endpoint() -> str | None:
    """
    Get the remote runtime endpoint from environment or config.yaml.
    Returns None if mode is embedded or endpoint is not configured.
    """
    env_endpoint = _get_runtime_endpoint_from_env()
    if env_endpoint is not None:
        return env_endpoint
    config = load_config()
    runtime_section = config.get("runtime")
    if not isinstance(runtime_section, dict):
        return None
    endpoint = runtime_section.get("endpoint")
    if isinstance(endpoint, str):
        return endpoint
    return None


def _get_runtime_endpoint_from_env() -> str | None:
    endpoint = os.environ.get(RUNTIME_ENDPOINT_ENV_VAR)
    if endpoint:
        return endpoint
    return None
