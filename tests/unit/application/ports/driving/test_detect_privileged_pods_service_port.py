from __future__ import annotations

from abc import ABC

import pytest


class TestDetectPrivilegedPodsServicePort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_service_port import (
            DetectPrivilegedPodsServicePort,
        )

        assert issubclass(DetectPrivilegedPodsServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_service_port import (
            DetectPrivilegedPodsServicePort,
        )

        with pytest.raises(TypeError):
            DetectPrivilegedPodsServicePort()  # type: ignore[abstract]
