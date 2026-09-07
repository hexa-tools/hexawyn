"""Unit tests for group_by_namespace — pure aggregation, no I/O."""

from __future__ import annotations

from hexawyn.domain.models.label_search import MatchedResourceResult
from hexawyn.domain.services.label_search.resource_grouping import group_by_namespace


def _resource(name: str, namespace: str, kind: str = "pod") -> MatchedResourceResult:
    return MatchedResourceResult(
        name=name,
        namespace=namespace,
        kind=kind,  # type: ignore[arg-type]
        node="worker-1" if kind == "pod" else None,
        phase="Running" if kind == "pod" else None,
        ready=True if kind == "pod" else None,
        is_healthy=True,
        labels={},
    )


class TestGroupByNamespace:
    def test_groups_resources_by_namespace(self) -> None:
        resources = [
            _resource("payment-pod-abc12", "production"),
            _resource("payment-pod-def34", "staging"),
            _resource("payment-pod-ghi56", "production"),
        ]

        groups = group_by_namespace(resources)

        assert len(groups) == 2  # noqa: PLR2004
        by_ns = {group.namespace: group for group in groups}
        assert len(by_ns["production"].resources) == 2  # noqa: PLR2004
        assert len(by_ns["staging"].resources) == 1

    def test_groups_sorted_by_namespace_name(self) -> None:
        resources = [_resource("pod-a", "zeta"), _resource("pod-b", "alpha")]

        groups = group_by_namespace(resources)

        assert [group.namespace for group in groups] == ["alpha", "zeta"]

    def test_resources_within_group_sorted_by_kind_then_name(self) -> None:
        resources = [
            _resource("web-svc", "production", kind="service"),
            _resource("zpod", "production", kind="pod"),
            _resource("apod", "production", kind="pod"),
        ]

        groups = group_by_namespace(resources)

        names = [resource.name for resource in groups[0].resources]
        assert names == ["apod", "zpod", "web-svc"]

    def test_empty_input_returns_empty_list(self) -> None:
        assert group_by_namespace([]) == []
