from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort


class TestPodLogWatchPort:
    def test_is_abstract(self) -> None:
        assert issubclass(PodLogWatchPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            PodLogWatchPort()  # type: ignore[abstract]
