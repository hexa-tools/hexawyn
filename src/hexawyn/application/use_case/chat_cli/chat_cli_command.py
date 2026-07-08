from dataclasses import dataclass, field


@dataclass(frozen=True)
class ChatCliCommand:
    query: str
    conversation_history: list[dict[str, str]] = field(default_factory=list)
