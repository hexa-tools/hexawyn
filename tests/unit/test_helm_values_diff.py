from dataclasses import fields


class TestValueDiff:
    def test_is_frozen_dataclass_with_expected_fields(self) -> None:
        from hexawyn.domain.models.helm_values_diff import ValueDiff

        field_names = {f.name for f in fields(ValueDiff)}

        assert field_names == {
            "key_path",
            "source_value",
            "target_value",
            "change_type",
            "severity",
            "is_secret",
            "type_mismatch",
            "suggestion",
        }

    def test_holds_values(self) -> None:
        from hexawyn.domain.models.helm_values_diff import ValueDiff

        diff = ValueDiff(
            key_path="image.tag",
            source_value="v1.3",
            target_value="v1.2",
            change_type="changed",
            severity="critical",
            is_secret=False,
            type_mismatch=False,
            suggestion="Different code is running between environments.",
        )

        assert diff.key_path == "image.tag"
        assert diff.change_type == "changed"
        assert diff.severity == "critical"


class TestHelmValuesDiffReport:
    def test_defaults_to_in_sync_empty(self) -> None:
        from hexawyn.domain.models.helm_values_diff import HelmValuesDiffReport

        report = HelmValuesDiffReport(
            release="payment-service", source_env="staging", target_env="production"
        )

        assert report.release == "payment-service"
        assert report.source_env == "staging"
        assert report.target_env == "production"
        assert report.critical == []
        assert report.warning == []
        assert report.informational == []
        assert report.total_differences == 0
        assert report.in_sync is True

    def test_holds_grouped_diffs(self) -> None:
        from hexawyn.domain.models.helm_values_diff import HelmValuesDiffReport, ValueDiff

        critical = ValueDiff(
            key_path="image.tag",
            source_value="v1.3",
            target_value="v1.2",
            change_type="changed",
            severity="critical",
            is_secret=False,
            type_mismatch=False,
            suggestion="",
        )
        report = HelmValuesDiffReport(
            release="payment-service",
            source_env="staging",
            target_env="production",
            critical=[critical],
            total_differences=1,
            in_sync=False,
        )

        assert report.critical[0].key_path == "image.tag"
        assert report.in_sync is False
