from hexawyn.domain.models.mcp_tool import MCPToolRegistry, MCPToolSchema


class TestMCPToolSchema:
    def test_creates_with_all_fields(self) -> None:
        tool = MCPToolSchema(
            name="list_namespaces",
            description="List namespaces",
            input_schema={"type": "object", "properties": {}},
        )
        assert tool.name == "list_namespaces"
        assert tool.description == "List namespaces"
        assert tool.input_schema == {"type": "object", "properties": {}}

    def test_is_frozen(self) -> None:
        tool = MCPToolSchema(name="x", description="d", input_schema={})
        with __import__("pytest").raises(AttributeError):
            tool.name = "other"  # type: ignore[misc]


class TestMCPToolRegistry:
    def test_default_tools_is_empty(self) -> None:
        registry = MCPToolRegistry()
        assert registry.tools == []

    def test_holds_multiple_tools(self) -> None:
        t1 = MCPToolSchema(name="a", description="aa", input_schema={})
        t2 = MCPToolSchema(name="b", description="bb", input_schema={})
        registry = MCPToolRegistry(tools=[t1, t2])
        assert len(registry.tools) == 2

    def test_to_payload_serializes_correctly(self) -> None:
        t = MCPToolSchema(
            name="list_namespaces",
            description="List namespaces",
            input_schema={"type": "object"},
        )
        registry = MCPToolRegistry(tools=[t])
        payload = registry.to_payload()
        assert payload == [
            {
                "name": "list_namespaces",
                "description": "List namespaces",
                "input_schema": {"type": "object"},
            }
        ]

    def test_to_payload_empty_registry(self) -> None:
        registry = MCPToolRegistry()
        assert registry.to_payload() == []
