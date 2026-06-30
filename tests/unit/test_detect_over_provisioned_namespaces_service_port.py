"""Tests for DetectOverProvisionedNamespacesServicePort (abstract contract)."""

import pytest
from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_service_port import (
    DetectOverProvisionedNamespacesServicePort,
)


class TestDetectOverProvisionedNamespacesServicePort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(DetectOverProvisionedNamespacesServicePort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            DetectOverProvisionedNamespacesServicePort()  # type: ignore[abstract]
