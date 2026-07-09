from hexawyn.adapters.provider_registry import CloudProvider
from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort
from hexawyn.infrastructure.config.provider_detector import detect_installed_providers


class GCPGKEProvider(CloudProvider):
    """CloudProvider plugin for GCP GKE clusters.

    Selected automatically by the adapter factory when the google-cloud
    dependencies are installed and the cluster context looks like GKE.
    """

    @classmethod
    def supports(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("gcp", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "gke" in name or provider == "gcp"

    @classmethod
    def build(cls, context: ClusterContext) -> K8sPort:
        return GCPGKEAdapter(context)

    @classmethod
    def provider_name(cls) -> str:
        return "GCP GKE"

    @classmethod
    def provider_badge(cls) -> str:
        return "☁ GCP"
