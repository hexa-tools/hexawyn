from dataclasses import dataclass

from hexawyn.domain.models.platform_reliability import PlatformReliabilityReport


@dataclass
class ReportPlatformReliabilityResponse:
    result: PlatformReliabilityReport
