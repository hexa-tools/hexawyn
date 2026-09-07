from __future__ import annotations

import math
from datetime import date, datetime, timedelta

_HOURS_PER_DAY = 24


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_deadline__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_deadline__mutmut)
def compute_deadline(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = _parse(event_date)
    if event is None:
        return None
    lead_time_days = math.ceil(provider_lead_time_hours / _HOURS_PER_DAY)
    deadline = event - timedelta(days=lead_time_days + safety_margin_days)
    return deadline.isoformat()


def x_compute_deadline__mutmut_orig(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = _parse(event_date)
    if event is None:
        return None
    lead_time_days = math.ceil(provider_lead_time_hours / _HOURS_PER_DAY)
    deadline = event - timedelta(days=lead_time_days + safety_margin_days)
    return deadline.isoformat()


def x_compute_deadline__mutmut_1(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = None
    if event is None:
        return None
    lead_time_days = math.ceil(provider_lead_time_hours / _HOURS_PER_DAY)
    deadline = event - timedelta(days=lead_time_days + safety_margin_days)
    return deadline.isoformat()


def x_compute_deadline__mutmut_2(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = _parse(None)
    if event is None:
        return None
    lead_time_days = math.ceil(provider_lead_time_hours / _HOURS_PER_DAY)
    deadline = event - timedelta(days=lead_time_days + safety_margin_days)
    return deadline.isoformat()


def x_compute_deadline__mutmut_3(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = _parse(event_date)
    if event is not None:
        return None
    lead_time_days = math.ceil(provider_lead_time_hours / _HOURS_PER_DAY)
    deadline = event - timedelta(days=lead_time_days + safety_margin_days)
    return deadline.isoformat()


def x_compute_deadline__mutmut_4(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = _parse(event_date)
    if event is None:
        return None
    lead_time_days = None
    deadline = event - timedelta(days=lead_time_days + safety_margin_days)
    return deadline.isoformat()


def x_compute_deadline__mutmut_5(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = _parse(event_date)
    if event is None:
        return None
    lead_time_days = math.ceil(None)
    deadline = event - timedelta(days=lead_time_days + safety_margin_days)
    return deadline.isoformat()


def x_compute_deadline__mutmut_6(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = _parse(event_date)
    if event is None:
        return None
    lead_time_days = math.ceil(provider_lead_time_hours * _HOURS_PER_DAY)
    deadline = event - timedelta(days=lead_time_days + safety_margin_days)
    return deadline.isoformat()


def x_compute_deadline__mutmut_7(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = _parse(event_date)
    if event is None:
        return None
    lead_time_days = math.ceil(provider_lead_time_hours / _HOURS_PER_DAY)
    deadline = None
    return deadline.isoformat()


def x_compute_deadline__mutmut_8(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = _parse(event_date)
    if event is None:
        return None
    lead_time_days = math.ceil(provider_lead_time_hours / _HOURS_PER_DAY)
    deadline = event + timedelta(days=lead_time_days + safety_margin_days)
    return deadline.isoformat()


def x_compute_deadline__mutmut_9(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = _parse(event_date)
    if event is None:
        return None
    lead_time_days = math.ceil(provider_lead_time_hours / _HOURS_PER_DAY)
    deadline = event - timedelta(days=None)
    return deadline.isoformat()


def x_compute_deadline__mutmut_10(
    event_date: str,
    provider_lead_time_hours: int,
    safety_margin_days: int,
) -> str | None:
    """Compute the latest safe provisioning date.

    Deadline = event date minus the provider's node lead time (rounded up to
    whole days) minus a safety margin. Returns None when the event date is
    malformed.
    """
    event = _parse(event_date)
    if event is None:
        return None
    lead_time_days = math.ceil(provider_lead_time_hours / _HOURS_PER_DAY)
    deadline = event - timedelta(days=lead_time_days - safety_margin_days)
    return deadline.isoformat()

mutants_x_compute_deadline__mutmut['_mutmut_orig'] = x_compute_deadline__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_deadline__mutmut['x_compute_deadline__mutmut_1'] = x_compute_deadline__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_deadline__mutmut['x_compute_deadline__mutmut_2'] = x_compute_deadline__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_deadline__mutmut['x_compute_deadline__mutmut_3'] = x_compute_deadline__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_deadline__mutmut['x_compute_deadline__mutmut_4'] = x_compute_deadline__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_deadline__mutmut['x_compute_deadline__mutmut_5'] = x_compute_deadline__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_deadline__mutmut['x_compute_deadline__mutmut_6'] = x_compute_deadline__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_deadline__mutmut['x_compute_deadline__mutmut_7'] = x_compute_deadline__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_deadline__mutmut['x_compute_deadline__mutmut_8'] = x_compute_deadline__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_deadline__mutmut['x_compute_deadline__mutmut_9'] = x_compute_deadline__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_deadline__mutmut['x_compute_deadline__mutmut_10'] = x_compute_deadline__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse__mutmut)
def _parse(event_date: str) -> date | None:
    try:
        return datetime.strptime(event_date, "%Y-%m-%d").date()
    except ValueError:
        return None


def x__parse__mutmut_orig(event_date: str) -> date | None:
    try:
        return datetime.strptime(event_date, "%Y-%m-%d").date()
    except ValueError:
        return None


def x__parse__mutmut_1(event_date: str) -> date | None:
    try:
        return datetime.strptime(None, "%Y-%m-%d").date()
    except ValueError:
        return None


def x__parse__mutmut_2(event_date: str) -> date | None:
    try:
        return datetime.strptime(event_date, None).date()
    except ValueError:
        return None


def x__parse__mutmut_3(event_date: str) -> date | None:
    try:
        return datetime.strptime("%Y-%m-%d").date()
    except ValueError:
        return None


def x__parse__mutmut_4(event_date: str) -> date | None:
    try:
        return datetime.strptime(event_date, ).date()
    except ValueError:
        return None


def x__parse__mutmut_5(event_date: str) -> date | None:
    try:
        return datetime.strptime(event_date, "XX%Y-%m-%dXX").date()
    except ValueError:
        return None


def x__parse__mutmut_6(event_date: str) -> date | None:
    try:
        return datetime.strptime(event_date, "%y-%m-%d").date()
    except ValueError:
        return None


def x__parse__mutmut_7(event_date: str) -> date | None:
    try:
        return datetime.strptime(event_date, "%Y-%M-%D").date()
    except ValueError:
        return None

mutants_x__parse__mutmut['_mutmut_orig'] = x__parse__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse__mutmut['x__parse__mutmut_1'] = x__parse__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse__mutmut['x__parse__mutmut_2'] = x__parse__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse__mutmut['x__parse__mutmut_3'] = x__parse__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse__mutmut['x__parse__mutmut_4'] = x__parse__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse__mutmut['x__parse__mutmut_5'] = x__parse__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse__mutmut['x__parse__mutmut_6'] = x__parse__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse__mutmut['x__parse__mutmut_7'] = x__parse__mutmut_7 # type: ignore # mutmut generated
