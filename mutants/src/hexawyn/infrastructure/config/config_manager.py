import os
from pathlib import Path

import yaml

from hexawyn.domain.errors import HexawynError
from hexawyn.infrastructure.config.llm_providers import LLM_PROVIDERS

CONFIG_PATH = Path.home() / ".hexawyn" / "config.yaml"
DEFAULT_RUNTIME_ENDPOINT = "https://api.hexawyn.com"
RUNTIME_ENDPOINT_ENV_VAR = "HEXAWYN_RUNTIME_ENDPOINT"
RUNTIME_MODE_ENV_VAR = "HEXAWYN_RUNTIME_MODE"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁConfigCorruptedErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class ConfigCorruptedError(HexawynError):
    """Raised when ~/.hexawyn/config.yaml exists but cannot be parsed as YAML."""

    @_mutmut_mutated(mutants_xǁConfigCorruptedErrorǁ__init____mutmut)
    def __init__(self, path: Path) -> None:
        super().__init__(
            f"config.yaml is corrupted, see {path} — fix or delete it to reset the config."
        )

    def xǁConfigCorruptedErrorǁ__init____mutmut_orig(self, path: Path) -> None:
        super().__init__(
            f"config.yaml is corrupted, see {path} — fix or delete it to reset the config."
        )

    def xǁConfigCorruptedErrorǁ__init____mutmut_1(self, path: Path) -> None:
        super().__init__(
            None
        )

mutants_xǁConfigCorruptedErrorǁ__init____mutmut['_mutmut_orig'] = ConfigCorruptedError.xǁConfigCorruptedErrorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁConfigCorruptedErrorǁ__init____mutmut['xǁConfigCorruptedErrorǁ__init____mutmut_1'] = ConfigCorruptedError.xǁConfigCorruptedErrorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_x_load_config__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_load_config__mutmut)
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


def x_load_config__mutmut_orig() -> dict[str, object]:
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


def x_load_config__mutmut_1() -> dict[str, object]:
    """Load config from ~/.hexawyn/config.yaml.

    Returns an empty dict when the file is absent. Raises ConfigCorruptedError
    when the file exists but is not valid YAML (never silently drops config).
    """
    if CONFIG_PATH.exists():
        return {}
    try:
        with open(CONFIG_PATH) as f:
            content: object = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        raise ConfigCorruptedError(CONFIG_PATH) from exc
    if isinstance(content, dict):
        return content
    return {}


def x_load_config__mutmut_2() -> dict[str, object]:
    """Load config from ~/.hexawyn/config.yaml.

    Returns an empty dict when the file is absent. Raises ConfigCorruptedError
    when the file exists but is not valid YAML (never silently drops config).
    """
    if not CONFIG_PATH.exists():
        return {}
    try:
        with open(None) as f:
            content: object = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        raise ConfigCorruptedError(CONFIG_PATH) from exc
    if isinstance(content, dict):
        return content
    return {}


def x_load_config__mutmut_3() -> dict[str, object]:
    """Load config from ~/.hexawyn/config.yaml.

    Returns an empty dict when the file is absent. Raises ConfigCorruptedError
    when the file exists but is not valid YAML (never silently drops config).
    """
    if not CONFIG_PATH.exists():
        return {}
    try:
        with open(CONFIG_PATH) as f:
            content: object = None
    except yaml.YAMLError as exc:
        raise ConfigCorruptedError(CONFIG_PATH) from exc
    if isinstance(content, dict):
        return content
    return {}


def x_load_config__mutmut_4() -> dict[str, object]:
    """Load config from ~/.hexawyn/config.yaml.

    Returns an empty dict when the file is absent. Raises ConfigCorruptedError
    when the file exists but is not valid YAML (never silently drops config).
    """
    if not CONFIG_PATH.exists():
        return {}
    try:
        with open(CONFIG_PATH) as f:
            content: object = yaml.safe_load(None)
    except yaml.YAMLError as exc:
        raise ConfigCorruptedError(CONFIG_PATH) from exc
    if isinstance(content, dict):
        return content
    return {}


def x_load_config__mutmut_5() -> dict[str, object]:
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
        raise ConfigCorruptedError(None) from exc
    if isinstance(content, dict):
        return content
    return {}

mutants_x_load_config__mutmut['_mutmut_orig'] = x_load_config__mutmut_orig # type: ignore # mutmut generated
mutants_x_load_config__mutmut['x_load_config__mutmut_1'] = x_load_config__mutmut_1 # type: ignore # mutmut generated
mutants_x_load_config__mutmut['x_load_config__mutmut_2'] = x_load_config__mutmut_2 # type: ignore # mutmut generated
mutants_x_load_config__mutmut['x_load_config__mutmut_3'] = x_load_config__mutmut_3 # type: ignore # mutmut generated
mutants_x_load_config__mutmut['x_load_config__mutmut_4'] = x_load_config__mutmut_4 # type: ignore # mutmut generated
mutants_x_load_config__mutmut['x_load_config__mutmut_5'] = x_load_config__mutmut_5 # type: ignore # mutmut generated
mutants_x_save_config__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_save_config__mutmut)
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


def x_save_config__mutmut_orig(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_1(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=None, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_2(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=None)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_3(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_4(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, )
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_5(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=False, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_6(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=False)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_7(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(None)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_8(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(449)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_9(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(None, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_10(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, None) as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_11(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open("w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_12(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, ) as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_13(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "XXwXX") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_14(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "W") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_15(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(None, f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_16(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, None)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_17(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(f)
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_18(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, )
    CONFIG_PATH.chmod(0o600)


def x_save_config__mutmut_19(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(None)


def x_save_config__mutmut_20(config: dict[str, object]) -> None:
    """Save config to ~/.hexawyn/config.yaml.

    Creates the directory (0o700) and restricts the file to owner-only read/write
    (0o600) because it can hold API keys and cloud credentials.
    """
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.parent.chmod(0o700)
    with open(CONFIG_PATH, "w") as f:
        yaml.safe_dump(config, f)
    CONFIG_PATH.chmod(385)

mutants_x_save_config__mutmut['_mutmut_orig'] = x_save_config__mutmut_orig # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_1'] = x_save_config__mutmut_1 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_2'] = x_save_config__mutmut_2 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_3'] = x_save_config__mutmut_3 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_4'] = x_save_config__mutmut_4 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_5'] = x_save_config__mutmut_5 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_6'] = x_save_config__mutmut_6 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_7'] = x_save_config__mutmut_7 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_8'] = x_save_config__mutmut_8 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_9'] = x_save_config__mutmut_9 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_10'] = x_save_config__mutmut_10 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_11'] = x_save_config__mutmut_11 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_12'] = x_save_config__mutmut_12 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_13'] = x_save_config__mutmut_13 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_14'] = x_save_config__mutmut_14 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_15'] = x_save_config__mutmut_15 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_16'] = x_save_config__mutmut_16 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_17'] = x_save_config__mutmut_17 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_18'] = x_save_config__mutmut_18 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_19'] = x_save_config__mutmut_19 # type: ignore # mutmut generated
mutants_x_save_config__mutmut['x_save_config__mutmut_20'] = x_save_config__mutmut_20 # type: ignore # mutmut generated
mutants_x__env_key_for_provider__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__env_key_for_provider__mutmut)
def _env_key_for_provider(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["name"] == provider:
            return provider_entry["env_key"]
    keyed_entry = LLM_PROVIDERS.get(provider)
    if keyed_entry is not None:
        return keyed_entry["env_key"]
    return None


def x__env_key_for_provider__mutmut_orig(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["name"] == provider:
            return provider_entry["env_key"]
    keyed_entry = LLM_PROVIDERS.get(provider)
    if keyed_entry is not None:
        return keyed_entry["env_key"]
    return None


def x__env_key_for_provider__mutmut_1(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["XXnameXX"] == provider:
            return provider_entry["env_key"]
    keyed_entry = LLM_PROVIDERS.get(provider)
    if keyed_entry is not None:
        return keyed_entry["env_key"]
    return None


def x__env_key_for_provider__mutmut_2(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["NAME"] == provider:
            return provider_entry["env_key"]
    keyed_entry = LLM_PROVIDERS.get(provider)
    if keyed_entry is not None:
        return keyed_entry["env_key"]
    return None


def x__env_key_for_provider__mutmut_3(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["name"] != provider:
            return provider_entry["env_key"]
    keyed_entry = LLM_PROVIDERS.get(provider)
    if keyed_entry is not None:
        return keyed_entry["env_key"]
    return None


def x__env_key_for_provider__mutmut_4(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["name"] == provider:
            return provider_entry["XXenv_keyXX"]
    keyed_entry = LLM_PROVIDERS.get(provider)
    if keyed_entry is not None:
        return keyed_entry["env_key"]
    return None


def x__env_key_for_provider__mutmut_5(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["name"] == provider:
            return provider_entry["ENV_KEY"]
    keyed_entry = LLM_PROVIDERS.get(provider)
    if keyed_entry is not None:
        return keyed_entry["env_key"]
    return None


def x__env_key_for_provider__mutmut_6(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["name"] == provider:
            return provider_entry["env_key"]
    keyed_entry = None
    if keyed_entry is not None:
        return keyed_entry["env_key"]
    return None


def x__env_key_for_provider__mutmut_7(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["name"] == provider:
            return provider_entry["env_key"]
    keyed_entry = LLM_PROVIDERS.get(None)
    if keyed_entry is not None:
        return keyed_entry["env_key"]
    return None


def x__env_key_for_provider__mutmut_8(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["name"] == provider:
            return provider_entry["env_key"]
    keyed_entry = LLM_PROVIDERS.get(provider)
    if keyed_entry is None:
        return keyed_entry["env_key"]
    return None


def x__env_key_for_provider__mutmut_9(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["name"] == provider:
            return provider_entry["env_key"]
    keyed_entry = LLM_PROVIDERS.get(provider)
    if keyed_entry is not None:
        return keyed_entry["XXenv_keyXX"]
    return None


def x__env_key_for_provider__mutmut_10(provider: str) -> str | None:
    """Resolve the dedicated env var name for a configured LLM provider."""
    for provider_entry in LLM_PROVIDERS.values():
        if provider_entry["name"] == provider:
            return provider_entry["env_key"]
    keyed_entry = LLM_PROVIDERS.get(provider)
    if keyed_entry is not None:
        return keyed_entry["ENV_KEY"]
    return None

mutants_x__env_key_for_provider__mutmut['_mutmut_orig'] = x__env_key_for_provider__mutmut_orig # type: ignore # mutmut generated
mutants_x__env_key_for_provider__mutmut['x__env_key_for_provider__mutmut_1'] = x__env_key_for_provider__mutmut_1 # type: ignore # mutmut generated
mutants_x__env_key_for_provider__mutmut['x__env_key_for_provider__mutmut_2'] = x__env_key_for_provider__mutmut_2 # type: ignore # mutmut generated
mutants_x__env_key_for_provider__mutmut['x__env_key_for_provider__mutmut_3'] = x__env_key_for_provider__mutmut_3 # type: ignore # mutmut generated
mutants_x__env_key_for_provider__mutmut['x__env_key_for_provider__mutmut_4'] = x__env_key_for_provider__mutmut_4 # type: ignore # mutmut generated
mutants_x__env_key_for_provider__mutmut['x__env_key_for_provider__mutmut_5'] = x__env_key_for_provider__mutmut_5 # type: ignore # mutmut generated
mutants_x__env_key_for_provider__mutmut['x__env_key_for_provider__mutmut_6'] = x__env_key_for_provider__mutmut_6 # type: ignore # mutmut generated
mutants_x__env_key_for_provider__mutmut['x__env_key_for_provider__mutmut_7'] = x__env_key_for_provider__mutmut_7 # type: ignore # mutmut generated
mutants_x__env_key_for_provider__mutmut['x__env_key_for_provider__mutmut_8'] = x__env_key_for_provider__mutmut_8 # type: ignore # mutmut generated
mutants_x__env_key_for_provider__mutmut['x__env_key_for_provider__mutmut_9'] = x__env_key_for_provider__mutmut_9 # type: ignore # mutmut generated
mutants_x__env_key_for_provider__mutmut['x__env_key_for_provider__mutmut_10'] = x__env_key_for_provider__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_api_key__mutmut)
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


def x_get_api_key__mutmut_orig() -> str | None:
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


def x_get_api_key__mutmut_1() -> str | None:
    """
    Get the LLM API key for the *configured* provider.

    Priority:
      1. env var dedicated to the configured provider (e.g. OPENAI_API_KEY).
      2. LLM_API_KEY as a voluntary universal override.
      3. api_key stored in config.yaml.
    A leftover env var for a different provider (e.g. DEEPSEEK_API_KEY while
    llm_provider is OpenAI) is intentionally ignored.
    """
    config = None
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


def x_get_api_key__mutmut_2() -> str | None:
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
    provider = None
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


def x_get_api_key__mutmut_3() -> str | None:
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
    provider = config.get(None)
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


def x_get_api_key__mutmut_4() -> str | None:
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
    provider = config.get("XXllm_providerXX")
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


def x_get_api_key__mutmut_5() -> str | None:
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
    provider = config.get("LLM_PROVIDER")
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


def x_get_api_key__mutmut_6() -> str | None:
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
        provider_env = None
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


def x_get_api_key__mutmut_7() -> str | None:
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
        provider_env = _env_key_for_provider(None)
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


def x_get_api_key__mutmut_8() -> str | None:
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
        if provider_env is None:
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


def x_get_api_key__mutmut_9() -> str | None:
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
            provider_key = None
            if provider_key:
                return provider_key
    llm_override = os.environ.get("LLM_API_KEY")
    if llm_override:
        return llm_override
    config_key = config.get("api_key")
    if isinstance(config_key, str):
        return config_key
    return None


def x_get_api_key__mutmut_10() -> str | None:
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
            provider_key = os.environ.get(None)
            if provider_key:
                return provider_key
    llm_override = os.environ.get("LLM_API_KEY")
    if llm_override:
        return llm_override
    config_key = config.get("api_key")
    if isinstance(config_key, str):
        return config_key
    return None


def x_get_api_key__mutmut_11() -> str | None:
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
    llm_override = None
    if llm_override:
        return llm_override
    config_key = config.get("api_key")
    if isinstance(config_key, str):
        return config_key
    return None


def x_get_api_key__mutmut_12() -> str | None:
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
    llm_override = os.environ.get(None)
    if llm_override:
        return llm_override
    config_key = config.get("api_key")
    if isinstance(config_key, str):
        return config_key
    return None


def x_get_api_key__mutmut_13() -> str | None:
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
    llm_override = os.environ.get("XXLLM_API_KEYXX")
    if llm_override:
        return llm_override
    config_key = config.get("api_key")
    if isinstance(config_key, str):
        return config_key
    return None


def x_get_api_key__mutmut_14() -> str | None:
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
    llm_override = os.environ.get("llm_api_key")
    if llm_override:
        return llm_override
    config_key = config.get("api_key")
    if isinstance(config_key, str):
        return config_key
    return None


def x_get_api_key__mutmut_15() -> str | None:
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
    config_key = None
    if isinstance(config_key, str):
        return config_key
    return None


def x_get_api_key__mutmut_16() -> str | None:
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
    config_key = config.get(None)
    if isinstance(config_key, str):
        return config_key
    return None


def x_get_api_key__mutmut_17() -> str | None:
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
    config_key = config.get("XXapi_keyXX")
    if isinstance(config_key, str):
        return config_key
    return None


def x_get_api_key__mutmut_18() -> str | None:
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
    config_key = config.get("API_KEY")
    if isinstance(config_key, str):
        return config_key
    return None

mutants_x_get_api_key__mutmut['_mutmut_orig'] = x_get_api_key__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_1'] = x_get_api_key__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_2'] = x_get_api_key__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_3'] = x_get_api_key__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_4'] = x_get_api_key__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_5'] = x_get_api_key__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_6'] = x_get_api_key__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_7'] = x_get_api_key__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_8'] = x_get_api_key__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_9'] = x_get_api_key__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_10'] = x_get_api_key__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_11'] = x_get_api_key__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_12'] = x_get_api_key__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_13'] = x_get_api_key__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_14'] = x_get_api_key__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_15'] = x_get_api_key__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_16'] = x_get_api_key__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_17'] = x_get_api_key__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_api_key__mutmut['x_get_api_key__mutmut_18'] = x_get_api_key__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_llm_config__mutmut)
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


def x_get_llm_config__mutmut_orig() -> dict[str, str]:
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


def x_get_llm_config__mutmut_1() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = None
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


def x_get_llm_config__mutmut_2() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = None
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


def x_get_llm_config__mutmut_3() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get(None)
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


def x_get_llm_config__mutmut_4() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("XXllm_providerXX")
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


def x_get_llm_config__mutmut_5() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("LLM_PROVIDER")
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


def x_get_llm_config__mutmut_6() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = None
    api_key = get_api_key()
    result: dict[str, str] = {}
    if isinstance(provider, str):
        result["provider"] = provider
    if isinstance(base_url, str):
        result["base_url"] = base_url
    if api_key:
        result["api_key"] = api_key
    return result


def x_get_llm_config__mutmut_7() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = config.get(None)
    api_key = get_api_key()
    result: dict[str, str] = {}
    if isinstance(provider, str):
        result["provider"] = provider
    if isinstance(base_url, str):
        result["base_url"] = base_url
    if api_key:
        result["api_key"] = api_key
    return result


def x_get_llm_config__mutmut_8() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = config.get("XXllm_base_urlXX")
    api_key = get_api_key()
    result: dict[str, str] = {}
    if isinstance(provider, str):
        result["provider"] = provider
    if isinstance(base_url, str):
        result["base_url"] = base_url
    if api_key:
        result["api_key"] = api_key
    return result


def x_get_llm_config__mutmut_9() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = config.get("LLM_BASE_URL")
    api_key = get_api_key()
    result: dict[str, str] = {}
    if isinstance(provider, str):
        result["provider"] = provider
    if isinstance(base_url, str):
        result["base_url"] = base_url
    if api_key:
        result["api_key"] = api_key
    return result


def x_get_llm_config__mutmut_10() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = config.get("llm_base_url")
    api_key = None
    result: dict[str, str] = {}
    if isinstance(provider, str):
        result["provider"] = provider
    if isinstance(base_url, str):
        result["base_url"] = base_url
    if api_key:
        result["api_key"] = api_key
    return result


def x_get_llm_config__mutmut_11() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = config.get("llm_base_url")
    api_key = get_api_key()
    result: dict[str, str] = None
    if isinstance(provider, str):
        result["provider"] = provider
    if isinstance(base_url, str):
        result["base_url"] = base_url
    if api_key:
        result["api_key"] = api_key
    return result


def x_get_llm_config__mutmut_12() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = config.get("llm_base_url")
    api_key = get_api_key()
    result: dict[str, str] = {}
    if isinstance(provider, str):
        result["provider"] = None
    if isinstance(base_url, str):
        result["base_url"] = base_url
    if api_key:
        result["api_key"] = api_key
    return result


def x_get_llm_config__mutmut_13() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = config.get("llm_base_url")
    api_key = get_api_key()
    result: dict[str, str] = {}
    if isinstance(provider, str):
        result["XXproviderXX"] = provider
    if isinstance(base_url, str):
        result["base_url"] = base_url
    if api_key:
        result["api_key"] = api_key
    return result


def x_get_llm_config__mutmut_14() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = config.get("llm_base_url")
    api_key = get_api_key()
    result: dict[str, str] = {}
    if isinstance(provider, str):
        result["PROVIDER"] = provider
    if isinstance(base_url, str):
        result["base_url"] = base_url
    if api_key:
        result["api_key"] = api_key
    return result


def x_get_llm_config__mutmut_15() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = config.get("llm_base_url")
    api_key = get_api_key()
    result: dict[str, str] = {}
    if isinstance(provider, str):
        result["provider"] = provider
    if isinstance(base_url, str):
        result["base_url"] = None
    if api_key:
        result["api_key"] = api_key
    return result


def x_get_llm_config__mutmut_16() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = config.get("llm_base_url")
    api_key = get_api_key()
    result: dict[str, str] = {}
    if isinstance(provider, str):
        result["provider"] = provider
    if isinstance(base_url, str):
        result["XXbase_urlXX"] = base_url
    if api_key:
        result["api_key"] = api_key
    return result


def x_get_llm_config__mutmut_17() -> dict[str, str]:
    """Get LLM provider configuration (base_url + api_key)."""
    config = load_config()
    provider = config.get("llm_provider")
    base_url = config.get("llm_base_url")
    api_key = get_api_key()
    result: dict[str, str] = {}
    if isinstance(provider, str):
        result["provider"] = provider
    if isinstance(base_url, str):
        result["BASE_URL"] = base_url
    if api_key:
        result["api_key"] = api_key
    return result


def x_get_llm_config__mutmut_18() -> dict[str, str]:
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
        result["api_key"] = None
    return result


def x_get_llm_config__mutmut_19() -> dict[str, str]:
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
        result["XXapi_keyXX"] = api_key
    return result


def x_get_llm_config__mutmut_20() -> dict[str, str]:
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
        result["API_KEY"] = api_key
    return result

mutants_x_get_llm_config__mutmut['_mutmut_orig'] = x_get_llm_config__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_1'] = x_get_llm_config__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_2'] = x_get_llm_config__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_3'] = x_get_llm_config__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_4'] = x_get_llm_config__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_5'] = x_get_llm_config__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_6'] = x_get_llm_config__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_7'] = x_get_llm_config__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_8'] = x_get_llm_config__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_9'] = x_get_llm_config__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_10'] = x_get_llm_config__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_11'] = x_get_llm_config__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_12'] = x_get_llm_config__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_13'] = x_get_llm_config__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_14'] = x_get_llm_config__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_15'] = x_get_llm_config__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_16'] = x_get_llm_config__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_17'] = x_get_llm_config__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_18'] = x_get_llm_config__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_19'] = x_get_llm_config__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_llm_config__mutmut['x_get_llm_config__mutmut_20'] = x_get_llm_config__mutmut_20 # type: ignore # mutmut generated
mutants_x_save_llm_config__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_save_llm_config__mutmut)
def save_llm_config(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["llm_provider"] = provider
    config["llm_base_url"] = base_url
    config["api_key"] = api_key
    save_config(config)


def x_save_llm_config__mutmut_orig(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["llm_provider"] = provider
    config["llm_base_url"] = base_url
    config["api_key"] = api_key
    save_config(config)


def x_save_llm_config__mutmut_1(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = None
    config["llm_provider"] = provider
    config["llm_base_url"] = base_url
    config["api_key"] = api_key
    save_config(config)


def x_save_llm_config__mutmut_2(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["llm_provider"] = None
    config["llm_base_url"] = base_url
    config["api_key"] = api_key
    save_config(config)


def x_save_llm_config__mutmut_3(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["XXllm_providerXX"] = provider
    config["llm_base_url"] = base_url
    config["api_key"] = api_key
    save_config(config)


def x_save_llm_config__mutmut_4(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["LLM_PROVIDER"] = provider
    config["llm_base_url"] = base_url
    config["api_key"] = api_key
    save_config(config)


def x_save_llm_config__mutmut_5(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["llm_provider"] = provider
    config["llm_base_url"] = None
    config["api_key"] = api_key
    save_config(config)


def x_save_llm_config__mutmut_6(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["llm_provider"] = provider
    config["XXllm_base_urlXX"] = base_url
    config["api_key"] = api_key
    save_config(config)


def x_save_llm_config__mutmut_7(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["llm_provider"] = provider
    config["LLM_BASE_URL"] = base_url
    config["api_key"] = api_key
    save_config(config)


def x_save_llm_config__mutmut_8(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["llm_provider"] = provider
    config["llm_base_url"] = base_url
    config["api_key"] = None
    save_config(config)


def x_save_llm_config__mutmut_9(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["llm_provider"] = provider
    config["llm_base_url"] = base_url
    config["XXapi_keyXX"] = api_key
    save_config(config)


def x_save_llm_config__mutmut_10(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["llm_provider"] = provider
    config["llm_base_url"] = base_url
    config["API_KEY"] = api_key
    save_config(config)


def x_save_llm_config__mutmut_11(provider: str, base_url: str, api_key: str) -> None:
    """Persist LLM provider, base URL, and API key to config.yaml."""
    config = load_config()
    config["llm_provider"] = provider
    config["llm_base_url"] = base_url
    config["api_key"] = api_key
    save_config(None)

mutants_x_save_llm_config__mutmut['_mutmut_orig'] = x_save_llm_config__mutmut_orig # type: ignore # mutmut generated
mutants_x_save_llm_config__mutmut['x_save_llm_config__mutmut_1'] = x_save_llm_config__mutmut_1 # type: ignore # mutmut generated
mutants_x_save_llm_config__mutmut['x_save_llm_config__mutmut_2'] = x_save_llm_config__mutmut_2 # type: ignore # mutmut generated
mutants_x_save_llm_config__mutmut['x_save_llm_config__mutmut_3'] = x_save_llm_config__mutmut_3 # type: ignore # mutmut generated
mutants_x_save_llm_config__mutmut['x_save_llm_config__mutmut_4'] = x_save_llm_config__mutmut_4 # type: ignore # mutmut generated
mutants_x_save_llm_config__mutmut['x_save_llm_config__mutmut_5'] = x_save_llm_config__mutmut_5 # type: ignore # mutmut generated
mutants_x_save_llm_config__mutmut['x_save_llm_config__mutmut_6'] = x_save_llm_config__mutmut_6 # type: ignore # mutmut generated
mutants_x_save_llm_config__mutmut['x_save_llm_config__mutmut_7'] = x_save_llm_config__mutmut_7 # type: ignore # mutmut generated
mutants_x_save_llm_config__mutmut['x_save_llm_config__mutmut_8'] = x_save_llm_config__mutmut_8 # type: ignore # mutmut generated
mutants_x_save_llm_config__mutmut['x_save_llm_config__mutmut_9'] = x_save_llm_config__mutmut_9 # type: ignore # mutmut generated
mutants_x_save_llm_config__mutmut['x_save_llm_config__mutmut_10'] = x_save_llm_config__mutmut_10 # type: ignore # mutmut generated
mutants_x_save_llm_config__mutmut['x_save_llm_config__mutmut_11'] = x_save_llm_config__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_runtime_mode__mutmut)
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


def x_get_runtime_mode__mutmut_orig() -> str:
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


def x_get_runtime_mode__mutmut_1() -> str:
    """
    Get the runtime mode from environment or config.yaml.
    Returns "remote" by default (production), "embedded" if explicitly configured.
    """
    env_mode = None
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


def x_get_runtime_mode__mutmut_2() -> str:
    """
    Get the runtime mode from environment or config.yaml.
    Returns "remote" by default (production), "embedded" if explicitly configured.
    """
    env_mode = os.environ.get(None)
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


def x_get_runtime_mode__mutmut_3() -> str:
    """
    Get the runtime mode from environment or config.yaml.
    Returns "remote" by default (production), "embedded" if explicitly configured.
    """
    env_mode = os.environ.get(RUNTIME_MODE_ENV_VAR)
    if env_mode not in ("embedded", "remote"):
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


def x_get_runtime_mode__mutmut_4() -> str:
    """
    Get the runtime mode from environment or config.yaml.
    Returns "remote" by default (production), "embedded" if explicitly configured.
    """
    env_mode = os.environ.get(RUNTIME_MODE_ENV_VAR)
    if env_mode in ("XXembeddedXX", "remote"):
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


def x_get_runtime_mode__mutmut_5() -> str:
    """
    Get the runtime mode from environment or config.yaml.
    Returns "remote" by default (production), "embedded" if explicitly configured.
    """
    env_mode = os.environ.get(RUNTIME_MODE_ENV_VAR)
    if env_mode in ("EMBEDDED", "remote"):
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


def x_get_runtime_mode__mutmut_6() -> str:
    """
    Get the runtime mode from environment or config.yaml.
    Returns "remote" by default (production), "embedded" if explicitly configured.
    """
    env_mode = os.environ.get(RUNTIME_MODE_ENV_VAR)
    if env_mode in ("embedded", "XXremoteXX"):
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


def x_get_runtime_mode__mutmut_7() -> str:
    """
    Get the runtime mode from environment or config.yaml.
    Returns "remote" by default (production), "embedded" if explicitly configured.
    """
    env_mode = os.environ.get(RUNTIME_MODE_ENV_VAR)
    if env_mode in ("embedded", "REMOTE"):
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


def x_get_runtime_mode__mutmut_8() -> str:
    """
    Get the runtime mode from environment or config.yaml.
    Returns "remote" by default (production), "embedded" if explicitly configured.
    """
    env_mode = os.environ.get(RUNTIME_MODE_ENV_VAR)
    if env_mode in ("embedded", "remote"):
        return env_mode
    if _get_runtime_endpoint_from_env() is None:
        return "remote"
    config = load_config()
    runtime_section = config.get("runtime")
    if isinstance(runtime_section, dict):
        mode = runtime_section.get("mode")
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_9() -> str:
    """
    Get the runtime mode from environment or config.yaml.
    Returns "remote" by default (production), "embedded" if explicitly configured.
    """
    env_mode = os.environ.get(RUNTIME_MODE_ENV_VAR)
    if env_mode in ("embedded", "remote"):
        return env_mode
    if _get_runtime_endpoint_from_env() is not None:
        return "XXremoteXX"
    config = load_config()
    runtime_section = config.get("runtime")
    if isinstance(runtime_section, dict):
        mode = runtime_section.get("mode")
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_10() -> str:
    """
    Get the runtime mode from environment or config.yaml.
    Returns "remote" by default (production), "embedded" if explicitly configured.
    """
    env_mode = os.environ.get(RUNTIME_MODE_ENV_VAR)
    if env_mode in ("embedded", "remote"):
        return env_mode
    if _get_runtime_endpoint_from_env() is not None:
        return "REMOTE"
    config = load_config()
    runtime_section = config.get("runtime")
    if isinstance(runtime_section, dict):
        mode = runtime_section.get("mode")
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_11() -> str:
    """
    Get the runtime mode from environment or config.yaml.
    Returns "remote" by default (production), "embedded" if explicitly configured.
    """
    env_mode = os.environ.get(RUNTIME_MODE_ENV_VAR)
    if env_mode in ("embedded", "remote"):
        return env_mode
    if _get_runtime_endpoint_from_env() is not None:
        return "remote"
    config = None
    runtime_section = config.get("runtime")
    if isinstance(runtime_section, dict):
        mode = runtime_section.get("mode")
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_12() -> str:
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
    runtime_section = None
    if isinstance(runtime_section, dict):
        mode = runtime_section.get("mode")
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_13() -> str:
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
    runtime_section = config.get(None)
    if isinstance(runtime_section, dict):
        mode = runtime_section.get("mode")
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_14() -> str:
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
    runtime_section = config.get("XXruntimeXX")
    if isinstance(runtime_section, dict):
        mode = runtime_section.get("mode")
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_15() -> str:
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
    runtime_section = config.get("RUNTIME")
    if isinstance(runtime_section, dict):
        mode = runtime_section.get("mode")
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_16() -> str:
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
        mode = None
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_17() -> str:
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
        mode = runtime_section.get(None)
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_18() -> str:
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
        mode = runtime_section.get("XXmodeXX")
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_19() -> str:
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
        mode = runtime_section.get("MODE")
        if mode in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_20() -> str:
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
        if mode not in ("embedded", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_21() -> str:
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
        if mode in ("XXembeddedXX", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_22() -> str:
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
        if mode in ("EMBEDDED", "remote"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_23() -> str:
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
        if mode in ("embedded", "XXremoteXX"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_24() -> str:
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
        if mode in ("embedded", "REMOTE"):
            return str(mode)
    return "remote"


def x_get_runtime_mode__mutmut_25() -> str:
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
            return str(None)
    return "remote"


def x_get_runtime_mode__mutmut_26() -> str:
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
    return "XXremoteXX"


def x_get_runtime_mode__mutmut_27() -> str:
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
    return "REMOTE"

mutants_x_get_runtime_mode__mutmut['_mutmut_orig'] = x_get_runtime_mode__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_1'] = x_get_runtime_mode__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_2'] = x_get_runtime_mode__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_3'] = x_get_runtime_mode__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_4'] = x_get_runtime_mode__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_5'] = x_get_runtime_mode__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_6'] = x_get_runtime_mode__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_7'] = x_get_runtime_mode__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_8'] = x_get_runtime_mode__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_9'] = x_get_runtime_mode__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_10'] = x_get_runtime_mode__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_11'] = x_get_runtime_mode__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_12'] = x_get_runtime_mode__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_13'] = x_get_runtime_mode__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_14'] = x_get_runtime_mode__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_15'] = x_get_runtime_mode__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_16'] = x_get_runtime_mode__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_17'] = x_get_runtime_mode__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_18'] = x_get_runtime_mode__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_19'] = x_get_runtime_mode__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_20'] = x_get_runtime_mode__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_21'] = x_get_runtime_mode__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_22'] = x_get_runtime_mode__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_23'] = x_get_runtime_mode__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_24'] = x_get_runtime_mode__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_25'] = x_get_runtime_mode__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_26'] = x_get_runtime_mode__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_runtime_mode__mutmut['x_get_runtime_mode__mutmut_27'] = x_get_runtime_mode__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_runtime_endpoint__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_runtime_endpoint__mutmut)
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


def x_get_runtime_endpoint__mutmut_orig() -> str | None:
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


def x_get_runtime_endpoint__mutmut_1() -> str | None:
    """
    Get the remote runtime endpoint from environment or config.yaml.
    Falls back to production API URL.
    """
    env_endpoint = None
    if env_endpoint is not None:
        return env_endpoint
    config = load_config()
    runtime_section = config.get("runtime")
    if isinstance(runtime_section, dict):
        endpoint = runtime_section.get("endpoint")
        if isinstance(endpoint, str):
            return endpoint
    return DEFAULT_RUNTIME_ENDPOINT


def x_get_runtime_endpoint__mutmut_2() -> str | None:
    """
    Get the remote runtime endpoint from environment or config.yaml.
    Falls back to production API URL.
    """
    env_endpoint = _get_runtime_endpoint_from_env()
    if env_endpoint is None:
        return env_endpoint
    config = load_config()
    runtime_section = config.get("runtime")
    if isinstance(runtime_section, dict):
        endpoint = runtime_section.get("endpoint")
        if isinstance(endpoint, str):
            return endpoint
    return DEFAULT_RUNTIME_ENDPOINT


def x_get_runtime_endpoint__mutmut_3() -> str | None:
    """
    Get the remote runtime endpoint from environment or config.yaml.
    Falls back to production API URL.
    """
    env_endpoint = _get_runtime_endpoint_from_env()
    if env_endpoint is not None:
        return env_endpoint
    config = None
    runtime_section = config.get("runtime")
    if isinstance(runtime_section, dict):
        endpoint = runtime_section.get("endpoint")
        if isinstance(endpoint, str):
            return endpoint
    return DEFAULT_RUNTIME_ENDPOINT


def x_get_runtime_endpoint__mutmut_4() -> str | None:
    """
    Get the remote runtime endpoint from environment or config.yaml.
    Falls back to production API URL.
    """
    env_endpoint = _get_runtime_endpoint_from_env()
    if env_endpoint is not None:
        return env_endpoint
    config = load_config()
    runtime_section = None
    if isinstance(runtime_section, dict):
        endpoint = runtime_section.get("endpoint")
        if isinstance(endpoint, str):
            return endpoint
    return DEFAULT_RUNTIME_ENDPOINT


def x_get_runtime_endpoint__mutmut_5() -> str | None:
    """
    Get the remote runtime endpoint from environment or config.yaml.
    Falls back to production API URL.
    """
    env_endpoint = _get_runtime_endpoint_from_env()
    if env_endpoint is not None:
        return env_endpoint
    config = load_config()
    runtime_section = config.get(None)
    if isinstance(runtime_section, dict):
        endpoint = runtime_section.get("endpoint")
        if isinstance(endpoint, str):
            return endpoint
    return DEFAULT_RUNTIME_ENDPOINT


def x_get_runtime_endpoint__mutmut_6() -> str | None:
    """
    Get the remote runtime endpoint from environment or config.yaml.
    Falls back to production API URL.
    """
    env_endpoint = _get_runtime_endpoint_from_env()
    if env_endpoint is not None:
        return env_endpoint
    config = load_config()
    runtime_section = config.get("XXruntimeXX")
    if isinstance(runtime_section, dict):
        endpoint = runtime_section.get("endpoint")
        if isinstance(endpoint, str):
            return endpoint
    return DEFAULT_RUNTIME_ENDPOINT


def x_get_runtime_endpoint__mutmut_7() -> str | None:
    """
    Get the remote runtime endpoint from environment or config.yaml.
    Falls back to production API URL.
    """
    env_endpoint = _get_runtime_endpoint_from_env()
    if env_endpoint is not None:
        return env_endpoint
    config = load_config()
    runtime_section = config.get("RUNTIME")
    if isinstance(runtime_section, dict):
        endpoint = runtime_section.get("endpoint")
        if isinstance(endpoint, str):
            return endpoint
    return DEFAULT_RUNTIME_ENDPOINT


def x_get_runtime_endpoint__mutmut_8() -> str | None:
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
        endpoint = None
        if isinstance(endpoint, str):
            return endpoint
    return DEFAULT_RUNTIME_ENDPOINT


def x_get_runtime_endpoint__mutmut_9() -> str | None:
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
        endpoint = runtime_section.get(None)
        if isinstance(endpoint, str):
            return endpoint
    return DEFAULT_RUNTIME_ENDPOINT


def x_get_runtime_endpoint__mutmut_10() -> str | None:
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
        endpoint = runtime_section.get("XXendpointXX")
        if isinstance(endpoint, str):
            return endpoint
    return DEFAULT_RUNTIME_ENDPOINT


def x_get_runtime_endpoint__mutmut_11() -> str | None:
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
        endpoint = runtime_section.get("ENDPOINT")
        if isinstance(endpoint, str):
            return endpoint
    return DEFAULT_RUNTIME_ENDPOINT

mutants_x_get_runtime_endpoint__mutmut['_mutmut_orig'] = x_get_runtime_endpoint__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_runtime_endpoint__mutmut['x_get_runtime_endpoint__mutmut_1'] = x_get_runtime_endpoint__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_runtime_endpoint__mutmut['x_get_runtime_endpoint__mutmut_2'] = x_get_runtime_endpoint__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_runtime_endpoint__mutmut['x_get_runtime_endpoint__mutmut_3'] = x_get_runtime_endpoint__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_runtime_endpoint__mutmut['x_get_runtime_endpoint__mutmut_4'] = x_get_runtime_endpoint__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_runtime_endpoint__mutmut['x_get_runtime_endpoint__mutmut_5'] = x_get_runtime_endpoint__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_runtime_endpoint__mutmut['x_get_runtime_endpoint__mutmut_6'] = x_get_runtime_endpoint__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_runtime_endpoint__mutmut['x_get_runtime_endpoint__mutmut_7'] = x_get_runtime_endpoint__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_runtime_endpoint__mutmut['x_get_runtime_endpoint__mutmut_8'] = x_get_runtime_endpoint__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_runtime_endpoint__mutmut['x_get_runtime_endpoint__mutmut_9'] = x_get_runtime_endpoint__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_runtime_endpoint__mutmut['x_get_runtime_endpoint__mutmut_10'] = x_get_runtime_endpoint__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_runtime_endpoint__mutmut['x_get_runtime_endpoint__mutmut_11'] = x_get_runtime_endpoint__mutmut_11 # type: ignore # mutmut generated
mutants_x__get_runtime_endpoint_from_env__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_runtime_endpoint_from_env__mutmut)
def _get_runtime_endpoint_from_env() -> str | None:
    endpoint = os.environ.get(RUNTIME_ENDPOINT_ENV_VAR)
    if endpoint:
        return endpoint
    return None


def x__get_runtime_endpoint_from_env__mutmut_orig() -> str | None:
    endpoint = os.environ.get(RUNTIME_ENDPOINT_ENV_VAR)
    if endpoint:
        return endpoint
    return None


def x__get_runtime_endpoint_from_env__mutmut_1() -> str | None:
    endpoint = None
    if endpoint:
        return endpoint
    return None


def x__get_runtime_endpoint_from_env__mutmut_2() -> str | None:
    endpoint = os.environ.get(None)
    if endpoint:
        return endpoint
    return None

mutants_x__get_runtime_endpoint_from_env__mutmut['_mutmut_orig'] = x__get_runtime_endpoint_from_env__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_runtime_endpoint_from_env__mutmut['x__get_runtime_endpoint_from_env__mutmut_1'] = x__get_runtime_endpoint_from_env__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_runtime_endpoint_from_env__mutmut['x__get_runtime_endpoint_from_env__mutmut_2'] = x__get_runtime_endpoint_from_env__mutmut_2 # type: ignore # mutmut generated
