from dataclasses import dataclass, field


@dataclass(frozen=True)
class MCPToolSchema:
    name: str
    description: str
    input_schema: dict[str, object]


@dataclass
class MCPToolRegistry:
    tools: list[MCPToolSchema] = field(default_factory=list)

    def to_payload(self) -> list[dict[str, object]]:
        return [
            {
                "name": t.name,
                "description": t.description,
                "input_schema": t.input_schema,
            }
            for t in self.tools
        ]
