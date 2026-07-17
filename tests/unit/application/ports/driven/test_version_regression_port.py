from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.version_regression_port import VersionRegressionPort


class TestVersionRegressionPort:
    def test_is_abstract(self) -> None:
        assert issubclass(VersionRegressionPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            VersionRegressionPort()  # type: ignore[abstract]
