"""RED → GREEN — MCP docs generator tests."""

from __future__ import annotations


class TestMCPDocsGenerator:
    def test_generates_header_with_tool_count(self) -> None:
        from hexawyn.domain.models.mcp_tool import MCPToolRegistry

        registry = MCPToolRegistry(tools=[])
        markdown = _generate(registry)
        assert "# hexawyn — MCP Tools Reference" in markdown
        assert "0 tools available" in markdown

    def test_groups_tools_by_category(self) -> None:
        from hexawyn.domain.models.mcp_tool import MCPToolRegistry, MCPToolSchema

        registry = MCPToolRegistry(
            tools=[
                MCPToolSchema(
                    name="detect_zombies",
                    description="Detect idle pods",
                    input_schema={
                        "properties": {
                            "analysis_window_hours": {
                                "type": "integer",
                                "description": "Hours to analyze",
                            }
                        }
                    },
                ),
                MCPToolSchema(
                    name="list_pods",
                    description="List all pods in a namespace",
                    input_schema={
                        "properties": {
                            "namespace": {"type": "string", "description": "K8s namespace"}
                        },
                        "required": ["namespace"],
                    },
                ),
            ]
        )
        markdown = _generate(registry)
        assert "## Core Operations" in markdown
        assert "## FinOps" in markdown
        assert "### `detect_zombies`" in markdown
        assert "### `list_pods`" in markdown

    def test_single_tool_has_all_sections(self) -> None:
        from hexawyn.domain.models.mcp_tool import MCPToolRegistry, MCPToolSchema

        registry = MCPToolRegistry(
            tools=[
                MCPToolSchema(
                    name="list_pods",
                    description="List all pods",
                    input_schema={
                        "properties": {
                            "namespace": {"type": "string", "description": "K8s namespace"}
                        },
                        "required": ["namespace"],
                    },
                )
            ]
        )
        markdown = _generate(registry)
        assert "### `list_pods`" in markdown
        assert "List all pods" in markdown
        assert "**Parameters:**" in markdown
        assert "`namespace`" in markdown
        assert "`string`" in markdown
        assert "K8s namespace" in markdown
        assert "**Example:**" in markdown

    def test_required_param_has_check(self) -> None:
        from hexawyn.domain.models.mcp_tool import MCPToolRegistry, MCPToolSchema

        registry = MCPToolRegistry(
            tools=[
                MCPToolSchema(
                    name="test_tool",
                    description="A test",
                    input_schema={
                        "properties": {
                            "required_arg": {"type": "string"},
                            "optional_arg": {"type": "integer"},
                        },
                        "required": ["required_arg"],
                    },
                )
            ]
        )
        markdown = _generate(registry)
        assert "| `required_arg` | `string` | ✅ | — |" in markdown
        assert "| `optional_arg` | `integer` | ❌ | — |" in markdown

    def test_tool_without_params(self) -> None:
        from hexawyn.domain.models.mcp_tool import MCPToolRegistry, MCPToolSchema

        registry = MCPToolRegistry(
            tools=[
                MCPToolSchema(
                    name="no_param_tool",
                    description="No parameters needed",
                    input_schema={},
                )
            ]
        )
        markdown = _generate(registry)
        assert "### `no_param_tool`" in markdown
        assert "No parameters" in markdown

    def test_generate_example_payload(self):
        from hexawyn.domain.models.mcp_tool import MCPToolRegistry, MCPToolSchema

        registry = MCPToolRegistry(
            tools=[
                MCPToolSchema(
                    name="detect_zombies",
                    description="Find zombie deployments",
                    input_schema={
                        "properties": {
                            "analysis_window_hours": {
                                "type": "integer",
                                "description": "Hours to analyze (default: 24)",
                            },
                            "namespace": {
                                "type": "string",
                                "description": "Filter by namespace",
                            },
                        }
                    },
                )
            ]
        )
        markdown = _generate(registry)
        assert '"tool": "detect_zombies"' in markdown
        assert '"analysis_window_hours"' in markdown

    def test_auto_generated_warning(self) -> None:
        from hexawyn.domain.models.mcp_tool import MCPToolRegistry

        registry = MCPToolRegistry(tools=[])
        markdown = _generate(registry)
        assert "Auto-generated" in markdown
        assert "do not edit manually" in markdown
        assert "scripts/generate_mcp_docs.py" in markdown

    def test_unknown_category_fallback(self) -> None:
        from hexawyn.domain.models.mcp_tool import MCPToolRegistry, MCPToolSchema

        registry = MCPToolRegistry(
            tools=[
                MCPToolSchema(
                    name="xyz_unknown_tool_123",
                    description="Something weird",
                    input_schema={},
                )
            ]
        )
        markdown = _generate(registry)
        assert "## Other" in markdown
        assert "### `xyz_unknown_tool_123`" in markdown


def _generate(registry):
    from scripts.generate_mcp_docs import generate_markdown

    return generate_markdown(registry)
