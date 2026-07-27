from hexawyn.application.ports.driven.network_policy_audit_port import NetworkPolicyAuditPort
from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.command import (
    DetectNetworkSegmentationGapsCommand,
)
from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.response import (
    DetectNetworkSegmentationGapsResponse,
)


class DetectNetworkSegmentationGapsUseCase:
    def __init__(self, port: NetworkPolicyAuditPort) -> None:
        self._port = port

    def execute(
        self, command: DetectNetworkSegmentationGapsCommand
    ) -> DetectNetworkSegmentationGapsResponse:
        namespaces = self._port.list_namespaces_with_pod_counts()
        policies = self._port.list_network_policies()

        uncovered = {
            ns["name"]
            for ns in namespaces
            if ns["pod_count"] > 0 and not any(p["namespace"] == ns["name"] for p in policies)
        }
        return DetectNetworkSegmentationGapsResponse(
            total_namespaces_checked=len(namespaces),
            fully_open_count=len(uncovered),
            findings=list(uncovered),  # type: ignore
        )
