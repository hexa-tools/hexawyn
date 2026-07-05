from __future__ import annotations

from abc import ABC

import pytest


class TestManualChangeOutsideGitOpsServicePort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_service_port import (
            ManualChangeOutsideGitOpsServicePort,
        )

        assert issubclass(ManualChangeOutsideGitOpsServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driving.manual_change_outside_gitops.manual_change_outside_gitops_service_port import (
            ManualChangeOutsideGitOpsServicePort,
        )

        with pytest.raises(TypeError):
            ManualChangeOutsideGitOpsServicePort()  # type: ignore[abstract]
