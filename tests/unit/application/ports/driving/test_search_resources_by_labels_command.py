from __future__ import annotations

from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_command import (
    SearchResourcesByLabelsCommand,
)


class TestSearchResourcesByLabelsCommand:
    def test_defaults(self) -> None:
        cmd = SearchResourcesByLabelsCommand(label_selector="app=payment")
        assert cmd.resource_types == ["pods", "deployments", "services", "configmaps"]
        assert cmd.namespace is None

    def test_explicit_values(self) -> None:
        cmd = SearchResourcesByLabelsCommand(
            label_selector="app=payment", resource_types=["pods"], namespace="production"
        )
        assert cmd.resource_types == ["pods"]
        assert cmd.namespace == "production"
