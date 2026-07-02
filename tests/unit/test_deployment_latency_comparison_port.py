from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
    DeploymentLatencyComparisonPort,
)


class TestDeploymentLatencyComparisonPort:
    def test_is_abstract(self) -> None:
        assert issubclass(DeploymentLatencyComparisonPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            DeploymentLatencyComparisonPort()  # type: ignore[abstract]
