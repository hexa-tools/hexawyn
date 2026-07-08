from dataclasses import dataclass, field


@dataclass
class ChatSlackResponse:
    message: str
    quota_display: str
    suggestions: list[str] = field(default_factory=list)
    is_pro: bool = False
