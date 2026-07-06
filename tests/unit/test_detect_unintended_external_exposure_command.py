from __future__ import annotations


class TestDetectUnintendedExternalExposureCommand:
    def test_defaults(self) -> None:
        from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_command import (
            DetectUnintendedExternalExposureCommand,
        )

        command = DetectUnintendedExternalExposureCommand()

        assert command.allowlist is None
        assert command.namespaces is None

    def test_accepts_custom_allowlist_and_namespaces(self) -> None:
        from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_command import (
            DetectUnintendedExternalExposureCommand,
        )

        command = DetectUnintendedExternalExposureCommand(
            allowlist=["api-gateway"], namespaces=["production"]
        )

        assert command.allowlist == ["api-gateway"]
        assert command.namespaces == ["production"]
