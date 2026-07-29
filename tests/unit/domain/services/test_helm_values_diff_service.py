from __future__ import annotations


class TestGroupingAndSummary:
    def test_identical_values_are_in_sync(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        values = {"image": {"tag": "v1.3"}, "replicaCount": 3}
        report = HelmValuesDiffService().diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values=values,
            target_values=dict(values),
        )

        assert report.in_sync is True
        assert report.total_differences == 0

    def test_groups_by_severity(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        report = HelmValuesDiffService().diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={
                "image": {"tag": "v1.3"},
                "replicaCount": 1,
                "logging": {"level": "DEBUG"},
            },
            target_values={
                "image": {"tag": "v1.2"},
                "replicaCount": 3,
                "logging": {"level": "INFO"},
            },
        )

        assert report.in_sync is False
        assert report.total_differences == 3  # noqa: PLR2004
        assert [d.key_path for d in report.critical] == ["image.tag"]
        assert [d.key_path for d in report.warning] == ["replicaCount"]
        assert [d.key_path for d in report.informational] == ["logging.level"]


class TestDirectionality:
    def test_source_is_staging_target_is_production(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        report = HelmValuesDiffService().diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={"image": {"tag": "v1.3"}},
            target_values={"image": {"tag": "v1.2"}},
        )

        diff = report.critical[0]
        assert diff.source_value == "v1.3"
        assert diff.target_value == "v1.2"


class TestSecretRedaction:
    def test_secret_values_are_redacted(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        report = HelmValuesDiffService().diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={"database": {"password": "s3cr3t-staging"}},
            target_values={"database": {"password": "s3cr3t-prod"}},
        )

        diff = report.critical[0]
        assert diff.is_secret is True
        assert diff.source_value == "[REDACTED]"
        assert diff.target_value == "[REDACTED]"
        assert "s3cr3t" not in diff.source_value
        assert "s3cr3t" not in diff.target_value


class TestTypeMismatchSuggestion:
    def test_type_mismatch_gets_suggestion(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        report = HelmValuesDiffService().diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={"service": {"port": 8080}},
            target_values={"service": {"port": "8080"}},
        )

        diff = report.informational[0]
        assert diff.type_mismatch is True
        assert "type mismatch" in diff.suggestion.lower()


class TestSuggestions:
    def test_image_tag_suggestion_mentions_code(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        report = HelmValuesDiffService().diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={"image": {"tag": "v1.3"}},
            target_values={"image": {"tag": "v1.2"}},
        )

        assert report.critical[0].suggestion != ""

    def test_replica_suggestion_mentions_availability(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        report = HelmValuesDiffService().diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={"replicaCount": 1},
            target_values={"replicaCount": 3},
        )

        assert "availability" in report.warning[0].suggestion.lower()

    def test_added_key_reported(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        report = HelmValuesDiffService().diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={"featureFlags": {"newUi": True}},
            target_values={},
        )

        assert report.total_differences == 1
        assert report.warning[0].change_type == "removed"

    def test_resource_limits_suggestion_mentions_performance(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        report = HelmValuesDiffService().diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={"resources": {"limits": {"memory": "512Mi"}}},
            target_values={"resources": {"limits": {"memory": "1Gi"}}},
        )

        assert "performance" in report.warning[0].suggestion.lower()

    def test_added_key_only_in_target_reports_target_env(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        report = HelmValuesDiffService().diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={},
            target_values={"extraConfig": {"beta": "on"}},
        )

        diff = report.informational[0]
        assert diff.change_type == "added"
        assert "production" in diff.suggestion

    def test_generic_changed_value_fallback_suggestion(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        report = HelmValuesDiffService().diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={"annotations": {"team": "payments"}},
            target_values={"annotations": {"team": "billing"}},
        )

        diff = report.informational[0]
        assert "differs between staging and production" in diff.suggestion


class TestDiffAge:
    def test_critical_diff_older_than_seven_days_flagged(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        def age_provider(key_path: str) -> int | None:
            return 21 if key_path == "image.tag" else None

        report = HelmValuesDiffService(diff_age_provider=age_provider).diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={"image": {"tag": "v1.3"}},
            target_values={"image": {"tag": "v1.2"}},
        )

        assert "21 days" in report.critical[0].suggestion

    def test_no_age_provider_no_age_mention(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        report = HelmValuesDiffService().diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={"image": {"tag": "v1.3"}},
            target_values={"image": {"tag": "v1.2"}},
        )

        assert "days" not in report.critical[0].suggestion

    def test_recent_critical_diff_not_flagged_as_chronic(self) -> None:
        from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
            HelmValuesDiffService,
        )

        report = HelmValuesDiffService(diff_age_provider=lambda key_path: 2).diff(
            release="payment-service",
            source_env="staging",
            target_env="production",
            source_values={"image": {"tag": "v1.3"}},
            target_values={"image": {"tag": "v1.2"}},
        )

        assert "days" not in report.critical[0].suggestion
