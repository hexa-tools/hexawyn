from hexawyn.adapters.secondary.adapter_factory import list_installed_providers
from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider
from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider
from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider
from hexawyn.application.ports.driven.k8s_port import ClusterContext
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


def _force_lines(context_name: str, provider: str) -> list[tuple[str, str]]:
    set_stack_override(context_name, provider)
    lines = [(f"Stack forced to '{provider}' for context '{context_name}'.", "green")]
    if not _provider_installed(provider):
        lines.append((_INSTALL_HINTS[provider], "yellow"))
    return lines


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


def _parse_argument(text: str) -> str | None:
    parts = text.split(maxsplit=1)
    if len(parts) < 2 or not parts[1].strip():
        return None
    return parts[1].strip().lower()


def _cluster_context(context_name: str) -> ClusterContext:
    return {
        "name": context_name,
        "cluster": context_name,
        "provider": "unknown",
        "namespace": "default",
    }


def _aws_supported(context_name: str) -> bool:
    return AWSEKSProvider.supports(_cluster_context(context_name))


def _gcp_supported(context_name: str) -> bool:
    return GCPGKEProvider.supports(_cluster_context(context_name))


def _azure_supported(context_name: str) -> bool:
    return AzureAKSProvider.supports(_cluster_context(context_name))


def _datadog_supported() -> bool:
    return is_datadog_configured()


def _provider_installed(provider: str) -> bool:
    if provider == "vanilla":
        return True
    return detect_installed_providers().get(provider, False)


def _installed_provider_names() -> list[str]:
    return [provider.provider_name() for provider in list_installed_providers()]
