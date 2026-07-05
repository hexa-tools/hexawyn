from __future__ import annotations


class TestDetectNetworkSegmentationGapsCommand:
    def test_defaults_namespaces_to_none(self) -> None:
        from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_command import (
            DetectNetworkSegmentationGapsCommand,
        )

        command = DetectNetworkSegmentationGapsCommand()

        assert command.namespaces is None

    def test_accepts_custom_namespaces(self) -> None:
        from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_command import (
            DetectNetworkSegmentationGapsCommand,
        )

        command = DetectNetworkSegmentationGapsCommand(namespaces=["dev", "staging"])

        assert command.namespaces == ["dev", "staging"]
