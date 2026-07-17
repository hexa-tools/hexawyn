from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort


class TestResourceYAMLTool:
    def test_returns_yaml(self) -> None:
        from hexawyn.mcp.tools.resource_yaml import resource_yaml

        with patch("hexawyn.mcp.server.build_resource_yaml_adapter") as m:
            a = MagicMock(spec=ResourceYAMLPort)
            a.resource_exists.return_value = True
            a.fetch_resource.return_value = {
                "kind": "Deployment",
                "spec": {
                    "template": {
                        "spec": {
                            "containers": [
                                {
                                    "name": "app",
                                    "image": "registry/order-api:v2.3.1",
                                    "resources": {"limits": {"cpu": "500m", "memory": "512Mi"}},
                                }
                            ]
                        }
                    }
                },
            }
            m.return_value = a
            r = resource_yaml(resource_name="order-api", namespace="production", kind="Deployment")
        assert r["error"] is None
        assert r["resource_found"] is True
        assert r["image_tags"] == ["registry/order-api:v2.3.1"]

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.resource_yaml import resource_yaml

        with patch(
            "hexawyn.mcp.server.build_resource_yaml_adapter", side_effect=RuntimeError("boom")
        ):
            r = resource_yaml(resource_name="x", namespace="ns", kind="Deployment")
        assert r["error"] == "boom"


class TestBuildResourceYAMLAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
        from hexawyn.mcp.server import build_resource_yaml_adapter

        assert isinstance(build_resource_yaml_adapter(), ResourceYAMLPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.resource_yaml")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
