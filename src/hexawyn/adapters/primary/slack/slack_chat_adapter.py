from hexawyn.application.ports.primary.slack_chat_port import SlackChatPort
from hexawyn.domain.errors import QuotaExceededError
from hexawyn.infrastructure.config.license_manager import is_pro
from hexawyn.infrastructure.config.quota_manager import get_quota_display


def run_investigation(query: str, cluster_name: str) -> str:
    """
    Stub: runs LangGraph investigation pipeline.
    TODO (ECA-next): wire to build_investigation_graph().
    """
    raise NotImplementedError("ECA-next: wire to LangGraph")


class SlackChatAdapter(SlackChatPort):
    """
    Primary adapter for Slack Chat.
    Receives Slack messages, feeds them into LangGraph,
    posts response back in Slack thread.

    Quota: shares investigation pool with CLI (50/month Free).
    Never raises — all errors returned as Slack messages.
    """

    def handle_message(
        self,
        query: str,
        cluster_name: str,
        channel_id: str,
        thread_ts: str | None = None,
    ) -> str:
        try:
            answer = run_investigation(query=query, cluster_name=cluster_name)
            quota = get_quota_display()
            pro = is_pro()
            return self.format_response(
                answer=answer,
                quota_display=quota,
                suggestions=[],
                is_pro=pro,
            )
        except QuotaExceededError as exc:
            return (
                f"❌ *Quota exceeded*\n"
                f"You've used {exc.used}/{exc.limit} free investigations this month.\n"
                f"Resets on the 1st of next month.\n"
                f"Upgrade to Pro: https://hexawyn.com/pro"
            )
        except Exception as exc:
            return (
                f"⚠️ *hexawyn error*\n"
                f"Could not complete investigation: {exc}\n"
                f"Please try again or check `/config` settings."
            )

    def format_response(
        self,
        answer: str,
        quota_display: str,
        suggestions: list[str],
        is_pro: bool = False,
    ) -> str:
        lines = [
            "🔍 *hexawyn investigation result*",
            "",
            answer,
            "",
            quota_display,
        ]
        if suggestions:
            lines.append("")
            lines.append("*Suggested questions:*")
            for suggestion in suggestions[:4]:
                lines.append(f"• {suggestion}")
        return "\n".join(lines)
