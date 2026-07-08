from abc import ABC, abstractmethod


class ChatPort(ABC):
    """
    Primary port for Chat — receives investigation questions from users (Slack, Teams, etc.).
    Inbound port (like CLI) — feeds the LangGraph investigation pipeline.

    Free tier: shares investigation quota with CLI (50/month total).
    Pro tier: unlimited investigations, enriched response format.
    """

    @abstractmethod
    def handle_message(
        self,
        query: str,
        cluster_name: str,
        channel_id: str,
        thread_ts: str | None = None,
    ) -> str:
        """
        Handle incoming chat message and run investigation pipeline.
        Returns formatted response to post back in the channel.
        Never raises — all errors returned as strings.
        """

    @abstractmethod
    def format_response(
        self,
        answer: str,
        quota_display: str,
        suggestions: list[str],
        is_pro: bool,
    ) -> str:
        """
        Format investigation result for the chat platform.
        Free tier: basic markdown text.
        Pro tier: enriched format with suggestion chips.
        """
