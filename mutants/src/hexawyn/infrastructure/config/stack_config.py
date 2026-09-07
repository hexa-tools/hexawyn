from hexawyn.infrastructure.config.config_manager import load_config, save_config

_OVERRIDES_KEY = "stack_overrides"
_VALID_PROVIDERS = ("aws", "vanilla", "gcp", "azure", "datadog")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_stack_override__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_stack_override__mutmut)
def get_stack_override(context_name: str) -> str | None:
    """Return the persisted stack override for a context, or None."""
    override = _load_overrides().get(context_name)
    return override if override in _VALID_PROVIDERS else None


def x_get_stack_override__mutmut_orig(context_name: str) -> str | None:
    """Return the persisted stack override for a context, or None."""
    override = _load_overrides().get(context_name)
    return override if override in _VALID_PROVIDERS else None


def x_get_stack_override__mutmut_1(context_name: str) -> str | None:
    """Return the persisted stack override for a context, or None."""
    override = None
    return override if override in _VALID_PROVIDERS else None


def x_get_stack_override__mutmut_2(context_name: str) -> str | None:
    """Return the persisted stack override for a context, or None."""
    override = _load_overrides().get(None)
    return override if override in _VALID_PROVIDERS else None


def x_get_stack_override__mutmut_3(context_name: str) -> str | None:
    """Return the persisted stack override for a context, or None."""
    override = _load_overrides().get(context_name)
    return override if override not in _VALID_PROVIDERS else None

mutants_x_get_stack_override__mutmut['_mutmut_orig'] = x_get_stack_override__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_stack_override__mutmut['x_get_stack_override__mutmut_1'] = x_get_stack_override__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_stack_override__mutmut['x_get_stack_override__mutmut_2'] = x_get_stack_override__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_stack_override__mutmut['x_get_stack_override__mutmut_3'] = x_get_stack_override__mutmut_3 # type: ignore # mutmut generated
mutants_x_set_stack_override__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_set_stack_override__mutmut)
def set_stack_override(context_name: str, provider: str) -> None:
    """Force a provider ('aws' or 'vanilla') for the given context."""
    if provider not in _VALID_PROVIDERS:
        raise ValueError(
            f"Invalid stack provider '{provider}'. Expected one of {_VALID_PROVIDERS}."
        )
    config = load_config()
    overrides = _overrides_from(config)
    overrides[context_name] = provider
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_set_stack_override__mutmut_orig(context_name: str, provider: str) -> None:
    """Force a provider ('aws' or 'vanilla') for the given context."""
    if provider not in _VALID_PROVIDERS:
        raise ValueError(
            f"Invalid stack provider '{provider}'. Expected one of {_VALID_PROVIDERS}."
        )
    config = load_config()
    overrides = _overrides_from(config)
    overrides[context_name] = provider
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_set_stack_override__mutmut_1(context_name: str, provider: str) -> None:
    """Force a provider ('aws' or 'vanilla') for the given context."""
    if provider in _VALID_PROVIDERS:
        raise ValueError(
            f"Invalid stack provider '{provider}'. Expected one of {_VALID_PROVIDERS}."
        )
    config = load_config()
    overrides = _overrides_from(config)
    overrides[context_name] = provider
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_set_stack_override__mutmut_2(context_name: str, provider: str) -> None:
    """Force a provider ('aws' or 'vanilla') for the given context."""
    if provider not in _VALID_PROVIDERS:
        raise ValueError(
            None
        )
    config = load_config()
    overrides = _overrides_from(config)
    overrides[context_name] = provider
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_set_stack_override__mutmut_3(context_name: str, provider: str) -> None:
    """Force a provider ('aws' or 'vanilla') for the given context."""
    if provider not in _VALID_PROVIDERS:
        raise ValueError(
            f"Invalid stack provider '{provider}'. Expected one of {_VALID_PROVIDERS}."
        )
    config = None
    overrides = _overrides_from(config)
    overrides[context_name] = provider
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_set_stack_override__mutmut_4(context_name: str, provider: str) -> None:
    """Force a provider ('aws' or 'vanilla') for the given context."""
    if provider not in _VALID_PROVIDERS:
        raise ValueError(
            f"Invalid stack provider '{provider}'. Expected one of {_VALID_PROVIDERS}."
        )
    config = load_config()
    overrides = None
    overrides[context_name] = provider
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_set_stack_override__mutmut_5(context_name: str, provider: str) -> None:
    """Force a provider ('aws' or 'vanilla') for the given context."""
    if provider not in _VALID_PROVIDERS:
        raise ValueError(
            f"Invalid stack provider '{provider}'. Expected one of {_VALID_PROVIDERS}."
        )
    config = load_config()
    overrides = _overrides_from(None)
    overrides[context_name] = provider
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_set_stack_override__mutmut_6(context_name: str, provider: str) -> None:
    """Force a provider ('aws' or 'vanilla') for the given context."""
    if provider not in _VALID_PROVIDERS:
        raise ValueError(
            f"Invalid stack provider '{provider}'. Expected one of {_VALID_PROVIDERS}."
        )
    config = load_config()
    overrides = _overrides_from(config)
    overrides[context_name] = None
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_set_stack_override__mutmut_7(context_name: str, provider: str) -> None:
    """Force a provider ('aws' or 'vanilla') for the given context."""
    if provider not in _VALID_PROVIDERS:
        raise ValueError(
            f"Invalid stack provider '{provider}'. Expected one of {_VALID_PROVIDERS}."
        )
    config = load_config()
    overrides = _overrides_from(config)
    overrides[context_name] = provider
    config[_OVERRIDES_KEY] = None
    save_config(config)


def x_set_stack_override__mutmut_8(context_name: str, provider: str) -> None:
    """Force a provider ('aws' or 'vanilla') for the given context."""
    if provider not in _VALID_PROVIDERS:
        raise ValueError(
            f"Invalid stack provider '{provider}'. Expected one of {_VALID_PROVIDERS}."
        )
    config = load_config()
    overrides = _overrides_from(config)
    overrides[context_name] = provider
    config[_OVERRIDES_KEY] = overrides
    save_config(None)

mutants_x_set_stack_override__mutmut['_mutmut_orig'] = x_set_stack_override__mutmut_orig # type: ignore # mutmut generated
mutants_x_set_stack_override__mutmut['x_set_stack_override__mutmut_1'] = x_set_stack_override__mutmut_1 # type: ignore # mutmut generated
mutants_x_set_stack_override__mutmut['x_set_stack_override__mutmut_2'] = x_set_stack_override__mutmut_2 # type: ignore # mutmut generated
mutants_x_set_stack_override__mutmut['x_set_stack_override__mutmut_3'] = x_set_stack_override__mutmut_3 # type: ignore # mutmut generated
mutants_x_set_stack_override__mutmut['x_set_stack_override__mutmut_4'] = x_set_stack_override__mutmut_4 # type: ignore # mutmut generated
mutants_x_set_stack_override__mutmut['x_set_stack_override__mutmut_5'] = x_set_stack_override__mutmut_5 # type: ignore # mutmut generated
mutants_x_set_stack_override__mutmut['x_set_stack_override__mutmut_6'] = x_set_stack_override__mutmut_6 # type: ignore # mutmut generated
mutants_x_set_stack_override__mutmut['x_set_stack_override__mutmut_7'] = x_set_stack_override__mutmut_7 # type: ignore # mutmut generated
mutants_x_set_stack_override__mutmut['x_set_stack_override__mutmut_8'] = x_set_stack_override__mutmut_8 # type: ignore # mutmut generated
mutants_x_clear_stack_override__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_clear_stack_override__mutmut)
def clear_stack_override(context_name: str) -> None:
    """Remove any override for the context, restoring auto-detection."""
    config = load_config()
    overrides = _overrides_from(config)
    if context_name not in overrides:
        return
    del overrides[context_name]
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_clear_stack_override__mutmut_orig(context_name: str) -> None:
    """Remove any override for the context, restoring auto-detection."""
    config = load_config()
    overrides = _overrides_from(config)
    if context_name not in overrides:
        return
    del overrides[context_name]
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_clear_stack_override__mutmut_1(context_name: str) -> None:
    """Remove any override for the context, restoring auto-detection."""
    config = None
    overrides = _overrides_from(config)
    if context_name not in overrides:
        return
    del overrides[context_name]
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_clear_stack_override__mutmut_2(context_name: str) -> None:
    """Remove any override for the context, restoring auto-detection."""
    config = load_config()
    overrides = None
    if context_name not in overrides:
        return
    del overrides[context_name]
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_clear_stack_override__mutmut_3(context_name: str) -> None:
    """Remove any override for the context, restoring auto-detection."""
    config = load_config()
    overrides = _overrides_from(None)
    if context_name not in overrides:
        return
    del overrides[context_name]
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_clear_stack_override__mutmut_4(context_name: str) -> None:
    """Remove any override for the context, restoring auto-detection."""
    config = load_config()
    overrides = _overrides_from(config)
    if context_name in overrides:
        return
    del overrides[context_name]
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def x_clear_stack_override__mutmut_5(context_name: str) -> None:
    """Remove any override for the context, restoring auto-detection."""
    config = load_config()
    overrides = _overrides_from(config)
    if context_name not in overrides:
        return
    del overrides[context_name]
    config[_OVERRIDES_KEY] = None
    save_config(config)


def x_clear_stack_override__mutmut_6(context_name: str) -> None:
    """Remove any override for the context, restoring auto-detection."""
    config = load_config()
    overrides = _overrides_from(config)
    if context_name not in overrides:
        return
    del overrides[context_name]
    config[_OVERRIDES_KEY] = overrides
    save_config(None)

mutants_x_clear_stack_override__mutmut['_mutmut_orig'] = x_clear_stack_override__mutmut_orig # type: ignore # mutmut generated
mutants_x_clear_stack_override__mutmut['x_clear_stack_override__mutmut_1'] = x_clear_stack_override__mutmut_1 # type: ignore # mutmut generated
mutants_x_clear_stack_override__mutmut['x_clear_stack_override__mutmut_2'] = x_clear_stack_override__mutmut_2 # type: ignore # mutmut generated
mutants_x_clear_stack_override__mutmut['x_clear_stack_override__mutmut_3'] = x_clear_stack_override__mutmut_3 # type: ignore # mutmut generated
mutants_x_clear_stack_override__mutmut['x_clear_stack_override__mutmut_4'] = x_clear_stack_override__mutmut_4 # type: ignore # mutmut generated
mutants_x_clear_stack_override__mutmut['x_clear_stack_override__mutmut_5'] = x_clear_stack_override__mutmut_5 # type: ignore # mutmut generated
mutants_x_clear_stack_override__mutmut['x_clear_stack_override__mutmut_6'] = x_clear_stack_override__mutmut_6 # type: ignore # mutmut generated
mutants_x__load_overrides__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__load_overrides__mutmut)
def _load_overrides() -> dict[str, str]:
    return _overrides_from(load_config())


def x__load_overrides__mutmut_orig() -> dict[str, str]:
    return _overrides_from(load_config())


def x__load_overrides__mutmut_1() -> dict[str, str]:
    return _overrides_from(None)

mutants_x__load_overrides__mutmut['_mutmut_orig'] = x__load_overrides__mutmut_orig # type: ignore # mutmut generated
mutants_x__load_overrides__mutmut['x__load_overrides__mutmut_1'] = x__load_overrides__mutmut_1 # type: ignore # mutmut generated
mutants_x__overrides_from__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__overrides_from__mutmut)
def _overrides_from(config: dict[str, object]) -> dict[str, str]:
    raw = config.get(_OVERRIDES_KEY, {})
    if isinstance(raw, dict):
        return {str(key): str(value) for key, value in raw.items()}
    return {}


def x__overrides_from__mutmut_orig(config: dict[str, object]) -> dict[str, str]:
    raw = config.get(_OVERRIDES_KEY, {})
    if isinstance(raw, dict):
        return {str(key): str(value) for key, value in raw.items()}
    return {}


def x__overrides_from__mutmut_1(config: dict[str, object]) -> dict[str, str]:
    raw = None
    if isinstance(raw, dict):
        return {str(key): str(value) for key, value in raw.items()}
    return {}


def x__overrides_from__mutmut_2(config: dict[str, object]) -> dict[str, str]:
    raw = config.get(None, {})
    if isinstance(raw, dict):
        return {str(key): str(value) for key, value in raw.items()}
    return {}


def x__overrides_from__mutmut_3(config: dict[str, object]) -> dict[str, str]:
    raw = config.get(_OVERRIDES_KEY, None)
    if isinstance(raw, dict):
        return {str(key): str(value) for key, value in raw.items()}
    return {}


def x__overrides_from__mutmut_4(config: dict[str, object]) -> dict[str, str]:
    raw = config.get({})
    if isinstance(raw, dict):
        return {str(key): str(value) for key, value in raw.items()}
    return {}


def x__overrides_from__mutmut_5(config: dict[str, object]) -> dict[str, str]:
    raw = config.get(_OVERRIDES_KEY, )
    if isinstance(raw, dict):
        return {str(key): str(value) for key, value in raw.items()}
    return {}


def x__overrides_from__mutmut_6(config: dict[str, object]) -> dict[str, str]:
    raw = config.get(_OVERRIDES_KEY, {})
    if isinstance(raw, dict):
        return {str(None): str(value) for key, value in raw.items()}
    return {}


def x__overrides_from__mutmut_7(config: dict[str, object]) -> dict[str, str]:
    raw = config.get(_OVERRIDES_KEY, {})
    if isinstance(raw, dict):
        return {str(key): str(None) for key, value in raw.items()}
    return {}

mutants_x__overrides_from__mutmut['_mutmut_orig'] = x__overrides_from__mutmut_orig # type: ignore # mutmut generated
mutants_x__overrides_from__mutmut['x__overrides_from__mutmut_1'] = x__overrides_from__mutmut_1 # type: ignore # mutmut generated
mutants_x__overrides_from__mutmut['x__overrides_from__mutmut_2'] = x__overrides_from__mutmut_2 # type: ignore # mutmut generated
mutants_x__overrides_from__mutmut['x__overrides_from__mutmut_3'] = x__overrides_from__mutmut_3 # type: ignore # mutmut generated
mutants_x__overrides_from__mutmut['x__overrides_from__mutmut_4'] = x__overrides_from__mutmut_4 # type: ignore # mutmut generated
mutants_x__overrides_from__mutmut['x__overrides_from__mutmut_5'] = x__overrides_from__mutmut_5 # type: ignore # mutmut generated
mutants_x__overrides_from__mutmut['x__overrides_from__mutmut_6'] = x__overrides_from__mutmut_6 # type: ignore # mutmut generated
mutants_x__overrides_from__mutmut['x__overrides_from__mutmut_7'] = x__overrides_from__mutmut_7 # type: ignore # mutmut generated
