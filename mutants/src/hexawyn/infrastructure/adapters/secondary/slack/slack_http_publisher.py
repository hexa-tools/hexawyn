from hexawyn.application.ports.driven.message_publisher_port import MessagePublisherPort
from hexawyn.infrastructure.adapters.secondary.slack.slack_http_client import SlackHttpClient


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSlackHttpPublisherǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlackHttpPublisherǁpost_message__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut: MutantDict = {}  # type: ignore


class SlackHttpPublisher(MessagePublisherPort):
    """
    Posts messages to Slack via chat.postMessage using SLACK_BOT_TOKEN.
    SlackHttpClient is injected — never instantiated internally.
    Never raises — delivery failures return None.
    """

    @_mutmut_mutated(mutants_xǁSlackHttpPublisherǁ__init____mutmut)
    def __init__(self, http_client: SlackHttpClient) -> None:
        self._client = http_client

    def xǁSlackHttpPublisherǁ__init____mutmut_orig(self, http_client: SlackHttpClient) -> None:
        self._client = http_client

    def xǁSlackHttpPublisherǁ__init____mutmut_1(self, http_client: SlackHttpClient) -> None:
        self._client = None

    @_mutmut_mutated(mutants_xǁSlackHttpPublisherǁpost_message__mutmut)
    def post_message(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_orig(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_1(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = None
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_2(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"XXchannelXX": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_3(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"CHANNEL": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_4(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "XXtextXX": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_5(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "TEXT": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_6(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_7(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = None
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_8(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["XXthread_tsXX"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_9(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["THREAD_TS"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_10(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = None
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_11(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post(None, payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_12(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", None)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_13(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post(payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_14(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", )
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_15(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("XXchat.postMessageXX", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_16(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postmessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_17(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("CHAT.POSTMESSAGE", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_18(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get(None):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_19(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("XXokXX"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_20(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("OK"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_21(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = None
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_22(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get(None)
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_23(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("XXtsXX")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_24(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("TS")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁpost_message__mutmut_25(
        self,
        channel_id: str,
        text: str,
        thread_ts: str | None = None,
    ) -> str | None:
        payload: dict[str, object] = {"channel": channel_id, "text": text}
        if thread_ts is not None:
            payload["thread_ts"] = thread_ts
        try:
            response = self._client.post("chat.postMessage", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(None) if raw_ts else None
            return None
        except Exception:
            return None

    @_mutmut_mutated(mutants_xǁSlackHttpPublisherǁupdate_message__mutmut)
    def update_message(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_orig(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_1(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = None
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_2(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "XXchannelXX": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_3(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "CHANNEL": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_4(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "XXtsXX": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_5(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "TS": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_6(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "XXtextXX": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_7(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "TEXT": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_8(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = None
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_9(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post(None, payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_10(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", None)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_11(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post(payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_12(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", )
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_13(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("XXchat.updateXX", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_14(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("CHAT.UPDATE", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_15(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get(None):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_16(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("XXokXX"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_17(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("OK"):
                raw_ts = response.get("ts")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_18(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = None
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_19(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get(None)
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_20(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("XXtsXX")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_21(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("TS")
                return str(raw_ts) if raw_ts else None
            return None
        except Exception:
            return None

    def xǁSlackHttpPublisherǁupdate_message__mutmut_22(
        self,
        channel_id: str,
        message_ts: str,
        text: str,
    ) -> str | None:
        payload: dict[str, object] = {
            "channel": channel_id,
            "ts": message_ts,
            "text": text,
        }
        try:
            response = self._client.post("chat.update", payload)
            if response.get("ok"):
                raw_ts = response.get("ts")
                return str(None) if raw_ts else None
            return None
        except Exception:
            return None

mutants_xǁSlackHttpPublisherǁ__init____mutmut['_mutmut_orig'] = SlackHttpPublisher.xǁSlackHttpPublisherǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁ__init____mutmut['xǁSlackHttpPublisherǁ__init____mutmut_1'] = SlackHttpPublisher.xǁSlackHttpPublisherǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁSlackHttpPublisherǁpost_message__mutmut['_mutmut_orig'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_1'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_2'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_3'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_4'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_5'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_6'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_7'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_8'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_9'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_10'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_11'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_12'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_13'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_14'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_15'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_16'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_17'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_18'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_19'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_20'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_21'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_22'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_23'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_24'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁpost_message__mutmut['xǁSlackHttpPublisherǁpost_message__mutmut_25'] = SlackHttpPublisher.xǁSlackHttpPublisherǁpost_message__mutmut_25 # type: ignore # mutmut generated

mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['_mutmut_orig'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_1'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_2'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_3'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_4'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_5'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_6'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_7'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_8'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_9'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_10'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_11'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_12'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_13'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_14'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_15'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_16'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_17'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_18'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_19'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_20'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_21'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSlackHttpPublisherǁupdate_message__mutmut['xǁSlackHttpPublisherǁupdate_message__mutmut_22'] = SlackHttpPublisher.xǁSlackHttpPublisherǁupdate_message__mutmut_22 # type: ignore # mutmut generated
