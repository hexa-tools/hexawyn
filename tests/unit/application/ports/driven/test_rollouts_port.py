from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.rollouts_port import RolloutsPort


class TestRolloutsPort:
    def test_is_abstract(self) -> None:
        assert issubclass(RolloutsPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            RolloutsPort()  # type: ignore[abstract]

    def test_has_detect_rollouts(self) -> None:
        method = RolloutsPort.detect_rollouts
        assert getattr(method, "__isabstractmethod__", False)

    def test_has_list_rollouts(self) -> None:
        method = RolloutsPort.list_rollouts
        assert getattr(method, "__isabstractmethod__", False)

    def test_has_get_rollout(self) -> None:
        method = RolloutsPort.get_rollout
        assert getattr(method, "__isabstractmethod__", False)

    def test_has_list_analysis_runs(self) -> None:
        method = RolloutsPort.list_analysis_runs
        assert getattr(method, "__isabstractmethod__", False)
