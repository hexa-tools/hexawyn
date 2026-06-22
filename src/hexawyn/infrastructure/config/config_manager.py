import os
from pathlib import Path

import yaml

CONFIG_PATH = Path.home() / ".hexawyn" / "config.yaml"


def load_config() -> dict[str, str | int | bool]:
    """Load config from ~/.hexawyn/config.yaml. Returns empty dict if not found."""
    if not CONFIG_PATH.exists():
        return {}
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f) or {}


def save_config(config: dict[str, str | int | bool]) -> None:
    """Save config to ~/.hexawyn/config.yaml. Creates directory if needed."""
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)


def get_api_key() -> str | None:
    """
    Get Anthropic API key.
    Priority: ANTHROPIC_API_KEY env var > config.yaml
    """
    env_key = os.environ.get("ANTHROPIC_API_KEY")
    if env_key:
        return env_key
    config_key = load_config().get("api_key")
    if isinstance(config_key, str):
        return config_key
    return None


def save_api_key(key: str) -> None:
    """Persist API key to config.yaml."""
    config = load_config()
    config["api_key"] = key
    save_config(config)
