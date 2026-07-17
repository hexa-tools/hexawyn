from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.watch_pod_logs.watch_pod_logs_service_port import (
    WatchPodLogsServicePort,
)


class TestWatchPodLogsServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(WatchPodLogsServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            WatchPodLogsServicePort()  # type: ignore[abstract]
