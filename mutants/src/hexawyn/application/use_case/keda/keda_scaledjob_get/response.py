from dataclasses import dataclass


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class KedaScaledjobGetResponse:
    name: str = ""
    namespace: str = ""
    phase: str = ""
    successful_jobs: int = 0
    failed_jobs: int = 0
    last_execution_time: str | None = None
    job_target_ref: str = ""
    cooldown_period_seconds: int = 0
    max_replica_count: int = 0
    message: str = ""
    error: str | None = None
