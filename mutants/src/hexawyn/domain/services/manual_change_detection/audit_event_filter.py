from __future__ import annotations

from datetime import datetime, timedelta

from hexawyn.domain.models.manual_change import ActorType


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_is_within_window__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_within_window__mutmut)
def is_within_window(timestamp: str, window_days: int, now: datetime) -> bool:
    parsed = _parse_timestamp(timestamp)
    window_start = now - timedelta(days=window_days)
    return parsed >= window_start


def x_is_within_window__mutmut_orig(timestamp: str, window_days: int, now: datetime) -> bool:
    parsed = _parse_timestamp(timestamp)
    window_start = now - timedelta(days=window_days)
    return parsed >= window_start


def x_is_within_window__mutmut_1(timestamp: str, window_days: int, now: datetime) -> bool:
    parsed = None
    window_start = now - timedelta(days=window_days)
    return parsed >= window_start


def x_is_within_window__mutmut_2(timestamp: str, window_days: int, now: datetime) -> bool:
    parsed = _parse_timestamp(None)
    window_start = now - timedelta(days=window_days)
    return parsed >= window_start


def x_is_within_window__mutmut_3(timestamp: str, window_days: int, now: datetime) -> bool:
    parsed = _parse_timestamp(timestamp)
    window_start = None
    return parsed >= window_start


def x_is_within_window__mutmut_4(timestamp: str, window_days: int, now: datetime) -> bool:
    parsed = _parse_timestamp(timestamp)
    window_start = now + timedelta(days=window_days)
    return parsed >= window_start


def x_is_within_window__mutmut_5(timestamp: str, window_days: int, now: datetime) -> bool:
    parsed = _parse_timestamp(timestamp)
    window_start = now - timedelta(days=None)
    return parsed >= window_start


def x_is_within_window__mutmut_6(timestamp: str, window_days: int, now: datetime) -> bool:
    parsed = _parse_timestamp(timestamp)
    window_start = now - timedelta(days=window_days)
    return parsed > window_start

mutants_x_is_within_window__mutmut['_mutmut_orig'] = x_is_within_window__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_within_window__mutmut['x_is_within_window__mutmut_1'] = x_is_within_window__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_within_window__mutmut['x_is_within_window__mutmut_2'] = x_is_within_window__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_within_window__mutmut['x_is_within_window__mutmut_3'] = x_is_within_window__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_within_window__mutmut['x_is_within_window__mutmut_4'] = x_is_within_window__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_within_window__mutmut['x_is_within_window__mutmut_5'] = x_is_within_window__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_within_window__mutmut['x_is_within_window__mutmut_6'] = x_is_within_window__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_manual_change__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_manual_change__mutmut)
def is_manual_change(actor_type: ActorType) -> bool:
    return actor_type != "gitops_controller"


def x_is_manual_change__mutmut_orig(actor_type: ActorType) -> bool:
    return actor_type != "gitops_controller"


def x_is_manual_change__mutmut_1(actor_type: ActorType) -> bool:
    return actor_type == "gitops_controller"


def x_is_manual_change__mutmut_2(actor_type: ActorType) -> bool:
    return actor_type != "XXgitops_controllerXX"


def x_is_manual_change__mutmut_3(actor_type: ActorType) -> bool:
    return actor_type != "GITOPS_CONTROLLER"

mutants_x_is_manual_change__mutmut['_mutmut_orig'] = x_is_manual_change__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_manual_change__mutmut['x_is_manual_change__mutmut_1'] = x_is_manual_change__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_manual_change__mutmut['x_is_manual_change__mutmut_2'] = x_is_manual_change__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_manual_change__mutmut['x_is_manual_change__mutmut_3'] = x_is_manual_change__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_partial_window__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_partial_window__mutmut)
def is_partial_window(earliest_timestamp: str | None, window_days: int, now: datetime) -> bool:
    if earliest_timestamp is None:
        return False
    window_start = now - timedelta(days=window_days)
    return _parse_timestamp(earliest_timestamp) > window_start


def x_is_partial_window__mutmut_orig(earliest_timestamp: str | None, window_days: int, now: datetime) -> bool:
    if earliest_timestamp is None:
        return False
    window_start = now - timedelta(days=window_days)
    return _parse_timestamp(earliest_timestamp) > window_start


def x_is_partial_window__mutmut_1(earliest_timestamp: str | None, window_days: int, now: datetime) -> bool:
    if earliest_timestamp is not None:
        return False
    window_start = now - timedelta(days=window_days)
    return _parse_timestamp(earliest_timestamp) > window_start


def x_is_partial_window__mutmut_2(earliest_timestamp: str | None, window_days: int, now: datetime) -> bool:
    if earliest_timestamp is None:
        return True
    window_start = now - timedelta(days=window_days)
    return _parse_timestamp(earliest_timestamp) > window_start


def x_is_partial_window__mutmut_3(earliest_timestamp: str | None, window_days: int, now: datetime) -> bool:
    if earliest_timestamp is None:
        return False
    window_start = None
    return _parse_timestamp(earliest_timestamp) > window_start


def x_is_partial_window__mutmut_4(earliest_timestamp: str | None, window_days: int, now: datetime) -> bool:
    if earliest_timestamp is None:
        return False
    window_start = now + timedelta(days=window_days)
    return _parse_timestamp(earliest_timestamp) > window_start


def x_is_partial_window__mutmut_5(earliest_timestamp: str | None, window_days: int, now: datetime) -> bool:
    if earliest_timestamp is None:
        return False
    window_start = now - timedelta(days=None)
    return _parse_timestamp(earliest_timestamp) > window_start


def x_is_partial_window__mutmut_6(earliest_timestamp: str | None, window_days: int, now: datetime) -> bool:
    if earliest_timestamp is None:
        return False
    window_start = now - timedelta(days=window_days)
    return _parse_timestamp(None) > window_start


def x_is_partial_window__mutmut_7(earliest_timestamp: str | None, window_days: int, now: datetime) -> bool:
    if earliest_timestamp is None:
        return False
    window_start = now - timedelta(days=window_days)
    return _parse_timestamp(earliest_timestamp) >= window_start

mutants_x_is_partial_window__mutmut['_mutmut_orig'] = x_is_partial_window__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_partial_window__mutmut['x_is_partial_window__mutmut_1'] = x_is_partial_window__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_partial_window__mutmut['x_is_partial_window__mutmut_2'] = x_is_partial_window__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_partial_window__mutmut['x_is_partial_window__mutmut_3'] = x_is_partial_window__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_partial_window__mutmut['x_is_partial_window__mutmut_4'] = x_is_partial_window__mutmut_4 # type: ignore # mutmut generated
mutants_x_is_partial_window__mutmut['x_is_partial_window__mutmut_5'] = x_is_partial_window__mutmut_5 # type: ignore # mutmut generated
mutants_x_is_partial_window__mutmut['x_is_partial_window__mutmut_6'] = x_is_partial_window__mutmut_6 # type: ignore # mutmut generated
mutants_x_is_partial_window__mutmut['x_is_partial_window__mutmut_7'] = x_is_partial_window__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_timestamp__mutmut)
def _parse_timestamp(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def x__parse_timestamp__mutmut_orig(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def x__parse_timestamp__mutmut_1(raw: str) -> datetime:
    return datetime.fromisoformat(None)


def x__parse_timestamp__mutmut_2(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace(None, "+00:00"))


def x__parse_timestamp__mutmut_3(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", None))


def x__parse_timestamp__mutmut_4(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("+00:00"))


def x__parse_timestamp__mutmut_5(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", ))


def x__parse_timestamp__mutmut_6(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("XXZXX", "+00:00"))


def x__parse_timestamp__mutmut_7(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("z", "+00:00"))


def x__parse_timestamp__mutmut_8(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "XX+00:00XX"))

mutants_x__parse_timestamp__mutmut['_mutmut_orig'] = x__parse_timestamp__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_1'] = x__parse_timestamp__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_2'] = x__parse_timestamp__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_3'] = x__parse_timestamp__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_4'] = x__parse_timestamp__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_5'] = x__parse_timestamp__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_6'] = x__parse_timestamp__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_7'] = x__parse_timestamp__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_8'] = x__parse_timestamp__mutmut_8 # type: ignore # mutmut generated
