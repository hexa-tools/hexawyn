from dataclasses import dataclass, field


@dataclass
class SlackBlock:
    type: str
    text: str = ""


@dataclass
class SlackMessage:
    """
    A Slack message to be sent via webhook.
    Free tier (is_pro_format=False): basic text format.
    Pro tier (is_pro_format=True): enriched format with blocks.
    """

    text: str
    blocks: list[SlackBlock] = field(default_factory=list)
    is_pro_format: bool = False

    def to_payload(self) -> dict[str, object]:
        payload: dict[str, object] = {"text": self.text}
        if self.is_pro_format and self.blocks:
            payload["blocks"] = [
                {"type": b.type, "text": {"type": "mrkdwn", "text": b.text}} for b in self.blocks
            ]
        return payload
