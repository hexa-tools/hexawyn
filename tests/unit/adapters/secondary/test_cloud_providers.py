from __future__ import annotations

from unittest.mock import patch

from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider
from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider
from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider


class TestAWSEKSProvider:
    def test_provider_name(self) -> None:
        assert AWSEKSProvider.provider_name() == "AWS EKS"

    def test_supports_eks(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.aws.aws_eks_provider.detect_installed_providers",
            return_value={"aws": True},
        ):
            assert (
                AWSEKSProvider.supports({"name": "my-eks-cluster", "provider": "vanilla"}) is True
            )

    def test_supports_aws_provider(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.aws.aws_eks_provider.detect_installed_providers",
            return_value={"aws": True},
        ):
            assert AWSEKSProvider.supports({"name": "my-cluster", "provider": "aws"}) is True

    def test_not_installed(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.aws.aws_eks_provider.detect_installed_providers",
            return_value={"aws": False},
        ):
            assert AWSEKSProvider.supports({"name": "eks-cluster", "provider": "vanilla"}) is False

    def test_not_eks(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.aws.aws_eks_provider.detect_installed_providers",
            return_value={"aws": True},
        ):
            assert AWSEKSProvider.supports({"name": "my-cluster", "provider": "gcp"}) is False


class TestAzureAKSProvider:
    def test_provider_name(self) -> None:
        assert AzureAKSProvider.provider_name() == "Azure AKS"


class TestGCPGKEProvider:
    def test_provider_name(self) -> None:
        assert GCPGKEProvider.provider_name() == "GCP GKE"
