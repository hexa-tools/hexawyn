import os

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.infrastructure.config.provider_detector import detect_installed_providers


def build_adapters(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter bundle for the given cluster name.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Datadog → if DD_API_KEY set + datadog package installed
    3. AWS EKS → if "eks" in cluster name + boto3 installed
    4. Azure AKS → if "aks" in cluster name + azure installed
    5. GCP GKE → if "gke" in cluster name + gcp installed
    6. OpenShift → if "ocp/openshift" in cluster name + openshift installed
    7. Vanilla → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    installed = detect_installed_providers()
    name = cluster_name.lower()

    if installed["datadog"] and os.environ.get("DD_API_KEY"):
        from hexawyn.adapters.secondary.datadog.datadog_adapter import DatadogAdapter

        return DatadogAdapter(cluster_name)  # type: ignore[no-any-return]

    if installed["aws"] and "eks" in name:
        from hexawyn.adapters.secondary.aws.aws_adapter import AWSAdapter

        return AWSAdapter(cluster_name)  # type: ignore[no-any-return]

    if installed["azure"] and "aks" in name:
        from hexawyn.adapters.secondary.azure.azure_adapter import AzureAdapter

        return AzureAdapter(cluster_name)  # type: ignore[no-any-return]

    if installed["gcp"] and "gke" in name:
        from hexawyn.adapters.secondary.gcp.gcp_adapter import GCPAdapter

        return GCPAdapter(cluster_name)  # type: ignore[no-any-return]

    if installed["openshift"] and ("openshift" in name or "ocp" in name):
        from hexawyn.adapters.secondary.openshift.openshift_adapter import OpenShiftAdapter

        return OpenShiftAdapter(cluster_name)  # type: ignore[no-any-return]

    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    return VanillaAdapter(cluster_name)
