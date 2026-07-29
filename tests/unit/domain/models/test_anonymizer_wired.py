"""Tests for wired anonymizer — Slack adapter + logging filter."""

from unittest.mock import MagicMock

from hexawyn.domain.models.anonymization import RedactionPolicy
from hexawyn.runtime.adapters.anonymize.regex_anonymizer import RegexAnonymizerAdapter


class TestSlackAnonymizerModule:
    def test_anonymizer_masks_and_returns_map(self) -> None:
        text = "Secret: my-app-secret and IP 10.0.0.1"
        masked, amap = RegexAnonymizerAdapter().mask(text, RedactionPolicy())
        assert "my-app-secret" not in masked
        assert "10.0.0.1" not in masked
        assert len(amap.matches) == 2  # noqa: PLR2004

    def test_anonymizer_disabled_does_nothing(self) -> None:
        text = "Normal message"
        masked, amap = RegexAnonymizerAdapter().mask(
            text, RedactionPolicy(mask_secrets=False, mask_ips=False, mask_tokens=False)
        )
        assert masked == text
        assert len(amap.matches) == 0


class TestLogAnonymizerFilter:
    def test_filter_anonymizes_log_message(self) -> None:
        from hexawyn.infrastructure.logging.tool_decorator import _AnonymizerFilter

        f = _AnonymizerFilter()
        record = MagicMock()
        record.msg = "Secret: my-app-secret and IP 10.0.0.1"
        record.args = ("arg1", "arg2")
        result = f.filter(record)
        assert result is True
        assert "my-app-secret" not in str(record.msg)

    def test_filter_handles_non_string_args(self) -> None:
        from hexawyn.infrastructure.logging.tool_decorator import _AnonymizerFilter

        f = _AnonymizerFilter()
        record = MagicMock()
        record.msg = "normal message"
        record.args = (42, None)
        result = f.filter(record)
        assert result is True

    def test_filter_handles_exception_gracefully(self) -> None:
        from hexawyn.infrastructure.logging.tool_decorator import _AnonymizerFilter

        f = _AnonymizerFilter()
        record = MagicMock()
        record.msg = object()  # will crash str()
        record.args = None
        result = f.filter(record)
        assert result is True


class TestAnonymizerPolicyVariations:
    def test_policy_ip_only(self) -> None:
        text = "Secret: my-secret and IP 10.0.0.1"
        masked, amap = RegexAnonymizerAdapter().mask(
            text, RedactionPolicy(mask_secrets=False, mask_tokens=False)
        )
        assert "my-secret" in masked
        assert "10.0.0.1" not in masked

    def test_policy_secret_only(self) -> None:
        text = "Secret: my-secret and IP 10.0.0.1"
        masked, amap = RegexAnonymizerAdapter().mask(
            text, RedactionPolicy(mask_ips=False, mask_tokens=False)
        )
        assert "my-secret" not in masked
        assert "10.0.0.1" in masked
