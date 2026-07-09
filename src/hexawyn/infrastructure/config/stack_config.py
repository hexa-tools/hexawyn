from hexawyn.infrastructure.config.config_manager import load_config, save_config

_OVERRIDES_KEY = "stack_overrides"
_VALID_PROVIDERS = ("aws", "vanilla")


def get_stack_override(context_name: str) -> str | None:
    """Return the persisted stack override for a context, or None."""
    override = _load_overrides().get(context_name)
    return override if override in _VALID_PROVIDERS else None


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


def clear_stack_override(context_name: str) -> None:
    """Remove any override for the context, restoring auto-detection."""
    config = load_config()
    overrides = _overrides_from(config)
    if context_name not in overrides:
        return
    del overrides[context_name]
    config[_OVERRIDES_KEY] = overrides
    save_config(config)


def _load_overrides() -> dict[str, str]:
    return _overrides_from(load_config())


def _overrides_from(config: dict[str, object]) -> dict[str, str]:
    raw = config.get(_OVERRIDES_KEY, {})
    if isinstance(raw, dict):
        return {str(key): str(value) for key, value in raw.items()}
    return {}
