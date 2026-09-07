from __future__ import annotations

from collections.abc import Mapping

_FIELD_PREFIX = "f:"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_extract_field_paths__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_extract_field_paths__mutmut)
def extract_field_paths(fields_v1: Mapping[str, object]) -> list[str]:
    paths: list[str] = []
    _walk(fields_v1, [], paths)
    return paths


def x_extract_field_paths__mutmut_orig(fields_v1: Mapping[str, object]) -> list[str]:
    paths: list[str] = []
    _walk(fields_v1, [], paths)
    return paths


def x_extract_field_paths__mutmut_1(fields_v1: Mapping[str, object]) -> list[str]:
    paths: list[str] = None
    _walk(fields_v1, [], paths)
    return paths


def x_extract_field_paths__mutmut_2(fields_v1: Mapping[str, object]) -> list[str]:
    paths: list[str] = []
    _walk(None, [], paths)
    return paths


def x_extract_field_paths__mutmut_3(fields_v1: Mapping[str, object]) -> list[str]:
    paths: list[str] = []
    _walk(fields_v1, None, paths)
    return paths


def x_extract_field_paths__mutmut_4(fields_v1: Mapping[str, object]) -> list[str]:
    paths: list[str] = []
    _walk(fields_v1, [], None)
    return paths


def x_extract_field_paths__mutmut_5(fields_v1: Mapping[str, object]) -> list[str]:
    paths: list[str] = []
    _walk([], paths)
    return paths


def x_extract_field_paths__mutmut_6(fields_v1: Mapping[str, object]) -> list[str]:
    paths: list[str] = []
    _walk(fields_v1, paths)
    return paths


def x_extract_field_paths__mutmut_7(fields_v1: Mapping[str, object]) -> list[str]:
    paths: list[str] = []
    _walk(fields_v1, [], )
    return paths

mutants_x_extract_field_paths__mutmut['_mutmut_orig'] = x_extract_field_paths__mutmut_orig # type: ignore # mutmut generated
mutants_x_extract_field_paths__mutmut['x_extract_field_paths__mutmut_1'] = x_extract_field_paths__mutmut_1 # type: ignore # mutmut generated
mutants_x_extract_field_paths__mutmut['x_extract_field_paths__mutmut_2'] = x_extract_field_paths__mutmut_2 # type: ignore # mutmut generated
mutants_x_extract_field_paths__mutmut['x_extract_field_paths__mutmut_3'] = x_extract_field_paths__mutmut_3 # type: ignore # mutmut generated
mutants_x_extract_field_paths__mutmut['x_extract_field_paths__mutmut_4'] = x_extract_field_paths__mutmut_4 # type: ignore # mutmut generated
mutants_x_extract_field_paths__mutmut['x_extract_field_paths__mutmut_5'] = x_extract_field_paths__mutmut_5 # type: ignore # mutmut generated
mutants_x_extract_field_paths__mutmut['x_extract_field_paths__mutmut_6'] = x_extract_field_paths__mutmut_6 # type: ignore # mutmut generated
mutants_x_extract_field_paths__mutmut['x_extract_field_paths__mutmut_7'] = x_extract_field_paths__mutmut_7 # type: ignore # mutmut generated
mutants_x__walk__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__walk__mutmut)
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


def x__walk__mutmut_orig(node: object, prefix: list[str], paths: list[str]) -> None:
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


def x__walk__mutmut_1(node: object, prefix: list[str], paths: list[str]) -> None:
    if isinstance(node, Mapping):
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


def x__walk__mutmut_2(node: object, prefix: list[str], paths: list[str]) -> None:
    if not isinstance(node, Mapping):
        return
    field_children = None
    if not field_children:
        if prefix:
            paths.append(".".join(prefix))
        return
    for key, value in field_children.items():
        field_name = key[len(_FIELD_PREFIX) :]
        _walk(value, [*prefix, field_name], paths)


def x__walk__mutmut_3(node: object, prefix: list[str], paths: list[str]) -> None:
    if not isinstance(node, Mapping):
        return
    field_children = {
        key: value
        for key, value in node.items()
        if isinstance(key, str) or key.startswith(_FIELD_PREFIX)
    }
    if not field_children:
        if prefix:
            paths.append(".".join(prefix))
        return
    for key, value in field_children.items():
        field_name = key[len(_FIELD_PREFIX) :]
        _walk(value, [*prefix, field_name], paths)


def x__walk__mutmut_4(node: object, prefix: list[str], paths: list[str]) -> None:
    if not isinstance(node, Mapping):
        return
    field_children = {
        key: value
        for key, value in node.items()
        if isinstance(key, str) and key.startswith(None)
    }
    if not field_children:
        if prefix:
            paths.append(".".join(prefix))
        return
    for key, value in field_children.items():
        field_name = key[len(_FIELD_PREFIX) :]
        _walk(value, [*prefix, field_name], paths)


def x__walk__mutmut_5(node: object, prefix: list[str], paths: list[str]) -> None:
    if not isinstance(node, Mapping):
        return
    field_children = {
        key: value
        for key, value in node.items()
        if isinstance(key, str) and key.startswith(_FIELD_PREFIX)
    }
    if field_children:
        if prefix:
            paths.append(".".join(prefix))
        return
    for key, value in field_children.items():
        field_name = key[len(_FIELD_PREFIX) :]
        _walk(value, [*prefix, field_name], paths)


def x__walk__mutmut_6(node: object, prefix: list[str], paths: list[str]) -> None:
    if not isinstance(node, Mapping):
        return
    field_children = {
        key: value
        for key, value in node.items()
        if isinstance(key, str) and key.startswith(_FIELD_PREFIX)
    }
    if not field_children:
        if prefix:
            paths.append(None)
        return
    for key, value in field_children.items():
        field_name = key[len(_FIELD_PREFIX) :]
        _walk(value, [*prefix, field_name], paths)


def x__walk__mutmut_7(node: object, prefix: list[str], paths: list[str]) -> None:
    if not isinstance(node, Mapping):
        return
    field_children = {
        key: value
        for key, value in node.items()
        if isinstance(key, str) and key.startswith(_FIELD_PREFIX)
    }
    if not field_children:
        if prefix:
            paths.append(".".join(None))
        return
    for key, value in field_children.items():
        field_name = key[len(_FIELD_PREFIX) :]
        _walk(value, [*prefix, field_name], paths)


def x__walk__mutmut_8(node: object, prefix: list[str], paths: list[str]) -> None:
    if not isinstance(node, Mapping):
        return
    field_children = {
        key: value
        for key, value in node.items()
        if isinstance(key, str) and key.startswith(_FIELD_PREFIX)
    }
    if not field_children:
        if prefix:
            paths.append("XX.XX".join(prefix))
        return
    for key, value in field_children.items():
        field_name = key[len(_FIELD_PREFIX) :]
        _walk(value, [*prefix, field_name], paths)


def x__walk__mutmut_9(node: object, prefix: list[str], paths: list[str]) -> None:
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
        field_name = None
        _walk(value, [*prefix, field_name], paths)


def x__walk__mutmut_10(node: object, prefix: list[str], paths: list[str]) -> None:
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
        _walk(None, [*prefix, field_name], paths)


def x__walk__mutmut_11(node: object, prefix: list[str], paths: list[str]) -> None:
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
        _walk(value, None, paths)


def x__walk__mutmut_12(node: object, prefix: list[str], paths: list[str]) -> None:
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
        _walk(value, [*prefix, field_name], None)


def x__walk__mutmut_13(node: object, prefix: list[str], paths: list[str]) -> None:
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
        _walk([*prefix, field_name], paths)


def x__walk__mutmut_14(node: object, prefix: list[str], paths: list[str]) -> None:
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
        _walk(value, paths)


def x__walk__mutmut_15(node: object, prefix: list[str], paths: list[str]) -> None:
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
        _walk(value, [*prefix, field_name], )

mutants_x__walk__mutmut['_mutmut_orig'] = x__walk__mutmut_orig # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_1'] = x__walk__mutmut_1 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_2'] = x__walk__mutmut_2 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_3'] = x__walk__mutmut_3 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_4'] = x__walk__mutmut_4 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_5'] = x__walk__mutmut_5 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_6'] = x__walk__mutmut_6 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_7'] = x__walk__mutmut_7 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_8'] = x__walk__mutmut_8 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_9'] = x__walk__mutmut_9 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_10'] = x__walk__mutmut_10 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_11'] = x__walk__mutmut_11 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_12'] = x__walk__mutmut_12 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_13'] = x__walk__mutmut_13 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_14'] = x__walk__mutmut_14 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_15'] = x__walk__mutmut_15 # type: ignore # mutmut generated
