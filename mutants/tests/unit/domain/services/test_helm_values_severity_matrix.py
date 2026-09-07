from __future__ import annotations


class TestCriticalKeys:
    def test_image_tag_is_critical(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import classify_severity

        assert classify_severity("image.tag") == "critical"

    def test_image_repository_is_critical(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import classify_severity

        assert classify_severity("image.repository") == "critical"

    def test_nested_image_tag_is_critical(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import classify_severity

        assert classify_severity("payment.image.tag") == "critical"

    def test_secret_key_is_critical(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import classify_severity

        assert classify_severity("database.secretKey") == "critical"

    def test_rbac_key_is_critical(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import classify_severity

        assert classify_severity("rbac.create") == "critical"


class TestWarningKeys:
    def test_replica_count_is_warning(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import classify_severity

        assert classify_severity("replicaCount") == "warning"

    def test_replicas_is_warning(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import classify_severity

        assert classify_severity("replicas") == "warning"

    def test_resource_limits_is_warning(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import classify_severity

        assert classify_severity("resources.limits.memory") == "warning"

    def test_resource_requests_is_warning(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import classify_severity

        assert classify_severity("resources.requests.cpu") == "warning"

    def test_feature_flag_is_warning(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import classify_severity

        assert classify_severity("featureFlags.newUi") == "warning"


class TestInformationalKeys:
    def test_logging_level_is_informational(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import classify_severity

        assert classify_severity("logging.level") == "informational"

    def test_unknown_key_defaults_to_informational(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import classify_severity

        assert classify_severity("annotations.team") == "informational"


class TestSecretDetection:
    def test_secret_keys_detected(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import is_secret_key

        assert is_secret_key("database.password") is True
        assert is_secret_key("api.secretKey") is True
        assert is_secret_key("auth.token") is True
        assert is_secret_key("tls.privateKey") is True

    def test_non_secret_keys_not_detected(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import is_secret_key

        assert is_secret_key("image.tag") is False
        assert is_secret_key("replicaCount") is False

    def test_case_insensitive(self) -> None:
        from hexawyn.domain.services.helm_values_diff.severity_matrix import is_secret_key

        assert is_secret_key("db.PASSWORD") is True
