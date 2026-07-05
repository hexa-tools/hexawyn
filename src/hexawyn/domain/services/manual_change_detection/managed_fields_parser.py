from __future__ import annotations

from collections.abc import Mapping

_FIELD_PREFIX = "f:"


def extract_field_paths(fields_v1: Mapping[str, object]) -> list[str]:
    paths: list[str] = []
    _walk(fields_v1, [], paths)
    return paths


def _walk(node: object, prefix: list[str], paths: list[str]) -> None:
    if not isinstance(node, Mapping):
        return
    field_children = {
        key: value
        for key, value in node.items()
        if isinstance(key, str) and key.startswith(_FIELD_PREFIX)
    }
    if not field_children:
        if prefix:
            paths.append(".".join(prefix))
        return
    for key, value in field_children.items():
        field_name = key[len(_FIELD_PREFIX) :]
        _walk(value, [*prefix, field_name], paths)
