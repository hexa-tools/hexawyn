from unittest.mock import patch

import pytest

pytest.importorskip("azure.identity")

from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort  # noqa: E402


def _context(name: str, provider: str = "unknown") -> ClusterContext:
    return {"name": name, "cluster": name, "provider": provider, "namespace": "default"}


class TestAzureAKSProviderContract:
    def test_is_a_cloud_provider(self) -> None:
        from hexawyn.adapters.provider_registry import CloudProvider
        from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

        assert issubclass(AzureAKSProvider, CloudProvider)

    def test_provider_name(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

        assert AzureAKSProvider.provider_name() == "Azure AKS"

    def test_provider_badge(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

        assert "Azure" in AzureAKSProvider.provider_badge()


class TestSupports:
    def test_supports_when_aks_in_name(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

        with patch(
            "hexawyn.adapters.secondary.azure.azure_aks_provider.detect_installed_providers",
            return_value={"azure": True},
        ):
            assert AzureAKSProvider.supports(_context("aks-prod")) is True

    def test_supports_when_provider_is_azure(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

        with patch(
            "hexawyn.adapters.secondary.azure.azure_aks_provider.detect_installed_providers",
            return_value={"azure": True},
        ):
            assert AzureAKSProvider.supports(_context("prod", provider="azure")) is True

    def test_does_not_support_when_azure_not_installed(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

        with patch(
            "hexawyn.adapters.secondary.azure.azure_aks_provider.detect_installed_providers",
            return_value={"azure": False},
        ):
            assert AzureAKSProvider.supports(_context("aks-prod")) is False

    def test_does_not_support_minikube(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

        with patch(
            "hexawyn.adapters.secondary.azure.azure_aks_provider.detect_installed_providers",
            return_value={"azure": True},
        ):
            assert AzureAKSProvider.supports(_context("minikube")) is False


class TestBuild:
    def test_build_returns_k8s_port(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

        assert isinstance(AzureAKSProvider.build(_context("aks-prod")), K8sPort)

    def test_build_returns_aks_adapter(self) -> None:
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter
        from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

        assert isinstance(AzureAKSProvider.build(_context("aks-prod")), AzureAKSAdapter)


class TestFactoryDiscovery:
    def test_factory_selects_aks_provider(self) -> None:
        import os

        from hexawyn.adapters.secondary.adapter_factory import build_adapters
        from hexawyn.adapters.secondary.azure.aks_adapter import AzureAKSAdapter

        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            adapter = build_adapters("aks-prod-cluster")

        assert isinstance(adapter, AzureAKSAdapter)

    def test_factory_falls_back_to_vanilla(self) -> None:
        import os

        from hexawyn.adapters.secondary.adapter_factory import build_adapters
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            adapter = build_adapters("plain-minikube")

        assert isinstance(adapter, VanillaAdapter)
