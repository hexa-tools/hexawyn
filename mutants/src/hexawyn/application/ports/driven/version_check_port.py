from abc import ABC, abstractmethod


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class VersionCheckPort(ABC):
    @abstractmethod
    def fetch_latest_version(self) -> str:
        """Return the latest published hexawyn version, or "" when unavailable."""
