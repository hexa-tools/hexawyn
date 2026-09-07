from __future__ import annotations

from collections.abc import Mapping

from hexawyn.domain.models.secret_rotation import ManagedFieldsEntry

_DATA_FIELD_KEY = "f:data"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_touches_data__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_touches_data__mutmut)
def touches_data(fields_v1_raw: Mapping[str, object]) -> bool:
    return _DATA_FIELD_KEY in fields_v1_raw


def x_touches_data__mutmut_orig(fields_v1_raw: Mapping[str, object]) -> bool:
    return _DATA_FIELD_KEY in fields_v1_raw


def x_touches_data__mutmut_1(fields_v1_raw: Mapping[str, object]) -> bool:
    return _DATA_FIELD_KEY not in fields_v1_raw

mutants_x_touches_data__mutmut['_mutmut_orig'] = x_touches_data__mutmut_orig # type: ignore # mutmut generated
mutants_x_touches_data__mutmut['x_touches_data__mutmut_1'] = x_touches_data__mutmut_1 # type: ignore # mutmut generated
mutants_x_find_last_data_change_time__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_find_last_data_change_time__mutmut)
def find_last_data_change_time(managed_fields: list[ManagedFieldsEntry]) -> str | None:
    data_changes = [entry for entry in managed_fields if touches_data(entry.fields_v1_raw)]
    if not data_changes:
        return None
    return max(entry.time for entry in data_changes)


def x_find_last_data_change_time__mutmut_orig(managed_fields: list[ManagedFieldsEntry]) -> str | None:
    data_changes = [entry for entry in managed_fields if touches_data(entry.fields_v1_raw)]
    if not data_changes:
        return None
    return max(entry.time for entry in data_changes)


def x_find_last_data_change_time__mutmut_1(managed_fields: list[ManagedFieldsEntry]) -> str | None:
    data_changes = None
    if not data_changes:
        return None
    return max(entry.time for entry in data_changes)


def x_find_last_data_change_time__mutmut_2(managed_fields: list[ManagedFieldsEntry]) -> str | None:
    data_changes = [entry for entry in managed_fields if touches_data(None)]
    if not data_changes:
        return None
    return max(entry.time for entry in data_changes)


def x_find_last_data_change_time__mutmut_3(managed_fields: list[ManagedFieldsEntry]) -> str | None:
    data_changes = [entry for entry in managed_fields if touches_data(entry.fields_v1_raw)]
    if data_changes:
        return None
    return max(entry.time for entry in data_changes)


def x_find_last_data_change_time__mutmut_4(managed_fields: list[ManagedFieldsEntry]) -> str | None:
    data_changes = [entry for entry in managed_fields if touches_data(entry.fields_v1_raw)]
    if not data_changes:
        return None
    return max(None)

mutants_x_find_last_data_change_time__mutmut['_mutmut_orig'] = x_find_last_data_change_time__mutmut_orig # type: ignore # mutmut generated
mutants_x_find_last_data_change_time__mutmut['x_find_last_data_change_time__mutmut_1'] = x_find_last_data_change_time__mutmut_1 # type: ignore # mutmut generated
mutants_x_find_last_data_change_time__mutmut['x_find_last_data_change_time__mutmut_2'] = x_find_last_data_change_time__mutmut_2 # type: ignore # mutmut generated
mutants_x_find_last_data_change_time__mutmut['x_find_last_data_change_time__mutmut_3'] = x_find_last_data_change_time__mutmut_3 # type: ignore # mutmut generated
mutants_x_find_last_data_change_time__mutmut['x_find_last_data_change_time__mutmut_4'] = x_find_last_data_change_time__mutmut_4 # type: ignore # mutmut generated
