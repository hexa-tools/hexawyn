from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.detect_cross_cluster_incident.command import (  # noqa: E501
    DetectCrossClusterIncidentCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_cross_cluster_incident.response import (  # noqa: E501
    DetectCrossClusterIncidentResponse,
)


class DetectCrossClusterIncidentServicePort(ABC):
    @abstractmethod
    def detect(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse: ...
