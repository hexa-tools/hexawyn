"""Tests for DetectOverProvisionedNamespacesCommand — covered fully in test_detect_over_provisioned_namespaces_use_case.py."""

import pytest
from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_command import (
    DetectOverProvisionedNamespacesCommand,
)


class TestDetectOverProvisionedNamespacesCommand:
    def test_frozen_dataclass(self) -> None:
        cmd = DetectOverProvisionedNamespacesCommand()
        with pytest.raises(AttributeError):
            cmd.analysis_window_days = 14  # type: ignore[misc]

    def test_defaults(self) -> None:
        cmd = DetectOverProvisionedNamespacesCommand()
        assert cmd.analysis_window_days == 7
        assert cmd.top_n == 5
