import os
from pathlib import Path
from unittest.mock import ANY, MagicMock, patch

import pytest
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.infrastructure.config.kubeconfig_reader import (
    _home_kube_dirs,
    _kube_config_path,
    get_active_context,
    list_available_contexts,
    load_kubeconfig,
    validate_connection,
)

_MINIMAL_KUBECONFIG = """apiVersion: v1
kind: Config
current-context: test
clusters:
- name: test-cluster
  cluster:
    server: https://test.example.com
users:
- name: test-user
  user:
    token: test-token
contexts:
- name: test
  context:
    cluster: test-cluster
    user: test-user
    namespace: default
"""


class TestLoadKubeconfig:
    def test_uses_kubeconfig_env_var_when_set(self, tmp_path: Path):
        kubeconfig_file = tmp_path / "kubeconfig"
        kubeconfig_file.write_text(_MINIMAL_KUBECONFIG)

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            with patch("kubernetes.config.load_kube_config") as mock_load:
                with patch(
                    "kubernetes.config.list_kube_config_contexts",
                    return_value=([], {"name": "test", "context": {"cluster": "test"}}),
                ):
                    load_kubeconfig()
                    mock_load.assert_called_once_with(
                        config_file=str(kubeconfig_file), context=None, client_configuration=ANY
                    )

    def test_uses_default_path_when_env_var_not_set(self, tmp_path: Path):
        kubeconfig_file = tmp_path / ".kube" / "config"
        kubeconfig_file.parent.mkdir(parents=True)
        kubeconfig_file.write_text(_MINIMAL_KUBECONFIG)

        with patch.dict("os.environ", {}, clear=True):
            with patch(
                "hexawyn.infrastructure.config.kubeconfig_reader.DEFAULT_KUBECONFIG",
                str(kubeconfig_file),
            ):
                with patch("kubernetes.config.load_kube_config") as mock_load:
                    with patch(
                        "kubernetes.config.list_kube_config_contexts",
                        return_value=([], {"name": "test", "context": {"cluster": "test"}}),
                    ):
                        load_kubeconfig()
                        call_args = mock_load.call_args[1]["config_file"]
                        assert call_args.endswith(".kube/config")

    def test_falls_back_to_incluster_when_no_kubeconfig(self, tmp_path: Path):
        kubeconfig_file = tmp_path / "nonexistent" / "kubeconfig"

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            with patch("kubernetes.config.load_incluster_config") as mock_incluster:
                load_kubeconfig()
                mock_incluster.assert_called_once()

    def test_raises_cluster_unreachable_when_no_config_at_all(self, tmp_path: Path):
        kubeconfig_file = tmp_path / "nonexistent" / "kubeconfig"

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            with patch(
                "kubernetes.config.load_incluster_config",
                side_effect=Exception("not in cluster"),
            ):
                with pytest.raises(ClusterUnreachableError):
                    load_kubeconfig()

    def test_raises_cluster_unreachable_when_kubeconfig_is_invalid(self, tmp_path: Path):
        kubeconfig_file = tmp_path / "bad.yaml"
        kubeconfig_file.write_text("invalid: yaml: content")

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            with patch(
                "kubernetes.config.load_kube_config",
                side_effect=Exception("Invalid kube-config. File is empty"),
            ):
                with pytest.raises(ClusterUnreachableError) as error:
                    load_kubeconfig()

        assert "Unable to load kubeconfig" in str(error.value)


_KUBECONFIG_WITH_TWO_CLUSTERS = """\
apiVersion: v1
clusters:
- cluster:
    server: https://hetzner-server.example.com:6443
    certificate-authority-data: dGVzdA==
  name: hetzner-cluster
- cluster:
    server: https://127.0.0.1:33831
    certificate-authority-data: dGVzdA==
  name: kind-hexawyn
contexts:
- context:
    cluster: hetzner-cluster
    user: admin
  name: hetzner-preprod
- context:
    cluster: kind-hexawyn
    user: kind-user
  name: kind-hexawyn
current-context: hetzner-preprod
kind: Config
preferences: {}
users:
- name: admin
  user:
    token: hetzner-token
- name: kind-user
  user:
    token: kind-token
"""


class TestCorrectClusterIsUsed:
    """Verify that load_kubeconfig() binds the returned API to the requested cluster.

    This is the end-to-end contract: when you ask for 'hetzner-preprod', the
    returned CoreV1Api must talk to the hetzner server, not to kind (127.0.0.1:33831).

    If this test fails, investigations will silently return data from the wrong cluster.
    """

    def test_api_host_matches_requested_context(self, tmp_path: Path) -> None:
        """The CoreV1Api returned for 'hetzner-preprod' must use the hetzner server URL,
        not the kind cluster URL, even when both are present in the kubeconfig.
        """
        kubeconfig_file = tmp_path / "kubeconfig"
        kubeconfig_file.write_text(_KUBECONFIG_WITH_TWO_CLUSTERS)

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            api = load_kubeconfig(context="hetzner-preprod")

        actual_host = api.api_client.configuration.host  # type: ignore[attr-defined]
        assert "hetzner" in actual_host or "hetzner-server.example.com" in actual_host, (
            f"CoreV1Api host is '{actual_host}' — expected hetzner server. "
            "This means pods would be fetched from the wrong cluster (kind)."
        )
        assert "127.0.0.1" not in actual_host, (
            f"CoreV1Api host is '{actual_host}' (kind-hexawyn). "
            "Investigations will return kind data instead of hetzner-preprod data."
        )

    def test_api_host_matches_kind_context_when_explicitly_requested(self, tmp_path: Path) -> None:
        """Verify the context selection works in the other direction too."""
        kubeconfig_file = tmp_path / "kubeconfig"
        kubeconfig_file.write_text(_KUBECONFIG_WITH_TWO_CLUSTERS)

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            api = load_kubeconfig(context="kind-hexawyn")

        actual_host = api.api_client.configuration.host  # type: ignore[attr-defined]
        assert "127.0.0.1" in actual_host

    def test_changing_global_config_does_not_affect_isolated_api(self, tmp_path: Path) -> None:
        """After a background task changes the global K8s config to kind,
        the CoreV1Api obtained for hetzner-preprod must still point to hetzner.

        This is the exact scenario that caused the wrong-cluster bug:
        _validate_connection() or startup_status() ran for kind-hexawyn AFTER
        the hetzner CoreV1Api was created, silently switching it to kind.
        """
        from kubernetes import config as k8s_config

        kubeconfig_file = tmp_path / "kubeconfig"
        kubeconfig_file.write_text(_KUBECONFIG_WITH_TWO_CLUSTERS)

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            api = load_kubeconfig(context="hetzner-preprod")

        hetzner_host = api.api_client.configuration.host  # type: ignore[attr-defined]
        assert "127.0.0.1" not in hetzner_host

        # Simulate background task changing global config (e.g. _validate_connection for kind)
        k8s_config.load_kube_config(
            config_file=str(kubeconfig_file),
            context="kind-hexawyn",
        )

        # The isolated CoreV1Api must still point to hetzner
        host_after_global_change = api.api_client.configuration.host  # type: ignore[attr-defined]
        assert host_after_global_change == hetzner_host, (
            f"Host changed from '{hetzner_host}' to '{host_after_global_change}' after "
            "a background config.load_kube_config() call. "
            "This is the global-config-pollution bug — CoreV1Api is not isolated."
        )
        assert "127.0.0.1" not in host_after_global_change


class TestListAvailableContexts:
    def test_returns_all_contexts(self):
        mock_contexts = [
            {"name": "prod-eu", "context": {"cluster": "cluster-eu", "namespace": "default"}},
            {"name": "staging-us", "context": {"cluster": "cluster-us", "namespace": "staging"}},
            {"name": "dev-local", "context": {"cluster": "minikube", "namespace": "default"}},
        ]
        with patch(
            "kubernetes.config.list_kube_config_contexts",
            return_value=(mock_contexts, mock_contexts[0]),
        ):
            contexts = list_available_contexts()
            assert len(contexts) == 3  # noqa: PLR2004
            assert contexts[0]["name"] == "prod-eu"

    def test_returns_empty_list_when_no_kubeconfig(self):
        with patch(
            "kubernetes.config.list_kube_config_contexts",
            side_effect=Exception("no kubeconfig"),
        ):
            contexts = list_available_contexts()
            assert contexts == []


class TestValidateConnection:
    def test_returns_connected_when_api_responds(self):
        mock_api = MagicMock()
        mock_api.list_namespace.return_value = MagicMock()
        result = validate_connection(mock_api, context_name="prod-eu")
        assert result["status"] == "connected"
        assert result["context"] == "prod-eu"

    def test_returns_unreachable_when_api_fails(self):
        mock_api = MagicMock()
        mock_api.list_namespace.side_effect = Exception("connection refused")
        result = validate_connection(mock_api, context_name="prod-eu")
        assert result["status"] == "unreachable"
        assert "connection refused" in result["error"]

    def test_timeout_is_5_seconds(self):
        mock_api = MagicMock()
        mock_api.list_namespace.return_value = MagicMock()
        validate_connection(mock_api, context_name="prod-eu")
        mock_api.list_namespace.assert_called_once_with(limit=1, timeout_seconds=5)


class TestGetActiveContext:
    def test_returns_active_context_name(self):
        mock_active = {"name": "prod-eu", "context": {"cluster": "cluster-eu"}}
        with patch(
            "kubernetes.config.list_kube_config_contexts",
            return_value=([], mock_active),
        ):
            ctx = get_active_context()
            assert ctx["name"] == "prod-eu"

    def test_returns_none_when_no_kubeconfig(self):
        with patch(
            "kubernetes.config.list_kube_config_contexts",
            side_effect=Exception("no kubeconfig"),
        ):
            ctx = get_active_context()
            assert ctx is None


class TestEmptyFileTolerance:
    """An empty kubeconfig file in the KUBECONFIG list must not break discovery.

    The Kubernetes python client treats a 0-byte file as an invalid config and
    aborts the whole merge, so hexawyn filters out empty files before listing
    contexts. The CLI/MCP must still see the remaining valid contexts.
    """

    def test_list_contexts_filters_empty_files(self, tmp_path: Path) -> None:
        good = tmp_path / "good.yaml"
        good.write_text(_MINIMAL_KUBECONFIG)
        empty = tmp_path / "empty.yaml"
        empty.write_text("")

        mock_contexts = [
            {"name": "prod-eu", "context": {"cluster": "cluster-eu", "namespace": "default"}}
        ]
        with patch.dict("os.environ", {"KUBECONFIG": f"{good}{os.pathsep}{empty}"}):
            with patch(
                "kubernetes.config.list_kube_config_contexts",
                return_value=(mock_contexts, mock_contexts[0]),
            ) as mock_list:
                contexts = list_available_contexts()

        assert contexts[0]["name"] == "prod-eu"
        merged = mock_list.call_args[1]["config_file"]
        assert good.name in merged
        assert empty.name not in merged

    def test_get_active_context_filters_empty_files(self, tmp_path: Path) -> None:
        good = tmp_path / "good.yaml"
        good.write_text(_MINIMAL_KUBECONFIG)
        empty = tmp_path / "empty.yaml"
        empty.write_text("")

        mock_active = {"name": "prod-eu", "context": {"cluster": "cluster-eu"}}
        with patch.dict("os.environ", {"KUBECONFIG": f"{good}{os.pathsep}{empty}"}):
            with patch(
                "kubernetes.config.list_kube_config_contexts",
                return_value=([], mock_active),
            ) as mock_list:
                ctx = get_active_context()

        assert ctx["name"] == "prod-eu"
        merged = mock_list.call_args[1]["config_file"]
        assert good.name in merged
        assert empty.name not in merged


class TestKubeDiscoveryFallback:
    """When KUBECONFIG is unset and nothing usable is found, hexawyn discovers a
    kubeconfig autonomously under the user's home (multi-OS). Without this, a
    cluster configured only via ``~/.kube/<name>.yaml`` is invisible to a spawned
    MCP server that does not inherit KUBECONFIG.
    """

    def test_discovers_kubeconfig_under_home_when_env_unset(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("HOME", str(tmp_path))
        monkeypatch.delenv("KUBECONFIG", raising=False)
        kube_dir = tmp_path / ".kube"
        kube_dir.mkdir()
        (kube_dir / "config").write_text("")
        real = kube_dir / "hetzner-preprod.yaml"
        real.write_text(_MINIMAL_KUBECONFIG)

        path = _kube_config_path()

        assert path == str(real)

    def test_returns_empty_when_no_config_anywhere(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("HOME", str(tmp_path))
        monkeypatch.delenv("KUBECONFIG", raising=False)

        assert _kube_config_path() == ""

    def test_home_kube_dirs_are_home_relative(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("HOME", "/fake-home")

        for directory in _home_kube_dirs():
            assert directory.startswith("/fake-home")
            assert "djepeno" not in directory


class TestConfigIsolation:
    """These tests catch the global-config-pollution bug.

    If load_kubeconfig() uses the global kubernetes Configuration (instead of an
    isolated one), background tasks that call config.load_kube_config() for a
    different context will silently change which cluster all existing CoreV1Api
    instances talk to. This causes the CLI to fetch pods from the wrong cluster
    (e.g. kind-hexawyn instead of hetzner-preprod).
    """

    def test_load_kubeconfig_passes_isolated_configuration_to_load_kube_config(
        self, tmp_path: Path
    ) -> None:
        """load_kubeconfig() must pass client_configuration= to config.load_kube_config().

        Without this, load_kube_config() updates the global singleton and every
        CoreV1Api() created later will talk to a different cluster.
        """
        kubeconfig_file = tmp_path / "kubeconfig"
        kubeconfig_file.write_text(_MINIMAL_KUBECONFIG)

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            with patch("kubernetes.config.load_kube_config") as mock_load:
                with patch(
                    "kubernetes.config.list_kube_config_contexts",
                    return_value=([], {"name": "test", "context": {"cluster": "test"}}),
                ):
                    load_kubeconfig(context="test")

        call_kwargs = mock_load.call_args[1]
        assert "client_configuration" in call_kwargs, (
            "load_kube_config() must be called with client_configuration= to create "
            "an isolated config. Without it, the global K8s config is modified and "
            "all CoreV1Api instances become affected by future context changes."
        )

    def test_load_kubeconfig_creates_api_client_with_isolated_configuration(
        self, tmp_path: Path
    ) -> None:
        """The returned CoreV1Api must be bound to an isolated ApiClient.

        Without ApiClient(configuration=cfg), CoreV1Api() falls back to the global
        configuration singleton and will talk to whatever context was loaded last.
        """
        kubeconfig_file = tmp_path / "kubeconfig"
        kubeconfig_file.write_text(_MINIMAL_KUBECONFIG)

        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            with patch("kubernetes.config.load_kube_config"):
                with patch("kubernetes.client.Configuration") as mock_cfg_class:
                    mock_cfg = MagicMock()
                    mock_cfg_class.return_value = mock_cfg
                    with patch("kubernetes.client.ApiClient") as mock_api_client_class:
                        with patch("kubernetes.client.CoreV1Api") as mock_core_v1:
                            with patch(
                                "kubernetes.config.list_kube_config_contexts",
                                return_value=([], {"name": "test", "context": {"cluster": "test"}}),
                            ):
                                load_kubeconfig(context="test")

        mock_api_client_class.assert_called_once_with(configuration=mock_cfg)
        mock_core_v1.assert_called_once_with(api_client=mock_api_client_class.return_value)


class TestEdgeCases:
    def test_multiple_kubeconfig_files_merged(self, tmp_path: Path):
        config_a = tmp_path / "a.yaml"
        config_b = tmp_path / "b.yaml"
        config_a.write_text(_MINIMAL_KUBECONFIG)
        config_b.write_text(_MINIMAL_KUBECONFIG)

        with patch.dict(
            "os.environ",
            {"KUBECONFIG": f"{config_a}{os.pathsep}{config_b}"},
        ):
            with patch("kubernetes.config.load_kube_config") as mock_load:
                with patch(
                    "kubernetes.config.list_kube_config_contexts",
                    return_value=([], {"name": "ctx", "context": {"cluster": "c"}}),
                ):
                    load_kubeconfig()
                    assert mock_load.called

    def test_list_contexts_returns_all_three(self):
        mock_contexts = [
            {
                "name": f"ctx-{i}",
                "context": {"cluster": f"cluster-{i}", "namespace": "default"},
            }
            for i in range(3)
        ]
        with patch(
            "kubernetes.config.list_kube_config_contexts",
            return_value=(mock_contexts, mock_contexts[0]),
        ):
            contexts = list_available_contexts()
            assert len(contexts) == 3  # noqa: PLR2004

    def test_validate_connection_timeout_on_unreachable(self):
        mock_api = MagicMock()
        mock_api.list_namespace.side_effect = Exception("timeout")
        result = validate_connection(mock_api, "prod-eu")
        assert result["status"] == "unreachable"
        assert result["context"] == "prod-eu"

    def test_active_context_with_non_dict_context_data(self, tmp_path: Path):
        kubeconfig_file = tmp_path / "kubeconfig"
        kubeconfig_file.write_text(_MINIMAL_KUBECONFIG)
        mock_active = {
            "name": "prod-eu",
            "context": "not-a-dict",
        }
        with patch.dict("os.environ", {"KUBECONFIG": str(kubeconfig_file)}):
            with patch("kubernetes.config.load_kube_config"):
                with patch(
                    "kubernetes.config.list_kube_config_contexts",
                    return_value=([], mock_active),
                ):
                    with patch(
                        "hexawyn.infrastructure.config.kubeconfig_reader.get_active_context",
                        return_value=mock_active,
                    ):
                        load_kubeconfig()
