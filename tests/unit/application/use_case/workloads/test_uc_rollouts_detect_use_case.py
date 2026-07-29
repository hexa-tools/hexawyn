from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.workloads.rollouts_detect.command import (
    RolloutsDetectCommand,
)
from hexawyn.application.use_case.workloads.rollouts_detect.response import (
    RolloutsDetectResponse,
)
from hexawyn.application.use_case.workloads.rollouts_detect.rollouts_detect_use_case import (
    RolloutsDetectUseCase,
)


class TestRolloutsDetectUseCase:
    def test_execute_returns_response(self) -> None:
        result_mock = MagicMock()
        result_mock.installed = False
        result_mock.version = None
        result_mock.namespace = None
        result_mock.total_rollouts = 0
        result_mock.healthy = 0
        result_mock.progressing = 0
        result_mock.degraded = 0
        result_mock.paused = 0

        port = MagicMock()
        port.detect_rollouts.return_value = result_mock

        use_case = RolloutsDetectUseCase(rollouts_port=port)
        result = use_case.execute(RolloutsDetectCommand())

        assert isinstance(result, RolloutsDetectResponse)
        assert result.installed is False
        assert result.total_rollouts == 0

    def test_execute_installed(self) -> None:
        result_mock = MagicMock()
        result_mock.installed = True
        result_mock.version = "1.6"
        result_mock.namespace = "argo-rollouts"
        total_rollouts = 3
        result_mock.total_rollouts = total_rollouts
        result_mock.healthy = 1
        result_mock.progressing = 1
        result_mock.degraded = 1
        result_mock.paused = 0

        port = MagicMock()
        port.detect_rollouts.return_value = result_mock

        use_case = RolloutsDetectUseCase(rollouts_port=port)
        result = use_case.execute(RolloutsDetectCommand())

        assert result.installed is True
        assert result.version == "1.6"
        assert result.total_rollouts == total_rollouts
        assert result.healthy == 1
        assert result.degraded == 1
