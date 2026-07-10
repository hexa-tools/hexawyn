from hexawyn.adapters.provider_registry import CloudProvider
from hexawyn.adapters.secondary.openshift.openshift_adapter import OpenShiftAdapter
from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort
from hexawyn.infrastructure.config.provider_detector import detect_installed_providers


class OpenShiftProvider(CloudProvider):
    """CloudProvider plugin for Red Hat OpenShift clusters.

    Selected automatically by the adapter factory when the openshift dependency
    is installed and the cluster context looks like OpenShift (CRC included).
    """

    @classmethod
    def supports(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("openshift", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "openshift" in name or "ocp" in name or provider == "openshift"

    @classmethod
    def build(cls, context: ClusterContext) -> K8sPort:
        return OpenShiftAdapter(context)

    @classmethod
    def provider_name(cls) -> str:
        return "OpenShift"

    @classmethod
    def provider_badge(cls) -> str:
        return "⛑ OpenShift"
