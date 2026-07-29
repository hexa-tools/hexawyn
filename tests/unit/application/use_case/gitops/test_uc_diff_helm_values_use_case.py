from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.gitops.diff_helm_values.diff_helm_values_use_case import (
    DiffHelmValuesUseCase,
)
from hexawyn.application.use_case.gitops.diff_helm_values.response import (
    DiffHelmValuesResponse,
)


class TestDiffHelmValuesUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_effective_values.return_value = {
            "release": "myapp",
            "namespace": "staging",
            "values": {},
        }

        command = MagicMock()
        command.release = "myapp"
        command.source_namespace = "staging"
        command.target_namespace = "production"
        command.source_env = "staging"
        command.target_env = "production"

        use_case = DiffHelmValuesUseCase(helm_values_port=port)
        result = use_case.execute(command)

        assert isinstance(result, DiffHelmValuesResponse)

    def test_execute_with_diffs(self) -> None:
        port = MagicMock()
        port.get_effective_values.side_effect = [
            {
                "release": "myapp",
                "namespace": "staging",
                "values": {"replicaCount": 2, "image": {"tag": "v1.2.0"}},
            },
            {
                "release": "myapp",
                "namespace": "production",
                "values": {"replicaCount": 3, "image": {"tag": "v1.1.0"}},
            },
        ]

        command = MagicMock()
        command.release = "myapp"
        command.source_namespace = "staging"
        command.target_namespace = "production"
        command.source_env = "staging"
        command.target_env = "production"

        use_case = DiffHelmValuesUseCase(helm_values_port=port)
        result = use_case.execute(command)

        assert isinstance(result, DiffHelmValuesResponse)
