from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.keda_port import KedaPort


class TestKedaPort:
    def test_is_abstract(self) -> None:
        assert issubclass(KedaPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            KedaPort()  # type: ignore[abstract]

    def test_has_methods(self) -> None:
        for name in [
            "detect",
            "list_scaledobjects",
            "get_scaledobject",
            "list_trigger_auths",
            "get_trigger_auth",
            "list_scaledjobs",
            "get_scaledjob",
        ]:
            assert getattr(getattr(KedaPort, name), "__isabstractmethod__", False)
