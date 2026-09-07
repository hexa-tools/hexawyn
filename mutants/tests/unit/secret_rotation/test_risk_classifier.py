"""Unit tests for classify_risk_level. Checker case 4: an Opaque secret
containing a DATABASE_URL key must be classified critical regardless of its
k8s `type` field — the keys are what matter, not the type alone (except TLS,
which is always critical)."""

from __future__ import annotations


class TestClassifyRiskLevel:
    def test_tls_type_is_always_critical_regardless_of_keys(self) -> None:
        """Test Scenario 2: TLS secret not rotated in 95 days -> critical."""
        from hexawyn.domain.services.secret_rotation.risk_classifier import classify_risk_level

        result = classify_risk_level("kubernetes.io/tls", data_keys=["tls.crt", "tls.key"])

        assert result == "critical"

    def test_opaque_with_database_url_key_is_critical(self) -> None:
        """Checker case 4's exact scenario."""
        from hexawyn.domain.services.secret_rotation.risk_classifier import classify_risk_level

        result = classify_risk_level("Opaque", data_keys=["DATABASE_URL"])

        assert result == "critical"

    def test_opaque_with_password_key_is_critical(self) -> None:
        """Test Scenario 1: DB password secret -> critical risk."""
        from hexawyn.domain.services.secret_rotation.risk_classifier import classify_risk_level

        result = classify_risk_level("Opaque", data_keys=["DB_PASSWORD"])

        assert result == "critical"

    def test_opaque_with_token_key_is_medium(self) -> None:
        from hexawyn.domain.services.secret_rotation.risk_classifier import classify_risk_level

        result = classify_risk_level("Opaque", data_keys=["ACCESS_TOKEN"])

        assert result == "medium"

    def test_opaque_with_plain_config_keys_is_low(self) -> None:
        from hexawyn.domain.services.secret_rotation.risk_classifier import classify_risk_level

        result = classify_risk_level("Opaque", data_keys=["LOG_LEVEL", "FEATURE_FLAG"])

        assert result == "low"

    def test_key_matching_is_case_insensitive(self) -> None:
        from hexawyn.domain.services.secret_rotation.risk_classifier import classify_risk_level

        result = classify_risk_level("Opaque", data_keys=["database_url"])

        assert result == "critical"

    def test_no_keys_is_low(self) -> None:
        from hexawyn.domain.services.secret_rotation.risk_classifier import classify_risk_level

        result = classify_risk_level("Opaque", data_keys=[])

        assert result == "low"
