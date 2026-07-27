"""MCP tool: resource_yaml — Get YAML definition of a k8s resource with secrets redacted."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.resource_yaml.command import (
    ResourceYamlCommand,
)
from hexawyn.application.use_case.cluster.resource_yaml.resource_yaml_use_case import (
    ResourceYAMLUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def resource_yaml(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(resource_yaml)
