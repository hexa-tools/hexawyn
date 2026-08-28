"""Tests for the CalicoDetect use case — maps port.detect() to a response."""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.calico.calico_detect.calico_detect_use_case import (
    CalicoDetectUseCase,
)
from hexawyn.application.use_case.calico.calico_detect.command import CalicoDetectCommand
from hexawyn.application.use_case.calico.calico_detect.response import CalicoDetectResponse
from hexawyn.domain.models.calico import DataplaneMode


class TestCalicoDetectUseCase:
    def _fill(self, response: MagicMock) -> MagicMock:
        response.installed = True
        response.status = "installed"
        response.not_installed_marker = None
        response.version = "v3.26.1"
        response.mode = DataplaneMode.IPIP
        response.namespace = "calico-system"
        response.tigera_operator = False
        response.enterprise = False
        response.agents = []
        response.total_nodes = 3
        response.ready_agents = 3
        response.degraded_agents = 0
        response.degraded_summary = None
        response.error = None
        return response

    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._fill(MagicMock())

        result = CalicoDetectUseCase(port=port).execute(CalicoDetectCommand())

        assert isinstance(result, CalicoDetectResponse)
        assert result.installed is True
        assert result.version == "v3.26.1"
        assert result.mode == DataplaneMode.IPIP
        assert result.total_nodes == 3  # noqa: PLR2004

    def test_execute_not_installed(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._fill(MagicMock())
        port.detect.return_value.installed = False
        port.detect.return_value.status = "not_installed"
        port.detect.return_value.not_installed_marker = "NOT_INSTALLED"

        result = CalicoDetectUseCase(port=port).execute(CalicoDetectCommand())

        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"

    def test_execute_surfaces_error(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._fill(MagicMock())
        port.detect.return_value.error = "boom"

        result = CalicoDetectUseCase(port=port).execute(CalicoDetectCommand())

        assert result.error == "boom"
