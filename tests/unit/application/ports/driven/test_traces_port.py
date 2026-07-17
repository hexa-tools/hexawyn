from abc import ABC

import pytest
from hexawyn.application.ports.driven.traces_port import TracesPort


class TestTracesPort:
    def test_is_abstract(self):
        assert issubclass(TracesPort, ABC)

    def test_cannot_instantiate_directly(self):
        with pytest.raises(TypeError):
            TracesPort()
