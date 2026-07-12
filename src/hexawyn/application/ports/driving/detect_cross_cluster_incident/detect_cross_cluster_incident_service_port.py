from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_command import (  # noqa: E501
    DetectCrossClusterIncidentCommand,
)
from hexawyn.application.ports.driving.detect_cross_cluster_incident.detect_cross_cluster_incident_response import (  # noqa: E501
    DetectCrossClusterIncidentResponse,
)


class DetectCrossClusterIncidentServicePort(ABC):
    @abstractmethod
    def detect(
        self, command: DetectCrossClusterIncidentCommand
    ) -> DetectCrossClusterIncidentResponse: ...
