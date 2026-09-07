"""Unit tests for classify_severity — currently always 'critical' for any
reported drift; the one place this decision lives, documented in the plan."""

from __future__ import annotations

from hexawyn.domain.services.image_drift.drift_severity import classify_severity


class TestClassifySeverity:
    def test_tag_mismatch_is_critical(self) -> None:
        assert classify_severity("tag_mismatch") == "critical"

    def test_digest_mismatch_is_critical(self) -> None:
        assert classify_severity("digest_mismatch") == "critical"
