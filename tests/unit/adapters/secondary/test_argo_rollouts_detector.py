from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.gitops.argo_rollouts_detector import ArgoRolloutsDetector
from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.domain.errors import ArgoRolloutsNotFoundError


class TestArgoRolloutsDetector:
    def test_implements_port(self) -> None:
        assert isinstance(ArgoRolloutsDetector(), RolloutsPort)

    def test_detect_rollouts(self) -> None:
        detector = ArgoRolloutsDetector()
        result = detector.detect_rollouts()
        assert result.installed is False
        assert result.total_rollouts == 0

    def test_list_rollouts_raises(self) -> None:
        with pytest.raises(ArgoRolloutsNotFoundError):
            ArgoRolloutsDetector().list_rollouts()

    def test_get_rollout_raises(self) -> None:
        with pytest.raises(ArgoRolloutsNotFoundError):
            ArgoRolloutsDetector().get_rollout("name", "ns")

    def test_list_analysis_runs_raises(self) -> None:
        with pytest.raises(ArgoRolloutsNotFoundError):
            ArgoRolloutsDetector().list_analysis_runs()
