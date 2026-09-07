# mypy: ignore-errors
from hexawyn.application.ports.primary.chat_port import ChatPort
from hexawyn.application.use_case.troubleshooting.chat_slack.chat_slack_command import (
    ChatSlackCommand,
)
from hexawyn.application.use_case.troubleshooting.chat_slack.chat_slack_use_case import (
    ChatSlackUseCase,
)
from hexawyn.domain.errors import QuotaExceededError


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSlackChatAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlackChatAdapterǁhandle_message__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlackChatAdapterǁformat_response__mutmut: MutantDict = {}  # type: ignore


class SlackChatAdapter(ChatPort):
    """
    Primary adapter for Slack Chat.
    Receives Slack messages, delegates to ChatSlackUseCase, posts response back.

    Never raises — all errors returned as Slack messages.
    Quota is enforced by ChatSlackUseCase (raises QuotaExceededError).
    """

    @_mutmut_mutated(mutants_xǁSlackChatAdapterǁ__init____mutmut)
    def __init__(self, use_case: ChatSlackUseCase | None = None) -> None:
        self._use_case: ChatSlackUseCase = use_case or ChatSlackUseCase()

    def xǁSlackChatAdapterǁ__init____mutmut_orig(self, use_case: ChatSlackUseCase | None = None) -> None:
        self._use_case: ChatSlackUseCase = use_case or ChatSlackUseCase()

    def xǁSlackChatAdapterǁ__init____mutmut_1(self, use_case: ChatSlackUseCase | None = None) -> None:
        self._use_case: ChatSlackUseCase = None

    def xǁSlackChatAdapterǁ__init____mutmut_2(self, use_case: ChatSlackUseCase | None = None) -> None:
        self._use_case: ChatSlackUseCase = use_case and ChatSlackUseCase()

    @_mutmut_mutated(mutants_xǁSlackChatAdapterǁhandle_message__mutmut)
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_orig(
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_1(
        self,
        query: str,
        cluster_name: str,
        channel_id: str,
        thread_ts: str | None = None,
    ) -> str:
        try:
            response = None
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_2(
        self,
        query: str,
        cluster_name: str,
        channel_id: str,
        thread_ts: str | None = None,
    ) -> str:
        try:
            response = self._use_case.execute(
                None
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_3(
        self,
        query: str,
        cluster_name: str,
        channel_id: str,
        thread_ts: str | None = None,
    ) -> str:
        try:
            response = self._use_case.execute(
                ChatSlackCommand(
                    query=None,
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_4(
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
                    cluster_name=None,
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_5(
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
                    channel_id=None,
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_6(
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
                    thread_ts=None,
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_7(
        self,
        query: str,
        cluster_name: str,
        channel_id: str,
        thread_ts: str | None = None,
    ) -> str:
        try:
            response = self._use_case.execute(
                ChatSlackCommand(
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_8(
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_9(
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_10(
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_11(
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
                answer=None,
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_12(
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
                quota_display=None,
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_13(
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
                suggestions=None,
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_14(
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
                is_pro=None,
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_15(
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_16(
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_17(
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

    def xǁSlackChatAdapterǁhandle_message__mutmut_18(
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

    @_mutmut_mutated(mutants_xǁSlackChatAdapterǁformat_response__mutmut)
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

    def xǁSlackChatAdapterǁformat_response__mutmut_orig(
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

    def xǁSlackChatAdapterǁformat_response__mutmut_1(
        self,
        answer: str,
        quota_display: str,
        suggestions: list[str],
        is_pro: bool = True,
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

    def xǁSlackChatAdapterǁformat_response__mutmut_2(
        self,
        answer: str,
        quota_display: str,
        suggestions: list[str],
        is_pro: bool = False,
    ) -> str:
        lines = None
        if suggestions:
            lines.append("")
            lines.append("*Suggested questions:*")
            for suggestion in suggestions[:4]:
                lines.append(f"• {suggestion}")
        return "\n".join(lines)

    def xǁSlackChatAdapterǁformat_response__mutmut_3(
        self,
        answer: str,
        quota_display: str,
        suggestions: list[str],
        is_pro: bool = False,
    ) -> str:
        lines = [
            "XX🔍 *hexawyn investigation result*XX",
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

    def xǁSlackChatAdapterǁformat_response__mutmut_4(
        self,
        answer: str,
        quota_display: str,
        suggestions: list[str],
        is_pro: bool = False,
    ) -> str:
        lines = [
            "🔍 *HEXAWYN INVESTIGATION RESULT*",
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

    def xǁSlackChatAdapterǁformat_response__mutmut_5(
        self,
        answer: str,
        quota_display: str,
        suggestions: list[str],
        is_pro: bool = False,
    ) -> str:
        lines = [
            "🔍 *hexawyn investigation result*",
            "XXXX",
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

    def xǁSlackChatAdapterǁformat_response__mutmut_6(
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
            "XXXX",
            quota_display,
        ]
        if suggestions:
            lines.append("")
            lines.append("*Suggested questions:*")
            for suggestion in suggestions[:4]:
                lines.append(f"• {suggestion}")
        return "\n".join(lines)

    def xǁSlackChatAdapterǁformat_response__mutmut_7(
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
            lines.append(None)
            lines.append("*Suggested questions:*")
            for suggestion in suggestions[:4]:
                lines.append(f"• {suggestion}")
        return "\n".join(lines)

    def xǁSlackChatAdapterǁformat_response__mutmut_8(
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
            lines.append("XXXX")
            lines.append("*Suggested questions:*")
            for suggestion in suggestions[:4]:
                lines.append(f"• {suggestion}")
        return "\n".join(lines)

    def xǁSlackChatAdapterǁformat_response__mutmut_9(
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
            lines.append(None)
            for suggestion in suggestions[:4]:
                lines.append(f"• {suggestion}")
        return "\n".join(lines)

    def xǁSlackChatAdapterǁformat_response__mutmut_10(
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
            lines.append("XX*Suggested questions:*XX")
            for suggestion in suggestions[:4]:
                lines.append(f"• {suggestion}")
        return "\n".join(lines)

    def xǁSlackChatAdapterǁformat_response__mutmut_11(
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
            lines.append("*suggested questions:*")
            for suggestion in suggestions[:4]:
                lines.append(f"• {suggestion}")
        return "\n".join(lines)

    def xǁSlackChatAdapterǁformat_response__mutmut_12(
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
            lines.append("*SUGGESTED QUESTIONS:*")
            for suggestion in suggestions[:4]:
                lines.append(f"• {suggestion}")
        return "\n".join(lines)

    def xǁSlackChatAdapterǁformat_response__mutmut_13(
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
            for suggestion in suggestions[:5]:
                lines.append(f"• {suggestion}")
        return "\n".join(lines)

    def xǁSlackChatAdapterǁformat_response__mutmut_14(
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
                lines.append(None)
        return "\n".join(lines)

    def xǁSlackChatAdapterǁformat_response__mutmut_15(
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
        return "\n".join(None)

    def xǁSlackChatAdapterǁformat_response__mutmut_16(
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
        return "XX\nXX".join(lines)

mutants_xǁSlackChatAdapterǁ__init____mutmut['_mutmut_orig'] = SlackChatAdapter.xǁSlackChatAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁ__init____mutmut['xǁSlackChatAdapterǁ__init____mutmut_1'] = SlackChatAdapter.xǁSlackChatAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁ__init____mutmut['xǁSlackChatAdapterǁ__init____mutmut_2'] = SlackChatAdapter.xǁSlackChatAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁSlackChatAdapterǁhandle_message__mutmut['_mutmut_orig'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_1'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_2'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_3'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_4'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_5'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_6'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_7'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_8'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_9'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_10'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_11'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_12'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_13'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_14'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_15'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_16'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_17'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁhandle_message__mutmut['xǁSlackChatAdapterǁhandle_message__mutmut_18'] = SlackChatAdapter.xǁSlackChatAdapterǁhandle_message__mutmut_18 # type: ignore # mutmut generated

mutants_xǁSlackChatAdapterǁformat_response__mutmut['_mutmut_orig'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_1'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_2'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_3'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_4'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_5'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_6'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_7'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_8'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_9'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_10'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_11'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_12'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_13'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_14'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_15'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSlackChatAdapterǁformat_response__mutmut['xǁSlackChatAdapterǁformat_response__mutmut_16'] = SlackChatAdapter.xǁSlackChatAdapterǁformat_response__mutmut_16 # type: ignore # mutmut generated
