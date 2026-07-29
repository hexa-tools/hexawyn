from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

    from hexawyn.application.ports.driven.k8s_port import ClusterContext

context_name: str = "unknown"


def _detect_provider(
    context: ClusterContext,
    provider_key: str,
    supports: Callable[[ClusterContext], bool],
) -> bool:
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is not None:
        return override == provider_key

    try:
        return supports(context)
    except Exception:
        return False


def _is_aws_eks_context(context: ClusterContext) -> bool:
    from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return _detect_provider(context, "aws", AWSEKSProvider.supports)


def _is_gcp_gke_context(context: ClusterContext) -> bool:
    from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return _detect_provider(context, "gcp", GCPGKEProvider.supports)


def _is_azure_aks_context(context: ClusterContext) -> bool:
    from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return _detect_provider(context, "azure", AzureAKSProvider.supports)


def _is_datadog_enabled(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is not None:
        return override == "datadog"
    return is_datadog_configured()


def _current_cluster_context() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "default"}
