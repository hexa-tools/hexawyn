from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.cluster.search_resources_by_labels.command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.use_case.cluster.search_resources_by_labels.response import (
    SearchResourcesByLabelsResponse,
)
from hexawyn.application.use_case.cluster.search_resources_by_labels.search_resources_by_labels_use_case import (  # noqa: E501
    SearchResourcesByLabelsUseCase,
)
from hexawyn.domain.errors import ResourceNotFoundError


class TestSearchResourcesByLabelsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.search_by_labels.return_value = []
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]

        use_case = SearchResourcesByLabelsUseCase(port=port, k8s_port=k8s)
        result = use_case.execute(
            SearchResourcesByLabelsCommand(
                label_selector="app=nginx",
                resource_types=["Deployment"],
                namespace="default",
            )
        )

        assert isinstance(result, SearchResourcesByLabelsResponse)

    def test_execute_raises_for_unknown_namespace(self) -> None:
        port = MagicMock()
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]

        use_case = SearchResourcesByLabelsUseCase(port=port, k8s_port=k8s)

        with pytest.raises(
            ResourceNotFoundError,
            match="Namespace 'production' not found",
        ):
            use_case.execute(
                SearchResourcesByLabelsCommand(
                    namespace="production",
                    resource_types=["Deployment"],
                )
            )

    def test_execute_empty_results(self) -> None:
        port = MagicMock()
        port.search_by_labels.return_value = []
        k8s = MagicMock()
        k8s.list_namespaces.return_value = [
            {"name": "default", "status": "Active", "age": "30d"},
        ]

        use_case = SearchResourcesByLabelsUseCase(port=port, k8s_port=k8s)
        result = use_case.execute(
            SearchResourcesByLabelsCommand(
                label_selector="nonexistent=value",
                resource_types=["Deployment"],
                namespace="default",
            )
        )

        assert result.total_resources == 0

    def test_execute_searches_pods(self) -> None:
        port = MagicMock()
        port.search_pods.return_value = []
        k8s = MagicMock()

        use_case = SearchResourcesByLabelsUseCase(port=port, k8s_port=k8s)
        result = use_case.execute(
            SearchResourcesByLabelsCommand(label_selector="app=nginx", resource_types=["pods"])
        )

        assert isinstance(result, SearchResourcesByLabelsResponse)
        port.search_pods.assert_called_once()

    def test_execute_searches_deployments(self) -> None:
        port = MagicMock()
        port.search_deployments.return_value = []
        k8s = MagicMock()

        use_case = SearchResourcesByLabelsUseCase(port=port, k8s_port=k8s)
        result = use_case.execute(
            SearchResourcesByLabelsCommand(
                label_selector="app=nginx", resource_types=["deployments"]
            )
        )

        assert isinstance(result, SearchResourcesByLabelsResponse)
        port.search_deployments.assert_called_once()

    def test_execute_searches_services(self) -> None:
        port = MagicMock()
        port.search_services.return_value = []
        k8s = MagicMock()

        use_case = SearchResourcesByLabelsUseCase(port=port, k8s_port=k8s)
        result = use_case.execute(
            SearchResourcesByLabelsCommand(label_selector="app=nginx", resource_types=["services"])
        )

        assert isinstance(result, SearchResourcesByLabelsResponse)
        port.search_services.assert_called_once()

    def test_execute_with_matches_returns_groups(self) -> None:
        port = MagicMock()
        port.search_pods.return_value = [
            {
                "name": "nginx",
                "namespace": "default",
                "kind": "pod",
                "node": "node-1",
                "phase": "Running",
                "ready": True,
                "labels": {"app": "nginx"},
            }
        ]
        k8s = MagicMock()

        use_case = SearchResourcesByLabelsUseCase(port=port, k8s_port=k8s)
        result = use_case.execute(
            SearchResourcesByLabelsCommand(label_selector="app=nginx", resource_types=["pods"])
        )

        assert isinstance(result, SearchResourcesByLabelsResponse)
        assert len(result.groups) > 0
