from unittest.mock import patch

from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort


def _context(name: str, provider: str = "unknown") -> ClusterContext:
    return {"name": name, "cluster": name, "provider": provider, "namespace": "default"}


class TestOpenShiftProviderContract:
    def test_is_a_cloud_provider(self) -> None:
        from hexawyn.adapters.provider_registry import CloudProvider
        from hexawyn.adapters.secondary.openshift.openshift_provider import (
            OpenShiftProvider,
        )

        assert issubclass(OpenShiftProvider, CloudProvider)

    def test_provider_name(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_provider import (
            OpenShiftProvider,
        )

        assert OpenShiftProvider.provider_name() == "OpenShift"

    def test_provider_badge(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_provider import (
            OpenShiftProvider,
        )

        assert "OpenShift" in OpenShiftProvider.provider_badge()


class TestSupports:
    def _patch_detector(self, installed: bool):
        return patch(
            "hexawyn.adapters.secondary.openshift.openshift_provider." "detect_installed_providers",
            return_value={"openshift": installed},
        )

    def test_supports_when_openshift_in_name(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_provider import (
            OpenShiftProvider,
        )

        with self._patch_detector(True):
            assert OpenShiftProvider.supports(_context("openshift-prod")) is True

    def test_supports_when_ocp_in_name(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_provider import (
            OpenShiftProvider,
        )

        with self._patch_detector(True):
            assert OpenShiftProvider.supports(_context("ocp-eu-1")) is True

    def test_supports_when_provider_is_openshift(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_provider import (
            OpenShiftProvider,
        )

        with self._patch_detector(True):
            assert OpenShiftProvider.supports(_context("prod", provider="openshift")) is True

    def test_supports_crc_local_cluster(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_provider import (
            OpenShiftProvider,
        )

        with self._patch_detector(True):
            assert OpenShiftProvider.supports(_context("crc-openshift")) is True

    def test_does_not_support_when_openshift_not_installed(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_provider import (
            OpenShiftProvider,
        )

        with self._patch_detector(False):
            assert OpenShiftProvider.supports(_context("openshift-prod")) is False

    def test_does_not_support_vanilla_cluster(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_provider import (
            OpenShiftProvider,
        )

        with self._patch_detector(True):
            assert OpenShiftProvider.supports(_context("minikube")) is False


class TestBuild:
    def test_build_returns_k8s_port(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_provider import (
            OpenShiftProvider,
        )

        assert isinstance(OpenShiftProvider.build(_context("ocp-prod")), K8sPort)

    def test_build_returns_openshift_adapter(self) -> None:
        from hexawyn.adapters.secondary.openshift.openshift_adapter import (
            OpenShiftAdapter,
        )
        from hexawyn.adapters.secondary.openshift.openshift_provider import (
            OpenShiftProvider,
        )

        assert isinstance(OpenShiftProvider.build(_context("ocp-prod")), OpenShiftAdapter)
