from unittest.mock import patch

import pytest

pytest.importorskip("boto3")

from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort  # noqa: E402


def _context(name: str, provider: str = "unknown") -> ClusterContext:
    return {"name": name, "cluster": name, "provider": provider, "namespace": "default"}


class TestAWSEKSProviderContract:
    def test_is_a_cloud_provider(self) -> None:
        from hexawyn.adapters.provider_registry import CloudProvider
        from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

        assert issubclass(AWSEKSProvider, CloudProvider)

    def test_provider_name(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

        assert AWSEKSProvider.provider_name() == "AWS EKS"

    def test_provider_badge(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

        assert "AWS" in AWSEKSProvider.provider_badge()


class TestSupports:
    def test_supports_when_eks_in_name(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

        with patch(
            "hexawyn.adapters.secondary.aws.aws_eks_provider.detect_installed_providers",
            return_value={"aws": True},
        ):
            assert AWSEKSProvider.supports(_context("my-eks-prod")) is True

    def test_supports_when_provider_is_aws(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

        with patch(
            "hexawyn.adapters.secondary.aws.aws_eks_provider.detect_installed_providers",
            return_value={"aws": True},
        ):
            assert AWSEKSProvider.supports(_context("prod", provider="aws")) is True

    def test_supports_when_eks_arn(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

        with patch(
            "hexawyn.adapters.secondary.aws.aws_eks_provider.detect_installed_providers",
            return_value={"aws": True},
        ):
            arn = "arn:aws:eks:eu-west-1:123456789012:cluster/prod"
            assert AWSEKSProvider.supports(_context(arn)) is True

    def test_does_not_support_when_boto3_missing(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

        with patch(
            "hexawyn.adapters.secondary.aws.aws_eks_provider.detect_installed_providers",
            return_value={"aws": False},
        ):
            assert AWSEKSProvider.supports(_context("my-eks-prod")) is False

    def test_does_not_support_vanilla_cluster(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

        with patch(
            "hexawyn.adapters.secondary.aws.aws_eks_provider.detect_installed_providers",
            return_value={"aws": True},
        ):
            assert AWSEKSProvider.supports(_context("minikube")) is False


class TestBuild:
    def test_build_returns_k8s_port(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

        result = AWSEKSProvider.build(_context("eks-prod"))

        assert isinstance(result, K8sPort)

    def test_build_returns_eks_adapter(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        result = AWSEKSProvider.build(_context("eks-prod"))

        assert isinstance(result, AWSEKSAdapter)


class TestFactoryDiscovery:
    def test_factory_selects_eks_provider_for_eks_cluster(self) -> None:
        import os

        from hexawyn.adapters.secondary.adapter_factory import build_adapters
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            adapter = build_adapters("prod-eks-cluster")

        assert isinstance(adapter, AWSEKSAdapter)

    def test_factory_falls_back_to_vanilla_for_non_eks(self) -> None:
        import os

        from hexawyn.adapters.secondary.adapter_factory import build_adapters
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            adapter = build_adapters("plain-minikube")

        assert isinstance(adapter, VanillaAdapter)
