# mypy: ignore-errors
from hexawyn.application.ports.primary.chat_port import ChatPort
from hexawyn.application.use_case.troubleshooting.chat_slack.chat_slack_command import (
    ChatSlackCommand,
)
from hexawyn.application.use_case.troubleshooting.chat_slack.chat_slack_use_case import (
    ChatSlackUseCase,
)
from hexawyn.domain.errors import QuotaExceededError


class SlackChatAdapter(ChatPort):
    """
    Primary adapter for Slack Chat.
    Receives Slack messages, delegates to ChatSlackUseCase, posts response back.

    Never raises — all errors returned as Slack messages.
    Quota is enforced by ChatSlackService (raises QuotaExceededError).
    """

    def __init__(self, use_case: ChatSlackUseCase | None = None) -> None:
        self._use_case: ChatSlackUseCase = use_case or ChatSlackService()  # noqa: F821  # type: ignore

    def handle_message(
        self,
        query: str,
        cluster_name: str,
        channel_id: str,
        thread_ts: str | None = None,
    ) -> str:
        try:
            response = self._use_case.execute(
                ChatSlackCommand(
                    query=query,
                    cluster_name=cluster_name,
                    channel_id=channel_id,
                    thread_ts=thread_ts,
                )
            )
            return self.format_response(
                answer=response.message,
                quota_display=response.quota_display,
                suggestions=response.suggestions,
                is_pro=response.is_pro,
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
