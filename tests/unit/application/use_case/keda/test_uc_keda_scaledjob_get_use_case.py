from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.keda.keda_scaledjob_get.command import (
    KedaScaledjobGetCommand,
)
from hexawyn.application.use_case.keda.keda_scaledjob_get.keda_scaledjob_get_use_case import (  # noqa: E501
    KedaScaledjobGetUseCase,
)
from hexawyn.application.use_case.keda.keda_scaledjob_get.response import (
    KedaScaledjobGetResponse,
)


class TestKedaScaledjobGetUseCase:
    def test_execute_returns_response(self) -> None:
        job = MagicMock()
        job.name = "my-job"
        job.namespace = "default"
        job.phase = MagicMock()
        job.phase.value = "Ready"
        job.successful_jobs = 3
        job.failed_jobs = 1
        job.last_execution_time = "2025-01-15T10:00:00Z"
        job.job_target_ref = "Deployment/worker"
        job.cooldown_period_seconds = 300
        job.max_replica_count = 1
        job.message = None

        port = MagicMock()
        port.get_scaledjob.return_value = job

        use_case = KedaScaledjobGetUseCase(port=port)
        result = use_case.execute(KedaScaledjobGetCommand(name="my-job", namespace="default"))

        assert isinstance(result, KedaScaledjobGetResponse)
        assert result.name == "my-job"
        assert result.phase == "Ready"

    def test_execute_failed_job(self) -> None:
        job = MagicMock()
        job.name = "failed"
        job.namespace = "default"
        job.phase = MagicMock()
        job.phase.value = "Failed"
        job.successful_jobs = 0
        job.failed_jobs = 5
        job.last_execution_time = None
        job.job_target_ref = ""
        job.cooldown_period_seconds = 0
        job.max_replica_count = 0
        job.message = "error"

        port = MagicMock()
        port.get_scaledjob.return_value = job

        use_case = KedaScaledjobGetUseCase(port=port)
        result = use_case.execute(KedaScaledjobGetCommand(name="failed", namespace="default"))

        assert result.phase == "Failed"
