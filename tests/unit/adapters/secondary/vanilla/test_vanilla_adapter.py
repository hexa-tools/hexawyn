from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter


class TestVanillaAdapterIngress:
    def test_list_ingresses_delegates_to_k8s_adapter(self) -> None:
        adapter = VanillaAdapter(cluster_name="prod-eu")
        mock_k8s = MagicMock()
        mock_k8s.list_ingresses.return_value = []
        adapter._k8s_adapter_inst = mock_k8s

        result = adapter.list_ingresses(namespace="production")

        assert result == []
        mock_k8s.list_ingresses.assert_called_once_with(namespace="production")
