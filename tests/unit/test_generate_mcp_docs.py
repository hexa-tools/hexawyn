from __future__ import annotations

from hexawyn.domain.models.tool_registry import ToolRegistry, ToolSchema


def _tool(name: str, desc: str = "desc") -> ToolSchema:
    return ToolSchema(name=name, description=desc, input_schema={})


class TestGenerateMCPDocs:
    def test_header_and_tool_count(self) -> None:
        from scripts.generate_mcp_docs import generate_markdown

        registry = ToolRegistry(tools=[_tool("detect_zombies", "Find idle pods")])

        result = generate_markdown(registry)

        assert "# hexawyn — MCP Tools Reference" in result
        assert "1 tool" in result
        assert "auto-generated" in result.lower()
        assert "detect_zombies" in result
        assert "Find idle pods" in result

    def test_groups_by_category(self) -> None:
        from scripts.generate_mcp_docs import generate_markdown

        registry = ToolRegistry(tools=[_tool("detect_zombies"), _tool("list_pods")])

        result = generate_markdown(registry)

        assert "## FinOps" in result or "## Cluster Inventory" in result

    def test_parameters_table(self) -> None:
        from scripts.generate_mcp_docs import generate_markdown

        tool = ToolSchema(
            name="detect_zombies",
            description="Find idle pods",
            input_schema={
                "properties": {
                    "namespace": {"type": "string", "description": "Filter by namespace"},
                    "hours": {"type": "integer", "description": "Time window"},
                },
                "required": ["hours"],
            },
        )
        registry = ToolRegistry(tools=[tool])

        result = generate_markdown(registry)

        assert "`namespace`" in result
        assert "`string`" in result
        assert "✅" in result
        assert "❌" in result

    def test_example_payload(self) -> None:
        from scripts.generate_mcp_docs import generate_markdown

        tool = ToolSchema(
            name="detect_zombies",
            description="Find idle pods",
            input_schema={
                "properties": {
                    "hours": {"type": "integer", "description": "Time window", "default": 24},
                },
            },
        )
        registry = ToolRegistry(tools=[tool])

        result = generate_markdown(registry)

        assert "```json" in result
        assert "detect_zombies" in result
        assert '"hours"' in result
