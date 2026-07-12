from dataclasses import fields


class TestToolSchema:
    def test_fields(self) -> None:
        from hexawyn.domain.models.tool_registry import ToolSchema

        names = {f.name for f in fields(ToolSchema)}
        assert names == {"name", "description", "input_schema"}

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.tool_registry import ToolSchema

        tool = ToolSchema(
            name="list_pods",
            description="List all pods",
            input_schema={"properties": {"namespace": {"type": "string"}}},
        )

        assert tool.name == "list_pods"
        assert tool.input_schema["properties"]["namespace"]["type"] == "string"


class TestToolRegistry:
    def test_to_payload(self) -> None:
        from hexawyn.domain.models.tool_registry import ToolRegistry, ToolSchema

        registry = ToolRegistry(
            tools=[ToolSchema(name="test", description="desc", input_schema={})]
        )

        payload = registry.to_payload()

        assert payload[0]["name"] == "test"
        assert payload[0]["description"] == "desc"

    def test_empty_registry(self) -> None:
        from hexawyn.domain.models.tool_registry import ToolRegistry

        assert ToolRegistry().to_payload() == []
