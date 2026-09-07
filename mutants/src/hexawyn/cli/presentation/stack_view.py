from hexawyn.application.ports.driven.k8s_port import ClusterContext
from hexawyn.infrastructure.adapters.secondary.adapter_factory import list_installed_providers
from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
from hexawyn.infrastructure.config.provider_detector import detect_installed_providers
from hexawyn.infrastructure.config.stack_config import (
    clear_stack_override,
    get_stack_override,
    set_stack_override,
)
from hexawyn.infrastructure.config.stack_resolver import StackDescription, resolve_stack

_FORCE_PROVIDERS = ("aws", "gcp", "azure", "datadog", "vanilla")
_AUTO = "auto"
_USAGE = "Usage: /stack [aws | gcp | azure | datadog | vanilla | auto]"
_INSTALL_HINTS = {
    "aws": "⚠ boto3 not installed — run: pip install 'hexawyn[aws]'",
    "gcp": "⚠ google-cloud libs not installed — run: pip install 'hexawyn[gcp]'",
    "azure": "⚠ azure libs not installed — run: pip install 'hexawyn[azure]'",
    "datadog": "⚠ datadog-api-client not installed — run: pip install 'hexawyn[datadog]'",
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_run_stack_command__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_run_stack_command__mutmut)
def run_stack_command(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_orig(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_1(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = None
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_2(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(None)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_3(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is not None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_4(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(None)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_5(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument != _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_6(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(None)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_7(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "XXgreenXX")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_8(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "GREEN")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_9(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument not in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_10(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(None, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_11(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, None)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_12(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_13(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, )
    return [(f"Unknown stack '{argument}'. {_USAGE}", "yellow")]


def x_run_stack_command__mutmut_14(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "XXyellowXX")]


def x_run_stack_command__mutmut_15(text: str, context_name: str) -> list[tuple[str, str]]:
    """Handle the `/stack` slash command, returning renderable (text, style) lines."""
    argument = _parse_argument(text)
    if argument is None:
        return _view_lines(context_name)
    if argument == _AUTO:
        clear_stack_override(context_name)
        return [(f"Stack override cleared for '{context_name}' — using auto-detection.", "green")]
    if argument in _FORCE_PROVIDERS:
        return _force_lines(context_name, argument)
    return [(f"Unknown stack '{argument}'. {_USAGE}", "YELLOW")]

mutants_x_run_stack_command__mutmut['_mutmut_orig'] = x_run_stack_command__mutmut_orig # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_1'] = x_run_stack_command__mutmut_1 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_2'] = x_run_stack_command__mutmut_2 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_3'] = x_run_stack_command__mutmut_3 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_4'] = x_run_stack_command__mutmut_4 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_5'] = x_run_stack_command__mutmut_5 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_6'] = x_run_stack_command__mutmut_6 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_7'] = x_run_stack_command__mutmut_7 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_8'] = x_run_stack_command__mutmut_8 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_9'] = x_run_stack_command__mutmut_9 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_10'] = x_run_stack_command__mutmut_10 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_11'] = x_run_stack_command__mutmut_11 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_12'] = x_run_stack_command__mutmut_12 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_13'] = x_run_stack_command__mutmut_13 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_14'] = x_run_stack_command__mutmut_14 # type: ignore # mutmut generated
mutants_x_run_stack_command__mutmut['x_run_stack_command__mutmut_15'] = x_run_stack_command__mutmut_15 # type: ignore # mutmut generated
mutants_x__force_lines__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__force_lines__mutmut)
def _force_lines(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, provider)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "green")]
    if not _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "yellow"))
    return lines


def x__force_lines__mutmut_orig(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, provider)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "green")]
    if not _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "yellow"))
    return lines


def x__force_lines__mutmut_1(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(None, provider)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "green")]
    if not _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "yellow"))
    return lines


def x__force_lines__mutmut_2(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, None)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "green")]
    if not _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "yellow"))
    return lines


def x__force_lines__mutmut_3(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(provider)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "green")]
    if not _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "yellow"))
    return lines


def x__force_lines__mutmut_4(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, )
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "green")]
    if not _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "yellow"))
    return lines


def x__force_lines__mutmut_5(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, provider)
    lines = None
    if not _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "yellow"))
    return lines


def x__force_lines__mutmut_6(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, provider)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "XXgreenXX")]
    if not _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "yellow"))
    return lines


def x__force_lines__mutmut_7(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, provider)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "GREEN")]
    if not _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "yellow"))
    return lines


def x__force_lines__mutmut_8(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, provider)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "green")]
    if _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "yellow"))
    return lines


def x__force_lines__mutmut_9(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, provider)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "green")]
    if not _provider_installed(None):
        lines.append((_INSTALL_HINTS[provider], "yellow"))
    return lines


def x__force_lines__mutmut_10(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, provider)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "green")]
    if not _provider_installed(provider):
        lines.append(None)
    return lines


def x__force_lines__mutmut_11(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, provider)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "green")]
    if not _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "XXyellowXX"))
    return lines


def x__force_lines__mutmut_12(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, provider)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "green")]
    if not _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "YELLOW"))
    return lines

mutants_x__force_lines__mutmut['_mutmut_orig'] = x__force_lines__mutmut_orig # type: ignore # mutmut generated
mutants_x__force_lines__mutmut['x__force_lines__mutmut_1'] = x__force_lines__mutmut_1 # type: ignore # mutmut generated
mutants_x__force_lines__mutmut['x__force_lines__mutmut_2'] = x__force_lines__mutmut_2 # type: ignore # mutmut generated
mutants_x__force_lines__mutmut['x__force_lines__mutmut_3'] = x__force_lines__mutmut_3 # type: ignore # mutmut generated
mutants_x__force_lines__mutmut['x__force_lines__mutmut_4'] = x__force_lines__mutmut_4 # type: ignore # mutmut generated
mutants_x__force_lines__mutmut['x__force_lines__mutmut_5'] = x__force_lines__mutmut_5 # type: ignore # mutmut generated
mutants_x__force_lines__mutmut['x__force_lines__mutmut_6'] = x__force_lines__mutmut_6 # type: ignore # mutmut generated
mutants_x__force_lines__mutmut['x__force_lines__mutmut_7'] = x__force_lines__mutmut_7 # type: ignore # mutmut generated
mutants_x__force_lines__mutmut['x__force_lines__mutmut_8'] = x__force_lines__mutmut_8 # type: ignore # mutmut generated
mutants_x__force_lines__mutmut['x__force_lines__mutmut_9'] = x__force_lines__mutmut_9 # type: ignore # mutmut generated
mutants_x__force_lines__mutmut['x__force_lines__mutmut_10'] = x__force_lines__mutmut_10 # type: ignore # mutmut generated
mutants_x__force_lines__mutmut['x__force_lines__mutmut_11'] = x__force_lines__mutmut_11 # type: ignore # mutmut generated
mutants_x__force_lines__mutmut['x__force_lines__mutmut_12'] = x__force_lines__mutmut_12 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__view_lines__mutmut)
def _view_lines(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_orig(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_1(context_name: str) -> list[tuple[str, str]]:
    override = None
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_2(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(None)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_3(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = None
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_4(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        None,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_5(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        None,
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_6(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        None,
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_7(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        None,
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_8(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        None,
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_9(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_10(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_11(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_12(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_13(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_14(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(None),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_15(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(None),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_16(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(None),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, _installed_provider_names())


def x__view_lines__mutmut_17(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(None, stack, _installed_provider_names())


def x__view_lines__mutmut_18(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, None, _installed_provider_names())


def x__view_lines__mutmut_19(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, None)


def x__view_lines__mutmut_20(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(stack, _installed_provider_names())


def x__view_lines__mutmut_21(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, _installed_provider_names())


def x__view_lines__mutmut_22(context_name: str) -> list[tuple[str, str]]:
    override = get_stack_override(context_name)
    stack = resolve_stack(
        override,
        _aws_supported(context_name),
        _gcp_supported(context_name),
        _azure_supported(context_name),
        _datadog_supported(),
    )
    return build_stack_lines(context_name, stack, )

mutants_x__view_lines__mutmut['_mutmut_orig'] = x__view_lines__mutmut_orig # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_1'] = x__view_lines__mutmut_1 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_2'] = x__view_lines__mutmut_2 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_3'] = x__view_lines__mutmut_3 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_4'] = x__view_lines__mutmut_4 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_5'] = x__view_lines__mutmut_5 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_6'] = x__view_lines__mutmut_6 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_7'] = x__view_lines__mutmut_7 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_8'] = x__view_lines__mutmut_8 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_9'] = x__view_lines__mutmut_9 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_10'] = x__view_lines__mutmut_10 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_11'] = x__view_lines__mutmut_11 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_12'] = x__view_lines__mutmut_12 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_13'] = x__view_lines__mutmut_13 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_14'] = x__view_lines__mutmut_14 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_15'] = x__view_lines__mutmut_15 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_16'] = x__view_lines__mutmut_16 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_17'] = x__view_lines__mutmut_17 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_18'] = x__view_lines__mutmut_18 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_19'] = x__view_lines__mutmut_19 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_20'] = x__view_lines__mutmut_20 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_21'] = x__view_lines__mutmut_21 # type: ignore # mutmut generated
mutants_x__view_lines__mutmut['x__view_lines__mutmut_22'] = x__view_lines__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_stack_lines__mutmut)
def build_stack_lines(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_orig(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_1(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = None
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_2(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(None) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_3(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = "XX, XX".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_4(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "XXnoneXX"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_5(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "NONE"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_6(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "XXboldXX"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_7(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "BOLD"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_8(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("XXXX", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_9(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", "XXXX"),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_10(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['XXproviderXX']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_11(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['PROVIDER']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_12(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['XXsourceXX']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_13(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['SOURCE']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_14(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", "XXXX"),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_15(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['XXmetricsXX']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_16(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['METRICS']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_17(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", "XXXX"),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_18(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['XXtracesXX']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_19(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['TRACES']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_20(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", "XXXX"),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_21(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['XXlogsXX']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_22(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['LOGS']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_23(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", "XXXX"),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_24(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("XXXX", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_25(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", "XXXX"),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_26(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "XXdimXX"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_27(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "DIM"),
        (_USAGE, "dim"),
    ]


def x_build_stack_lines__mutmut_28(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "XXdimXX"),
    ]


def x_build_stack_lines__mutmut_29(
    context_name: str, stack: StackDescription, installed_providers: list[str]
) -> list[tuple[str, str]]:
    installed = ", ".join(installed_providers) if installed_providers else "none"
    return [
        (f"Observability stack for context '{context_name}'", "bold"),
        ("", ""),
        (f"Provider : {stack['provider']}  ({stack['source']})", ""),
        (f"Metrics  : {stack['metrics']}", ""),
        (f"Traces   : {stack['traces']}", ""),
        (f"Logs     : {stack['logs']}", ""),
        ("", ""),
        (f"Installed providers: {installed}", "dim"),
        (_USAGE, "DIM"),
    ]

mutants_x_build_stack_lines__mutmut['_mutmut_orig'] = x_build_stack_lines__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_1'] = x_build_stack_lines__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_2'] = x_build_stack_lines__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_3'] = x_build_stack_lines__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_4'] = x_build_stack_lines__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_5'] = x_build_stack_lines__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_6'] = x_build_stack_lines__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_7'] = x_build_stack_lines__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_8'] = x_build_stack_lines__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_9'] = x_build_stack_lines__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_10'] = x_build_stack_lines__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_11'] = x_build_stack_lines__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_12'] = x_build_stack_lines__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_13'] = x_build_stack_lines__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_14'] = x_build_stack_lines__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_15'] = x_build_stack_lines__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_16'] = x_build_stack_lines__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_17'] = x_build_stack_lines__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_18'] = x_build_stack_lines__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_19'] = x_build_stack_lines__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_20'] = x_build_stack_lines__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_21'] = x_build_stack_lines__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_22'] = x_build_stack_lines__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_23'] = x_build_stack_lines__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_24'] = x_build_stack_lines__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_25'] = x_build_stack_lines__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_26'] = x_build_stack_lines__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_27'] = x_build_stack_lines__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_28'] = x_build_stack_lines__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_stack_lines__mutmut['x_build_stack_lines__mutmut_29'] = x_build_stack_lines__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_argument__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_argument__mutmut)
def _parse_argument(text: str) -> str | None:
    parts = text.split(maxsplit=1)
    if len(parts) < 2 or not parts[1].strip():  # noqa: PLR2004
        return None
    return parts[1].strip().lower()


def x__parse_argument__mutmut_orig(text: str) -> str | None:
    parts = text.split(maxsplit=1)
    if len(parts) < 2 or not parts[1].strip():  # noqa: PLR2004
        return None
    return parts[1].strip().lower()


def x__parse_argument__mutmut_1(text: str) -> str | None:
    parts = None
    if len(parts) < 2 or not parts[1].strip():  # noqa: PLR2004
        return None
    return parts[1].strip().lower()


def x__parse_argument__mutmut_2(text: str) -> str | None:
    parts = text.split(maxsplit=None)
    if len(parts) < 2 or not parts[1].strip():  # noqa: PLR2004
        return None
    return parts[1].strip().lower()


def x__parse_argument__mutmut_3(text: str) -> str | None:
    parts = text.rsplit(maxsplit=1)
    if len(parts) < 2 or not parts[1].strip():  # noqa: PLR2004
        return None
    return parts[1].strip().lower()


def x__parse_argument__mutmut_4(text: str) -> str | None:
    parts = text.split(maxsplit=2)
    if len(parts) < 2 or not parts[1].strip():  # noqa: PLR2004
        return None
    return parts[1].strip().lower()


def x__parse_argument__mutmut_5(text: str) -> str | None:
    parts = text.split(maxsplit=1)
    if len(parts) < 2 and not parts[1].strip():  # noqa: PLR2004
        return None
    return parts[1].strip().lower()


def x__parse_argument__mutmut_6(text: str) -> str | None:
    parts = text.split(maxsplit=1)
    if len(parts) <= 2 or not parts[1].strip():  # noqa: PLR2004
        return None
    return parts[1].strip().lower()


def x__parse_argument__mutmut_7(text: str) -> str | None:
    parts = text.split(maxsplit=1)
    if len(parts) < 3 or not parts[1].strip():  # noqa: PLR2004
        return None
    return parts[1].strip().lower()


def x__parse_argument__mutmut_8(text: str) -> str | None:
    parts = text.split(maxsplit=1)
    if len(parts) < 2 or parts[1].strip():  # noqa: PLR2004
        return None
    return parts[1].strip().lower()


def x__parse_argument__mutmut_9(text: str) -> str | None:
    parts = text.split(maxsplit=1)
    if len(parts) < 2 or not parts[2].strip():  # noqa: PLR2004
        return None
    return parts[1].strip().lower()


def x__parse_argument__mutmut_10(text: str) -> str | None:
    parts = text.split(maxsplit=1)
    if len(parts) < 2 or not parts[1].strip():  # noqa: PLR2004
        return None
    return parts[1].strip().upper()


def x__parse_argument__mutmut_11(text: str) -> str | None:
    parts = text.split(maxsplit=1)
    if len(parts) < 2 or not parts[1].strip():  # noqa: PLR2004
        return None
    return parts[2].strip().lower()

mutants_x__parse_argument__mutmut['_mutmut_orig'] = x__parse_argument__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_argument__mutmut['x__parse_argument__mutmut_1'] = x__parse_argument__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_argument__mutmut['x__parse_argument__mutmut_2'] = x__parse_argument__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_argument__mutmut['x__parse_argument__mutmut_3'] = x__parse_argument__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_argument__mutmut['x__parse_argument__mutmut_4'] = x__parse_argument__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_argument__mutmut['x__parse_argument__mutmut_5'] = x__parse_argument__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_argument__mutmut['x__parse_argument__mutmut_6'] = x__parse_argument__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_argument__mutmut['x__parse_argument__mutmut_7'] = x__parse_argument__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_argument__mutmut['x__parse_argument__mutmut_8'] = x__parse_argument__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_argument__mutmut['x__parse_argument__mutmut_9'] = x__parse_argument__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_argument__mutmut['x__parse_argument__mutmut_10'] = x__parse_argument__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_argument__mutmut['x__parse_argument__mutmut_11'] = x__parse_argument__mutmut_11 # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__cluster_context__mutmut)
def _cluster_context(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "cluster": context_name,
        "provider": "unknown",
        "namespace": "default",
    }


def x__cluster_context__mutmut_orig(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "cluster": context_name,
        "provider": "unknown",
        "namespace": "default",
    }


def x__cluster_context__mutmut_1(context_name: str) -> ClusterContext:
    return {
        "XXnameXX": context_name,
        "cluster": context_name,
        "provider": "unknown",
        "namespace": "default",
    }


def x__cluster_context__mutmut_2(context_name: str) -> ClusterContext:
    return {
        "NAME": context_name,
        "cluster": context_name,
        "provider": "unknown",
        "namespace": "default",
    }


def x__cluster_context__mutmut_3(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "XXclusterXX": context_name,
        "provider": "unknown",
        "namespace": "default",
    }


def x__cluster_context__mutmut_4(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "CLUSTER": context_name,
        "provider": "unknown",
        "namespace": "default",
    }


def x__cluster_context__mutmut_5(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "cluster": context_name,
        "XXproviderXX": "unknown",
        "namespace": "default",
    }


def x__cluster_context__mutmut_6(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "cluster": context_name,
        "PROVIDER": "unknown",
        "namespace": "default",
    }


def x__cluster_context__mutmut_7(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "cluster": context_name,
        "provider": "XXunknownXX",
        "namespace": "default",
    }


def x__cluster_context__mutmut_8(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "cluster": context_name,
        "provider": "UNKNOWN",
        "namespace": "default",
    }


def x__cluster_context__mutmut_9(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "cluster": context_name,
        "provider": "unknown",
        "XXnamespaceXX": "default",
    }


def x__cluster_context__mutmut_10(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "cluster": context_name,
        "provider": "unknown",
        "NAMESPACE": "default",
    }


def x__cluster_context__mutmut_11(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "cluster": context_name,
        "provider": "unknown",
        "namespace": "XXdefaultXX",
    }


def x__cluster_context__mutmut_12(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "cluster": context_name,
        "provider": "unknown",
        "namespace": "DEFAULT",
    }

mutants_x__cluster_context__mutmut['_mutmut_orig'] = x__cluster_context__mutmut_orig # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut['x__cluster_context__mutmut_1'] = x__cluster_context__mutmut_1 # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut['x__cluster_context__mutmut_2'] = x__cluster_context__mutmut_2 # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut['x__cluster_context__mutmut_3'] = x__cluster_context__mutmut_3 # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut['x__cluster_context__mutmut_4'] = x__cluster_context__mutmut_4 # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut['x__cluster_context__mutmut_5'] = x__cluster_context__mutmut_5 # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut['x__cluster_context__mutmut_6'] = x__cluster_context__mutmut_6 # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut['x__cluster_context__mutmut_7'] = x__cluster_context__mutmut_7 # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut['x__cluster_context__mutmut_8'] = x__cluster_context__mutmut_8 # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut['x__cluster_context__mutmut_9'] = x__cluster_context__mutmut_9 # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut['x__cluster_context__mutmut_10'] = x__cluster_context__mutmut_10 # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut['x__cluster_context__mutmut_11'] = x__cluster_context__mutmut_11 # type: ignore # mutmut generated
mutants_x__cluster_context__mutmut['x__cluster_context__mutmut_12'] = x__cluster_context__mutmut_12 # type: ignore # mutmut generated
mutants_x__aws_supported__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__aws_supported__mutmut)
def _aws_supported(context_name: str) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return AWSEKSProvider.supports(_cluster_context(context_name))


def x__aws_supported__mutmut_orig(context_name: str) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return AWSEKSProvider.supports(_cluster_context(context_name))


def x__aws_supported__mutmut_1(context_name: str) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return AWSEKSProvider.supports(None)


def x__aws_supported__mutmut_2(context_name: str) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return AWSEKSProvider.supports(_cluster_context(None))

mutants_x__aws_supported__mutmut['_mutmut_orig'] = x__aws_supported__mutmut_orig # type: ignore # mutmut generated
mutants_x__aws_supported__mutmut['x__aws_supported__mutmut_1'] = x__aws_supported__mutmut_1 # type: ignore # mutmut generated
mutants_x__aws_supported__mutmut['x__aws_supported__mutmut_2'] = x__aws_supported__mutmut_2 # type: ignore # mutmut generated
mutants_x__gcp_supported__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__gcp_supported__mutmut)
def _gcp_supported(context_name: str) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return GCPGKEProvider.supports(_cluster_context(context_name))


def x__gcp_supported__mutmut_orig(context_name: str) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return GCPGKEProvider.supports(_cluster_context(context_name))


def x__gcp_supported__mutmut_1(context_name: str) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return GCPGKEProvider.supports(None)


def x__gcp_supported__mutmut_2(context_name: str) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return GCPGKEProvider.supports(_cluster_context(None))

mutants_x__gcp_supported__mutmut['_mutmut_orig'] = x__gcp_supported__mutmut_orig # type: ignore # mutmut generated
mutants_x__gcp_supported__mutmut['x__gcp_supported__mutmut_1'] = x__gcp_supported__mutmut_1 # type: ignore # mutmut generated
mutants_x__gcp_supported__mutmut['x__gcp_supported__mutmut_2'] = x__gcp_supported__mutmut_2 # type: ignore # mutmut generated
mutants_x__azure_supported__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__azure_supported__mutmut)
def _azure_supported(context_name: str) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return AzureAKSProvider.supports(_cluster_context(context_name))


def x__azure_supported__mutmut_orig(context_name: str) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return AzureAKSProvider.supports(_cluster_context(context_name))


def x__azure_supported__mutmut_1(context_name: str) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return AzureAKSProvider.supports(None)


def x__azure_supported__mutmut_2(context_name: str) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return AzureAKSProvider.supports(_cluster_context(None))

mutants_x__azure_supported__mutmut['_mutmut_orig'] = x__azure_supported__mutmut_orig # type: ignore # mutmut generated
mutants_x__azure_supported__mutmut['x__azure_supported__mutmut_1'] = x__azure_supported__mutmut_1 # type: ignore # mutmut generated
mutants_x__azure_supported__mutmut['x__azure_supported__mutmut_2'] = x__azure_supported__mutmut_2 # type: ignore # mutmut generated


def _datadog_supported() -> bool:
    return is_datadog_configured()
mutants_x__provider_installed__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__provider_installed__mutmut)
def _provider_installed(provider: str) -> bool:
    if provider == "vanilla":
        return True
    return detect_installed_providers().get(provider, False)


def x__provider_installed__mutmut_orig(provider: str) -> bool:
    if provider == "vanilla":
        return True
    return detect_installed_providers().get(provider, False)


def x__provider_installed__mutmut_1(provider: str) -> bool:
    if provider != "vanilla":
        return True
    return detect_installed_providers().get(provider, False)


def x__provider_installed__mutmut_2(provider: str) -> bool:
    if provider == "XXvanillaXX":
        return True
    return detect_installed_providers().get(provider, False)


def x__provider_installed__mutmut_3(provider: str) -> bool:
    if provider == "VANILLA":
        return True
    return detect_installed_providers().get(provider, False)


def x__provider_installed__mutmut_4(provider: str) -> bool:
    if provider == "vanilla":
        return False
    return detect_installed_providers().get(provider, False)


def x__provider_installed__mutmut_5(provider: str) -> bool:
    if provider == "vanilla":
        return True
    return detect_installed_providers().get(None, False)


def x__provider_installed__mutmut_6(provider: str) -> bool:
    if provider == "vanilla":
        return True
    return detect_installed_providers().get(provider, None)


def x__provider_installed__mutmut_7(provider: str) -> bool:
    if provider == "vanilla":
        return True
    return detect_installed_providers().get(False)


def x__provider_installed__mutmut_8(provider: str) -> bool:
    if provider == "vanilla":
        return True
    return detect_installed_providers().get(provider, )


def x__provider_installed__mutmut_9(provider: str) -> bool:
    if provider == "vanilla":
        return True
    return detect_installed_providers().get(provider, True)

mutants_x__provider_installed__mutmut['_mutmut_orig'] = x__provider_installed__mutmut_orig # type: ignore # mutmut generated
mutants_x__provider_installed__mutmut['x__provider_installed__mutmut_1'] = x__provider_installed__mutmut_1 # type: ignore # mutmut generated
mutants_x__provider_installed__mutmut['x__provider_installed__mutmut_2'] = x__provider_installed__mutmut_2 # type: ignore # mutmut generated
mutants_x__provider_installed__mutmut['x__provider_installed__mutmut_3'] = x__provider_installed__mutmut_3 # type: ignore # mutmut generated
mutants_x__provider_installed__mutmut['x__provider_installed__mutmut_4'] = x__provider_installed__mutmut_4 # type: ignore # mutmut generated
mutants_x__provider_installed__mutmut['x__provider_installed__mutmut_5'] = x__provider_installed__mutmut_5 # type: ignore # mutmut generated
mutants_x__provider_installed__mutmut['x__provider_installed__mutmut_6'] = x__provider_installed__mutmut_6 # type: ignore # mutmut generated
mutants_x__provider_installed__mutmut['x__provider_installed__mutmut_7'] = x__provider_installed__mutmut_7 # type: ignore # mutmut generated
mutants_x__provider_installed__mutmut['x__provider_installed__mutmut_8'] = x__provider_installed__mutmut_8 # type: ignore # mutmut generated
mutants_x__provider_installed__mutmut['x__provider_installed__mutmut_9'] = x__provider_installed__mutmut_9 # type: ignore # mutmut generated


def _installed_provider_names() -> list[str]:
    return [provider.provider_name() for provider in list_installed_providers()]
