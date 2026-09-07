"""Anonymizer port — mask/unmask sensitive data for external destinations."""

from abc import ABC, abstractmethod

from hexawyn.domain.models.anonymization import AnonymizationMap, Destination, RedactionPolicy


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class AnonymizerPort(ABC):
    @abstractmethod
    def mask(self, text: str, policy: RedactionPolicy) -> tuple[str, AnonymizationMap]: ...

    @abstractmethod
    def unmask(self, text: str, mapping: AnonymizationMap, destination: Destination) -> str: ...
