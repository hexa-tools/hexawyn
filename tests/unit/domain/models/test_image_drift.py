"""Unit tests for the Container Image Drift Detection domain models."""

from __future__ import annotations

import dataclasses

import pytest


class TestImageReference:
    def test_creates_reference_with_all_fields(self) -> None:
        from hexawyn.domain.models.image_drift import ImageReference

        ref = ImageReference(repository="payment", tag="v1.2", digest=None)

        assert ref.repository == "payment"
        assert ref.tag == "v1.2"
        assert ref.digest is None

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.image_drift import ImageReference

        ref = ImageReference(repository="payment", tag="v1.2", digest=None)

        with pytest.raises(dataclasses.FrozenInstanceError):
            ref.tag = "v1.3"  # type: ignore[misc]


class TestContainerImageDrift:
    def test_creates_drift_with_expected_fields(self) -> None:
        from hexawyn.domain.models.image_drift import ContainerImageDrift

        drift = ContainerImageDrift(
            deployment="payment-service",
            namespace="production",
            container="payment-app",
            running_image="payment:v1.3-hotfix",
            declared_image="payment:v1.2",
            source_of_truth="helm-release:payment-chart",
            drift_type="tag_mismatch",
            severity="critical",
        )

        assert drift.deployment == "payment-service"
        assert drift.namespace == "production"
        assert drift.container == "payment-app"
        assert drift.running_image == "payment:v1.3-hotfix"
        assert drift.declared_image == "payment:v1.2"
        assert drift.source_of_truth == "helm-release:payment-chart"
        assert drift.drift_type == "tag_mismatch"
        assert drift.severity == "critical"

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.image_drift import ContainerImageDrift

        drift = ContainerImageDrift(
            deployment="d",
            namespace="n",
            container="c",
            running_image="a:1",
            declared_image="a:2",
            source_of_truth="helm-release:x",
            drift_type="tag_mismatch",
            severity="critical",
        )

        with pytest.raises(dataclasses.FrozenInstanceError):
            drift.severity = "critical"  # type: ignore[misc]


class TestContainerImageDriftRequest:
    def test_defaults_kustomize_paths_to_empty_list(self) -> None:
        from hexawyn.domain.models.image_drift import ContainerImageDriftRequest

        request = ContainerImageDriftRequest(namespace="production")

        assert request.namespace == "production"
        assert request.kustomize_paths == []

    def test_accepts_custom_kustomize_paths(self) -> None:
        from hexawyn.domain.models.image_drift import ContainerImageDriftRequest

        request = ContainerImageDriftRequest(
            namespace="production", kustomize_paths=["overlays/production"]
        )

        assert request.kustomize_paths == ["overlays/production"]


class TestContainerImageDriftReport:
    def test_creates_report_with_expected_fields(self) -> None:
        from hexawyn.domain.models.image_drift import (
            ContainerImageDrift,
            ContainerImageDriftReport,
        )

        drift = ContainerImageDrift(
            deployment="payment-service",
            namespace="production",
            container="payment-app",
            running_image="payment:v1.3-hotfix",
            declared_image="payment:v1.2",
            source_of_truth="helm-release:payment-chart",
            drift_type="tag_mismatch",
            severity="critical",
        )
        report = ContainerImageDriftReport(
            out_of_sync=[drift],
            in_sync_count=38,
            excluded_count=1,
            total_checked=39,
            summary="1 out of sync.",
        )

        assert report.out_of_sync == [drift]
        assert report.in_sync_count == 38
        assert report.excluded_count == 1
        assert report.total_checked == 39
        assert report.summary == "1 out of sync."
