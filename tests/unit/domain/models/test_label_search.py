"""Unit tests for label-search domain models (pure dataclasses)."""

from __future__ import annotations

from hexawyn.domain.models.label_search import (
    LabelSearchRequest,
    LabelSearchResult,
    MatchedResourceResult,
    NamespaceGroup,
)


class TestMatchedResourceResult:
    def test_pod_fields(self) -> None:
        resource = MatchedResourceResult(
            name="payment-pod-abc12",
            namespace="production",
            kind="pod",
            node="worker-1",
            phase="Running",
            ready=True,
            is_healthy=True,
            labels={"app": "payment", "env": "production"},
        )
        assert resource.node == "worker-1"
        assert resource.ready is True

    def test_non_pod_fields_default_to_none(self) -> None:
        resource = MatchedResourceResult(
            name="payment-service",
            namespace="production",
            kind="service",
            node=None,
            phase=None,
            ready=None,
            is_healthy=True,
            labels={"app": "payment"},
        )
        assert resource.node is None
        assert resource.phase is None
        assert resource.ready is None


class TestNamespaceGroup:
    def test_fields(self) -> None:
        resource = MatchedResourceResult(
            name="payment-pod-abc12",
            namespace="production",
            kind="pod",
            node="worker-1",
            phase="Running",
            ready=True,
            is_healthy=True,
            labels={},
        )
        group = NamespaceGroup(namespace="production", resources=[resource])
        assert group.namespace == "production"
        assert len(group.resources) == 1


class TestLabelSearchRequest:
    def test_defaults(self) -> None:
        request = LabelSearchRequest(label_selector="app=payment")
        assert request.resource_types == ["pods", "deployments", "services", "configmaps"]
        assert request.namespace is None

    def test_custom_values(self) -> None:
        request = LabelSearchRequest(
            label_selector="app=payment", resource_types=["pods"], namespace="production"
        )
        assert request.resource_types == ["pods"]
        assert request.namespace == "production"


class TestLabelSearchResult:
    def test_defaults(self) -> None:
        result = LabelSearchResult(label_selector="app=payment", total_matched=0)
        assert result.groups == []
        assert result.has_more is False
        assert result.remaining_count == 0
        assert result.no_matches is False
        assert result.summary == ""

    def test_with_groups(self) -> None:
        resource = MatchedResourceResult(
            name="payment-pod-abc12",
            namespace="production",
            kind="pod",
            node="worker-1",
            phase="Running",
            ready=True,
            is_healthy=True,
            labels={},
        )
        group = NamespaceGroup(namespace="production", resources=[resource])
        result = LabelSearchResult(label_selector="app=payment", total_matched=1, groups=[group])
        assert len(result.groups) == 1
        assert result.groups[0].namespace == "production"
