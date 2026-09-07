from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.command import (
    DetectNetworkSegmentationGapsCommand,
)
from hexawyn.application.use_case.networking.detect_network_segmentation_gaps.response import (
    DetectNetworkSegmentationGapsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DetectNetworkSegmentationGapsServicePort(ABC):
    @abstractmethod
    def detect_segmentation_gaps(
        self, command: DetectNetworkSegmentationGapsCommand
    ) -> DetectNetworkSegmentationGapsResponse: ...
