from pathlib import Path
from unittest.mock import ANY, MagicMock, patch

from hexawyn.infrastructure.config.kubernetes_context import (
    FileKubernetesDiscoveryService,
    HexawynContextConfig,
)


def _write_kubeconfig(path: Path, current_context: str, contexts: list[str]) -> None:
    context_entries = "\n".join(
        f"- name: {context_name}\n"
        f"  context:\n"
        f"    cluster: cluster-{context_name}\n"
        f"    namespace: namespace-{context_name}\n"
        f"    user: user-{context_name}"
        for context_name in contexts
    )
    cluster_entries = "\n".join(
        f"- name: cluster-{context_name}\n"
        f"  cluster:\n"
        f"    server: https://{context_name}.example.test"
        for context_name in contexts
    )
    user_entries = "\n".join(
        f"- name: user-{context_name}\n  user:\n    token: token-{context_name}"
        for context_name in contexts
    )
    path.write_text(
        f"apiVersion: v1\n"
        f"kind: Config\n"
        f"current-context: {current_context}\n"
        f"clusters:\n{cluster_entries}\n"
        f"users:\n{user_entries}\n"
        f"contexts:\n{context_entries}\n",
        encoding="utf-8",
    )


class TestKubernetesContextDiscovery:
    def test_uses_kubeconfig_env_var_before_default_path(self, tmp_path: Path) -> None:
        env_config = tmp_path / "prod.yaml"
        default_config = tmp_path / "home" / ".kube" / "config"
        default_config.parent.mkdir(parents=True)
        _write_kubeconfig(env_config, "prod", ["prod"])
        _write_kubeconfig(default_config, "dev", ["dev"])
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )

        with patch.dict("os.environ", {"KUBECONFIG": str(env_config)}):
            current_context = service.current()

        assert current_context is not None
        assert current_context.name == "prod"
        assert current_context.cluster == "cluster-prod"

    def test_supports_multiple_kubeconfig_paths_from_env(self, tmp_path: Path) -> None:
        prod_config = tmp_path / "prod.yaml"
        staging_config = tmp_path / "staging.yaml"
        _write_kubeconfig(prod_config, "prod", ["prod"])
        _write_kubeconfig(staging_config, "staging", ["staging"])
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )

        with patch.dict("os.environ", {"KUBECONFIG": f"{prod_config}:{staging_config}"}):
            contexts = service.discover()

        assert [context.name for context in contexts] == ["prod", "staging"]
        assert contexts[0].is_current is True
        assert contexts[1].is_current is False

    def test_uses_standard_kubeconfig_when_env_is_missing(self, tmp_path: Path) -> None:
        default_config = tmp_path / "home" / ".kube" / "config"
        default_config.parent.mkdir(parents=True)
        _write_kubeconfig(default_config, "prod", ["prod", "staging", "dev"])
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )

        with patch.dict("os.environ", {}, clear=True):
            contexts = service.discover()
            current_context = service.current()

        assert len(contexts) == 3  # noqa: PLR2004
        assert current_context is not None
        assert current_context.name == "prod"

    def test_kubernetes_current_context_wins_over_persisted_context(self, tmp_path: Path) -> None:
        default_config = tmp_path / "home" / ".kube" / "config"
        hexawyn_config = tmp_path / "config" / "hexawyn" / "config.yaml"
        default_config.parent.mkdir(parents=True)
        _write_kubeconfig(default_config, "prod", ["prod", "staging"])
        HexawynContextConfig(config_path=hexawyn_config).save_context("staging")
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(config_path=hexawyn_config),
        )

        with patch.dict("os.environ", {}, clear=True):
            current_context = service.current()

        assert current_context is not None
        assert current_context.name == "prod"
        assert current_context.is_current is True

    def test_falls_back_to_kubernetes_current_context_when_persisted_context_is_missing(
        self, tmp_path: Path
    ) -> None:
        default_config = tmp_path / "home" / ".kube" / "config"
        hexawyn_config = tmp_path / "config" / "hexawyn" / "config.yaml"
        default_config.parent.mkdir(parents=True)
        _write_kubeconfig(default_config, "prod", ["prod"])
        HexawynContextConfig(config_path=hexawyn_config).save_context("deleted")
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(config_path=hexawyn_config),
        )

        with patch.dict("os.environ", {}, clear=True):
            current_context = service.current()

        assert current_context is not None
        assert current_context.name == "prod"

    def test_startup_status_reports_unreachable_without_blocking(self, tmp_path: Path) -> None:
        default_config = tmp_path / "home" / ".kube" / "config"
        default_config.parent.mkdir(parents=True)
        _write_kubeconfig(default_config, "prod", ["prod"])
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )

        with (
            patch.dict("os.environ", {}, clear=True),
            patch("kubernetes.config.load_kube_config"),
            patch("kubernetes.client.VersionApi") as version_api,
        ):
            version_api.return_value.get_code.side_effect = Exception("connection refused")
            status = service.startup_status()

        assert status.current_context is not None
        assert status.current_context.name == "prod"
        assert status.connected is False
        assert status.connection_error is not None
        assert "connection refused" in status.connection_error

    def test_switch_context_saves_preferred_context_and_revalidates(self, tmp_path: Path) -> None:
        env_config = tmp_path / "prod.yaml"
        hexawyn_config = tmp_path / "hexawyn-config.yaml"
        _write_kubeconfig(env_config, "prod", ["prod", "kind-ecom-local"])
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(hexawyn_config),
        )

        with (
            patch.dict("os.environ", {"KUBECONFIG": str(env_config)}),
            patch("kubernetes.config.load_kube_config") as load_kube_config,
            patch("kubernetes.client.VersionApi") as version_api,
        ):
            version_api.return_value.get_code.return_value = MagicMock()
            result = service.switch_context("kind-ecom-local")

        assert result.switched is True
        assert result.current_context is not None
        assert result.current_context.name == "kind-ecom-local"
        assert result.current_context.namespace == "namespace-kind-ecom-local"
        assert result.connected is True
        kubeconfig_after_switch = env_config.read_text(encoding="utf-8")
        assert "current-context: kind-ecom-local" in kubeconfig_after_switch
        load_kube_config.assert_called_once_with(
            config_file=str(env_config),
            context="kind-ecom-local",
            client_configuration=ANY,
        )

    def test_switch_context_reports_available_contexts_when_name_is_invalid(
        self, tmp_path: Path
    ) -> None:
        env_config = tmp_path / "prod.yaml"
        hexawyn_config = tmp_path / "hexawyn-config.yaml"
        _write_kubeconfig(env_config, "prod", ["prod", "kind-ecom-local"])
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(hexawyn_config),
        )

        with (
            patch.dict("os.environ", {"KUBECONFIG": str(env_config)}),
            patch("kubernetes.config.load_kube_config") as load_kube_config,
        ):
            result = service.switch_context("production")

        assert result.switched is False
        assert result.current_context is not None
        assert result.current_context.name == "prod"
        assert [context.name for context in result.contexts] == ["prod", "kind-ecom-local"]
        assert HexawynContextConfig(hexawyn_config).load_preferred_context() is None
        load_kube_config.assert_not_called()

    def test_startup_status_reports_connected(self, tmp_path: Path) -> None:
        env_config = tmp_path / "prod.yaml"
        _write_kubeconfig(env_config, "prod", ["prod"])
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )

        with (
            patch.dict("os.environ", {"KUBECONFIG": str(env_config)}),
            patch("kubernetes.config.load_kube_config") as load_kube_config,
            patch("kubernetes.client.VersionApi") as version_api,
        ):
            version_api.return_value.get_code.return_value = MagicMock()
            status = service.startup_status()

        assert status.connected is True
        assert status.current_context is not None
        assert status.current_context.name == "prod"
        load_kube_config.assert_called_once_with(
            config_file=str(env_config), context="prod", client_configuration=ANY
        )
