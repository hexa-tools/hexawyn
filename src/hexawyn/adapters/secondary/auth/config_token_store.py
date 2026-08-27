"""Config-backed token store for Hexawyn Cloud authentication.

Persists the hexawyn cloud token in ~/.hexawyn/config.yaml using the
existing configuration mechanism. The HEXAWYN_TOKEN environment variable
takes precedence over the config file and is never persisted here.
"""

from __future__ import annotations

import os

from hexawyn.infrastructure.config.config_manager import load_config, save_config

TOKEN_ENV_VAR = "HEXAWYN_TOKEN"
CONFIG_TOKEN_KEY = "hexawyn_token"


class ConfigTokenStore:
    """Reads/writes the cloud token via the existing config manager."""

    def get_token(self) -> str | None:
        """Resolve token: HEXAWYN_TOKEN env › config.yaml hexawyn_token."""
        env_token = os.environ.get(TOKEN_ENV_VAR)
        if env_token:
            return env_token
        config = load_config()
        config_token = config.get(CONFIG_TOKEN_KEY)
        if isinstance(config_token, str) and config_token:
            return config_token
        return None

    def save_token(self, token: str) -> None:
        """Persist a validated token to config.yaml."""
        config = load_config()
        config[CONFIG_TOKEN_KEY] = token
        save_config(config)
