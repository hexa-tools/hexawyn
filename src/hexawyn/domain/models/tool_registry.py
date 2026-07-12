from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ToolSchema:
    name: str
    description: str
    input_schema: dict[str, object]


@dataclass
class ToolRegistry:
    tools: list[ToolSchema] = field(default_factory=list)

    def to_payload(self) -> list[dict[str, object]]:
        return [
            {"name": t.name, "description": t.description, "input_schema": t.input_schema}
            for t in self.tools
        ]
