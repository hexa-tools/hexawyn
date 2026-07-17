from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.pipeline_for_service_port import (
    PipelineForServicePort,
)
from hexawyn.domain.models.pipeline_for_service import ServicePipeline


class TestPipelineForServiceTool:
    def test_finds_pipeline(self) -> None:
        from hexawyn.mcp.tools.pipeline_for_service import pipeline_for_service

        with patch("hexawyn.mcp.server.build_pipeline_for_service_adapter") as m:
            a = MagicMock(spec=PipelineForServicePort)
            a.find_pipelines.return_value = [
                ServicePipeline(
                    pipeline_name="deploy-checkout",
                    namespace="ci",
                    repo_url="https://github.com/org/checkout",
                    branch="main",
                    trigger="webhook",
                    last_run_status="succeeded",
                    last_run_timestamp="2026-07-01T10:00:00Z",
                ),
            ]
            m.return_value = a
            r = pipeline_for_service(service_name="checkout-service")
        assert r["error"] is None
        assert r["pipelines_found"] == 1
        assert r["pipelines"][0]["repo_url"] == "https://github.com/org/checkout"

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.pipeline_for_service import pipeline_for_service

        with patch(
            "hexawyn.mcp.server.build_pipeline_for_service_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = pipeline_for_service(service_name="x")
        assert r["error"] == "boom"


class TestBuildPipelineForServiceAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.pipeline_for_service_port import (
            PipelineForServicePort,
        )
        from hexawyn.mcp.server import build_pipeline_for_service_adapter

        assert isinstance(build_pipeline_for_service_adapter(), PipelineForServicePort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.pipeline_for_service")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
