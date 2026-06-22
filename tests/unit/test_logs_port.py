from abc import ABC

import pytest

from hexawyn.application.ports.driven.logs_port import LogsPort


class TestLogsPort:
    def test_is_abstract(self):
        assert issubclass(LogsPort, ABC)

    def test_cannot_instantiate_directly(self):
        with pytest.raises(TypeError):
            LogsPort()
