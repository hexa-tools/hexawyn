"""Get resource usage — use case."""

from hexawyn.application.use_case.cluster.get_resource_usage.get_resource_usage_use_case import (
    GetResourceUsageUseCase,
)

__all__ = ["GetResourceUsageUseCase"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
