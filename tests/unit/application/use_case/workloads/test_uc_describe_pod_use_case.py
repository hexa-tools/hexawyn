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
