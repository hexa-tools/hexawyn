"""Unit tests for MCP tool: snapshots."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestSnapshotsTool:
    def test_snapshots_list_returns_dict_with_items(self) -> None:
        from hexawyn.mcp.tools.snapshots import snapshots_list

        mock_crd = MagicMock()
        mock_crd.list_cluster_custom_object.return_value = {
            "items": [
                {
                    "metadata": {
                        "name": "snap1",
                        "namespace": "ns1",
                        "creationTimestamp": "2024-01-01",
                    },
                    "spec": {
                        "volumeSnapshotClassName": "csi",
                        "source": {"persistentVolumeClaimName": "pvc1"},
                    },
                    "status": {"readyToUse": True, "restoreSize": "1Gi"},
                }
            ]
        }
        mock_vanilla = MagicMock()
        mock_vanilla._crd_api_client.return_value = mock_crd

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter",
            return_value=mock_vanilla,
        ):
            result = snapshots_list()

        assert isinstance(result, dict)
        assert "snapshots" in result
        assert len(result["snapshots"]) == 1

    def test_snapshots_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.snapshots import snapshots_list

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter",
            side_effect=RuntimeError("test error"),
        ):
            result = snapshots_list()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_snapshots_list_namespaced(self) -> None:
        from hexawyn.mcp.tools.snapshots import snapshots_list

        mock_crd = MagicMock()
        mock_crd.list_namespaced_custom_object.return_value = {"items": []}
        mock_vanilla = MagicMock()
        mock_vanilla._crd_api_client.return_value = mock_crd

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter",
            return_value=mock_vanilla,
        ):
            result = snapshots_list("test-ns")

        assert isinstance(result, dict)
        assert "snapshots" in result

    def test_snapshot_get_returns_dict(self) -> None:
        from hexawyn.mcp.tools.snapshots import snapshot_get

        mock_crd = MagicMock()
        mock_crd.get_namespaced_custom_object.return_value = {
            "metadata": {"name": "snap1", "namespace": "ns1", "creationTimestamp": "2024-01-01"},
            "spec": {
                "volumeSnapshotClassName": "csi",
                "source": {"persistentVolumeClaimName": "pvc1"},
            },
            "status": {"readyToUse": True, "restoreSize": "1Gi"},
        }
        mock_vanilla = MagicMock()
        mock_vanilla._crd_api_client.return_value = mock_crd

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter",
            return_value=mock_vanilla,
        ):
            result = snapshot_get("snap1", "ns1")

        assert isinstance(result, dict)
        assert result["name"] == "snap1"

    def test_snapshot_get_handles_error(self) -> None:
        from hexawyn.mcp.tools.snapshots import snapshot_get

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter",
            side_effect=RuntimeError("test error"),
        ):
            result = snapshot_get("snap1", "ns1")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_snapshot_get_not_dict(self) -> None:
        from hexawyn.mcp.tools.snapshots import snapshot_get

        mock_crd = MagicMock()
        mock_crd.get_namespaced_custom_object.return_value = "not-a-dict"
        mock_vanilla = MagicMock()
        mock_vanilla._crd_api_client.return_value = mock_crd

        with patch(
            "hexawyn.adapters.secondary.vanilla.vanilla_adapter.VanillaAdapter",
            return_value=mock_vanilla,
        ):
            result = snapshot_get("snap1", "ns1")

        assert isinstance(result, dict)
        assert result.get("error") == "Not found"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.snapshots")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
