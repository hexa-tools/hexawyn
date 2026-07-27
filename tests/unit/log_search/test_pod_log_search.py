"""Unit tests for search_pod_logs — pure domain orchestration.

Test data mirrors the ticket's own fixture: pattern "connection refused to postgres",
checkout-pod-xyz (production, checkout-app) and payment-pod-abc (production, payment-worker).
"""

from __future__ import annotations

from hexawyn.application.ports.driven.log_search_port import RawContainerLog, RawPodLogData
from hexawyn.domain.models.log_search import (
    LogSearchRequest,
    SkippedNamespace,
    SkippedPod,
)
from hexawyn.domain.services.log_search.pod_log_search import search_pod_logs


def _container_log(container: str, lines: list[str], truncated: bool = False) -> RawContainerLog:
    return RawContainerLog(container=container, lines=lines, truncated=truncated)


def _pod_data(pod_name: str, namespace: str, containers: list[RawContainerLog]) -> RawPodLogData:
    return RawPodLogData(pod_name=pod_name, namespace=namespace, containers=containers)


def _request(pattern: str = "connection refused to postgres") -> LogSearchRequest:
    return LogSearchRequest(pattern=pattern, time_window_minutes=60)


class TestPatternFoundAcrossDeployments:
    """TC1: pattern found in 3 pods from 2 different deployments → grouped result."""

    def test_grouped_by_service_with_correct_counts(self) -> None:
        raw_pod_logs = [
            _pod_data(
                "checkout-pod-7d8f9-abc12",
                "production",
                [
                    _container_log(
                        "checkout-app",
                        ["2024-01-01T10:32:15Z ERROR: connection refused to postgres"],
                    )
                ],
            ),
            _pod_data(
                "checkout-pod-7d8f9-def34",
                "production",
                [
                    _container_log(
                        "checkout-app",
                        ["2024-01-01T10:33:00Z ERROR: connection refused to postgres"],
                    )
                ],
            ),
            _pod_data(
                "payment-pod-9a1b2-ghi56",
                "production",
                [
                    _container_log(
                        "payment-worker",
                        ["2024-01-01T10:34:00Z FATAL: connection refused to postgres - retrying"],
                    )
                ],
            ),
        ]

        result = search_pod_logs(
            _request(),
            raw_pod_logs,
            skipped_pods=[],
            skipped_namespaces=[],
            scanned_namespaces=["production"],
            namespaces_total=1,
        )

        assert result.pods_affected == 3  # noqa: PLR2004
        assert result.services_affected == 2  # noqa: PLR2004
        assert len(result.groups) == 2  # noqa: PLR2004
        assert result.no_matches is False


class TestNoMatches:
    """TC2: pattern not found in any pod → clear 'no matches' message."""

    def test_empty_result_with_message(self) -> None:
        raw_pod_logs = [
            _pod_data(
                "checkout-pod-abc12", "production", [_container_log("checkout-app", ["all good"])]
            )
        ]

        result = search_pod_logs(
            _request(),
            raw_pod_logs,
            skipped_pods=[],
            skipped_namespaces=[],
            scanned_namespaces=["production"],
            namespaces_total=1,
        )

        assert result.no_matches is True
        assert result.pods_affected == 0
        assert "connection refused to postgres" in result.summary


class TestMultipleContainersSamePod:
    """TC4: pattern matches in multiple containers of the same pod → each container listed."""

    def test_each_container_produces_its_own_match(self) -> None:
        raw_pod_logs = [
            _pod_data(
                "checkout-pod-abc12",
                "production",
                [
                    _container_log("app", ["connection refused to postgres"]),
                    _container_log("sidecar", ["connection refused to postgres (proxy)"]),
                ],
            )
        ]

        result = search_pod_logs(
            _request(),
            raw_pod_logs,
            skipped_pods=[],
            skipped_namespaces=[],
            scanned_namespaces=["production"],
            namespaces_total=1,
        )

        containers = {pod.container for group in result.groups for pod in group.pods}
        assert containers == {"app", "sidecar"}
        assert result.pods_affected == 1


class TestSkipTracking:
    def test_skipped_pods_and_namespaces_passed_through(self) -> None:
        skipped_pods = [
            SkippedPod(
                pod_name="pending-pod", namespace="staging", reason="Pending: no logs available"
            )
        ]
        skipped_namespaces = [SkippedNamespace(namespace="kube-system", reason="RBAC denied")]

        result = search_pod_logs(
            _request(),
            raw_pod_logs=[],
            skipped_pods=skipped_pods,
            skipped_namespaces=skipped_namespaces,
            scanned_namespaces=["production", "staging"],
            namespaces_total=3,
        )

        assert result.skipped_pods == skipped_pods
        assert result.skipped_namespaces == skipped_namespaces
        assert result.scanned_namespaces == ["production", "staging"]
        assert result.namespaces_total == 3  # noqa: PLR2004


class TestEmptyInput:
    def test_no_pods_returns_no_matches(self) -> None:
        result = search_pod_logs(
            _request(),
            raw_pod_logs=[],
            skipped_pods=[],
            skipped_namespaces=[],
            scanned_namespaces=[],
            namespaces_total=0,
        )

        assert result.no_matches is True
        assert result.groups == []
