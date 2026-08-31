from __future__ import annotations

import pytest
from hexawyn.adapters.secondary.gitops.keda_detector import KedaDetector
from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.domain.errors import ComponentNotInstalledError


class TestKedaDetector:
    def test_implements_port(self) -> None:
        assert isinstance(KedaDetector(), KedaPort)

    def test_detect_not_installed(self) -> None:
        r = KedaDetector().detect()
        assert r.installed is False

    def test_list_scaledobjects_raises(self) -> None:
        with pytest.raises(ComponentNotInstalledError):
            KedaDetector().list_scaledobjects()

    def test_get_scaledobject_raises(self) -> None:
        with pytest.raises(ComponentNotInstalledError):
            KedaDetector().get_scaledobject("x", "ns")

    def test_list_trigger_auths_raises(self) -> None:
        with pytest.raises(ComponentNotInstalledError):
            KedaDetector().list_trigger_auths()

    def test_get_trigger_auth_raises(self) -> None:
        with pytest.raises(ComponentNotInstalledError):
            KedaDetector().get_trigger_auth("x", "ns")

    def test_list_scaledjobs_raises(self) -> None:
        with pytest.raises(ComponentNotInstalledError):
            KedaDetector().list_scaledjobs()

    def test_get_scaledjob_raises(self) -> None:
        with pytest.raises(ComponentNotInstalledError):
            KedaDetector().get_scaledjob("x", "ns")
