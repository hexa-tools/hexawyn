from hexawyn.application.ports.driven.network_policy_audit_port import NetworkPolicyAuditPort
from hexawyn.application.use_case.detect_network_segmentation_gaps.command import (
    DetectNetworkSegmentationGapsCommand,
)
from hexawyn.application.use_case.detect_network_segmentation_gaps.response import (
    DetectNetworkSegmentationGapsResponse,
)


class DetectNetworkSegmentationGapsUseCase:
    def __init__(self, port: NetworkPolicyAuditPort) -> None:
        self._port = port

    def execute(
        self, command: DetectNetworkSegmentationGapsCommand
    ) -> DetectNetworkSegmentationGapsResponse:
        return DetectNetworkSegmentationGapsResponse()
