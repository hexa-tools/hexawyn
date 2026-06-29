from dataclasses import dataclass


@dataclass(frozen=True)
class ChatCliCommand:
    query: str
