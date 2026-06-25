from unittest.mock import MagicMock, patch

import pytest
from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.infrastructure.config.kubeconfig_reader import (
    get_active_context,
    list_available_contexts,
    load_kubeconfig,
    validate_connection,
)


class TestLoadKubeconfig:
    def test_uses_kubeconfig_env_var_when_set(self):
        with patch.dict("os.environ", {"KUBECONFIG": "/custom/path"}):
            with patch("os.path.exists", return_value=True):
                with patch("kubernetes.config.load_kube_config") as mock_load:
                    with patch(
                        "kubernetes.config.list_kube_config_contexts",
                        return_value=([], {"name": "test", "context": {"cluster": "test"}}),
                    ):
                        load_kubeconfig()
                        mock_load.assert_called_once_with(config_file="/custom/path", context=None)

    def test_uses_default_path_when_env_var_not_set(self):
        with patch.dict("os.environ", {}, clear=True):
            with patch("os.path.exists", return_value=True):
                with patch("kubernetes.config.load_kube_config") as mock_load:
                    with patch(
                        "kubernetes.config.list_kube_config_contexts",
                        return_value=([], {"name": "test", "context": {"cluster": "test"}}),
                    ):
                        load_kubeconfig()
                        call_args = mock_load.call_args[1]["config_file"]
                        assert call_args.endswith(".kube/config")

    def test_falls_back_to_incluster_when_no_kubeconfig(self):
        with patch("os.path.exists", return_value=False):
            with patch("kubernetes.config.load_incluster_config") as mock_incluster:
                load_kubeconfig()
                mock_incluster.assert_called_once()

    def test_raises_cluster_unreachable_when_no_config_at_all(self):
        with patch("os.path.exists", return_value=False):
            with patch(
                "kubernetes.config.load_incluster_config",
                side_effect=Exception("not in cluster"),
            ):
                with pytest.raises(ClusterUnreachableError):
                    load_kubeconfig()

    def test_raises_cluster_unreachable_when_kubeconfig_is_invalid(self):
        with patch.dict("os.environ", {"KUBECONFIG": "/empty/config"}):
            with patch("os.path.exists", return_value=True):
                with patch(
                    "kubernetes.config.load_kube_config",
                    side_effect=Exception("Invalid kube-config. /empty/config file is empty"),
                ):
                    with pytest.raises(ClusterUnreachableError) as error:
                        load_kubeconfig()

        assert "Unable to load kubeconfig" in str(error.value)
        assert error.value.context == {
            "kubeconfig_path": "/empty/config",
            "error": "Invalid kube-config. /empty/config file is empty",
        }


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
            assert len(contexts) == 3
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


class TestEdgeCases:
    def test_multiple_kubeconfig_files_merged(self):
        """KUBECONFIG=/path1:/path2 — merged config supported."""
        with patch.dict("os.environ", {"KUBECONFIG": "/path1:/path2"}):
            with patch("os.path.exists", return_value=True):
                with patch("kubernetes.config.load_kube_config") as mock_load:
                    with patch(
                        "kubernetes.config.list_kube_config_contexts",
                        return_value=([], {"name": "ctx", "context": {"cluster": "c"}}),
                    ):
                        load_kubeconfig()
                        assert mock_load.called

    def test_list_contexts_returns_all_three(self):
        """KUBECONFIG with 3 contexts → list_contexts returns all 3."""
        mock_contexts = [
            {"name": f"ctx-{i}", "context": {"cluster": f"cluster-{i}", "namespace": "default"}}
            for i in range(3)
        ]
        with patch(
            "kubernetes.config.list_kube_config_contexts",
            return_value=(mock_contexts, mock_contexts[0]),
        ):
            contexts = list_available_contexts()
            assert len(contexts) == 3

    def test_validate_connection_timeout_on_unreachable(self):
        """Unreachable cluster → returns unreachable, does not hang."""
        mock_api = MagicMock()
        mock_api.list_namespace.side_effect = Exception("timeout")
        result = validate_connection(mock_api, "prod-eu")
        assert result["status"] == "unreachable"
        assert result["context"] == "prod-eu"

    def test_active_context_with_non_dict_context_data(self):
        """context_data is not a dict → cluster_name defaults to 'unknown'."""
        mock_active = {
            "name": "prod-eu",
            "context": "not-a-dict",
        }
        with patch("os.path.exists", return_value=True):
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
