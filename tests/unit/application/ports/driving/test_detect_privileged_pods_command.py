from __future__ import annotations


class TestDetectPrivilegedPodsCommand:
    def test_defaults_namespaces_to_none(self) -> None:
        from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_command import (
            DetectPrivilegedPodsCommand,
        )

        command = DetectPrivilegedPodsCommand()

        assert command.namespaces is None

    def test_accepts_custom_namespaces(self) -> None:
        from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_command import (
            DetectPrivilegedPodsCommand,
        )

        command = DetectPrivilegedPodsCommand(namespaces=["production", "staging"])

        assert command.namespaces == ["production", "staging"]
