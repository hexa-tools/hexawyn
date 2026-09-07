import os

import httpx

from hexawyn.application.ports.driven.alert_notification_port import (
    AlertMessage,
    AlertNotificationPort,
)
from hexawyn.domain.models.slack import SlackBlock, SlackMessage
from hexawyn.infrastructure.config.quota_manager import (
    check_slack_quota,
    increment_slack_quota,
)

_SEVERITY_EMOJI: dict[str, str] = {
    "critical": "🚨",
    "high": "⚠️",
    "warning": "⚠️",
    "info": "ℹ️",
}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSlackAlertAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlackAlertAdapterǁsend_test_ping__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSlackAlertAdapterǁ_post__mutmut: MutantDict = {}  # type: ignore


class SlackAlertAdapter(AlertNotificationPort):
    """
    Sends alerts to Slack via incoming webhook.
    Free tier: 5 alerts/month (quota enforced via check_slack_quota).
    Pro tier: unlimited + enriched blocks format.

    Never raises on network errors — returns False instead.
    Raises SlackQuotaExceededError when monthly limit is reached.
    """

    @_mutmut_mutated(mutants_xǁSlackAlertAdapterǁ__init____mutmut)
    def __init__(self, webhook_url: str | None = None) -> None:
        self._webhook_url = webhook_url or os.environ.get("HEXAWYN_SLACK_WEBHOOK_URL", "")

    def xǁSlackAlertAdapterǁ__init____mutmut_orig(self, webhook_url: str | None = None) -> None:
        self._webhook_url = webhook_url or os.environ.get("HEXAWYN_SLACK_WEBHOOK_URL", "")

    def xǁSlackAlertAdapterǁ__init____mutmut_1(self, webhook_url: str | None = None) -> None:
        self._webhook_url = None

    def xǁSlackAlertAdapterǁ__init____mutmut_2(self, webhook_url: str | None = None) -> None:
        self._webhook_url = webhook_url and os.environ.get("HEXAWYN_SLACK_WEBHOOK_URL", "")

    def xǁSlackAlertAdapterǁ__init____mutmut_3(self, webhook_url: str | None = None) -> None:
        self._webhook_url = webhook_url or os.environ.get(None, "")

    def xǁSlackAlertAdapterǁ__init____mutmut_4(self, webhook_url: str | None = None) -> None:
        self._webhook_url = webhook_url or os.environ.get("HEXAWYN_SLACK_WEBHOOK_URL", None)

    def xǁSlackAlertAdapterǁ__init____mutmut_5(self, webhook_url: str | None = None) -> None:
        self._webhook_url = webhook_url or os.environ.get("")

    def xǁSlackAlertAdapterǁ__init____mutmut_6(self, webhook_url: str | None = None) -> None:
        self._webhook_url = webhook_url or os.environ.get("HEXAWYN_SLACK_WEBHOOK_URL", )

    def xǁSlackAlertAdapterǁ__init____mutmut_7(self, webhook_url: str | None = None) -> None:
        self._webhook_url = webhook_url or os.environ.get("XXHEXAWYN_SLACK_WEBHOOK_URLXX", "")

    def xǁSlackAlertAdapterǁ__init____mutmut_8(self, webhook_url: str | None = None) -> None:
        self._webhook_url = webhook_url or os.environ.get("hexawyn_slack_webhook_url", "")

    def xǁSlackAlertAdapterǁ__init____mutmut_9(self, webhook_url: str | None = None) -> None:
        self._webhook_url = webhook_url or os.environ.get("HEXAWYN_SLACK_WEBHOOK_URL", "XXXX")

    @_mutmut_mutated(mutants_xǁSlackAlertAdapterǁsend_alert__mutmut)
    def send_alert(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_orig(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_1(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").upper() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_2(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get(None, "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_3(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", None).lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_4(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_5(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", ).lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_6(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("XXHEXAWYN_ANONYMIZE_ENABLEDXX", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_7(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("hexawyn_anonymize_enabled", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_8(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "XXfalseXX").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_9(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "FALSE").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_10(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() != "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_11(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "XXtrueXX":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_12(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "TRUE":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_13(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = None
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_14(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = None
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_15(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = None
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_16(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get(None, "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_17(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", None)
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_18(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_19(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", )
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_20(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("XXmessageXX", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_21(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("MESSAGE", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_22(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "XXXX")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_23(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = None
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_24(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(None, policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_25(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), None)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_26(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_27(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), )
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_28(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(None), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_29(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = None  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_30(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["XXmessageXX"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_31(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["MESSAGE"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_32(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = None
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_33(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(None)
        return self._post(slack_msg, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_34(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(None, track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_35(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=None)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_36(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(track_quota=True)

    def xǁSlackAlertAdapterǁsend_alert__mutmut_37(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, )

    def xǁSlackAlertAdapterǁsend_alert__mutmut_38(self, message: AlertMessage) -> bool:
        check_slack_quota()
        import os

        if os.environ.get("HEXAWYN_ANONYMIZE_ENABLED", "false").lower() == "true":
            from hexawyn.domain.models.anonymization import RedactionPolicy
            from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter

            adapter = RegexAnonymizerAdapter()
            policy = RedactionPolicy()
            raw = message.get("message", "")
            masked, _ = adapter.mask(str(raw), policy)
            message["message"] = masked  # type: ignore[typeddict-unknown-key]
        slack_msg = self._to_slack_message(message)
        return self._post(slack_msg, track_quota=False)

    @_mutmut_mutated(mutants_xǁSlackAlertAdapterǁsend_test_ping__mutmut)
    def send_test_ping(self) -> bool:
        """Send a connectivity test without consuming quota."""
        return self._post(
            SlackMessage(text="✅ hexawyn Slack integration is working!"), track_quota=False
        )

    def xǁSlackAlertAdapterǁsend_test_ping__mutmut_orig(self) -> bool:
        """Send a connectivity test without consuming quota."""
        return self._post(
            SlackMessage(text="✅ hexawyn Slack integration is working!"), track_quota=False
        )

    def xǁSlackAlertAdapterǁsend_test_ping__mutmut_1(self) -> bool:
        """Send a connectivity test without consuming quota."""
        return self._post(
            None, track_quota=False
        )

    def xǁSlackAlertAdapterǁsend_test_ping__mutmut_2(self) -> bool:
        """Send a connectivity test without consuming quota."""
        return self._post(
            SlackMessage(text="✅ hexawyn Slack integration is working!"), track_quota=None
        )

    def xǁSlackAlertAdapterǁsend_test_ping__mutmut_3(self) -> bool:
        """Send a connectivity test without consuming quota."""
        return self._post(
            track_quota=False
        )

    def xǁSlackAlertAdapterǁsend_test_ping__mutmut_4(self) -> bool:
        """Send a connectivity test without consuming quota."""
        return self._post(
            SlackMessage(text="✅ hexawyn Slack integration is working!"), )

    def xǁSlackAlertAdapterǁsend_test_ping__mutmut_5(self) -> bool:
        """Send a connectivity test without consuming quota."""
        return self._post(
            SlackMessage(text=None), track_quota=False
        )

    def xǁSlackAlertAdapterǁsend_test_ping__mutmut_6(self) -> bool:
        """Send a connectivity test without consuming quota."""
        return self._post(
            SlackMessage(text="XX✅ hexawyn Slack integration is working!XX"), track_quota=False
        )

    def xǁSlackAlertAdapterǁsend_test_ping__mutmut_7(self) -> bool:
        """Send a connectivity test without consuming quota."""
        return self._post(
            SlackMessage(text="✅ hexawyn slack integration is working!"), track_quota=False
        )

    def xǁSlackAlertAdapterǁsend_test_ping__mutmut_8(self) -> bool:
        """Send a connectivity test without consuming quota."""
        return self._post(
            SlackMessage(text="✅ HEXAWYN SLACK INTEGRATION IS WORKING!"), track_quota=False
        )

    def xǁSlackAlertAdapterǁsend_test_ping__mutmut_9(self) -> bool:
        """Send a connectivity test without consuming quota."""
        return self._post(
            SlackMessage(text="✅ hexawyn Slack integration is working!"), track_quota=True
        )

    @_mutmut_mutated(mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut)
    def format_finding_alert(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_orig(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_1(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = True,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_2(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = None
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_3(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get(None, "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_4(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", None)
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_5(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_6(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", )
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_7(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("XXseverityXX", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_8(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("SEVERITY", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_9(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "XXinfoXX")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_10(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "INFO")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_11(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = None
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_12(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get(None, "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_13(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", None)
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_14(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_15(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", )
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_16(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("XXmessageXX", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_17(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("MESSAGE", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_18(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "XXXX")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_19(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = None
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_20(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get(None, "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_21(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", None)
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_22(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_23(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", )
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_24(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("XXremediationXX", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_25(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("REMEDIATION", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_26(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "XXXX")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_27(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = None
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_28(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(None, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_29(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, None)
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_30(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get("ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_31(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, )
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_32(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "XXℹ️XX")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_33(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = None  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_34(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "XXDEGRADEDXX" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_35(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "degraded" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_36(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score <= 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_37(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 86 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_38(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "XXHEALTHYXX"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_39(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "healthy"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_40(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = None

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_41(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=None,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_42(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=None,
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_43(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=None,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_44(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_45(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=None,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_46(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=None,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_47(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=None,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_48(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_49(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_50(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_51(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_52(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            score=score,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_53(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            is_pro=is_pro,
        )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_54(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation or None,
            cluster_name=cluster_name,
            score=score,
            )

    def xǁSlackAlertAdapterǁformat_finding_alert__mutmut_55(
        self,
        finding: dict[str, str],
        cluster_name: str,
        score: int,
        is_pro: bool = False,
    ) -> AlertMessage:
        severity = finding.get("severity", "info")
        message = finding.get("message", "")
        remediation = finding.get("remediation", "")
        emoji = _SEVERITY_EMOJI.get(severity, "ℹ️")
        status = "DEGRADED" if score < 85 else "HEALTHY"  # noqa: PLR2004

        text = (
            f"{emoji} *hexawyn Alert — {cluster_name}*\n"
            f"Status: {status} · Score: {score}/100\n"
            f"• {message}"
        )

        return AlertMessage(
            text=text,
            title=f"{emoji} hexawyn Alert — {cluster_name}",
            severity=severity,
            remediation=remediation and None,
            cluster_name=cluster_name,
            score=score,
            is_pro=is_pro,
        )

    @_mutmut_mutated(mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut)
    def _to_slack_message(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_orig(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_1(self, message: AlertMessage) -> SlackMessage:
        if message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_2(self, message: AlertMessage) -> SlackMessage:
        if not message["XXis_proXX"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_3(self, message: AlertMessage) -> SlackMessage:
        if not message["IS_PRO"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_4(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=None, is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_5(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=None)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_6(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_7(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], )

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_8(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["XXtextXX"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_9(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["TEXT"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_10(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=True)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_11(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = None  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_12(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "XXDEGRADEDXX" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_13(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "degraded" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_14(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["XXscoreXX"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_15(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["SCORE"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_16(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] <= 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_17(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 86 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_18(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "XXHEALTHYXX"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_19(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "healthy"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_20(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = None
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_21(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] and message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_22(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["XXtitleXX"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_23(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["TITLE"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_24(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["XXtextXX"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_25(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["TEXT"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_26(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = None
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_27(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type=None, text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_28(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=None),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_29(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_30(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", ),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_31(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="XXheaderXX", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_32(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="HEADER", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_33(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type=None,
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_34(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=None,
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_35(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_36(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_37(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="XXsectionXX",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_38(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="SECTION",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_39(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['XXscoreXX']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_40(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['SCORE']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_41(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type=None, text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_42(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=None),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_43(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_44(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", ),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_45(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="XXsectionXX", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_46(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="SECTION", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_47(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['XXtextXX']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_48(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['TEXT']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_49(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type=None, text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_50(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=None),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_51(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_52(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", ),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_53(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="XXsectionXX", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_54(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="SECTION", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_55(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] and ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_56(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['XXremediationXX'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_57(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['REMEDIATION'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_58(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or 'XXXX'}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_59(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type=None, text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_60(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=None),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_61(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_62(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", ),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_63(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="XXdividerXX", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_64(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="DIVIDER", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_65(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text="XXXX"),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_66(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=None, blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_67(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=None, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_68(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=None)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_69(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_70(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_71(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, )

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_72(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["XXtextXX"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_73(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["TEXT"], blocks=blocks, is_pro_format=True)

    def xǁSlackAlertAdapterǁ_to_slack_message__mutmut_74(self, message: AlertMessage) -> SlackMessage:
        if not message["is_pro"]:
            return SlackMessage(text=message["text"], is_pro_format=False)

        status = "DEGRADED" if message["score"] < 85 else "HEALTHY"  # noqa: PLR2004
        title = message["title"] or message["text"]
        blocks = [
            SlackBlock(type="header", text=title),
            SlackBlock(
                type="section",
                text=f"*Status:* {status} · *Score:* {message['score']}/100",
            ),
            SlackBlock(type="section", text=f"*Finding:* {message['text']}"),
            SlackBlock(type="section", text=f"*Remediation:* {message['remediation'] or ''}"),
            SlackBlock(type="divider", text=""),
        ]
        return SlackMessage(text=message["text"], blocks=blocks, is_pro_format=False)

    @_mutmut_mutated(mutants_xǁSlackAlertAdapterǁ_post__mutmut)
    def _post(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                timeout=10.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_orig(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                timeout=10.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_1(self, message: SlackMessage, track_quota: bool) -> bool:
        if self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                timeout=10.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_2(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return True
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                timeout=10.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_3(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = None
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_4(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                None,
                json=message.to_payload(),
                timeout=10.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_5(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=None,
                timeout=10.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_6(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                timeout=None,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_7(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                json=message.to_payload(),
                timeout=10.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_8(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                timeout=10.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_9(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_10(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                timeout=11.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_11(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                timeout=10.0,
            )
            if response.status_code != 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_12(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                timeout=10.0,
            )
            if response.status_code == 201:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_13(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                timeout=10.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return False
            return False
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_14(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                timeout=10.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return True
        except Exception:
            return False

    def xǁSlackAlertAdapterǁ_post__mutmut_15(self, message: SlackMessage, track_quota: bool) -> bool:
        if not self._webhook_url:
            return False
        try:
            response = httpx.post(
                self._webhook_url,
                json=message.to_payload(),
                timeout=10.0,
            )
            if response.status_code == 200:  # noqa: PLR2004
                if track_quota:
                    increment_slack_quota()
                return True
            return False
        except Exception:
            return True

mutants_xǁSlackAlertAdapterǁ__init____mutmut['_mutmut_orig'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ__init____mutmut['xǁSlackAlertAdapterǁ__init____mutmut_1'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ__init____mutmut['xǁSlackAlertAdapterǁ__init____mutmut_2'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ__init____mutmut['xǁSlackAlertAdapterǁ__init____mutmut_3'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ__init____mutmut['xǁSlackAlertAdapterǁ__init____mutmut_4'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ__init____mutmut['xǁSlackAlertAdapterǁ__init____mutmut_5'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ__init____mutmut['xǁSlackAlertAdapterǁ__init____mutmut_6'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ__init____mutmut['xǁSlackAlertAdapterǁ__init____mutmut_7'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ__init____mutmut['xǁSlackAlertAdapterǁ__init____mutmut_8'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ__init____mutmut['xǁSlackAlertAdapterǁ__init____mutmut_9'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ__init____mutmut_9 # type: ignore # mutmut generated

mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['_mutmut_orig'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_1'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_2'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_3'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_4'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_5'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_6'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_7'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_8'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_9'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_10'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_11'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_12'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_13'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_14'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_15'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_16'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_17'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_18'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_19'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_20'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_21'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_22'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_23'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_24'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_25'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_26'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_26 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_27'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_27 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_28'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_28 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_29'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_29 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_30'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_30 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_31'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_31 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_32'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_32 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_33'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_33 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_34'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_34 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_35'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_35 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_36'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_36 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_37'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_37 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_alert__mutmut['xǁSlackAlertAdapterǁsend_alert__mutmut_38'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_alert__mutmut_38 # type: ignore # mutmut generated

mutants_xǁSlackAlertAdapterǁsend_test_ping__mutmut['_mutmut_orig'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_test_ping__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_test_ping__mutmut['xǁSlackAlertAdapterǁsend_test_ping__mutmut_1'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_test_ping__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_test_ping__mutmut['xǁSlackAlertAdapterǁsend_test_ping__mutmut_2'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_test_ping__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_test_ping__mutmut['xǁSlackAlertAdapterǁsend_test_ping__mutmut_3'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_test_ping__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_test_ping__mutmut['xǁSlackAlertAdapterǁsend_test_ping__mutmut_4'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_test_ping__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_test_ping__mutmut['xǁSlackAlertAdapterǁsend_test_ping__mutmut_5'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_test_ping__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_test_ping__mutmut['xǁSlackAlertAdapterǁsend_test_ping__mutmut_6'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_test_ping__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_test_ping__mutmut['xǁSlackAlertAdapterǁsend_test_ping__mutmut_7'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_test_ping__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_test_ping__mutmut['xǁSlackAlertAdapterǁsend_test_ping__mutmut_8'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_test_ping__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁsend_test_ping__mutmut['xǁSlackAlertAdapterǁsend_test_ping__mutmut_9'] = SlackAlertAdapter.xǁSlackAlertAdapterǁsend_test_ping__mutmut_9 # type: ignore # mutmut generated

mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['_mutmut_orig'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_1'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_2'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_3'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_4'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_5'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_6'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_7'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_8'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_9'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_10'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_11'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_12'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_13'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_14'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_15'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_16'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_17'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_18'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_19'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_20'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_21'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_22'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_23'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_24'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_25'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_26'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_26 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_27'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_27 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_28'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_28 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_29'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_29 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_30'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_30 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_31'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_31 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_32'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_32 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_33'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_33 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_34'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_34 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_35'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_35 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_36'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_36 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_37'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_37 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_38'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_38 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_39'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_39 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_40'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_40 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_41'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_41 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_42'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_42 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_43'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_43 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_44'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_44 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_45'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_45 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_46'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_46 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_47'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_47 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_48'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_48 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_49'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_49 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_50'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_50 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_51'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_51 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_52'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_52 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_53'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_53 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_54'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_54 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁformat_finding_alert__mutmut['xǁSlackAlertAdapterǁformat_finding_alert__mutmut_55'] = SlackAlertAdapter.xǁSlackAlertAdapterǁformat_finding_alert__mutmut_55 # type: ignore # mutmut generated

mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['_mutmut_orig'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_1'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_2'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_3'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_4'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_5'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_6'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_7'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_8'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_9'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_10'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_11'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_12'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_13'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_14'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_15'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_16'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_17'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_18'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_19'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_20'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_21'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_22'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_23'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_24'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_25'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_26'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_26 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_27'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_27 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_28'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_28 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_29'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_29 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_30'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_30 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_31'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_31 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_32'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_32 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_33'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_33 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_34'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_34 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_35'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_35 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_36'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_36 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_37'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_37 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_38'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_38 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_39'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_39 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_40'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_40 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_41'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_41 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_42'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_42 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_43'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_43 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_44'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_44 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_45'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_45 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_46'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_46 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_47'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_47 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_48'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_48 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_49'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_49 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_50'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_50 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_51'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_51 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_52'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_52 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_53'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_53 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_54'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_54 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_55'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_55 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_56'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_56 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_57'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_57 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_58'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_58 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_59'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_59 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_60'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_60 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_61'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_61 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_62'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_62 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_63'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_63 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_64'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_64 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_65'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_65 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_66'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_66 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_67'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_67 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_68'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_68 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_69'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_69 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_70'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_70 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_71'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_71 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_72'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_72 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_73'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_73 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_to_slack_message__mutmut['xǁSlackAlertAdapterǁ_to_slack_message__mutmut_74'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_to_slack_message__mutmut_74 # type: ignore # mutmut generated

mutants_xǁSlackAlertAdapterǁ_post__mutmut['_mutmut_orig'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_1'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_2'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_3'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_4'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_5'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_6'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_7'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_8'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_9'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_10'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_11'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_12'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_13'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_14'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSlackAlertAdapterǁ_post__mutmut['xǁSlackAlertAdapterǁ_post__mutmut_15'] = SlackAlertAdapter.xǁSlackAlertAdapterǁ_post__mutmut_15 # type: ignore # mutmut generated
