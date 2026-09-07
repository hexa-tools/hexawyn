"""Unit tests for is_internal_load_balancer. Edge Case 5 / Checker case 3:
a service with a cloud-provider internal-LoadBalancer annotation is not
actually public, regardless of its type being LoadBalancer."""

from __future__ import annotations

_ANNOTATIONS = (
    ("service.beta.kubernetes.io/aws-load-balancer-internal", "true"),
    ("networking.gke.io/load-balancer-type", "Internal"),
)


class TestIsInternalLoadBalancer:
    def test_aws_internal_annotation_matches(self) -> None:
        from hexawyn.domain.services.external_exposure.internal_exposure_detector import (
            is_internal_load_balancer,
        )

        annotations = {"service.beta.kubernetes.io/aws-load-balancer-internal": "true"}

        assert is_internal_load_balancer(annotations, _ANNOTATIONS) is True

    def test_gke_internal_annotation_matches(self) -> None:
        from hexawyn.domain.services.external_exposure.internal_exposure_detector import (
            is_internal_load_balancer,
        )

        annotations = {"networking.gke.io/load-balancer-type": "Internal"}

        assert is_internal_load_balancer(annotations, _ANNOTATIONS) is True

    def test_wrong_value_does_not_match(self) -> None:
        from hexawyn.domain.services.external_exposure.internal_exposure_detector import (
            is_internal_load_balancer,
        )

        annotations = {"service.beta.kubernetes.io/aws-load-balancer-internal": "false"}

        assert is_internal_load_balancer(annotations, _ANNOTATIONS) is False

    def test_no_annotations_does_not_match(self) -> None:
        from hexawyn.domain.services.external_exposure.internal_exposure_detector import (
            is_internal_load_balancer,
        )

        assert is_internal_load_balancer({}, _ANNOTATIONS) is False
