from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort


class TestPodLogsPort:
    def test_is_abstract(self) -> None:
        assert issubclass(PodLogsPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            PodLogsPort()  # type: ignore[abstract]
