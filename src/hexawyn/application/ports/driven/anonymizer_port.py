"""Anonymizer port — mask/unmask sensitive data for external destinations."""

from abc import ABC, abstractmethod

from hexawyn.domain.models.anonymization import AnonymizationMap, Destination, RedactionPolicy


class AnonymizerPort(ABC):
    @abstractmethod
    def mask(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]: ...

    @abstractmethod
    def unmask(self, text: str, mapping: AnonymizationMap, destination: Destination) -> str: ...
