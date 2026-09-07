from __future__ import annotations

from hexawyn.domain.models.helm_values_diff import ValueDiff

_MISSING = object()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_deep_diff__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_deep_diff__mutmut)
def deep_diff(source: dict[str, object], target: dict[str, object]) -> list[ValueDiff]:
    """Type-aware recursive diff of two Helm values trees.

    Produces one ValueDiff per differing leaf key, with dotted key paths.
    Values that render to the same string but have different Python types
    (e.g. ``8080`` vs ``"8080"``) are flagged as ``type_mismatch``.

    Severity, secret redaction and suggestions are left neutral here; the
    domain service enriches them so this function stays a pure structural diff.
    """
    diffs: list[ValueDiff] = []
    _walk(source, target, prefix="", diffs=diffs)
    return diffs


def x_deep_diff__mutmut_orig(source: dict[str, object], target: dict[str, object]) -> list[ValueDiff]:
    """Type-aware recursive diff of two Helm values trees.

    Produces one ValueDiff per differing leaf key, with dotted key paths.
    Values that render to the same string but have different Python types
    (e.g. ``8080`` vs ``"8080"``) are flagged as ``type_mismatch``.

    Severity, secret redaction and suggestions are left neutral here; the
    domain service enriches them so this function stays a pure structural diff.
    """
    diffs: list[ValueDiff] = []
    _walk(source, target, prefix="", diffs=diffs)
    return diffs


def x_deep_diff__mutmut_1(source: dict[str, object], target: dict[str, object]) -> list[ValueDiff]:
    """Type-aware recursive diff of two Helm values trees.

    Produces one ValueDiff per differing leaf key, with dotted key paths.
    Values that render to the same string but have different Python types
    (e.g. ``8080`` vs ``"8080"``) are flagged as ``type_mismatch``.

    Severity, secret redaction and suggestions are left neutral here; the
    domain service enriches them so this function stays a pure structural diff.
    """
    diffs: list[ValueDiff] = None
    _walk(source, target, prefix="", diffs=diffs)
    return diffs


def x_deep_diff__mutmut_2(source: dict[str, object], target: dict[str, object]) -> list[ValueDiff]:
    """Type-aware recursive diff of two Helm values trees.

    Produces one ValueDiff per differing leaf key, with dotted key paths.
    Values that render to the same string but have different Python types
    (e.g. ``8080`` vs ``"8080"``) are flagged as ``type_mismatch``.

    Severity, secret redaction and suggestions are left neutral here; the
    domain service enriches them so this function stays a pure structural diff.
    """
    diffs: list[ValueDiff] = []
    _walk(None, target, prefix="", diffs=diffs)
    return diffs


def x_deep_diff__mutmut_3(source: dict[str, object], target: dict[str, object]) -> list[ValueDiff]:
    """Type-aware recursive diff of two Helm values trees.

    Produces one ValueDiff per differing leaf key, with dotted key paths.
    Values that render to the same string but have different Python types
    (e.g. ``8080`` vs ``"8080"``) are flagged as ``type_mismatch``.

    Severity, secret redaction and suggestions are left neutral here; the
    domain service enriches them so this function stays a pure structural diff.
    """
    diffs: list[ValueDiff] = []
    _walk(source, None, prefix="", diffs=diffs)
    return diffs


def x_deep_diff__mutmut_4(source: dict[str, object], target: dict[str, object]) -> list[ValueDiff]:
    """Type-aware recursive diff of two Helm values trees.

    Produces one ValueDiff per differing leaf key, with dotted key paths.
    Values that render to the same string but have different Python types
    (e.g. ``8080`` vs ``"8080"``) are flagged as ``type_mismatch``.

    Severity, secret redaction and suggestions are left neutral here; the
    domain service enriches them so this function stays a pure structural diff.
    """
    diffs: list[ValueDiff] = []
    _walk(source, target, prefix=None, diffs=diffs)
    return diffs


def x_deep_diff__mutmut_5(source: dict[str, object], target: dict[str, object]) -> list[ValueDiff]:
    """Type-aware recursive diff of two Helm values trees.

    Produces one ValueDiff per differing leaf key, with dotted key paths.
    Values that render to the same string but have different Python types
    (e.g. ``8080`` vs ``"8080"``) are flagged as ``type_mismatch``.

    Severity, secret redaction and suggestions are left neutral here; the
    domain service enriches them so this function stays a pure structural diff.
    """
    diffs: list[ValueDiff] = []
    _walk(source, target, prefix="", diffs=None)
    return diffs


def x_deep_diff__mutmut_6(source: dict[str, object], target: dict[str, object]) -> list[ValueDiff]:
    """Type-aware recursive diff of two Helm values trees.

    Produces one ValueDiff per differing leaf key, with dotted key paths.
    Values that render to the same string but have different Python types
    (e.g. ``8080`` vs ``"8080"``) are flagged as ``type_mismatch``.

    Severity, secret redaction and suggestions are left neutral here; the
    domain service enriches them so this function stays a pure structural diff.
    """
    diffs: list[ValueDiff] = []
    _walk(target, prefix="", diffs=diffs)
    return diffs


def x_deep_diff__mutmut_7(source: dict[str, object], target: dict[str, object]) -> list[ValueDiff]:
    """Type-aware recursive diff of two Helm values trees.

    Produces one ValueDiff per differing leaf key, with dotted key paths.
    Values that render to the same string but have different Python types
    (e.g. ``8080`` vs ``"8080"``) are flagged as ``type_mismatch``.

    Severity, secret redaction and suggestions are left neutral here; the
    domain service enriches them so this function stays a pure structural diff.
    """
    diffs: list[ValueDiff] = []
    _walk(source, prefix="", diffs=diffs)
    return diffs


def x_deep_diff__mutmut_8(source: dict[str, object], target: dict[str, object]) -> list[ValueDiff]:
    """Type-aware recursive diff of two Helm values trees.

    Produces one ValueDiff per differing leaf key, with dotted key paths.
    Values that render to the same string but have different Python types
    (e.g. ``8080`` vs ``"8080"``) are flagged as ``type_mismatch``.

    Severity, secret redaction and suggestions are left neutral here; the
    domain service enriches them so this function stays a pure structural diff.
    """
    diffs: list[ValueDiff] = []
    _walk(source, target, diffs=diffs)
    return diffs


def x_deep_diff__mutmut_9(source: dict[str, object], target: dict[str, object]) -> list[ValueDiff]:
    """Type-aware recursive diff of two Helm values trees.

    Produces one ValueDiff per differing leaf key, with dotted key paths.
    Values that render to the same string but have different Python types
    (e.g. ``8080`` vs ``"8080"``) are flagged as ``type_mismatch``.

    Severity, secret redaction and suggestions are left neutral here; the
    domain service enriches them so this function stays a pure structural diff.
    """
    diffs: list[ValueDiff] = []
    _walk(source, target, prefix="", )
    return diffs


def x_deep_diff__mutmut_10(source: dict[str, object], target: dict[str, object]) -> list[ValueDiff]:
    """Type-aware recursive diff of two Helm values trees.

    Produces one ValueDiff per differing leaf key, with dotted key paths.
    Values that render to the same string but have different Python types
    (e.g. ``8080`` vs ``"8080"``) are flagged as ``type_mismatch``.

    Severity, secret redaction and suggestions are left neutral here; the
    domain service enriches them so this function stays a pure structural diff.
    """
    diffs: list[ValueDiff] = []
    _walk(source, target, prefix="XXXX", diffs=diffs)
    return diffs

mutants_x_deep_diff__mutmut['_mutmut_orig'] = x_deep_diff__mutmut_orig # type: ignore # mutmut generated
mutants_x_deep_diff__mutmut['x_deep_diff__mutmut_1'] = x_deep_diff__mutmut_1 # type: ignore # mutmut generated
mutants_x_deep_diff__mutmut['x_deep_diff__mutmut_2'] = x_deep_diff__mutmut_2 # type: ignore # mutmut generated
mutants_x_deep_diff__mutmut['x_deep_diff__mutmut_3'] = x_deep_diff__mutmut_3 # type: ignore # mutmut generated
mutants_x_deep_diff__mutmut['x_deep_diff__mutmut_4'] = x_deep_diff__mutmut_4 # type: ignore # mutmut generated
mutants_x_deep_diff__mutmut['x_deep_diff__mutmut_5'] = x_deep_diff__mutmut_5 # type: ignore # mutmut generated
mutants_x_deep_diff__mutmut['x_deep_diff__mutmut_6'] = x_deep_diff__mutmut_6 # type: ignore # mutmut generated
mutants_x_deep_diff__mutmut['x_deep_diff__mutmut_7'] = x_deep_diff__mutmut_7 # type: ignore # mutmut generated
mutants_x_deep_diff__mutmut['x_deep_diff__mutmut_8'] = x_deep_diff__mutmut_8 # type: ignore # mutmut generated
mutants_x_deep_diff__mutmut['x_deep_diff__mutmut_9'] = x_deep_diff__mutmut_9 # type: ignore # mutmut generated
mutants_x_deep_diff__mutmut['x_deep_diff__mutmut_10'] = x_deep_diff__mutmut_10 # type: ignore # mutmut generated
mutants_x__walk__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__walk__mutmut)
def _walk(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_orig(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_1(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) or isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_2(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(None, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_3(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, None, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_4(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, None, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_5(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, None)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_6(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_7(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_8(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_9(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, )
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_10(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) or target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_11(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is not _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_12(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(None, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_13(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, None, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_14(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, None, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_15(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, None)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_16(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts({}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_17(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_18(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_19(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, )
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_20(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) or source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_21(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is not _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_22(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts(None, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_23(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, None, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_24(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, None, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_25(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, None)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_26(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts(target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_27(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_28(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_29(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, )
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_30(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is not _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_31(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(None)
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_32(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(None, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_33(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, None, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_34(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, None, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_35(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, None))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_36(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(_MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_37(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_38(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_39(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, ))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_40(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "XXaddedXX"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_41(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "ADDED"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_42(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is not _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_43(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(None)
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_44(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(None, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_45(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, None, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_46(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, None, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_47(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, None))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_48(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_49(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_50(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_51(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, ))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_52(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "XXremovedXX"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_53(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "REMOVED"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_54(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(None, target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_55(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, None):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_56(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(target):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_57(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, ):
        diffs.append(_leaf(prefix, source, target, "changed"))


def x__walk__mutmut_58(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(None)


def x__walk__mutmut_59(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(None, source, target, "changed"))


def x__walk__mutmut_60(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, None, target, "changed"))


def x__walk__mutmut_61(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, None, "changed"))


def x__walk__mutmut_62(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, None))


def x__walk__mutmut_63(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(source, target, "changed"))


def x__walk__mutmut_64(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, target, "changed"))


def x__walk__mutmut_65(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, "changed"))


def x__walk__mutmut_66(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, ))


def x__walk__mutmut_67(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "XXchangedXX"))


def x__walk__mutmut_68(source: object, target: object, prefix: str, diffs: list[ValueDiff]) -> None:
    if isinstance(source, dict) and isinstance(target, dict):
        _walk_dicts(source, target, prefix, diffs)
        return
    if isinstance(source, dict) and target is _MISSING:
        _walk_dicts(source, {}, prefix, diffs)
        return
    if isinstance(target, dict) and source is _MISSING:
        _walk_dicts({}, target, prefix, diffs)
        return
    if source is _MISSING:
        diffs.append(_leaf(prefix, _MISSING, target, "added"))
        return
    if target is _MISSING:
        diffs.append(_leaf(prefix, source, _MISSING, "removed"))
        return
    if _differs(source, target):
        diffs.append(_leaf(prefix, source, target, "CHANGED"))

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
mutants_x__walk__mutmut['x__walk__mutmut_16'] = x__walk__mutmut_16 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_17'] = x__walk__mutmut_17 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_18'] = x__walk__mutmut_18 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_19'] = x__walk__mutmut_19 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_20'] = x__walk__mutmut_20 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_21'] = x__walk__mutmut_21 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_22'] = x__walk__mutmut_22 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_23'] = x__walk__mutmut_23 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_24'] = x__walk__mutmut_24 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_25'] = x__walk__mutmut_25 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_26'] = x__walk__mutmut_26 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_27'] = x__walk__mutmut_27 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_28'] = x__walk__mutmut_28 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_29'] = x__walk__mutmut_29 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_30'] = x__walk__mutmut_30 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_31'] = x__walk__mutmut_31 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_32'] = x__walk__mutmut_32 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_33'] = x__walk__mutmut_33 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_34'] = x__walk__mutmut_34 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_35'] = x__walk__mutmut_35 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_36'] = x__walk__mutmut_36 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_37'] = x__walk__mutmut_37 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_38'] = x__walk__mutmut_38 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_39'] = x__walk__mutmut_39 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_40'] = x__walk__mutmut_40 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_41'] = x__walk__mutmut_41 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_42'] = x__walk__mutmut_42 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_43'] = x__walk__mutmut_43 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_44'] = x__walk__mutmut_44 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_45'] = x__walk__mutmut_45 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_46'] = x__walk__mutmut_46 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_47'] = x__walk__mutmut_47 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_48'] = x__walk__mutmut_48 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_49'] = x__walk__mutmut_49 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_50'] = x__walk__mutmut_50 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_51'] = x__walk__mutmut_51 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_52'] = x__walk__mutmut_52 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_53'] = x__walk__mutmut_53 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_54'] = x__walk__mutmut_54 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_55'] = x__walk__mutmut_55 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_56'] = x__walk__mutmut_56 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_57'] = x__walk__mutmut_57 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_58'] = x__walk__mutmut_58 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_59'] = x__walk__mutmut_59 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_60'] = x__walk__mutmut_60 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_61'] = x__walk__mutmut_61 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_62'] = x__walk__mutmut_62 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_63'] = x__walk__mutmut_63 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_64'] = x__walk__mutmut_64 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_65'] = x__walk__mutmut_65 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_66'] = x__walk__mutmut_66 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_67'] = x__walk__mutmut_67 # type: ignore # mutmut generated
mutants_x__walk__mutmut['x__walk__mutmut_68'] = x__walk__mutmut_68 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__walk_dicts__mutmut)
def _walk_dicts(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_orig(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_1(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(None, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_2(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, None):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_3(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_4(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, ):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_5(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = None
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_6(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = None
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_7(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(None, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_8(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, None)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_9(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(_MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_10(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, )
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_11(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = None
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_12(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(None, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_13(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, None)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_14(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(_MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_15(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, )
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_16(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) or isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_17(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(None, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_18(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, None, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_19(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, None, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_20(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, None)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_21(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_22(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_23(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, diffs)
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_24(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, )
        else:
            _walk(source_child, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_25(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(None, target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_26(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, None, child_prefix, diffs)


def x__walk_dicts__mutmut_27(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, None, diffs)


def x__walk_dicts__mutmut_28(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, None)


def x__walk_dicts__mutmut_29(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(target_child, child_prefix, diffs)


def x__walk_dicts__mutmut_30(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, child_prefix, diffs)


def x__walk_dicts__mutmut_31(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, diffs)


def x__walk_dicts__mutmut_32(
    source: dict[str, object], target: dict[str, object], prefix: str, diffs: list[ValueDiff]
) -> None:
    for key in _ordered_keys(source, target):
        child_prefix = f"{prefix}.{key}" if prefix else key
        source_child = source.get(key, _MISSING)
        target_child = target.get(key, _MISSING)
        if isinstance(source_child, dict) and isinstance(target_child, dict):
            _walk_dicts(source_child, target_child, child_prefix, diffs)
        else:
            _walk(source_child, target_child, child_prefix, )

mutants_x__walk_dicts__mutmut['_mutmut_orig'] = x__walk_dicts__mutmut_orig # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_1'] = x__walk_dicts__mutmut_1 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_2'] = x__walk_dicts__mutmut_2 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_3'] = x__walk_dicts__mutmut_3 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_4'] = x__walk_dicts__mutmut_4 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_5'] = x__walk_dicts__mutmut_5 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_6'] = x__walk_dicts__mutmut_6 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_7'] = x__walk_dicts__mutmut_7 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_8'] = x__walk_dicts__mutmut_8 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_9'] = x__walk_dicts__mutmut_9 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_10'] = x__walk_dicts__mutmut_10 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_11'] = x__walk_dicts__mutmut_11 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_12'] = x__walk_dicts__mutmut_12 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_13'] = x__walk_dicts__mutmut_13 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_14'] = x__walk_dicts__mutmut_14 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_15'] = x__walk_dicts__mutmut_15 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_16'] = x__walk_dicts__mutmut_16 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_17'] = x__walk_dicts__mutmut_17 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_18'] = x__walk_dicts__mutmut_18 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_19'] = x__walk_dicts__mutmut_19 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_20'] = x__walk_dicts__mutmut_20 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_21'] = x__walk_dicts__mutmut_21 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_22'] = x__walk_dicts__mutmut_22 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_23'] = x__walk_dicts__mutmut_23 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_24'] = x__walk_dicts__mutmut_24 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_25'] = x__walk_dicts__mutmut_25 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_26'] = x__walk_dicts__mutmut_26 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_27'] = x__walk_dicts__mutmut_27 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_28'] = x__walk_dicts__mutmut_28 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_29'] = x__walk_dicts__mutmut_29 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_30'] = x__walk_dicts__mutmut_30 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_31'] = x__walk_dicts__mutmut_31 # type: ignore # mutmut generated
mutants_x__walk_dicts__mutmut['x__walk_dicts__mutmut_32'] = x__walk_dicts__mutmut_32 # type: ignore # mutmut generated
mutants_x__ordered_keys__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__ordered_keys__mutmut)
def _ordered_keys(source: dict[str, object], target: dict[str, object]) -> list[str]:
    ordered = list(source.keys())
    for key in target:
        if key not in source:
            ordered.append(key)
    return ordered


def x__ordered_keys__mutmut_orig(source: dict[str, object], target: dict[str, object]) -> list[str]:
    ordered = list(source.keys())
    for key in target:
        if key not in source:
            ordered.append(key)
    return ordered


def x__ordered_keys__mutmut_1(source: dict[str, object], target: dict[str, object]) -> list[str]:
    ordered = None
    for key in target:
        if key not in source:
            ordered.append(key)
    return ordered


def x__ordered_keys__mutmut_2(source: dict[str, object], target: dict[str, object]) -> list[str]:
    ordered = list(None)
    for key in target:
        if key not in source:
            ordered.append(key)
    return ordered


def x__ordered_keys__mutmut_3(source: dict[str, object], target: dict[str, object]) -> list[str]:
    ordered = list(source.keys())
    for key in target:
        if key in source:
            ordered.append(key)
    return ordered


def x__ordered_keys__mutmut_4(source: dict[str, object], target: dict[str, object]) -> list[str]:
    ordered = list(source.keys())
    for key in target:
        if key not in source:
            ordered.append(None)
    return ordered

mutants_x__ordered_keys__mutmut['_mutmut_orig'] = x__ordered_keys__mutmut_orig # type: ignore # mutmut generated
mutants_x__ordered_keys__mutmut['x__ordered_keys__mutmut_1'] = x__ordered_keys__mutmut_1 # type: ignore # mutmut generated
mutants_x__ordered_keys__mutmut['x__ordered_keys__mutmut_2'] = x__ordered_keys__mutmut_2 # type: ignore # mutmut generated
mutants_x__ordered_keys__mutmut['x__ordered_keys__mutmut_3'] = x__ordered_keys__mutmut_3 # type: ignore # mutmut generated
mutants_x__ordered_keys__mutmut['x__ordered_keys__mutmut_4'] = x__ordered_keys__mutmut_4 # type: ignore # mutmut generated
mutants_x__differs__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__differs__mutmut)
def _differs(source: object, target: object) -> bool:
    if type(source) is not type(target):
        return True
    return source != target


def x__differs__mutmut_orig(source: object, target: object) -> bool:
    if type(source) is not type(target):
        return True
    return source != target


def x__differs__mutmut_1(source: object, target: object) -> bool:
    if type(None) is not type(target):
        return True
    return source != target


def x__differs__mutmut_2(source: object, target: object) -> bool:
    if type(source) is type(target):
        return True
    return source != target


def x__differs__mutmut_3(source: object, target: object) -> bool:
    if type(source) is not type(None):
        return True
    return source != target


def x__differs__mutmut_4(source: object, target: object) -> bool:
    if type(source) is not type(target):
        return False
    return source != target


def x__differs__mutmut_5(source: object, target: object) -> bool:
    if type(source) is not type(target):
        return True
    return source == target

mutants_x__differs__mutmut['_mutmut_orig'] = x__differs__mutmut_orig # type: ignore # mutmut generated
mutants_x__differs__mutmut['x__differs__mutmut_1'] = x__differs__mutmut_1 # type: ignore # mutmut generated
mutants_x__differs__mutmut['x__differs__mutmut_2'] = x__differs__mutmut_2 # type: ignore # mutmut generated
mutants_x__differs__mutmut['x__differs__mutmut_3'] = x__differs__mutmut_3 # type: ignore # mutmut generated
mutants_x__differs__mutmut['x__differs__mutmut_4'] = x__differs__mutmut_4 # type: ignore # mutmut generated
mutants_x__differs__mutmut['x__differs__mutmut_5'] = x__differs__mutmut_5 # type: ignore # mutmut generated
mutants_x__leaf__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__leaf__mutmut)
def _leaf(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_orig(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_1(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = None
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_2(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_3(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = None
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_4(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_5(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=None,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_6(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=None,
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_7(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=None,
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_8(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=None,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_9(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity=None,
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_10(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=None,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_11(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=None,
        suggestion="",
    )


def x__leaf__mutmut_12(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion=None,
    )


def x__leaf__mutmut_13(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_14(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_15(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_16(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_17(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_18(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_19(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        suggestion="",
    )


def x__leaf__mutmut_20(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        )


def x__leaf__mutmut_21(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(None) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_22(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "XXXX",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_23(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(None) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_24(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "XXXX",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_25(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="XXinformationalXX",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_26(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="INFORMATIONAL",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_27(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=True,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_28(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target) or _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_29(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present or type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_30(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present or target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_31(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(None) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_32(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is type(target)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_33(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(None)
            and _render(source) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_34(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(None) == _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_35(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) != _render(target)
        ),
        suggestion="",
    )


def x__leaf__mutmut_36(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(None)
        ),
        suggestion="",
    )


def x__leaf__mutmut_37(key_path: str, source: object, target: object, change_type: str) -> ValueDiff:
    source_present = source is not _MISSING
    target_present = target is not _MISSING
    return ValueDiff(
        key_path=key_path,
        source_value=_render(source) if source_present else "",
        target_value=_render(target) if target_present else "",
        change_type=change_type,  # type: ignore[arg-type]
        severity="informational",
        is_secret=False,
        type_mismatch=(
            source_present
            and target_present
            and type(source) is not type(target)
            and _render(source) == _render(target)
        ),
        suggestion="XXXX",
    )

mutants_x__leaf__mutmut['_mutmut_orig'] = x__leaf__mutmut_orig # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_1'] = x__leaf__mutmut_1 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_2'] = x__leaf__mutmut_2 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_3'] = x__leaf__mutmut_3 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_4'] = x__leaf__mutmut_4 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_5'] = x__leaf__mutmut_5 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_6'] = x__leaf__mutmut_6 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_7'] = x__leaf__mutmut_7 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_8'] = x__leaf__mutmut_8 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_9'] = x__leaf__mutmut_9 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_10'] = x__leaf__mutmut_10 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_11'] = x__leaf__mutmut_11 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_12'] = x__leaf__mutmut_12 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_13'] = x__leaf__mutmut_13 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_14'] = x__leaf__mutmut_14 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_15'] = x__leaf__mutmut_15 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_16'] = x__leaf__mutmut_16 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_17'] = x__leaf__mutmut_17 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_18'] = x__leaf__mutmut_18 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_19'] = x__leaf__mutmut_19 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_20'] = x__leaf__mutmut_20 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_21'] = x__leaf__mutmut_21 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_22'] = x__leaf__mutmut_22 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_23'] = x__leaf__mutmut_23 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_24'] = x__leaf__mutmut_24 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_25'] = x__leaf__mutmut_25 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_26'] = x__leaf__mutmut_26 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_27'] = x__leaf__mutmut_27 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_28'] = x__leaf__mutmut_28 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_29'] = x__leaf__mutmut_29 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_30'] = x__leaf__mutmut_30 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_31'] = x__leaf__mutmut_31 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_32'] = x__leaf__mutmut_32 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_33'] = x__leaf__mutmut_33 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_34'] = x__leaf__mutmut_34 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_35'] = x__leaf__mutmut_35 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_36'] = x__leaf__mutmut_36 # type: ignore # mutmut generated
mutants_x__leaf__mutmut['x__leaf__mutmut_37'] = x__leaf__mutmut_37 # type: ignore # mutmut generated
mutants_x__render__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__render__mutmut)
def _render(value: object) -> str:
    return str(value)


def x__render__mutmut_orig(value: object) -> str:
    return str(value)


def x__render__mutmut_1(value: object) -> str:
    return str(None)

mutants_x__render__mutmut['_mutmut_orig'] = x__render__mutmut_orig # type: ignore # mutmut generated
mutants_x__render__mutmut['x__render__mutmut_1'] = x__render__mutmut_1 # type: ignore # mutmut generated
