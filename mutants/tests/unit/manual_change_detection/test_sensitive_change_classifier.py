"""Unit tests for classify_severity — Secret is always critical; ConfigMap
is critical only when its name matches a sensitive (RBAC/TLS) keyword."""

from __future__ import annotations

_KEYWORDS = ("rbac", "role", "tls", "cert", "certificate")


class TestSecretSeverity:
    def test_secret_is_always_critical(self) -> None:
        from hexawyn.domain.services.manual_change_detection.sensitive_change_classifier import (
            classify_severity,
        )

        assert classify_severity("Secret", "db-password", _KEYWORDS) == "critical"

    def test_secret_with_unrelated_name_is_still_critical(self) -> None:
        from hexawyn.domain.services.manual_change_detection.sensitive_change_classifier import (
            classify_severity,
        )

        assert classify_severity("Secret", "anything-at-all", _KEYWORDS) == "critical"


class TestConfigMapSeverity:
    def test_plain_configmap_is_warning(self) -> None:
        from hexawyn.domain.services.manual_change_detection.sensitive_change_classifier import (
            classify_severity,
        )

        assert classify_severity("ConfigMap", "app-config", _KEYWORDS) == "warning"

    def test_rbac_related_configmap_is_critical(self) -> None:
        from hexawyn.domain.services.manual_change_detection.sensitive_change_classifier import (
            classify_severity,
        )

        assert classify_severity("ConfigMap", "rbac-policy", _KEYWORDS) == "critical"

    def test_tls_related_configmap_is_critical(self) -> None:
        from hexawyn.domain.services.manual_change_detection.sensitive_change_classifier import (
            classify_severity,
        )

        assert classify_severity("ConfigMap", "tls-config", _KEYWORDS) == "critical"

    def test_keyword_match_is_case_insensitive(self) -> None:
        from hexawyn.domain.services.manual_change_detection.sensitive_change_classifier import (
            classify_severity,
        )

        assert classify_severity("ConfigMap", "TLS-Config", _KEYWORDS) == "critical"
