from __future__ import annotations

from hexawyn.domain.models.helm_values_diff import ValueDiff

_MISSING = object()


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


def _ordered_keys(source: dict[str, object], target: dict[str, object]) -> list[str]:
    ordered = list(source.keys())
    for key in target:
        if key not in source:
            ordered.append(key)
    return ordered


def _differs(source: object, target: object) -> bool:
    if type(source) is not type(target):
        return True
    return source != target


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


def _render(value: object) -> str:
    return str(value)
