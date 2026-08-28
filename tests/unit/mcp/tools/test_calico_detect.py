"""Unit tests for MCP tool: calico_detect."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from kubernetes.client.rest import ApiException


class TestCalicoDetectTool:
    def test_calico_detect_returns_dict(self) -> None:
        from hexawyn.mcp.tools.calico_detect import calico_detect

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.status = "installed"
        mock_response.not_installed_marker = None
        mock_response.version = "v3.26.1"
        mock_response.mode = "IPIP"
        mock_response.namespace = "calico-system"
        mock_response.tigera_operator = False
        mock_response.enterprise = False
        mock_response.agents = []
        mock_response.total_nodes = 3
        mock_response.ready_agents = 3
        mock_response.degraded_agents = 0
        mock_response.degraded_summary = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_calico_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.calico_detect.CalicoDetectUseCase",
                return_value=mock_uc,
            ),
        ):
            result = calico_detect()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["version"] == "v3.26.1"
        assert result["mode"] == "IPIP"
        assert result["error"] is None

    def test_calico_detect_handles_error(self) -> None:
        from hexawyn.mcp.tools.calico_detect import calico_detect

        with patch(
            "hexawyn.mcp.server.build_calico_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = calico_detect()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("installed") is False

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.calico_detect")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))

    def test_agent_dict_converts_phase(self) -> None:
        from hexawyn.domain.models.calico import CalicoAgentPhase, CalicoNodeAgent
        from hexawyn.mcp.tools.calico_detect import _agent_dict

        agent = CalicoNodeAgent(
            node="n1",
            phase=CalicoAgentPhase.READY,
            ready=True,
            ready_replicas=1,
            desired_replicas=1,
            available_replicas=1,
        )
        result = _agent_dict(agent)

        assert result["node"] == "n1"
        assert result["phase"] == "ready"
        assert result["ready"] is True

    def test_calico_detect_end_to_end_via_real_adapter(self) -> None:
        from hexawyn.adapters.secondary.calico.calico_k8s_adapter import CalicoK8sAdapter
        from hexawyn.mcp.tools.calico_detect import calico_detect

        pool_item = {
            "metadata": {"name": "p1"},
            "spec": {
                "cidr": "10.1.0.0/16",
                "ipipMode": "Always",
                "vxlanMode": "Never",
                "disabled": False,
            },
        }
        crd = MagicMock()

        def list_cluster(group: str, version: str, plural: str) -> object:
            if plural == "ippools":
                return {"items": [pool_item]}
            raise ApiException(status=404, reason="not found")

        crd.list_cluster_custom_object.side_effect = list_cluster

        container = MagicMock()
        container.image = "quay.io/calico/node:v3.26.1"
        ds = MagicMock()
        ds.metadata.namespace = "calico-system"
        ds.metadata.name = "calico-node"
        ds.spec.template.spec.containers = [container]
        apps = MagicMock()
        apps.list_daemon_set_for_all_namespaces.return_value = MagicMock(items=[ds])

        pod = MagicMock()
        pod.metadata.name = "calico-node-a"
        pod.spec.node_name = "node-a"
        pod.status.phase = "Running"
        pod.status.conditions = [MagicMock(type="Ready", status="True")]
        pod.status.container_statuses = []
        core = MagicMock()
        core.list_pod_for_all_namespaces.return_value = MagicMock(items=[pod])
        core.list_node.return_value = MagicMock(items=[])

        adapter = CalicoK8sAdapter(core_api=core, apps_api=apps, crd_api=crd, metrics_source=None)
        with patch("hexawyn.mcp.server.build_calico_adapter", return_value=adapter):
            result = calico_detect()

        assert result["installed"] is True
        assert result["version"] == "v3.26.1"
        assert result["mode"] == "IPIP"
        assert result["ready_agents"] == 1  # noqa: PLR2004
        assert result["agents"][0]["node"] == "node-a"
