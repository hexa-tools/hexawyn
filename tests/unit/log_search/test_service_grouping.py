"""Unit tests for derive_service_name / group_by_service — pure grouping logic."""

from __future__ import annotations

from hexawyn.domain.models.log_search import PodLogMatch
from hexawyn.domain.services.log_search.service_grouping import (
    derive_service_name,
    group_by_service,
)


class TestDeriveServiceName:
    def test_deployment_style_pod_name(self) -> None:
        assert derive_service_name("payment-worker-7d8f9c6b5-abc12") == "payment-worker"

    def test_statefulset_style_pod_name(self) -> None:
        assert derive_service_name("postgres-0") == "postgres"

    def test_no_dash_pod_name_returned_as_is(self) -> None:
        assert derive_service_name("standalone") == "standalone"


class TestGroupByService:
    def test_groups_multiple_pods_into_two_services(self) -> None:
        """TC1: pattern found in 3 pods from 2 different deployments."""
        matches = [
            PodLogMatch(
                pod_name="checkout-pod-7d8f9-abc12",
                namespace="production",
                container="checkout-app",
            ),
            PodLogMatch(
                pod_name="checkout-pod-7d8f9-def34",
                namespace="production",
                container="checkout-app",
            ),
            PodLogMatch(
                pod_name="payment-pod-9a1b2-ghi56",
                namespace="production",
                container="payment-worker",
            ),
        ]

        groups = group_by_service(matches)

        assert len(groups) == 2
        by_service = {group.service_name: group for group in groups}
        assert len(by_service["checkout-pod"].pods) == 2
        assert len(by_service["payment-pod"].pods) == 1

    def test_groups_sorted_by_namespace_then_service(self) -> None:
        matches = [
            PodLogMatch(pod_name="zeta-svc-abc-123", namespace="staging", container="app"),
            PodLogMatch(pod_name="alpha-svc-abc-123", namespace="production", container="app"),
        ]

        groups = group_by_service(matches)

        assert [(g.namespace, g.service_name) for g in groups] == [
            ("production", "alpha-svc"),
            ("staging", "zeta-svc"),
        ]

    def test_empty_input_returns_empty_list(self) -> None:
        assert group_by_service([]) == []
