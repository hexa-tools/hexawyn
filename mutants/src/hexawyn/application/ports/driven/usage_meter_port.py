from abc import ABC, abstractmethod


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class UsageMeterPort(ABC):
    """Current consumption — read-only for display purposes."""

    @abstractmethod
    def get_usage(self, resource: str) -> int:
        """Current month's consumption for this resource."""
