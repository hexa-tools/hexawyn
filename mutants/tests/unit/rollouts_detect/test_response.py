from __future__ import annotations

from hexawyn.application.use_case.workloads.rollouts_detect.response import (
    RolloutsDetectResponse,
)


class TestRolloutsDetectResponse:
    def test_default_values(self) -> None:
        response = RolloutsDetectResponse()

        assert response.installed is False
        assert response.version is None
        assert response.namespace is None
        assert response.total_rollouts == 0
        assert response.healthy == 0
        assert response.progressing == 0
        assert response.degraded == 0
        assert response.paused == 0
        assert response.error is None

    def test_full_values(self) -> None:
        response = RolloutsDetectResponse(
            installed=True,
            version="1.6",
            namespace="argo-rollouts",
            total_rollouts=5,
            healthy=3,
            progressing=1,
            degraded=1,
            paused=0,
            error=None,
        )

        assert response.installed is True
        assert response.version == "1.6"
        assert response.total_rollouts == 5  # noqa: PLR2004
        assert response.healthy == 3  # noqa: PLR2004
