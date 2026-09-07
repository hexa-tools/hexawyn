from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class RolloutStatusResponse:
    name: str = ""
    namespace: str = ""
    phase: str = ""
    strategy: str = ""
    canary_weight: str | None = None
    step_index: int | None = None
    total_steps: int | None = None
    current_step_type: str | None = None
    paused_at: str | None = None
    pause_reason: str | None = None
    message: str = ""
    error: str | None = None
