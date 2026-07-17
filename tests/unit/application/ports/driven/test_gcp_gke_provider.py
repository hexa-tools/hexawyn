from unittest.mock import patch

import pytest

pytest.importorskip("google.cloud.container")

from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort  # noqa: E402


def _context(name: str, provider: str = "unknown") -> ClusterContext:
    return {"name": name, "cluster": name, "provider": provider, "namespace": "default"}


class TestGCPGKEProviderContract:
    def test_is_a_cloud_provider(self) -> None:
        from hexawyn.adapters.provider_registry import CloudProvider
        from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

        assert issubclass(GCPGKEProvider, CloudProvider)

    def test_provider_name(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

        assert GCPGKEProvider.provider_name() == "GCP GKE"

    def test_provider_badge(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

        assert "GCP" in GCPGKEProvider.provider_badge()


class TestSupports:
    def test_supports_when_gke_in_name(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

        with patch(
            "hexawyn.adapters.secondary.gcp.gcp_gke_provider.detect_installed_providers",
            return_value={"gcp": True},
        ):
            assert GCPGKEProvider.supports(_context("gke_my-project_europe-west1_cluster")) is True

    def test_supports_when_provider_is_gcp(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

        with patch(
            "hexawyn.adapters.secondary.gcp.gcp_gke_provider.detect_installed_providers",
            return_value={"gcp": True},
        ):
            assert GCPGKEProvider.supports(_context("prod", provider="gcp")) is True

    def test_does_not_support_when_google_not_installed(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

        with patch(
            "hexawyn.adapters.secondary.gcp.gcp_gke_provider.detect_installed_providers",
            return_value={"gcp": False},
        ):
            assert GCPGKEProvider.supports(_context("gke_my-project_europe-west1_cluster")) is False

    def test_does_not_support_minikube(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

        with patch(
            "hexawyn.adapters.secondary.gcp.gcp_gke_provider.detect_installed_providers",
            return_value={"gcp": True},
        ):
            assert GCPGKEProvider.supports(_context("minikube")) is False


class TestBuild:
    def test_build_returns_k8s_port(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

        result = GCPGKEProvider.build(_context("gke_p_r_c"))

        assert isinstance(result, K8sPort)

    def test_build_returns_gke_adapter(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        result = GCPGKEProvider.build(_context("gke_p_r_c"))

        assert isinstance(result, GCPGKEAdapter)


class TestFactoryDiscovery:
    def test_factory_selects_gke_provider_for_gke_cluster(self) -> None:
        import os

        from hexawyn.adapters.secondary.adapter_factory import build_adapters
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            adapter = build_adapters("gke_my-project_europe-west1_prod")

        assert isinstance(adapter, GCPGKEAdapter)

    def test_factory_falls_back_to_vanilla_for_non_gke(self) -> None:
        import os

        from hexawyn.adapters.secondary.adapter_factory import build_adapters
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            adapter = build_adapters("plain-minikube")

        assert isinstance(adapter, VanillaAdapter)
