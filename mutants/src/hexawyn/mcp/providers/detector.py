from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

    from hexawyn.application.ports.driven.k8s_port import ClusterContext

context_name: str = "unknown"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__detect_provider__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_provider__mutmut)
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


def x__detect_provider__mutmut_orig(
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


def x__detect_provider__mutmut_1(
    context: ClusterContext,
    provider_key: str,
    supports: Callable[[ClusterContext], bool],
) -> bool:
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = None
    if override is not None:
        return override == provider_key

    try:
        return supports(context)
    except Exception:
        return False


def x__detect_provider__mutmut_2(
    context: ClusterContext,
    provider_key: str,
    supports: Callable[[ClusterContext], bool],
) -> bool:
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(None)
    if override is not None:
        return override == provider_key

    try:
        return supports(context)
    except Exception:
        return False


def x__detect_provider__mutmut_3(
    context: ClusterContext,
    provider_key: str,
    supports: Callable[[ClusterContext], bool],
) -> bool:
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["XXnameXX"])
    if override is not None:
        return override == provider_key

    try:
        return supports(context)
    except Exception:
        return False


def x__detect_provider__mutmut_4(
    context: ClusterContext,
    provider_key: str,
    supports: Callable[[ClusterContext], bool],
) -> bool:
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["NAME"])
    if override is not None:
        return override == provider_key

    try:
        return supports(context)
    except Exception:
        return False


def x__detect_provider__mutmut_5(
    context: ClusterContext,
    provider_key: str,
    supports: Callable[[ClusterContext], bool],
) -> bool:
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is None:
        return override == provider_key

    try:
        return supports(context)
    except Exception:
        return False


def x__detect_provider__mutmut_6(
    context: ClusterContext,
    provider_key: str,
    supports: Callable[[ClusterContext], bool],
) -> bool:
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is not None:
        return override != provider_key

    try:
        return supports(context)
    except Exception:
        return False


def x__detect_provider__mutmut_7(
    context: ClusterContext,
    provider_key: str,
    supports: Callable[[ClusterContext], bool],
) -> bool:
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is not None:
        return override == provider_key

    try:
        return supports(None)
    except Exception:
        return False


def x__detect_provider__mutmut_8(
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
        return True

mutants_x__detect_provider__mutmut['_mutmut_orig'] = x__detect_provider__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_provider__mutmut['x__detect_provider__mutmut_1'] = x__detect_provider__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_provider__mutmut['x__detect_provider__mutmut_2'] = x__detect_provider__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_provider__mutmut['x__detect_provider__mutmut_3'] = x__detect_provider__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_provider__mutmut['x__detect_provider__mutmut_4'] = x__detect_provider__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_provider__mutmut['x__detect_provider__mutmut_5'] = x__detect_provider__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_provider__mutmut['x__detect_provider__mutmut_6'] = x__detect_provider__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_provider__mutmut['x__detect_provider__mutmut_7'] = x__detect_provider__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_provider__mutmut['x__detect_provider__mutmut_8'] = x__detect_provider__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_aws_eks_context__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_aws_eks_context__mutmut)
def _is_aws_eks_context(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return _detect_provider(context, "aws", AWSEKSProvider.supports)


def x__is_aws_eks_context__mutmut_orig(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return _detect_provider(context, "aws", AWSEKSProvider.supports)


def x__is_aws_eks_context__mutmut_1(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return _detect_provider(None, "aws", AWSEKSProvider.supports)


def x__is_aws_eks_context__mutmut_2(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return _detect_provider(context, None, AWSEKSProvider.supports)


def x__is_aws_eks_context__mutmut_3(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return _detect_provider(context, "aws", None)


def x__is_aws_eks_context__mutmut_4(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return _detect_provider("aws", AWSEKSProvider.supports)


def x__is_aws_eks_context__mutmut_5(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return _detect_provider(context, AWSEKSProvider.supports)


def x__is_aws_eks_context__mutmut_6(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return _detect_provider(context, "aws", )


def x__is_aws_eks_context__mutmut_7(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return _detect_provider(context, "XXawsXX", AWSEKSProvider.supports)


def x__is_aws_eks_context__mutmut_8(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return _detect_provider(context, "AWS", AWSEKSProvider.supports)

mutants_x__is_aws_eks_context__mutmut['_mutmut_orig'] = x__is_aws_eks_context__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_aws_eks_context__mutmut['x__is_aws_eks_context__mutmut_1'] = x__is_aws_eks_context__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_aws_eks_context__mutmut['x__is_aws_eks_context__mutmut_2'] = x__is_aws_eks_context__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_aws_eks_context__mutmut['x__is_aws_eks_context__mutmut_3'] = x__is_aws_eks_context__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_aws_eks_context__mutmut['x__is_aws_eks_context__mutmut_4'] = x__is_aws_eks_context__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_aws_eks_context__mutmut['x__is_aws_eks_context__mutmut_5'] = x__is_aws_eks_context__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_aws_eks_context__mutmut['x__is_aws_eks_context__mutmut_6'] = x__is_aws_eks_context__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_aws_eks_context__mutmut['x__is_aws_eks_context__mutmut_7'] = x__is_aws_eks_context__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_aws_eks_context__mutmut['x__is_aws_eks_context__mutmut_8'] = x__is_aws_eks_context__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_gcp_gke_context__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_gcp_gke_context__mutmut)
def _is_gcp_gke_context(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return _detect_provider(context, "gcp", GCPGKEProvider.supports)


def x__is_gcp_gke_context__mutmut_orig(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return _detect_provider(context, "gcp", GCPGKEProvider.supports)


def x__is_gcp_gke_context__mutmut_1(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return _detect_provider(None, "gcp", GCPGKEProvider.supports)


def x__is_gcp_gke_context__mutmut_2(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return _detect_provider(context, None, GCPGKEProvider.supports)


def x__is_gcp_gke_context__mutmut_3(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return _detect_provider(context, "gcp", None)


def x__is_gcp_gke_context__mutmut_4(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return _detect_provider("gcp", GCPGKEProvider.supports)


def x__is_gcp_gke_context__mutmut_5(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return _detect_provider(context, GCPGKEProvider.supports)


def x__is_gcp_gke_context__mutmut_6(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return _detect_provider(context, "gcp", )


def x__is_gcp_gke_context__mutmut_7(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return _detect_provider(context, "XXgcpXX", GCPGKEProvider.supports)


def x__is_gcp_gke_context__mutmut_8(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return _detect_provider(context, "GCP", GCPGKEProvider.supports)

mutants_x__is_gcp_gke_context__mutmut['_mutmut_orig'] = x__is_gcp_gke_context__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_gcp_gke_context__mutmut['x__is_gcp_gke_context__mutmut_1'] = x__is_gcp_gke_context__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_gcp_gke_context__mutmut['x__is_gcp_gke_context__mutmut_2'] = x__is_gcp_gke_context__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_gcp_gke_context__mutmut['x__is_gcp_gke_context__mutmut_3'] = x__is_gcp_gke_context__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_gcp_gke_context__mutmut['x__is_gcp_gke_context__mutmut_4'] = x__is_gcp_gke_context__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_gcp_gke_context__mutmut['x__is_gcp_gke_context__mutmut_5'] = x__is_gcp_gke_context__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_gcp_gke_context__mutmut['x__is_gcp_gke_context__mutmut_6'] = x__is_gcp_gke_context__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_gcp_gke_context__mutmut['x__is_gcp_gke_context__mutmut_7'] = x__is_gcp_gke_context__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_gcp_gke_context__mutmut['x__is_gcp_gke_context__mutmut_8'] = x__is_gcp_gke_context__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_azure_aks_context__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_azure_aks_context__mutmut)
def _is_azure_aks_context(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return _detect_provider(context, "azure", AzureAKSProvider.supports)


def x__is_azure_aks_context__mutmut_orig(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return _detect_provider(context, "azure", AzureAKSProvider.supports)


def x__is_azure_aks_context__mutmut_1(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return _detect_provider(None, "azure", AzureAKSProvider.supports)


def x__is_azure_aks_context__mutmut_2(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return _detect_provider(context, None, AzureAKSProvider.supports)


def x__is_azure_aks_context__mutmut_3(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return _detect_provider(context, "azure", None)


def x__is_azure_aks_context__mutmut_4(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return _detect_provider("azure", AzureAKSProvider.supports)


def x__is_azure_aks_context__mutmut_5(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return _detect_provider(context, AzureAKSProvider.supports)


def x__is_azure_aks_context__mutmut_6(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return _detect_provider(context, "azure", )


def x__is_azure_aks_context__mutmut_7(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return _detect_provider(context, "XXazureXX", AzureAKSProvider.supports)


def x__is_azure_aks_context__mutmut_8(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return _detect_provider(context, "AZURE", AzureAKSProvider.supports)

mutants_x__is_azure_aks_context__mutmut['_mutmut_orig'] = x__is_azure_aks_context__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_azure_aks_context__mutmut['x__is_azure_aks_context__mutmut_1'] = x__is_azure_aks_context__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_azure_aks_context__mutmut['x__is_azure_aks_context__mutmut_2'] = x__is_azure_aks_context__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_azure_aks_context__mutmut['x__is_azure_aks_context__mutmut_3'] = x__is_azure_aks_context__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_azure_aks_context__mutmut['x__is_azure_aks_context__mutmut_4'] = x__is_azure_aks_context__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_azure_aks_context__mutmut['x__is_azure_aks_context__mutmut_5'] = x__is_azure_aks_context__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_azure_aks_context__mutmut['x__is_azure_aks_context__mutmut_6'] = x__is_azure_aks_context__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_azure_aks_context__mutmut['x__is_azure_aks_context__mutmut_7'] = x__is_azure_aks_context__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_azure_aks_context__mutmut['x__is_azure_aks_context__mutmut_8'] = x__is_azure_aks_context__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_datadog_enabled__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_datadog_enabled__mutmut)
def _is_datadog_enabled(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is not None:
        return override == "datadog"
    return is_datadog_configured()


def x__is_datadog_enabled__mutmut_orig(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is not None:
        return override == "datadog"
    return is_datadog_configured()


def x__is_datadog_enabled__mutmut_1(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = None
    if override is not None:
        return override == "datadog"
    return is_datadog_configured()


def x__is_datadog_enabled__mutmut_2(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(None)
    if override is not None:
        return override == "datadog"
    return is_datadog_configured()


def x__is_datadog_enabled__mutmut_3(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["XXnameXX"])
    if override is not None:
        return override == "datadog"
    return is_datadog_configured()


def x__is_datadog_enabled__mutmut_4(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["NAME"])
    if override is not None:
        return override == "datadog"
    return is_datadog_configured()


def x__is_datadog_enabled__mutmut_5(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is None:
        return override == "datadog"
    return is_datadog_configured()


def x__is_datadog_enabled__mutmut_6(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is not None:
        return override != "datadog"
    return is_datadog_configured()


def x__is_datadog_enabled__mutmut_7(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is not None:
        return override == "XXdatadogXX"
    return is_datadog_configured()


def x__is_datadog_enabled__mutmut_8(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is not None:
        return override == "DATADOG"
    return is_datadog_configured()

mutants_x__is_datadog_enabled__mutmut['_mutmut_orig'] = x__is_datadog_enabled__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_datadog_enabled__mutmut['x__is_datadog_enabled__mutmut_1'] = x__is_datadog_enabled__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_datadog_enabled__mutmut['x__is_datadog_enabled__mutmut_2'] = x__is_datadog_enabled__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_datadog_enabled__mutmut['x__is_datadog_enabled__mutmut_3'] = x__is_datadog_enabled__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_datadog_enabled__mutmut['x__is_datadog_enabled__mutmut_4'] = x__is_datadog_enabled__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_datadog_enabled__mutmut['x__is_datadog_enabled__mutmut_5'] = x__is_datadog_enabled__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_datadog_enabled__mutmut['x__is_datadog_enabled__mutmut_6'] = x__is_datadog_enabled__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_datadog_enabled__mutmut['x__is_datadog_enabled__mutmut_7'] = x__is_datadog_enabled__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_datadog_enabled__mutmut['x__is_datadog_enabled__mutmut_8'] = x__is_datadog_enabled__mutmut_8 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__current_cluster_context__mutmut)
def _current_cluster_context() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_orig() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_1() -> ClusterContext:
    name = None
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_2() -> ClusterContext:
    name = context_name if context_name == "unknown" else "default"
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_3() -> ClusterContext:
    name = context_name if context_name != "XXunknownXX" else "default"
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_4() -> ClusterContext:
    name = context_name if context_name != "UNKNOWN" else "default"
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_5() -> ClusterContext:
    name = context_name if context_name != "unknown" else "XXdefaultXX"
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_6() -> ClusterContext:
    name = context_name if context_name != "unknown" else "DEFAULT"
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_7() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"XXnameXX": name, "cluster": name, "provider": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_8() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"NAME": name, "cluster": name, "provider": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_9() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "XXclusterXX": name, "provider": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_10() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "CLUSTER": name, "provider": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_11() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "XXproviderXX": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_12() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "PROVIDER": "unknown", "namespace": "default"}


def x__current_cluster_context__mutmut_13() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "provider": "XXunknownXX", "namespace": "default"}


def x__current_cluster_context__mutmut_14() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "provider": "UNKNOWN", "namespace": "default"}


def x__current_cluster_context__mutmut_15() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "provider": "unknown", "XXnamespaceXX": "default"}


def x__current_cluster_context__mutmut_16() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "provider": "unknown", "NAMESPACE": "default"}


def x__current_cluster_context__mutmut_17() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "XXdefaultXX"}


def x__current_cluster_context__mutmut_18() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "DEFAULT"}

mutants_x__current_cluster_context__mutmut['_mutmut_orig'] = x__current_cluster_context__mutmut_orig # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_1'] = x__current_cluster_context__mutmut_1 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_2'] = x__current_cluster_context__mutmut_2 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_3'] = x__current_cluster_context__mutmut_3 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_4'] = x__current_cluster_context__mutmut_4 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_5'] = x__current_cluster_context__mutmut_5 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_6'] = x__current_cluster_context__mutmut_6 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_7'] = x__current_cluster_context__mutmut_7 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_8'] = x__current_cluster_context__mutmut_8 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_9'] = x__current_cluster_context__mutmut_9 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_10'] = x__current_cluster_context__mutmut_10 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_11'] = x__current_cluster_context__mutmut_11 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_12'] = x__current_cluster_context__mutmut_12 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_13'] = x__current_cluster_context__mutmut_13 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_14'] = x__current_cluster_context__mutmut_14 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_15'] = x__current_cluster_context__mutmut_15 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_16'] = x__current_cluster_context__mutmut_16 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_17'] = x__current_cluster_context__mutmut_17 # type: ignore # mutmut generated
mutants_x__current_cluster_context__mutmut['x__current_cluster_context__mutmut_18'] = x__current_cluster_context__mutmut_18 # type: ignore # mutmut generated
