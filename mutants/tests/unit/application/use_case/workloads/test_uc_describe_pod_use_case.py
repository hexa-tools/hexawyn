from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.workloads.describe_pod.command import (
    DescribePodCommand,
)
from hexawyn.application.use_case.workloads.describe_pod.describe_pod_use_case import (
    DescribePodUseCase,
)
from hexawyn.application.use_case.workloads.describe_pod.response import (
    DescribePodResponse,
)


class TestDescribePodUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_pods.return_value = []
        use_case = DescribePodUseCase(k8s_port=port)
        result = use_case.execute(DescribePodCommand())
        assert isinstance(result, DescribePodResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.list_pods.return_value = []
        use_case = DescribePodUseCase(k8s_port=port)
        result = use_case.execute(DescribePodCommand())
        assert isinstance(result, DescribePodResponse)

    def test_execute_finds_pod_by_name(self) -> None:
        port = MagicMock()
        port.list_pods.return_value = [
            {
                "name": "my-nginx",
                "namespace": "default",
                "status": "Running",
                "restarts": 3,
                "node": "node-1",
                "age": "5d",
            },
        ]

        use_case = DescribePodUseCase(k8s_port=port)
        result = use_case.execute(DescribePodCommand(pod_name="my-nginx", namespace="default"))

        assert result.pod_name == "my-nginx"
        assert result.status == "Running"
        assert result.restarts == 3  # noqa: PLR2004

    def test_execute_pod_not_found_returns_not_found_status(self) -> None:
        port = MagicMock()
        port.list_pods.return_value = [
            {"name": "other-pod", "namespace": "default", "status": "Running"},
        ]

        use_case = DescribePodUseCase(k8s_port=port)
        result = use_case.execute(DescribePodCommand(pod_name="missing-pod", namespace="default"))

        assert result.status == "NotFound"
