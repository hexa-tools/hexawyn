"""Edge case tests for kubernetes_context.py uncovered branches."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import yaml
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


class TestHexawynContextConfigEdges:
    """Cover HexawynContextConfig.load_preferred_context missing branches."""

    def test_loads_default_context(self, tmp_path: Path) -> None:
        config_path = tmp_path / "hexawyn-config.yaml"
        config_data = yaml.safe_dump({"default_context": "prod-eu"})
        config_path.write_text(config_data, encoding="utf-8")

        cfg = HexawynContextConfig(config_path=config_path)
        assert cfg.load_preferred_context() == "prod-eu"

    def test_loads_last_context_when_no_default(self, tmp_path: Path) -> None:
        config_path = tmp_path / "hexawyn-config.yaml"
        config_data = yaml.safe_dump({"last_context": "staging-us"})
        config_path.write_text(config_data, encoding="utf-8")

        cfg = HexawynContextConfig(config_path=config_path)
        assert cfg.load_preferred_context() == "staging-us"

    def test_default_context_preferred_over_last(self, tmp_path: Path) -> None:
        config_path = tmp_path / "hexawyn-config.yaml"
        config_data = yaml.safe_dump({"default_context": "prod-eu", "last_context": "staging-us"})
        config_path.write_text(config_data, encoding="utf-8")

        cfg = HexawynContextConfig(config_path=config_path)
        assert cfg.load_preferred_context() == "prod-eu"

    def test_returns_none_when_config_not_a_dict(self, tmp_path: Path) -> None:
        config_path = tmp_path / "hexawyn-config.yaml"
        config_path.write_text("just a string, not a dict\n", encoding="utf-8")

        cfg = HexawynContextConfig(config_path=config_path)
        assert cfg.load_preferred_context() is None

    def test_returns_none_when_empty_string_values(self, tmp_path: Path) -> None:
        config_path = tmp_path / "hexawyn-config.yaml"
        config_data = yaml.safe_dump({"default_context": "", "last_context": ""})
        config_path.write_text(config_data, encoding="utf-8")

        cfg = HexawynContextConfig(config_path=config_path)
        assert cfg.load_preferred_context() is None

    def test_returns_none_when_default_not_string(self, tmp_path: Path) -> None:
        config_path = tmp_path / "hexawyn-config.yaml"
        config_data = yaml.safe_dump({"default_context": 12345})
        config_path.write_text(config_data, encoding="utf-8")

        cfg = HexawynContextConfig(config_path=config_path)
        assert cfg.load_preferred_context() is None

    def test_save_context_creates_directory_and_file(self, tmp_path: Path) -> None:
        config_path = tmp_path / "sub" / "dir" / "hexawyn-config.yaml"
        cfg = HexawynContextConfig(config_path=config_path)
        cfg.save_context("kind-ecom-local")

        loaded = HexawynContextConfig(config_path=config_path)
        assert loaded.load_preferred_context() == "kind-ecom-local"


class TestKubernetesContextNoKubeconfig:
    """Cover branches when no kubeconfig is available."""

    def test_discover_returns_empty_list_when_no_kubeconfig(self, tmp_path: Path) -> None:
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        with patch.dict("os.environ", {}, clear=True):
            contexts = service.discover()
        assert contexts == []

    def test_current_returns_none_when_no_contexts(self, tmp_path: Path) -> None:
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        with patch.dict("os.environ", {}, clear=True):
            assert service.current() is None

    def test_startup_status_without_any_context(self, tmp_path: Path) -> None:
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        with patch.dict("os.environ", {}, clear=True):
            status = service.startup_status()

        assert status.current_context is None
        assert status.connected is False
        assert status.contexts == []
        assert "No Kubernetes context" in status.connection_error


class TestKubernetesContextEdgeBranches:
    """Cover remaining edge branches in private methods."""

    def test_current_returns_none_when_no_current_in_contexts(self, tmp_path: Path) -> None:
        kubeconfig = tmp_path / "kubeconfig.yaml"
        _write_kubeconfig(kubeconfig, "prod", [])
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig)}):
            assert service.current() is None

    def test_read_contexts_skips_non_list_contexts(self, tmp_path: Path) -> None:
        file_path = tmp_path / "bad-kubeconfig.yaml"
        file_path.write_text(
            "apiVersion: v1\n"
            "kind: Config\n"
            "current-context: prod\n"
            "clusters: []\n"
            "users: []\n"
            "contexts: not_a_list\n",
            encoding="utf-8",
        )
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        with patch.dict("os.environ", {"KUBECONFIG": str(file_path)}):
            contexts = service.discover()
        assert contexts == []

    def test_parse_contexts_skips_non_mapping_entries(self, tmp_path: Path) -> None:
        file_path = tmp_path / "bad-kubeconfig.yaml"
        file_path.write_text(
            "apiVersion: v1\n"
            "kind: Config\n"
            "current-context: prod\n"
            "clusters: []\n"
            "users: []\n"
            "contexts:\n"
            "  - just_a_string\n"
            "  - {}\n"
            "  - name: prod\n"
            "    context:\n"
            "      cluster: cluster-prod\n"
            "      namespace: ns-prod\n"
            "      user: user-prod\n",
            encoding="utf-8",
        )
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        with patch.dict("os.environ", {"KUBECONFIG": str(file_path)}):
            contexts = service.discover()
        assert len(contexts) == 1
        assert contexts[0].name == "prod"

    def test_parse_contexts_skips_missing_name_or_context(self, tmp_path: Path) -> None:
        file_path = tmp_path / "bad-kubeconfig.yaml"
        file_path.write_text(
            "apiVersion: v1\n"
            "kind: Config\n"
            "current-context: prod\n"
            "clusters: []\n"
            "users: []\n"
            "contexts:\n"
            "  - name: prod\n"
            "    context: not_a_mapping_value\n"
            "  - other: prod\n"
            "    context:\n"
            "      cluster: c\n"
            "      namespace: ns\n"
            "      user: u\n",
            encoding="utf-8",
        )
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        with patch.dict("os.environ", {"KUBECONFIG": str(file_path)}):
            contexts = service.discover()
        assert contexts == []

    def test_has_context_returns_false_when_not_list(self, tmp_path: Path) -> None:
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        assert not service._has_context("not_a_list", "prod")

    def test_has_context_returns_false_when_not_found(self, tmp_path: Path) -> None:
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        raw_contexts = [{"name": "prod"}, {"name": "staging"}]
        assert not service._has_context(raw_contexts, "dev")

    def test_has_context_skips_non_mapping_entries(self, tmp_path: Path) -> None:
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        raw_contexts = ["not_a_mapping", {"name": "prod"}]
        assert service._has_context(raw_contexts, "prod")

    def test_find_context_kubeconfig_path_returns_none(self, tmp_path: Path) -> None:
        kubeconfig = tmp_path / "kubeconfig.yaml"
        _write_kubeconfig(kubeconfig, "prod", ["prod"])
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig)}):
            assert service._find_context_kubeconfig_path("nonexistent") is None

    def test_set_kubernetes_current_context_when_not_found(self, tmp_path: Path) -> None:
        kubeconfig = tmp_path / "kubeconfig.yaml"
        _write_kubeconfig(kubeconfig, "prod", ["prod"])
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig)}):
            service._set_kubernetes_current_context("nonexistent")

        content = kubeconfig.read_text(encoding="utf-8")
        assert "current-context: prod" in content

    def test_set_kubernetes_current_context_when_loaded_not_dict(self, tmp_path: Path) -> None:
        kubeconfig = tmp_path / "kubeconfig.yaml"
        kubeconfig.write_text("just a string value\n", encoding="utf-8")
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig)}):
            with patch.object(service, "_find_context_kubeconfig_path", return_value=kubeconfig):
                service._set_kubernetes_current_context("prod")
                content = kubeconfig.read_text(encoding="utf-8")
                assert "current-context:" not in content

    def test_kubeconfig_loader_path_returns_none_when_no_paths(self, tmp_path: Path) -> None:
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        with patch.dict("os.environ", {}, clear=True):
            assert service._kubeconfig_loader_path() is None

    def test_load_yaml_mapping_returns_empty_on_non_mapping(self, tmp_path: Path) -> None:
        kubeconfig = tmp_path / "kubeconfig.yaml"
        kubeconfig.write_text("just a string value\n", encoding="utf-8")
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        result = service._load_yaml_mapping(kubeconfig)
        assert result == {}

    def test_read_current_context_name_returns_none_when_no_current(self, tmp_path: Path) -> None:
        kubeconfig = tmp_path / "kubeconfig.yaml"
        kubeconfig.write_text(
            "apiVersion: v1\nkind: Config\ncontexts: []\n",
            encoding="utf-8",
        )
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig)}):
            result = service._read_current_context_name([kubeconfig])
        assert result is None

    def test_current_from_contexts_returns_none_when_empty(self, tmp_path: Path) -> None:
        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        assert service._current_from_contexts([]) is None

    def test_current_from_contexts_returns_none_when_none_current(self, tmp_path: Path) -> None:
        from hexawyn.infrastructure.config.kubernetes_context import ClusterContext

        service = FileKubernetesDiscoveryService(
            home_path=tmp_path / "home",
            hexawyn_config=HexawynContextConfig(tmp_path / "hexawyn-config.yaml"),
        )
        ctx = ClusterContext(name="prod", cluster="c1", namespace="ns", user="u", is_current=False)
        assert service._current_from_contexts([ctx]) is None
