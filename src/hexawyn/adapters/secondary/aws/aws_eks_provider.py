from hexawyn.adapters.provider_registry import CloudProvider
from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort
from hexawyn.infrastructure.config.provider_detector import detect_installed_providers

_EKS_ARN_PREFIX = "arn:aws:eks:"


class AWSEKSProvider(CloudProvider):
    """CloudProvider plugin for AWS EKS clusters.

    Selected automatically by the adapter factory when the boto3 dependency is
    installed and the cluster context looks like an EKS cluster.
    """

    @classmethod
    def supports(cls, context: ClusterContext) -> bool:
        if not detect_installed_providers().get("aws", False):
            return False
        name = context.get("name", "").lower()
        provider = context.get("provider", "").lower()
        return "eks" in name or provider == "aws" or name.startswith(_EKS_ARN_PREFIX)

    @classmethod
    def build(cls, context: ClusterContext) -> K8sPort:
        return AWSEKSAdapter(context)

    @classmethod
    def provider_name(cls) -> str:
        return "AWS EKS"

    @classmethod
    def provider_badge(cls) -> str:
        return "☁ AWS"
