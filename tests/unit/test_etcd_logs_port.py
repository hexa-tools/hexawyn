from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.etcd_logs_port import ETCDLogsPort


class TestETCDLogsPort:
    def test_is_abstract(self) -> None:
        assert issubclass(ETCDLogsPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            ETCDLogsPort()  # type: ignore[abstract]
