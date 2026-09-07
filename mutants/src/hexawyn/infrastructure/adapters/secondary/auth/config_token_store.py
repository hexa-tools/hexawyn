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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁConfigTokenStoreǁget_token__mutmut: MutantDict = {}  # type: ignore
mutants_xǁConfigTokenStoreǁsave_token__mutmut: MutantDict = {}  # type: ignore


class ConfigTokenStore:
    """Reads/writes the cloud token via the existing config manager."""

    @_mutmut_mutated(mutants_xǁConfigTokenStoreǁget_token__mutmut)
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

    def xǁConfigTokenStoreǁget_token__mutmut_orig(self) -> str | None:
        """Resolve token: HEXAWYN_TOKEN env › config.yaml hexawyn_token."""
        env_token = os.environ.get(TOKEN_ENV_VAR)
        if env_token:
            return env_token
        config = load_config()
        config_token = config.get(CONFIG_TOKEN_KEY)
        if isinstance(config_token, str) and config_token:
            return config_token
        return None

    def xǁConfigTokenStoreǁget_token__mutmut_1(self) -> str | None:
        """Resolve token: HEXAWYN_TOKEN env › config.yaml hexawyn_token."""
        env_token = None
        if env_token:
            return env_token
        config = load_config()
        config_token = config.get(CONFIG_TOKEN_KEY)
        if isinstance(config_token, str) and config_token:
            return config_token
        return None

    def xǁConfigTokenStoreǁget_token__mutmut_2(self) -> str | None:
        """Resolve token: HEXAWYN_TOKEN env › config.yaml hexawyn_token."""
        env_token = os.environ.get(None)
        if env_token:
            return env_token
        config = load_config()
        config_token = config.get(CONFIG_TOKEN_KEY)
        if isinstance(config_token, str) and config_token:
            return config_token
        return None

    def xǁConfigTokenStoreǁget_token__mutmut_3(self) -> str | None:
        """Resolve token: HEXAWYN_TOKEN env › config.yaml hexawyn_token."""
        env_token = os.environ.get(TOKEN_ENV_VAR)
        if env_token:
            return env_token
        config = None
        config_token = config.get(CONFIG_TOKEN_KEY)
        if isinstance(config_token, str) and config_token:
            return config_token
        return None

    def xǁConfigTokenStoreǁget_token__mutmut_4(self) -> str | None:
        """Resolve token: HEXAWYN_TOKEN env › config.yaml hexawyn_token."""
        env_token = os.environ.get(TOKEN_ENV_VAR)
        if env_token:
            return env_token
        config = load_config()
        config_token = None
        if isinstance(config_token, str) and config_token:
            return config_token
        return None

    def xǁConfigTokenStoreǁget_token__mutmut_5(self) -> str | None:
        """Resolve token: HEXAWYN_TOKEN env › config.yaml hexawyn_token."""
        env_token = os.environ.get(TOKEN_ENV_VAR)
        if env_token:
            return env_token
        config = load_config()
        config_token = config.get(None)
        if isinstance(config_token, str) and config_token:
            return config_token
        return None

    def xǁConfigTokenStoreǁget_token__mutmut_6(self) -> str | None:
        """Resolve token: HEXAWYN_TOKEN env › config.yaml hexawyn_token."""
        env_token = os.environ.get(TOKEN_ENV_VAR)
        if env_token:
            return env_token
        config = load_config()
        config_token = config.get(CONFIG_TOKEN_KEY)
        if isinstance(config_token, str) or config_token:
            return config_token
        return None

    @_mutmut_mutated(mutants_xǁConfigTokenStoreǁsave_token__mutmut)
    def save_token(self, token: str) -> None:
        """Persist a validated token to config.yaml."""
        config = load_config()
        config[CONFIG_TOKEN_KEY] = token
        save_config(config)

    def xǁConfigTokenStoreǁsave_token__mutmut_orig(self, token: str) -> None:
        """Persist a validated token to config.yaml."""
        config = load_config()
        config[CONFIG_TOKEN_KEY] = token
        save_config(config)

    def xǁConfigTokenStoreǁsave_token__mutmut_1(self, token: str) -> None:
        """Persist a validated token to config.yaml."""
        config = None
        config[CONFIG_TOKEN_KEY] = token
        save_config(config)

    def xǁConfigTokenStoreǁsave_token__mutmut_2(self, token: str) -> None:
        """Persist a validated token to config.yaml."""
        config = load_config()
        config[CONFIG_TOKEN_KEY] = None
        save_config(config)

    def xǁConfigTokenStoreǁsave_token__mutmut_3(self, token: str) -> None:
        """Persist a validated token to config.yaml."""
        config = load_config()
        config[CONFIG_TOKEN_KEY] = token
        save_config(None)

mutants_xǁConfigTokenStoreǁget_token__mutmut['_mutmut_orig'] = ConfigTokenStore.xǁConfigTokenStoreǁget_token__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConfigTokenStoreǁget_token__mutmut['xǁConfigTokenStoreǁget_token__mutmut_1'] = ConfigTokenStore.xǁConfigTokenStoreǁget_token__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConfigTokenStoreǁget_token__mutmut['xǁConfigTokenStoreǁget_token__mutmut_2'] = ConfigTokenStore.xǁConfigTokenStoreǁget_token__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConfigTokenStoreǁget_token__mutmut['xǁConfigTokenStoreǁget_token__mutmut_3'] = ConfigTokenStore.xǁConfigTokenStoreǁget_token__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConfigTokenStoreǁget_token__mutmut['xǁConfigTokenStoreǁget_token__mutmut_4'] = ConfigTokenStore.xǁConfigTokenStoreǁget_token__mutmut_4 # type: ignore # mutmut generated
mutants_xǁConfigTokenStoreǁget_token__mutmut['xǁConfigTokenStoreǁget_token__mutmut_5'] = ConfigTokenStore.xǁConfigTokenStoreǁget_token__mutmut_5 # type: ignore # mutmut generated
mutants_xǁConfigTokenStoreǁget_token__mutmut['xǁConfigTokenStoreǁget_token__mutmut_6'] = ConfigTokenStore.xǁConfigTokenStoreǁget_token__mutmut_6 # type: ignore # mutmut generated

mutants_xǁConfigTokenStoreǁsave_token__mutmut['_mutmut_orig'] = ConfigTokenStore.xǁConfigTokenStoreǁsave_token__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConfigTokenStoreǁsave_token__mutmut['xǁConfigTokenStoreǁsave_token__mutmut_1'] = ConfigTokenStore.xǁConfigTokenStoreǁsave_token__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConfigTokenStoreǁsave_token__mutmut['xǁConfigTokenStoreǁsave_token__mutmut_2'] = ConfigTokenStore.xǁConfigTokenStoreǁsave_token__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConfigTokenStoreǁsave_token__mutmut['xǁConfigTokenStoreǁsave_token__mutmut_3'] = ConfigTokenStore.xǁConfigTokenStoreǁsave_token__mutmut_3 # type: ignore # mutmut generated
