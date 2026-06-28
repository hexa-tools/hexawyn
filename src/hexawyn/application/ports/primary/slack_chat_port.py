from abc import ABC, abstractmethod


class SlackChatPort(ABC):
    """
    Primary port for Slack Chat — receives questions from Slack users.
    Inbound port (like CLI) — feeds the LangGraph investigation pipeline.

    Free tier: shares investigation quota with CLI (50/month total).
    Pro tier: unlimited investigations, enriched Slack blocks response.
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
        Handle incoming Slack message and run investigation pipeline.
        Returns formatted response to post back in Slack.
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
        Format investigation result for Slack.
        Free tier: basic markdown text.
        Pro tier: enriched format with suggestion chips.
        """
