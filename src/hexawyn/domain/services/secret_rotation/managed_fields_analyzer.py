from __future__ import annotations

from collections.abc import Mapping

from hexawyn.domain.models.secret_rotation import ManagedFieldsEntry

_DATA_FIELD_KEY = "f:data"


def touches_data(fields_v1_raw: Mapping[str, object]) -> bool:
    return _DATA_FIELD_KEY in fields_v1_raw


def find_last_data_change_time(managed_fields: list[ManagedFieldsEntry]) -> str | None:
    data_changes = [entry for entry in managed_fields if touches_data(entry.fields_v1_raw)]
    if not data_changes:
        return None
    return max(entry.time for entry in data_changes)
