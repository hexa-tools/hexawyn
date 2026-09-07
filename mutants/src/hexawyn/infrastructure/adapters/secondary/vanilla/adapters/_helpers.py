from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import cast


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_items_from__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_items_from__mutmut)
def items_from(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(items)


def x_items_from__mutmut_orig(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(items)


def x_items_from__mutmut_1(item_list: object) -> list[object]:
    items = None
    return _object_sequence(items)


def x_items_from__mutmut_2(item_list: object) -> list[object]:
    items = getattr(None, "items", [])
    return _object_sequence(items)


def x_items_from__mutmut_3(item_list: object) -> list[object]:
    items = getattr(item_list, None, [])
    return _object_sequence(items)


def x_items_from__mutmut_4(item_list: object) -> list[object]:
    items = getattr(item_list, "items", None)
    return _object_sequence(items)


def x_items_from__mutmut_5(item_list: object) -> list[object]:
    items = getattr("items", [])
    return _object_sequence(items)


def x_items_from__mutmut_6(item_list: object) -> list[object]:
    items = getattr(item_list, [])
    return _object_sequence(items)


def x_items_from__mutmut_7(item_list: object) -> list[object]:
    items = getattr(item_list, "items", )
    return _object_sequence(items)


def x_items_from__mutmut_8(item_list: object) -> list[object]:
    items = getattr(item_list, "XXitemsXX", [])
    return _object_sequence(items)


def x_items_from__mutmut_9(item_list: object) -> list[object]:
    items = getattr(item_list, "ITEMS", [])
    return _object_sequence(items)


def x_items_from__mutmut_10(item_list: object) -> list[object]:
    items = getattr(item_list, "items", [])
    return _object_sequence(None)

mutants_x_items_from__mutmut['_mutmut_orig'] = x_items_from__mutmut_orig # type: ignore # mutmut generated
mutants_x_items_from__mutmut['x_items_from__mutmut_1'] = x_items_from__mutmut_1 # type: ignore # mutmut generated
mutants_x_items_from__mutmut['x_items_from__mutmut_2'] = x_items_from__mutmut_2 # type: ignore # mutmut generated
mutants_x_items_from__mutmut['x_items_from__mutmut_3'] = x_items_from__mutmut_3 # type: ignore # mutmut generated
mutants_x_items_from__mutmut['x_items_from__mutmut_4'] = x_items_from__mutmut_4 # type: ignore # mutmut generated
mutants_x_items_from__mutmut['x_items_from__mutmut_5'] = x_items_from__mutmut_5 # type: ignore # mutmut generated
mutants_x_items_from__mutmut['x_items_from__mutmut_6'] = x_items_from__mutmut_6 # type: ignore # mutmut generated
mutants_x_items_from__mutmut['x_items_from__mutmut_7'] = x_items_from__mutmut_7 # type: ignore # mutmut generated
mutants_x_items_from__mutmut['x_items_from__mutmut_8'] = x_items_from__mutmut_8 # type: ignore # mutmut generated
mutants_x_items_from__mutmut['x_items_from__mutmut_9'] = x_items_from__mutmut_9 # type: ignore # mutmut generated
mutants_x_items_from__mutmut['x_items_from__mutmut_10'] = x_items_from__mutmut_10 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__object_sequence__mutmut)
def _object_sequence(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


def x__object_sequence__mutmut_orig(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


def x__object_sequence__mutmut_1(value: object) -> list[object]:
    if isinstance(value, Sequence) or not isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


def x__object_sequence__mutmut_2(value: object) -> list[object]:
    if isinstance(value, Sequence) and isinstance(value, str | bytes):
        return list(cast(Sequence[object], value))
    return []


def x__object_sequence__mutmut_3(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(None)
    return []


def x__object_sequence__mutmut_4(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(None, value))
    return []


def x__object_sequence__mutmut_5(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], None))
    return []


def x__object_sequence__mutmut_6(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(value))
    return []


def x__object_sequence__mutmut_7(value: object) -> list[object]:
    if isinstance(value, Sequence) and not isinstance(value, str | bytes):
        return list(cast(Sequence[object], ))
    return []

mutants_x__object_sequence__mutmut['_mutmut_orig'] = x__object_sequence__mutmut_orig # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_1'] = x__object_sequence__mutmut_1 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_2'] = x__object_sequence__mutmut_2 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_3'] = x__object_sequence__mutmut_3 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_4'] = x__object_sequence__mutmut_4 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_5'] = x__object_sequence__mutmut_5 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_6'] = x__object_sequence__mutmut_6 # type: ignore # mutmut generated
mutants_x__object_sequence__mutmut['x__object_sequence__mutmut_7'] = x__object_sequence__mutmut_7 # type: ignore # mutmut generated
mutants_x_text_attr__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_text_attr__mutmut)
def text_attr(source: object, attr_name: str, default: str) -> str:
    value = optional_text_attr(source, attr_name)
    return value if value is not None else default


def x_text_attr__mutmut_orig(source: object, attr_name: str, default: str) -> str:
    value = optional_text_attr(source, attr_name)
    return value if value is not None else default


def x_text_attr__mutmut_1(source: object, attr_name: str, default: str) -> str:
    value = None
    return value if value is not None else default


def x_text_attr__mutmut_2(source: object, attr_name: str, default: str) -> str:
    value = optional_text_attr(None, attr_name)
    return value if value is not None else default


def x_text_attr__mutmut_3(source: object, attr_name: str, default: str) -> str:
    value = optional_text_attr(source, None)
    return value if value is not None else default


def x_text_attr__mutmut_4(source: object, attr_name: str, default: str) -> str:
    value = optional_text_attr(attr_name)
    return value if value is not None else default


def x_text_attr__mutmut_5(source: object, attr_name: str, default: str) -> str:
    value = optional_text_attr(source, )
    return value if value is not None else default


def x_text_attr__mutmut_6(source: object, attr_name: str, default: str) -> str:
    value = optional_text_attr(source, attr_name)
    return value if value is None else default

mutants_x_text_attr__mutmut['_mutmut_orig'] = x_text_attr__mutmut_orig # type: ignore # mutmut generated
mutants_x_text_attr__mutmut['x_text_attr__mutmut_1'] = x_text_attr__mutmut_1 # type: ignore # mutmut generated
mutants_x_text_attr__mutmut['x_text_attr__mutmut_2'] = x_text_attr__mutmut_2 # type: ignore # mutmut generated
mutants_x_text_attr__mutmut['x_text_attr__mutmut_3'] = x_text_attr__mutmut_3 # type: ignore # mutmut generated
mutants_x_text_attr__mutmut['x_text_attr__mutmut_4'] = x_text_attr__mutmut_4 # type: ignore # mutmut generated
mutants_x_text_attr__mutmut['x_text_attr__mutmut_5'] = x_text_attr__mutmut_5 # type: ignore # mutmut generated
mutants_x_text_attr__mutmut['x_text_attr__mutmut_6'] = x_text_attr__mutmut_6 # type: ignore # mutmut generated
mutants_x_optional_text_attr__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_optional_text_attr__mutmut)
def optional_text_attr(source: object, attr_name: str) -> str | None:
    value = getattr(source, attr_name, None)
    if isinstance(value, str) and value:
        return value
    return None


def x_optional_text_attr__mutmut_orig(source: object, attr_name: str) -> str | None:
    value = getattr(source, attr_name, None)
    if isinstance(value, str) and value:
        return value
    return None


def x_optional_text_attr__mutmut_1(source: object, attr_name: str) -> str | None:
    value = None
    if isinstance(value, str) and value:
        return value
    return None


def x_optional_text_attr__mutmut_2(source: object, attr_name: str) -> str | None:
    value = getattr(None, attr_name, None)
    if isinstance(value, str) and value:
        return value
    return None


def x_optional_text_attr__mutmut_3(source: object, attr_name: str) -> str | None:
    value = getattr(source, None, None)
    if isinstance(value, str) and value:
        return value
    return None


def x_optional_text_attr__mutmut_4(source: object, attr_name: str) -> str | None:
    value = getattr(attr_name, None)
    if isinstance(value, str) and value:
        return value
    return None


def x_optional_text_attr__mutmut_5(source: object, attr_name: str) -> str | None:
    value = getattr(source, None)
    if isinstance(value, str) and value:
        return value
    return None


def x_optional_text_attr__mutmut_6(source: object, attr_name: str) -> str | None:
    value = getattr(source, attr_name, )
    if isinstance(value, str) and value:
        return value
    return None


def x_optional_text_attr__mutmut_7(source: object, attr_name: str) -> str | None:
    value = getattr(source, attr_name, None)
    if isinstance(value, str) or value:
        return value
    return None

mutants_x_optional_text_attr__mutmut['_mutmut_orig'] = x_optional_text_attr__mutmut_orig # type: ignore # mutmut generated
mutants_x_optional_text_attr__mutmut['x_optional_text_attr__mutmut_1'] = x_optional_text_attr__mutmut_1 # type: ignore # mutmut generated
mutants_x_optional_text_attr__mutmut['x_optional_text_attr__mutmut_2'] = x_optional_text_attr__mutmut_2 # type: ignore # mutmut generated
mutants_x_optional_text_attr__mutmut['x_optional_text_attr__mutmut_3'] = x_optional_text_attr__mutmut_3 # type: ignore # mutmut generated
mutants_x_optional_text_attr__mutmut['x_optional_text_attr__mutmut_4'] = x_optional_text_attr__mutmut_4 # type: ignore # mutmut generated
mutants_x_optional_text_attr__mutmut['x_optional_text_attr__mutmut_5'] = x_optional_text_attr__mutmut_5 # type: ignore # mutmut generated
mutants_x_optional_text_attr__mutmut['x_optional_text_attr__mutmut_6'] = x_optional_text_attr__mutmut_6 # type: ignore # mutmut generated
mutants_x_optional_text_attr__mutmut['x_optional_text_attr__mutmut_7'] = x_optional_text_attr__mutmut_7 # type: ignore # mutmut generated
mutants_x_integer_attr__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_integer_attr__mutmut)
def integer_attr(source: object, attr_name: str) -> int:
    value = getattr(source, attr_name, 0)
    return value if isinstance(value, int) else 0


def x_integer_attr__mutmut_orig(source: object, attr_name: str) -> int:
    value = getattr(source, attr_name, 0)
    return value if isinstance(value, int) else 0


def x_integer_attr__mutmut_1(source: object, attr_name: str) -> int:
    value = None
    return value if isinstance(value, int) else 0


def x_integer_attr__mutmut_2(source: object, attr_name: str) -> int:
    value = getattr(None, attr_name, 0)
    return value if isinstance(value, int) else 0


def x_integer_attr__mutmut_3(source: object, attr_name: str) -> int:
    value = getattr(source, None, 0)
    return value if isinstance(value, int) else 0


def x_integer_attr__mutmut_4(source: object, attr_name: str) -> int:
    value = getattr(source, attr_name, None)
    return value if isinstance(value, int) else 0


def x_integer_attr__mutmut_5(source: object, attr_name: str) -> int:
    value = getattr(attr_name, 0)
    return value if isinstance(value, int) else 0


def x_integer_attr__mutmut_6(source: object, attr_name: str) -> int:
    value = getattr(source, 0)
    return value if isinstance(value, int) else 0


def x_integer_attr__mutmut_7(source: object, attr_name: str) -> int:
    value = getattr(source, attr_name, )
    return value if isinstance(value, int) else 0


def x_integer_attr__mutmut_8(source: object, attr_name: str) -> int:
    value = getattr(source, attr_name, 1)
    return value if isinstance(value, int) else 0


def x_integer_attr__mutmut_9(source: object, attr_name: str) -> int:
    value = getattr(source, attr_name, 0)
    return value if isinstance(value, int) else 1

mutants_x_integer_attr__mutmut['_mutmut_orig'] = x_integer_attr__mutmut_orig # type: ignore # mutmut generated
mutants_x_integer_attr__mutmut['x_integer_attr__mutmut_1'] = x_integer_attr__mutmut_1 # type: ignore # mutmut generated
mutants_x_integer_attr__mutmut['x_integer_attr__mutmut_2'] = x_integer_attr__mutmut_2 # type: ignore # mutmut generated
mutants_x_integer_attr__mutmut['x_integer_attr__mutmut_3'] = x_integer_attr__mutmut_3 # type: ignore # mutmut generated
mutants_x_integer_attr__mutmut['x_integer_attr__mutmut_4'] = x_integer_attr__mutmut_4 # type: ignore # mutmut generated
mutants_x_integer_attr__mutmut['x_integer_attr__mutmut_5'] = x_integer_attr__mutmut_5 # type: ignore # mutmut generated
mutants_x_integer_attr__mutmut['x_integer_attr__mutmut_6'] = x_integer_attr__mutmut_6 # type: ignore # mutmut generated
mutants_x_integer_attr__mutmut['x_integer_attr__mutmut_7'] = x_integer_attr__mutmut_7 # type: ignore # mutmut generated
mutants_x_integer_attr__mutmut['x_integer_attr__mutmut_8'] = x_integer_attr__mutmut_8 # type: ignore # mutmut generated
mutants_x_integer_attr__mutmut['x_integer_attr__mutmut_9'] = x_integer_attr__mutmut_9 # type: ignore # mutmut generated
mutants_x_conditions__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_conditions__mutmut)
def conditions(status: object) -> list[object]:
    conditions_list = getattr(status, "conditions", [])
    return _object_sequence(conditions_list)


def x_conditions__mutmut_orig(status: object) -> list[object]:
    conditions_list = getattr(status, "conditions", [])
    return _object_sequence(conditions_list)


def x_conditions__mutmut_1(status: object) -> list[object]:
    conditions_list = None
    return _object_sequence(conditions_list)


def x_conditions__mutmut_2(status: object) -> list[object]:
    conditions_list = getattr(None, "conditions", [])
    return _object_sequence(conditions_list)


def x_conditions__mutmut_3(status: object) -> list[object]:
    conditions_list = getattr(status, None, [])
    return _object_sequence(conditions_list)


def x_conditions__mutmut_4(status: object) -> list[object]:
    conditions_list = getattr(status, "conditions", None)
    return _object_sequence(conditions_list)


def x_conditions__mutmut_5(status: object) -> list[object]:
    conditions_list = getattr("conditions", [])
    return _object_sequence(conditions_list)


def x_conditions__mutmut_6(status: object) -> list[object]:
    conditions_list = getattr(status, [])
    return _object_sequence(conditions_list)


def x_conditions__mutmut_7(status: object) -> list[object]:
    conditions_list = getattr(status, "conditions", )
    return _object_sequence(conditions_list)


def x_conditions__mutmut_8(status: object) -> list[object]:
    conditions_list = getattr(status, "XXconditionsXX", [])
    return _object_sequence(conditions_list)


def x_conditions__mutmut_9(status: object) -> list[object]:
    conditions_list = getattr(status, "CONDITIONS", [])
    return _object_sequence(conditions_list)


def x_conditions__mutmut_10(status: object) -> list[object]:
    conditions_list = getattr(status, "conditions", [])
    return _object_sequence(None)

mutants_x_conditions__mutmut['_mutmut_orig'] = x_conditions__mutmut_orig # type: ignore # mutmut generated
mutants_x_conditions__mutmut['x_conditions__mutmut_1'] = x_conditions__mutmut_1 # type: ignore # mutmut generated
mutants_x_conditions__mutmut['x_conditions__mutmut_2'] = x_conditions__mutmut_2 # type: ignore # mutmut generated
mutants_x_conditions__mutmut['x_conditions__mutmut_3'] = x_conditions__mutmut_3 # type: ignore # mutmut generated
mutants_x_conditions__mutmut['x_conditions__mutmut_4'] = x_conditions__mutmut_4 # type: ignore # mutmut generated
mutants_x_conditions__mutmut['x_conditions__mutmut_5'] = x_conditions__mutmut_5 # type: ignore # mutmut generated
mutants_x_conditions__mutmut['x_conditions__mutmut_6'] = x_conditions__mutmut_6 # type: ignore # mutmut generated
mutants_x_conditions__mutmut['x_conditions__mutmut_7'] = x_conditions__mutmut_7 # type: ignore # mutmut generated
mutants_x_conditions__mutmut['x_conditions__mutmut_8'] = x_conditions__mutmut_8 # type: ignore # mutmut generated
mutants_x_conditions__mutmut['x_conditions__mutmut_9'] = x_conditions__mutmut_9 # type: ignore # mutmut generated
mutants_x_conditions__mutmut['x_conditions__mutmut_10'] = x_conditions__mutmut_10 # type: ignore # mutmut generated
mutants_x_container_statuses__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_container_statuses__mutmut)
def container_statuses(status: object) -> list[object]:
    cs = getattr(status, "container_statuses", [])
    return _object_sequence(cs)


def x_container_statuses__mutmut_orig(status: object) -> list[object]:
    cs = getattr(status, "container_statuses", [])
    return _object_sequence(cs)


def x_container_statuses__mutmut_1(status: object) -> list[object]:
    cs = None
    return _object_sequence(cs)


def x_container_statuses__mutmut_2(status: object) -> list[object]:
    cs = getattr(None, "container_statuses", [])
    return _object_sequence(cs)


def x_container_statuses__mutmut_3(status: object) -> list[object]:
    cs = getattr(status, None, [])
    return _object_sequence(cs)


def x_container_statuses__mutmut_4(status: object) -> list[object]:
    cs = getattr(status, "container_statuses", None)
    return _object_sequence(cs)


def x_container_statuses__mutmut_5(status: object) -> list[object]:
    cs = getattr("container_statuses", [])
    return _object_sequence(cs)


def x_container_statuses__mutmut_6(status: object) -> list[object]:
    cs = getattr(status, [])
    return _object_sequence(cs)


def x_container_statuses__mutmut_7(status: object) -> list[object]:
    cs = getattr(status, "container_statuses", )
    return _object_sequence(cs)


def x_container_statuses__mutmut_8(status: object) -> list[object]:
    cs = getattr(status, "XXcontainer_statusesXX", [])
    return _object_sequence(cs)


def x_container_statuses__mutmut_9(status: object) -> list[object]:
    cs = getattr(status, "CONTAINER_STATUSES", [])
    return _object_sequence(cs)


def x_container_statuses__mutmut_10(status: object) -> list[object]:
    cs = getattr(status, "container_statuses", [])
    return _object_sequence(None)

mutants_x_container_statuses__mutmut['_mutmut_orig'] = x_container_statuses__mutmut_orig # type: ignore # mutmut generated
mutants_x_container_statuses__mutmut['x_container_statuses__mutmut_1'] = x_container_statuses__mutmut_1 # type: ignore # mutmut generated
mutants_x_container_statuses__mutmut['x_container_statuses__mutmut_2'] = x_container_statuses__mutmut_2 # type: ignore # mutmut generated
mutants_x_container_statuses__mutmut['x_container_statuses__mutmut_3'] = x_container_statuses__mutmut_3 # type: ignore # mutmut generated
mutants_x_container_statuses__mutmut['x_container_statuses__mutmut_4'] = x_container_statuses__mutmut_4 # type: ignore # mutmut generated
mutants_x_container_statuses__mutmut['x_container_statuses__mutmut_5'] = x_container_statuses__mutmut_5 # type: ignore # mutmut generated
mutants_x_container_statuses__mutmut['x_container_statuses__mutmut_6'] = x_container_statuses__mutmut_6 # type: ignore # mutmut generated
mutants_x_container_statuses__mutmut['x_container_statuses__mutmut_7'] = x_container_statuses__mutmut_7 # type: ignore # mutmut generated
mutants_x_container_statuses__mutmut['x_container_statuses__mutmut_8'] = x_container_statuses__mutmut_8 # type: ignore # mutmut generated
mutants_x_container_statuses__mutmut['x_container_statuses__mutmut_9'] = x_container_statuses__mutmut_9 # type: ignore # mutmut generated
mutants_x_container_statuses__mutmut['x_container_statuses__mutmut_10'] = x_container_statuses__mutmut_10 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_waiting_reason__mutmut)
def waiting_reason(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_orig(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_1(status: object) -> str | None:
    for cs in container_statuses(None):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_2(status: object) -> str | None:
    for cs in container_statuses(status):
        state = None
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_3(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(None, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_4(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, None, None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_5(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr("state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_6(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_7(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", )
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_8(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "XXstateXX", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_9(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "STATE", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_10(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = None
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_11(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(None, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_12(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, None, None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_13(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr("waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_14(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_15(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", )
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_16(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "XXwaitingXX", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_17(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "WAITING", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_18(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = None
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_19(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(None, "reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_20(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, None)
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_21(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr("reason")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_22(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, )
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_23(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "XXreasonXX")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_24(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "REASON")
        if reason:
            return "CrashLoop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_25(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "XXCrashLoopXX" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_26(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "crashloop" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_27(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CRASHLOOP" if reason == "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_28(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason != "CrashLoopBackOff" else reason
    return None


def x_waiting_reason__mutmut_29(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "XXCrashLoopBackOffXX" else reason
    return None


def x_waiting_reason__mutmut_30(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "crashloopbackoff" else reason
    return None


def x_waiting_reason__mutmut_31(status: object) -> str | None:
    for cs in container_statuses(status):
        state = getattr(cs, "state", None)
        waiting = getattr(state, "waiting", None)
        reason = optional_text_attr(waiting, "reason")
        if reason:
            return "CrashLoop" if reason == "CRASHLOOPBACKOFF" else reason
    return None

mutants_x_waiting_reason__mutmut['_mutmut_orig'] = x_waiting_reason__mutmut_orig # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_1'] = x_waiting_reason__mutmut_1 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_2'] = x_waiting_reason__mutmut_2 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_3'] = x_waiting_reason__mutmut_3 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_4'] = x_waiting_reason__mutmut_4 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_5'] = x_waiting_reason__mutmut_5 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_6'] = x_waiting_reason__mutmut_6 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_7'] = x_waiting_reason__mutmut_7 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_8'] = x_waiting_reason__mutmut_8 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_9'] = x_waiting_reason__mutmut_9 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_10'] = x_waiting_reason__mutmut_10 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_11'] = x_waiting_reason__mutmut_11 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_12'] = x_waiting_reason__mutmut_12 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_13'] = x_waiting_reason__mutmut_13 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_14'] = x_waiting_reason__mutmut_14 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_15'] = x_waiting_reason__mutmut_15 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_16'] = x_waiting_reason__mutmut_16 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_17'] = x_waiting_reason__mutmut_17 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_18'] = x_waiting_reason__mutmut_18 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_19'] = x_waiting_reason__mutmut_19 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_20'] = x_waiting_reason__mutmut_20 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_21'] = x_waiting_reason__mutmut_21 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_22'] = x_waiting_reason__mutmut_22 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_23'] = x_waiting_reason__mutmut_23 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_24'] = x_waiting_reason__mutmut_24 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_25'] = x_waiting_reason__mutmut_25 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_26'] = x_waiting_reason__mutmut_26 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_27'] = x_waiting_reason__mutmut_27 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_28'] = x_waiting_reason__mutmut_28 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_29'] = x_waiting_reason__mutmut_29 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_30'] = x_waiting_reason__mutmut_30 # type: ignore # mutmut generated
mutants_x_waiting_reason__mutmut['x_waiting_reason__mutmut_31'] = x_waiting_reason__mutmut_31 # type: ignore # mutmut generated
mutants_x_restart_count__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_restart_count__mutmut)
def restart_count(status: object) -> int:
    return sum(integer_attr(cs, "restart_count") for cs in container_statuses(status))


def x_restart_count__mutmut_orig(status: object) -> int:
    return sum(integer_attr(cs, "restart_count") for cs in container_statuses(status))


def x_restart_count__mutmut_1(status: object) -> int:
    return sum(None)


def x_restart_count__mutmut_2(status: object) -> int:
    return sum(integer_attr(None, "restart_count") for cs in container_statuses(status))


def x_restart_count__mutmut_3(status: object) -> int:
    return sum(integer_attr(cs, None) for cs in container_statuses(status))


def x_restart_count__mutmut_4(status: object) -> int:
    return sum(integer_attr("restart_count") for cs in container_statuses(status))


def x_restart_count__mutmut_5(status: object) -> int:
    return sum(integer_attr(cs, ) for cs in container_statuses(status))


def x_restart_count__mutmut_6(status: object) -> int:
    return sum(integer_attr(cs, "XXrestart_countXX") for cs in container_statuses(status))


def x_restart_count__mutmut_7(status: object) -> int:
    return sum(integer_attr(cs, "RESTART_COUNT") for cs in container_statuses(status))


def x_restart_count__mutmut_8(status: object) -> int:
    return sum(integer_attr(cs, "restart_count") for cs in container_statuses(None))

mutants_x_restart_count__mutmut['_mutmut_orig'] = x_restart_count__mutmut_orig # type: ignore # mutmut generated
mutants_x_restart_count__mutmut['x_restart_count__mutmut_1'] = x_restart_count__mutmut_1 # type: ignore # mutmut generated
mutants_x_restart_count__mutmut['x_restart_count__mutmut_2'] = x_restart_count__mutmut_2 # type: ignore # mutmut generated
mutants_x_restart_count__mutmut['x_restart_count__mutmut_3'] = x_restart_count__mutmut_3 # type: ignore # mutmut generated
mutants_x_restart_count__mutmut['x_restart_count__mutmut_4'] = x_restart_count__mutmut_4 # type: ignore # mutmut generated
mutants_x_restart_count__mutmut['x_restart_count__mutmut_5'] = x_restart_count__mutmut_5 # type: ignore # mutmut generated
mutants_x_restart_count__mutmut['x_restart_count__mutmut_6'] = x_restart_count__mutmut_6 # type: ignore # mutmut generated
mutants_x_restart_count__mutmut['x_restart_count__mutmut_7'] = x_restart_count__mutmut_7 # type: ignore # mutmut generated
mutants_x_restart_count__mutmut['x_restart_count__mutmut_8'] = x_restart_count__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_cpu__mutmut)
def parse_cpu(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:-1]))
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_orig(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:-1]))
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_1(cpu_str: str) -> int:
    if cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:-1]))
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_2(cpu_str: str) -> int:
    if not cpu_str:
        return 1
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:-1]))
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_3(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = None
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:-1]))
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_4(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(None).strip()
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:-1]))
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_5(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith(None):
        return int(float(cpu_str[:-1]))
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_6(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("XXmXX"):
        return int(float(cpu_str[:-1]))
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_7(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("M"):
        return int(float(cpu_str[:-1]))
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_8(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(None)
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_9(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(float(None))
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_10(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:+1]))
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_11(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:-2]))
    return int(float(cpu_str) * 1000)


def x_parse_cpu__mutmut_12(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:-1]))
    return int(None)


def x_parse_cpu__mutmut_13(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:-1]))
    return int(float(cpu_str) / 1000)


def x_parse_cpu__mutmut_14(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:-1]))
    return int(float(None) * 1000)


def x_parse_cpu__mutmut_15(cpu_str: str) -> int:
    if not cpu_str:
        return 0
    cpu_str = str(cpu_str).strip()
    if cpu_str.endswith("m"):
        return int(float(cpu_str[:-1]))
    return int(float(cpu_str) * 1001)

mutants_x_parse_cpu__mutmut['_mutmut_orig'] = x_parse_cpu__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_1'] = x_parse_cpu__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_2'] = x_parse_cpu__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_3'] = x_parse_cpu__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_4'] = x_parse_cpu__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_5'] = x_parse_cpu__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_6'] = x_parse_cpu__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_7'] = x_parse_cpu__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_8'] = x_parse_cpu__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_9'] = x_parse_cpu__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_10'] = x_parse_cpu__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_11'] = x_parse_cpu__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_12'] = x_parse_cpu__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_13'] = x_parse_cpu__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_14'] = x_parse_cpu__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_cpu__mutmut['x_parse_cpu__mutmut_15'] = x_parse_cpu__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_memory__mutmut)
def parse_memory(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_orig(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_1(mem_str: str) -> int:
    if mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_2(mem_str: str) -> int:
    if not mem_str:
        return 1
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_3(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = None
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_4(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(None).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_5(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith(None):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_6(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("XXMiXX"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_7(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_8(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("MI"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_9(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(None)
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_10(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(None))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_11(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:+2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_12(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-3]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_13(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith(None):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_14(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("XXGiXX"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_15(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_16(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("GI"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_17(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(None)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_18(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) / 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_19(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(None) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_20(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:+2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_21(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-3]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_22(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1025)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_23(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith(None):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_24(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("XXKiXX"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_25(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_26(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("KI"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_27(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(None)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_28(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) * 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_29(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(None) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_30(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:+2]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_31(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-3]) / 1024)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_32(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1025)
    return int(float(mem_str) / (1024 * 1024))


def x_parse_memory__mutmut_33(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(None)


def x_parse_memory__mutmut_34(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) * (1024 * 1024))


def x_parse_memory__mutmut_35(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(None) / (1024 * 1024))


def x_parse_memory__mutmut_36(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 / 1024))


def x_parse_memory__mutmut_37(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1025 * 1024))


def x_parse_memory__mutmut_38(mem_str: str) -> int:
    if not mem_str:
        return 0
    mem_str = str(mem_str).strip()
    if mem_str.endswith("Mi"):
        return int(float(mem_str[:-2]))
    if mem_str.endswith("Gi"):
        return int(float(mem_str[:-2]) * 1024)
    if mem_str.endswith("Ki"):
        return int(float(mem_str[:-2]) / 1024)
    return int(float(mem_str) / (1024 * 1025))

mutants_x_parse_memory__mutmut['_mutmut_orig'] = x_parse_memory__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_1'] = x_parse_memory__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_2'] = x_parse_memory__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_3'] = x_parse_memory__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_4'] = x_parse_memory__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_5'] = x_parse_memory__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_6'] = x_parse_memory__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_7'] = x_parse_memory__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_8'] = x_parse_memory__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_9'] = x_parse_memory__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_10'] = x_parse_memory__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_11'] = x_parse_memory__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_12'] = x_parse_memory__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_13'] = x_parse_memory__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_14'] = x_parse_memory__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_15'] = x_parse_memory__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_16'] = x_parse_memory__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_17'] = x_parse_memory__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_18'] = x_parse_memory__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_19'] = x_parse_memory__mutmut_19 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_20'] = x_parse_memory__mutmut_20 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_21'] = x_parse_memory__mutmut_21 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_22'] = x_parse_memory__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_23'] = x_parse_memory__mutmut_23 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_24'] = x_parse_memory__mutmut_24 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_25'] = x_parse_memory__mutmut_25 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_26'] = x_parse_memory__mutmut_26 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_27'] = x_parse_memory__mutmut_27 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_28'] = x_parse_memory__mutmut_28 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_29'] = x_parse_memory__mutmut_29 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_30'] = x_parse_memory__mutmut_30 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_31'] = x_parse_memory__mutmut_31 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_32'] = x_parse_memory__mutmut_32 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_33'] = x_parse_memory__mutmut_33 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_34'] = x_parse_memory__mutmut_34 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_35'] = x_parse_memory__mutmut_35 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_36'] = x_parse_memory__mutmut_36 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_37'] = x_parse_memory__mutmut_37 # type: ignore # mutmut generated
mutants_x_parse_memory__mutmut['x_parse_memory__mutmut_38'] = x_parse_memory__mutmut_38 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_namespace_age__mutmut)
def namespace_age(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_orig(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_1(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = None
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_2(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(None, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_3(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, None, None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_4(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr("creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_5(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_6(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", )
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_7(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "XXcreation_timestampXX", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_8(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "CREATION_TIMESTAMP", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_9(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is not None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_10(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "XXunknownXX"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_11(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "UNKNOWN"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_12(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = None
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_13(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(None)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_14(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = None
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_15(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now + timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_16(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = None
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_17(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total >= 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_18(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 1:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_19(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = None
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_20(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds / 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_21(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3601
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_22(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours >= 0:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_23(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 1:
        return f"{hours}h"
    minutes = delta.seconds // 60
    return f"{minutes}m"


def x_namespace_age__mutmut_24(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = None
    return f"{minutes}m"


def x_namespace_age__mutmut_25(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds / 60
    return f"{minutes}m"


def x_namespace_age__mutmut_26(metadata: object) -> str:
    from datetime import UTC, datetime

    timestamp = getattr(metadata, "creation_timestamp", None)
    if timestamp is None:
        return "unknown"
    now = datetime.now(UTC)
    delta = now - timestamp
    days_total = delta.days
    if days_total > 0:
        return f"{days_total}d"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h"
    minutes = delta.seconds // 61
    return f"{minutes}m"

mutants_x_namespace_age__mutmut['_mutmut_orig'] = x_namespace_age__mutmut_orig # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_1'] = x_namespace_age__mutmut_1 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_2'] = x_namespace_age__mutmut_2 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_3'] = x_namespace_age__mutmut_3 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_4'] = x_namespace_age__mutmut_4 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_5'] = x_namespace_age__mutmut_5 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_6'] = x_namespace_age__mutmut_6 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_7'] = x_namespace_age__mutmut_7 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_8'] = x_namespace_age__mutmut_8 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_9'] = x_namespace_age__mutmut_9 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_10'] = x_namespace_age__mutmut_10 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_11'] = x_namespace_age__mutmut_11 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_12'] = x_namespace_age__mutmut_12 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_13'] = x_namespace_age__mutmut_13 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_14'] = x_namespace_age__mutmut_14 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_15'] = x_namespace_age__mutmut_15 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_16'] = x_namespace_age__mutmut_16 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_17'] = x_namespace_age__mutmut_17 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_18'] = x_namespace_age__mutmut_18 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_19'] = x_namespace_age__mutmut_19 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_20'] = x_namespace_age__mutmut_20 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_21'] = x_namespace_age__mutmut_21 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_22'] = x_namespace_age__mutmut_22 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_23'] = x_namespace_age__mutmut_23 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_24'] = x_namespace_age__mutmut_24 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_25'] = x_namespace_age__mutmut_25 # type: ignore # mutmut generated
mutants_x_namespace_age__mutmut['x_namespace_age__mutmut_26'] = x_namespace_age__mutmut_26 # type: ignore # mutmut generated


def mapping_from(value: object) -> Mapping[object, object] | None:
    return value if isinstance(value, Mapping) else None
mutants_x_mapping_text__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_mapping_text__mutmut)
def mapping_text(mapping: Mapping[object, object], key: str) -> str:
    value = mapping.get(key, "")
    return value if isinstance(value, str) else ""


def x_mapping_text__mutmut_orig(mapping: Mapping[object, object], key: str) -> str:
    value = mapping.get(key, "")
    return value if isinstance(value, str) else ""


def x_mapping_text__mutmut_1(mapping: Mapping[object, object], key: str) -> str:
    value = None
    return value if isinstance(value, str) else ""


def x_mapping_text__mutmut_2(mapping: Mapping[object, object], key: str) -> str:
    value = mapping.get(None, "")
    return value if isinstance(value, str) else ""


def x_mapping_text__mutmut_3(mapping: Mapping[object, object], key: str) -> str:
    value = mapping.get(key, None)
    return value if isinstance(value, str) else ""


def x_mapping_text__mutmut_4(mapping: Mapping[object, object], key: str) -> str:
    value = mapping.get("")
    return value if isinstance(value, str) else ""


def x_mapping_text__mutmut_5(mapping: Mapping[object, object], key: str) -> str:
    value = mapping.get(key, )
    return value if isinstance(value, str) else ""


def x_mapping_text__mutmut_6(mapping: Mapping[object, object], key: str) -> str:
    value = mapping.get(key, "XXXX")
    return value if isinstance(value, str) else ""


def x_mapping_text__mutmut_7(mapping: Mapping[object, object], key: str) -> str:
    value = mapping.get(key, "")
    return value if isinstance(value, str) else "XXXX"

mutants_x_mapping_text__mutmut['_mutmut_orig'] = x_mapping_text__mutmut_orig # type: ignore # mutmut generated
mutants_x_mapping_text__mutmut['x_mapping_text__mutmut_1'] = x_mapping_text__mutmut_1 # type: ignore # mutmut generated
mutants_x_mapping_text__mutmut['x_mapping_text__mutmut_2'] = x_mapping_text__mutmut_2 # type: ignore # mutmut generated
mutants_x_mapping_text__mutmut['x_mapping_text__mutmut_3'] = x_mapping_text__mutmut_3 # type: ignore # mutmut generated
mutants_x_mapping_text__mutmut['x_mapping_text__mutmut_4'] = x_mapping_text__mutmut_4 # type: ignore # mutmut generated
mutants_x_mapping_text__mutmut['x_mapping_text__mutmut_5'] = x_mapping_text__mutmut_5 # type: ignore # mutmut generated
mutants_x_mapping_text__mutmut['x_mapping_text__mutmut_6'] = x_mapping_text__mutmut_6 # type: ignore # mutmut generated
mutants_x_mapping_text__mutmut['x_mapping_text__mutmut_7'] = x_mapping_text__mutmut_7 # type: ignore # mutmut generated
mutants_x_metric_items__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_metric_items__mutmut)
def metric_items(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(metrics)
    if m is None:
        return []
    items = m.get("items", [])
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def x_metric_items__mutmut_orig(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(metrics)
    if m is None:
        return []
    items = m.get("items", [])
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def x_metric_items__mutmut_1(metrics: object) -> list[Mapping[object, object]]:
    m = None
    if m is None:
        return []
    items = m.get("items", [])
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def x_metric_items__mutmut_2(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(None)
    if m is None:
        return []
    items = m.get("items", [])
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def x_metric_items__mutmut_3(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(metrics)
    if m is not None:
        return []
    items = m.get("items", [])
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def x_metric_items__mutmut_4(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(metrics)
    if m is None:
        return []
    items = None
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def x_metric_items__mutmut_5(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(metrics)
    if m is None:
        return []
    items = m.get(None, [])
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def x_metric_items__mutmut_6(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(metrics)
    if m is None:
        return []
    items = m.get("items", None)
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def x_metric_items__mutmut_7(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(metrics)
    if m is None:
        return []
    items = m.get([])
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def x_metric_items__mutmut_8(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(metrics)
    if m is None:
        return []
    items = m.get("items", )
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def x_metric_items__mutmut_9(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(metrics)
    if m is None:
        return []
    items = m.get("XXitemsXX", [])
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def x_metric_items__mutmut_10(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(metrics)
    if m is None:
        return []
    items = m.get("ITEMS", [])
    return [item for item in _object_sequence(items) if isinstance(item, Mapping)]


def x_metric_items__mutmut_11(metrics: object) -> list[Mapping[object, object]]:
    m = mapping_from(metrics)
    if m is None:
        return []
    items = m.get("items", [])
    return [item for item in _object_sequence(None) if isinstance(item, Mapping)]

mutants_x_metric_items__mutmut['_mutmut_orig'] = x_metric_items__mutmut_orig # type: ignore # mutmut generated
mutants_x_metric_items__mutmut['x_metric_items__mutmut_1'] = x_metric_items__mutmut_1 # type: ignore # mutmut generated
mutants_x_metric_items__mutmut['x_metric_items__mutmut_2'] = x_metric_items__mutmut_2 # type: ignore # mutmut generated
mutants_x_metric_items__mutmut['x_metric_items__mutmut_3'] = x_metric_items__mutmut_3 # type: ignore # mutmut generated
mutants_x_metric_items__mutmut['x_metric_items__mutmut_4'] = x_metric_items__mutmut_4 # type: ignore # mutmut generated
mutants_x_metric_items__mutmut['x_metric_items__mutmut_5'] = x_metric_items__mutmut_5 # type: ignore # mutmut generated
mutants_x_metric_items__mutmut['x_metric_items__mutmut_6'] = x_metric_items__mutmut_6 # type: ignore # mutmut generated
mutants_x_metric_items__mutmut['x_metric_items__mutmut_7'] = x_metric_items__mutmut_7 # type: ignore # mutmut generated
mutants_x_metric_items__mutmut['x_metric_items__mutmut_8'] = x_metric_items__mutmut_8 # type: ignore # mutmut generated
mutants_x_metric_items__mutmut['x_metric_items__mutmut_9'] = x_metric_items__mutmut_9 # type: ignore # mutmut generated
mutants_x_metric_items__mutmut['x_metric_items__mutmut_10'] = x_metric_items__mutmut_10 # type: ignore # mutmut generated
mutants_x_metric_items__mutmut['x_metric_items__mutmut_11'] = x_metric_items__mutmut_11 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_cpu_to_cores__mutmut)
def cpu_to_cores(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_orig(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_1(value: str) -> float:
    if value.endswith(None):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_2(value: str) -> float:
    if value.endswith("XXnXX"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_3(value: str) -> float:
    if value.endswith("N"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_4(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") * 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_5(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(None, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_6(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, None) / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_7(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix("n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_8(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, ) / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_9(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "XXnXX") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_10(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "N") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_11(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1000000001
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_12(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith(None):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_13(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("XXuXX"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_14(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("U"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_15(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") * 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_16(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(None, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_17(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, None) / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_18(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix("u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_19(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, ) / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_20(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "XXuXX") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_21(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "U") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_22(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1000001
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_23(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith(None):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_24(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("XXmXX"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_25(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("M"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_26(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") * 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_27(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(None, "m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_28(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, None) / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_29(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix("m") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_30(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, ) / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_31(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "XXmXX") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_32(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "M") / 1_000
    return _safe_float(value)


def x_cpu_to_cores__mutmut_33(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1001
    return _safe_float(value)


def x_cpu_to_cores__mutmut_34(value: str) -> float:
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(None)

mutants_x_cpu_to_cores__mutmut['_mutmut_orig'] = x_cpu_to_cores__mutmut_orig # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_1'] = x_cpu_to_cores__mutmut_1 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_2'] = x_cpu_to_cores__mutmut_2 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_3'] = x_cpu_to_cores__mutmut_3 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_4'] = x_cpu_to_cores__mutmut_4 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_5'] = x_cpu_to_cores__mutmut_5 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_6'] = x_cpu_to_cores__mutmut_6 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_7'] = x_cpu_to_cores__mutmut_7 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_8'] = x_cpu_to_cores__mutmut_8 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_9'] = x_cpu_to_cores__mutmut_9 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_10'] = x_cpu_to_cores__mutmut_10 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_11'] = x_cpu_to_cores__mutmut_11 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_12'] = x_cpu_to_cores__mutmut_12 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_13'] = x_cpu_to_cores__mutmut_13 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_14'] = x_cpu_to_cores__mutmut_14 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_15'] = x_cpu_to_cores__mutmut_15 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_16'] = x_cpu_to_cores__mutmut_16 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_17'] = x_cpu_to_cores__mutmut_17 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_18'] = x_cpu_to_cores__mutmut_18 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_19'] = x_cpu_to_cores__mutmut_19 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_20'] = x_cpu_to_cores__mutmut_20 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_21'] = x_cpu_to_cores__mutmut_21 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_22'] = x_cpu_to_cores__mutmut_22 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_23'] = x_cpu_to_cores__mutmut_23 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_24'] = x_cpu_to_cores__mutmut_24 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_25'] = x_cpu_to_cores__mutmut_25 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_26'] = x_cpu_to_cores__mutmut_26 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_27'] = x_cpu_to_cores__mutmut_27 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_28'] = x_cpu_to_cores__mutmut_28 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_29'] = x_cpu_to_cores__mutmut_29 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_30'] = x_cpu_to_cores__mutmut_30 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_31'] = x_cpu_to_cores__mutmut_31 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_32'] = x_cpu_to_cores__mutmut_32 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_33'] = x_cpu_to_cores__mutmut_33 # type: ignore # mutmut generated
mutants_x_cpu_to_cores__mutmut['x_cpu_to_cores__mutmut_34'] = x_cpu_to_cores__mutmut_34 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_memory_to_bytes__mutmut)
def memory_to_bytes(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_orig(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_1(value: str) -> float:
    multipliers = None
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_2(value: str) -> float:
    multipliers = {"XXKiXX": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_3(value: str) -> float:
    multipliers = {"ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_4(value: str) -> float:
    multipliers = {"KI": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_5(value: str) -> float:
    multipliers = {"Ki": 1025.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_6(value: str) -> float:
    multipliers = {"Ki": 1024.0, "XXMiXX": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_7(value: str) -> float:
    multipliers = {"Ki": 1024.0, "mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_8(value: str) -> float:
    multipliers = {"Ki": 1024.0, "MI": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_9(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0 * 2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_10(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1025.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_11(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**3, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_12(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "XXGiXX": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_13(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_14(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "GI": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_15(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0 * 3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_16(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1025.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_17(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**4, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_18(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "XXTiXX": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_19(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_20(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "TI": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_21(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0 * 4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_22(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1025.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_23(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**5}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_24(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(None):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_25(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) / multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_26(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(None, suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_27(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, None) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_28(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(suffix) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_29(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, ) * multiplier
    return _safe_float(value)


def x_memory_to_bytes__mutmut_30(value: str) -> float:
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier
    return _safe_float(None)

mutants_x_memory_to_bytes__mutmut['_mutmut_orig'] = x_memory_to_bytes__mutmut_orig # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_1'] = x_memory_to_bytes__mutmut_1 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_2'] = x_memory_to_bytes__mutmut_2 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_3'] = x_memory_to_bytes__mutmut_3 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_4'] = x_memory_to_bytes__mutmut_4 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_5'] = x_memory_to_bytes__mutmut_5 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_6'] = x_memory_to_bytes__mutmut_6 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_7'] = x_memory_to_bytes__mutmut_7 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_8'] = x_memory_to_bytes__mutmut_8 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_9'] = x_memory_to_bytes__mutmut_9 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_10'] = x_memory_to_bytes__mutmut_10 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_11'] = x_memory_to_bytes__mutmut_11 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_12'] = x_memory_to_bytes__mutmut_12 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_13'] = x_memory_to_bytes__mutmut_13 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_14'] = x_memory_to_bytes__mutmut_14 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_15'] = x_memory_to_bytes__mutmut_15 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_16'] = x_memory_to_bytes__mutmut_16 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_17'] = x_memory_to_bytes__mutmut_17 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_18'] = x_memory_to_bytes__mutmut_18 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_19'] = x_memory_to_bytes__mutmut_19 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_20'] = x_memory_to_bytes__mutmut_20 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_21'] = x_memory_to_bytes__mutmut_21 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_22'] = x_memory_to_bytes__mutmut_22 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_23'] = x_memory_to_bytes__mutmut_23 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_24'] = x_memory_to_bytes__mutmut_24 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_25'] = x_memory_to_bytes__mutmut_25 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_26'] = x_memory_to_bytes__mutmut_26 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_27'] = x_memory_to_bytes__mutmut_27 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_28'] = x_memory_to_bytes__mutmut_28 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_29'] = x_memory_to_bytes__mutmut_29 # type: ignore # mutmut generated
mutants_x_memory_to_bytes__mutmut['x_memory_to_bytes__mutmut_30'] = x_memory_to_bytes__mutmut_30 # type: ignore # mutmut generated
mutants_x__float_prefix__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__float_prefix__mutmut)
def _float_prefix(value: str, suffix: str) -> float:
    return _safe_float(value[: -len(suffix)])


def x__float_prefix__mutmut_orig(value: str, suffix: str) -> float:
    return _safe_float(value[: -len(suffix)])


def x__float_prefix__mutmut_1(value: str, suffix: str) -> float:
    return _safe_float(None)


def x__float_prefix__mutmut_2(value: str, suffix: str) -> float:
    return _safe_float(value[: +len(suffix)])

mutants_x__float_prefix__mutmut['_mutmut_orig'] = x__float_prefix__mutmut_orig # type: ignore # mutmut generated
mutants_x__float_prefix__mutmut['x__float_prefix__mutmut_1'] = x__float_prefix__mutmut_1 # type: ignore # mutmut generated
mutants_x__float_prefix__mutmut['x__float_prefix__mutmut_2'] = x__float_prefix__mutmut_2 # type: ignore # mutmut generated
mutants_x__safe_float__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__safe_float__mutmut)
def _safe_float(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return 0.0


def x__safe_float__mutmut_orig(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return 0.0


def x__safe_float__mutmut_1(value: str) -> float:
    try:
        return float(None)
    except ValueError:
        return 0.0


def x__safe_float__mutmut_2(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return 1.0

mutants_x__safe_float__mutmut['_mutmut_orig'] = x__safe_float__mutmut_orig # type: ignore # mutmut generated
mutants_x__safe_float__mutmut['x__safe_float__mutmut_1'] = x__safe_float__mutmut_1 # type: ignore # mutmut generated
mutants_x__safe_float__mutmut['x__safe_float__mutmut_2'] = x__safe_float__mutmut_2 # type: ignore # mutmut generated
mutants_x_percentage__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_percentage__mutmut)
def percentage(used: float, capacity: float) -> float:
    if capacity <= 0:
        return 0.0
    return round((used / capacity) * 100, 2)


def x_percentage__mutmut_orig(used: float, capacity: float) -> float:
    if capacity <= 0:
        return 0.0
    return round((used / capacity) * 100, 2)


def x_percentage__mutmut_1(used: float, capacity: float) -> float:
    if capacity < 0:
        return 0.0
    return round((used / capacity) * 100, 2)


def x_percentage__mutmut_2(used: float, capacity: float) -> float:
    if capacity <= 1:
        return 0.0
    return round((used / capacity) * 100, 2)


def x_percentage__mutmut_3(used: float, capacity: float) -> float:
    if capacity <= 0:
        return 1.0
    return round((used / capacity) * 100, 2)


def x_percentage__mutmut_4(used: float, capacity: float) -> float:
    if capacity <= 0:
        return 0.0
    return round(None, 2)


def x_percentage__mutmut_5(used: float, capacity: float) -> float:
    if capacity <= 0:
        return 0.0
    return round((used / capacity) * 100, None)


def x_percentage__mutmut_6(used: float, capacity: float) -> float:
    if capacity <= 0:
        return 0.0
    return round(2)


def x_percentage__mutmut_7(used: float, capacity: float) -> float:
    if capacity <= 0:
        return 0.0
    return round((used / capacity) * 100, )


def x_percentage__mutmut_8(used: float, capacity: float) -> float:
    if capacity <= 0:
        return 0.0
    return round((used / capacity) / 100, 2)


def x_percentage__mutmut_9(used: float, capacity: float) -> float:
    if capacity <= 0:
        return 0.0
    return round((used * capacity) * 100, 2)


def x_percentage__mutmut_10(used: float, capacity: float) -> float:
    if capacity <= 0:
        return 0.0
    return round((used / capacity) * 101, 2)


def x_percentage__mutmut_11(used: float, capacity: float) -> float:
    if capacity <= 0:
        return 0.0
    return round((used / capacity) * 100, 3)

mutants_x_percentage__mutmut['_mutmut_orig'] = x_percentage__mutmut_orig # type: ignore # mutmut generated
mutants_x_percentage__mutmut['x_percentage__mutmut_1'] = x_percentage__mutmut_1 # type: ignore # mutmut generated
mutants_x_percentage__mutmut['x_percentage__mutmut_2'] = x_percentage__mutmut_2 # type: ignore # mutmut generated
mutants_x_percentage__mutmut['x_percentage__mutmut_3'] = x_percentage__mutmut_3 # type: ignore # mutmut generated
mutants_x_percentage__mutmut['x_percentage__mutmut_4'] = x_percentage__mutmut_4 # type: ignore # mutmut generated
mutants_x_percentage__mutmut['x_percentage__mutmut_5'] = x_percentage__mutmut_5 # type: ignore # mutmut generated
mutants_x_percentage__mutmut['x_percentage__mutmut_6'] = x_percentage__mutmut_6 # type: ignore # mutmut generated
mutants_x_percentage__mutmut['x_percentage__mutmut_7'] = x_percentage__mutmut_7 # type: ignore # mutmut generated
mutants_x_percentage__mutmut['x_percentage__mutmut_8'] = x_percentage__mutmut_8 # type: ignore # mutmut generated
mutants_x_percentage__mutmut['x_percentage__mutmut_9'] = x_percentage__mutmut_9 # type: ignore # mutmut generated
mutants_x_percentage__mutmut['x_percentage__mutmut_10'] = x_percentage__mutmut_10 # type: ignore # mutmut generated
mutants_x_percentage__mutmut['x_percentage__mutmut_11'] = x_percentage__mutmut_11 # type: ignore # mutmut generated
