from hexawyn.adapters.provider_registry import CloudProvider
from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter
from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort
from hexawyn.infrastructure.config.provider_detector import detect_installed_providers


class AzureAKSProvider(CloudProvider):
    """CloudProvider plugin for Azure AKS clusters.

    Selected automatically by the adapter factory when the azure dependencies
    are installed and the cluster context looks like AKS.
    """

    @classmethod
    def supports(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("azure", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "aks" in name or provider == "azure"

    @classmethod
    def build(cls, context: ClusterContext) -> K8sPort:
        return AzureAKSAdapter(context)

    @classmethod
    def provider_name(cls) -> str:
        return "Azure AKS"

    @classmethod
    def provider_badge(cls) -> str:
        return "☁ Azure"
