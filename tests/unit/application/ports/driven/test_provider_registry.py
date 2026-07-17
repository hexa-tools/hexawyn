from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort


class TestCloudProviderABC:
    def test_cloud_provider_is_abstract(self) -> None:
        from hexawyn.adapters.provider_registry import CloudProvider

        with pytest.raises(TypeError):
            CloudProvider()  # type: ignore[abstract]

    def test_concrete_provider_implements_abc(self) -> None:
        from hexawyn.adapters.provider_registry import CloudProvider

        class FakeProvider(CloudProvider):
            @classmethod
            def supports(cls, context: ClusterContext) -> bool:
                return True

            @classmethod
            def build(cls, context: ClusterContext) -> K8sPort:
                return MagicMock(spec=K8sPort)

            @classmethod
            def provider_name(cls) -> str:
                return "Fake"

            @classmethod
            def provider_badge(cls) -> str:
                return "F"

        assert FakeProvider.supports(
            {"name": "test", "cluster": "test", "provider": "test", "namespace": "test"}
        )
        assert FakeProvider.provider_name() == "Fake"
        assert FakeProvider.provider_badge() == "F"

    def test_supports_must_be_implemented(self) -> None:
        from hexawyn.adapters.provider_registry import CloudProvider

        class IncompleteProvider(CloudProvider):
            @classmethod
            def build(cls, context: ClusterContext) -> K8sPort:
                return MagicMock(spec=K8sPort)

            @classmethod
            def provider_name(cls) -> str:
                return "Incomplete"

            @classmethod
            def provider_badge(cls) -> str:
                return "I"

        with pytest.raises(TypeError):
            IncompleteProvider()  # type: ignore[abstract]

    def test_abstract_methods_are_defined(self) -> None:
        from hexawyn.adapters.provider_registry import CloudProvider

        methods = {"supports", "build", "provider_name", "provider_badge"}
        abstract_methods = {m for m in dir(CloudProvider) if not m.startswith("_")}
        assert methods.issubset(abstract_methods)


class TestDiscoverEntryPoints:
    def test_python_3_12_entry_points_with_group(self) -> None:
        """entry_points(group=...) works on Python 3.12+."""
        from hexawyn.adapters.secondary.adapter_factory import _discover_entry_points

        result = _discover_entry_points()
        assert isinstance(result, list)

    def test_python_pre_3_12_fallback_via_typeerror(self) -> None:
        """When entry_points(group=...) raises TypeError, fall back to .get()."""

        def pre_312_entry_points(**kwargs):
            if kwargs:
                raise TypeError("entry_points() got an unexpected keyword argument 'group'")
            return {}

        with patch(
            "hexawyn.adapters.secondary.adapter_factory.entry_points",
            side_effect=pre_312_entry_points,
        ):
            from hexawyn.adapters.secondary.adapter_factory import _discover_entry_points

            result = _discover_entry_points()
            assert isinstance(result, list)


class TestListInstalledProviders:
    def test_returns_empty_when_no_providers(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.adapter_factory._discover_entry_points",
            return_value=[],
        ):
            from hexawyn.adapters.secondary.adapter_factory import (
                list_installed_providers,
            )

            providers = list_installed_providers()
            assert providers == []

    def test_skips_entry_point_that_fails_to_load(self) -> None:
        bad_ep = MagicMock()
        bad_ep.load.side_effect = ImportError("broken package")

        with patch(
            "hexawyn.adapters.secondary.adapter_factory._discover_entry_points",
            return_value=[bad_ep],
        ):
            from hexawyn.adapters.secondary.adapter_factory import (
                list_installed_providers,
            )

            providers = list_installed_providers()
            assert providers == []


class TestAdapterFactoryEntryPointsDiscovery:
    def test_demo_mode_still_wins(self) -> None:
        import os

        with patch.dict(
            os.environ,
            {"HEXAWYN_DEMO_MODE": "true", "HEXAWYN_DEMO_SCENARIO": "gcp_gke"},
        ):
            from hexawyn.adapters.secondary.adapter_factory import build_adapters
            from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

            adapter = build_adapters("any-cluster")
            assert isinstance(adapter, DemoAdapter)
            assert adapter.scenario == "gcp_gke"

    def test_demo_mode_false_no_demo_adapter(self) -> None:
        import os

        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}):
            from hexawyn.adapters.secondary.adapter_factory import build_adapters
            from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

            adapter = build_adapters("any-cluster")
            assert not isinstance(adapter, DemoAdapter)

    def test_vanilla_fallback_when_no_providers_installed(self) -> None:
        import os

        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            with patch(
                "hexawyn.adapters.secondary.adapter_factory.entry_points",
                return_value=[],
            ):
                from hexawyn.adapters.secondary.adapter_factory import build_adapters
                from hexawyn.adapters.secondary.vanilla.vanilla_adapter import (
                    VanillaAdapter,
                )

                adapter = build_adapters("any-cluster")
                assert isinstance(adapter, VanillaAdapter)

    def test_entry_points_discovery_selects_matching_provider(self) -> None:
        import os

        mock_provider = MagicMock()
        mock_provider.supports.return_value = True
        mock_provider.build.return_value = MagicMock(spec=K8sPort)
        mock_entry_point = MagicMock()
        mock_entry_point.load.return_value = mock_provider

        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            with patch(
                "hexawyn.adapters.secondary.adapter_factory.entry_points",
                return_value=[mock_entry_point],
            ):
                from hexawyn.adapters.secondary.adapter_factory import build_adapters

                build_adapters("eks-cluster")
                mock_provider.supports.assert_called_once()
                mock_provider.build.assert_called_once()

    def test_entry_points_skip_non_matching_provider(self) -> None:
        import os

        mock_aws = MagicMock()
        mock_aws.supports.return_value = False
        mock_aws.build.return_value = MagicMock(spec=K8sPort)
        ep_aws = MagicMock()
        ep_aws.load.return_value = mock_aws

        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            with patch(
                "hexawyn.adapters.secondary.adapter_factory.entry_points",
                return_value=[ep_aws],
            ):
                from hexawyn.adapters.secondary.adapter_factory import build_adapters
                from hexawyn.adapters.secondary.vanilla.vanilla_adapter import (
                    VanillaAdapter,
                )

                adapter = build_adapters("minikube")
                assert isinstance(adapter, VanillaAdapter)
                mock_aws.build.assert_not_called()

    def test_entry_points_skip_on_load_error(self) -> None:
        import os

        bad_ep = MagicMock()
        bad_ep.load.side_effect = ImportError("package not installed")

        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            with patch(
                "hexawyn.adapters.secondary.adapter_factory.entry_points",
                return_value=[bad_ep],
            ):
                from hexawyn.adapters.secondary.adapter_factory import build_adapters
                from hexawyn.adapters.secondary.vanilla.vanilla_adapter import (
                    VanillaAdapter,
                )

                adapter = build_adapters("any-cluster")
                assert isinstance(adapter, VanillaAdapter)

    def test_entry_points_skip_on_runtime_error(self) -> None:
        import os

        bad_ep = MagicMock()
        bad_ep.load.return_value.supports.side_effect = RuntimeError("unexpected error")

        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}, clear=False):
            with patch(
                "hexawyn.adapters.secondary.adapter_factory.entry_points",
                return_value=[bad_ep],
            ):
                from hexawyn.adapters.secondary.adapter_factory import build_adapters
                from hexawyn.adapters.secondary.vanilla.vanilla_adapter import (
                    VanillaAdapter,
                )

                adapter = build_adapters("any-cluster")
                assert isinstance(adapter, VanillaAdapter)

    def test_list_installed_providers_returns_providers(self) -> None:
        mock_provider = MagicMock()
        mock_entry_point = MagicMock()
        mock_entry_point.load.return_value = mock_provider

        with patch(
            "hexawyn.adapters.secondary.adapter_factory.entry_points",
            return_value=[mock_entry_point],
        ):
            from hexawyn.adapters.secondary.adapter_factory import (
                list_installed_providers,
            )

            providers = list_installed_providers()
            assert len(providers) == 1
            assert providers[0] is mock_provider

    def test_unknown_demo_scenario_falls_back_to_aws_eks(self) -> None:
        import os

        with patch.dict(
            os.environ,
            {"HEXAWYN_DEMO_MODE": "true", "HEXAWYN_DEMO_SCENARIO": "unknown"},
        ):
            from hexawyn.adapters.secondary.adapter_factory import build_adapters
            from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

            adapter = build_adapters("any-cluster")
            assert isinstance(adapter, DemoAdapter)
            assert adapter.scenario == "aws_eks"
