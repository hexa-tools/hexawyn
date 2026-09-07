from dataclasses import dataclass

from hexawyn.domain.models.recurring_incident import RecurringIncidentReport


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class DetectRecurringIncidentsResponse:
    result: RecurringIncidentReport
