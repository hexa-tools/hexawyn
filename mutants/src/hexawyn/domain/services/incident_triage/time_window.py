from __future__ import annotations

from datetime import UTC, datetime, timedelta


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_within_window__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_within_window__mutmut)
def within_window(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_orig(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_1(start_time: str | None, window_minutes: int) -> bool:
    if start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_2(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return True
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_3(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = None
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_4(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(None)
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_5(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace(None, "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_6(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", None))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_7(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_8(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", ))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_9(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("XXZXX", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_10(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_11(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "XX+00:00XX"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_12(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return True
    return parsed >= datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_13(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed > datetime.now(UTC) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_14(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) + timedelta(minutes=window_minutes)


def x_within_window__mutmut_15(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(None) - timedelta(minutes=window_minutes)


def x_within_window__mutmut_16(start_time: str | None, window_minutes: int) -> bool:
    if not start_time:
        return False
    try:
        parsed = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed >= datetime.now(UTC) - timedelta(minutes=None)

mutants_x_within_window__mutmut['_mutmut_orig'] = x_within_window__mutmut_orig # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_1'] = x_within_window__mutmut_1 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_2'] = x_within_window__mutmut_2 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_3'] = x_within_window__mutmut_3 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_4'] = x_within_window__mutmut_4 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_5'] = x_within_window__mutmut_5 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_6'] = x_within_window__mutmut_6 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_7'] = x_within_window__mutmut_7 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_8'] = x_within_window__mutmut_8 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_9'] = x_within_window__mutmut_9 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_10'] = x_within_window__mutmut_10 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_11'] = x_within_window__mutmut_11 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_12'] = x_within_window__mutmut_12 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_13'] = x_within_window__mutmut_13 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_14'] = x_within_window__mutmut_14 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_15'] = x_within_window__mutmut_15 # type: ignore # mutmut generated
mutants_x_within_window__mutmut['x_within_window__mutmut_16'] = x_within_window__mutmut_16 # type: ignore # mutmut generated
