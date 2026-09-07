from __future__ import annotations

from hexawyn.domain.models.metrics_query import UnitHint

_BYTES_IN_KB = 1_000
_BYTES_IN_MB = 1_000_000
_BYTES_IN_GB = 1_000_000_000


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_format_metric_value__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_format_metric_value__mutmut)
def format_metric_value(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "cores":
        return _format_cores(value)
    if unit_hint == "bytes":
        return _format_bytes(value)
    if unit_hint == "percent":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_orig(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "cores":
        return _format_cores(value)
    if unit_hint == "bytes":
        return _format_bytes(value)
    if unit_hint == "percent":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_1(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint != "cores":
        return _format_cores(value)
    if unit_hint == "bytes":
        return _format_bytes(value)
    if unit_hint == "percent":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_2(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "XXcoresXX":
        return _format_cores(value)
    if unit_hint == "bytes":
        return _format_bytes(value)
    if unit_hint == "percent":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_3(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "CORES":
        return _format_cores(value)
    if unit_hint == "bytes":
        return _format_bytes(value)
    if unit_hint == "percent":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_4(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "cores":
        return _format_cores(None)
    if unit_hint == "bytes":
        return _format_bytes(value)
    if unit_hint == "percent":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_5(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "cores":
        return _format_cores(value)
    if unit_hint != "bytes":
        return _format_bytes(value)
    if unit_hint == "percent":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_6(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "cores":
        return _format_cores(value)
    if unit_hint == "XXbytesXX":
        return _format_bytes(value)
    if unit_hint == "percent":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_7(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "cores":
        return _format_cores(value)
    if unit_hint == "BYTES":
        return _format_bytes(value)
    if unit_hint == "percent":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_8(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "cores":
        return _format_cores(value)
    if unit_hint == "bytes":
        return _format_bytes(None)
    if unit_hint == "percent":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_9(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "cores":
        return _format_cores(value)
    if unit_hint == "bytes":
        return _format_bytes(value)
    if unit_hint != "percent":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_10(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "cores":
        return _format_cores(value)
    if unit_hint == "bytes":
        return _format_bytes(value)
    if unit_hint == "XXpercentXX":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_11(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "cores":
        return _format_cores(value)
    if unit_hint == "bytes":
        return _format_bytes(value)
    if unit_hint == "PERCENT":
        return f"{value:.1f}%"
    return _format_raw(value)


def x_format_metric_value__mutmut_12(value: float, unit_hint: UnitHint) -> str:
    """Formats a raw Prometheus scalar into a human-readable string.

    `unit_hint` is caller-supplied (the SRE/agent knows what they queried) —
    PromQL results carry no unit metadata to infer this reliably.
    """
    if unit_hint == "cores":
        return _format_cores(value)
    if unit_hint == "bytes":
        return _format_bytes(value)
    if unit_hint == "percent":
        return f"{value:.1f}%"
    return _format_raw(None)

mutants_x_format_metric_value__mutmut['_mutmut_orig'] = x_format_metric_value__mutmut_orig # type: ignore # mutmut generated
mutants_x_format_metric_value__mutmut['x_format_metric_value__mutmut_1'] = x_format_metric_value__mutmut_1 # type: ignore # mutmut generated
mutants_x_format_metric_value__mutmut['x_format_metric_value__mutmut_2'] = x_format_metric_value__mutmut_2 # type: ignore # mutmut generated
mutants_x_format_metric_value__mutmut['x_format_metric_value__mutmut_3'] = x_format_metric_value__mutmut_3 # type: ignore # mutmut generated
mutants_x_format_metric_value__mutmut['x_format_metric_value__mutmut_4'] = x_format_metric_value__mutmut_4 # type: ignore # mutmut generated
mutants_x_format_metric_value__mutmut['x_format_metric_value__mutmut_5'] = x_format_metric_value__mutmut_5 # type: ignore # mutmut generated
mutants_x_format_metric_value__mutmut['x_format_metric_value__mutmut_6'] = x_format_metric_value__mutmut_6 # type: ignore # mutmut generated
mutants_x_format_metric_value__mutmut['x_format_metric_value__mutmut_7'] = x_format_metric_value__mutmut_7 # type: ignore # mutmut generated
mutants_x_format_metric_value__mutmut['x_format_metric_value__mutmut_8'] = x_format_metric_value__mutmut_8 # type: ignore # mutmut generated
mutants_x_format_metric_value__mutmut['x_format_metric_value__mutmut_9'] = x_format_metric_value__mutmut_9 # type: ignore # mutmut generated
mutants_x_format_metric_value__mutmut['x_format_metric_value__mutmut_10'] = x_format_metric_value__mutmut_10 # type: ignore # mutmut generated
mutants_x_format_metric_value__mutmut['x_format_metric_value__mutmut_11'] = x_format_metric_value__mutmut_11 # type: ignore # mutmut generated
mutants_x_format_metric_value__mutmut['x_format_metric_value__mutmut_12'] = x_format_metric_value__mutmut_12 # type: ignore # mutmut generated
mutants_x__format_cores__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__format_cores__mutmut)
def _format_cores(value: float) -> str:
    if abs(value) < 1:
        millicores = round(value * 1000, 6)
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def x__format_cores__mutmut_orig(value: float) -> str:
    if abs(value) < 1:
        millicores = round(value * 1000, 6)
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def x__format_cores__mutmut_1(value: float) -> str:
    if abs(None) < 1:
        millicores = round(value * 1000, 6)
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def x__format_cores__mutmut_2(value: float) -> str:
    if abs(value) <= 1:
        millicores = round(value * 1000, 6)
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def x__format_cores__mutmut_3(value: float) -> str:
    if abs(value) < 2:
        millicores = round(value * 1000, 6)
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def x__format_cores__mutmut_4(value: float) -> str:
    if abs(value) < 1:
        millicores = None
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def x__format_cores__mutmut_5(value: float) -> str:
    if abs(value) < 1:
        millicores = round(None, 6)
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def x__format_cores__mutmut_6(value: float) -> str:
    if abs(value) < 1:
        millicores = round(value * 1000, None)
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def x__format_cores__mutmut_7(value: float) -> str:
    if abs(value) < 1:
        millicores = round(6)
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def x__format_cores__mutmut_8(value: float) -> str:
    if abs(value) < 1:
        millicores = round(value * 1000, )
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def x__format_cores__mutmut_9(value: float) -> str:
    if abs(value) < 1:
        millicores = round(value / 1000, 6)
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def x__format_cores__mutmut_10(value: float) -> str:
    if abs(value) < 1:
        millicores = round(value * 1001, 6)
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"


def x__format_cores__mutmut_11(value: float) -> str:
    if abs(value) < 1:
        millicores = round(value * 1000, 7)
        return f"{millicores:g}m cores"
    return f"{value:.2f} cores"

mutants_x__format_cores__mutmut['_mutmut_orig'] = x__format_cores__mutmut_orig # type: ignore # mutmut generated
mutants_x__format_cores__mutmut['x__format_cores__mutmut_1'] = x__format_cores__mutmut_1 # type: ignore # mutmut generated
mutants_x__format_cores__mutmut['x__format_cores__mutmut_2'] = x__format_cores__mutmut_2 # type: ignore # mutmut generated
mutants_x__format_cores__mutmut['x__format_cores__mutmut_3'] = x__format_cores__mutmut_3 # type: ignore # mutmut generated
mutants_x__format_cores__mutmut['x__format_cores__mutmut_4'] = x__format_cores__mutmut_4 # type: ignore # mutmut generated
mutants_x__format_cores__mutmut['x__format_cores__mutmut_5'] = x__format_cores__mutmut_5 # type: ignore # mutmut generated
mutants_x__format_cores__mutmut['x__format_cores__mutmut_6'] = x__format_cores__mutmut_6 # type: ignore # mutmut generated
mutants_x__format_cores__mutmut['x__format_cores__mutmut_7'] = x__format_cores__mutmut_7 # type: ignore # mutmut generated
mutants_x__format_cores__mutmut['x__format_cores__mutmut_8'] = x__format_cores__mutmut_8 # type: ignore # mutmut generated
mutants_x__format_cores__mutmut['x__format_cores__mutmut_9'] = x__format_cores__mutmut_9 # type: ignore # mutmut generated
mutants_x__format_cores__mutmut['x__format_cores__mutmut_10'] = x__format_cores__mutmut_10 # type: ignore # mutmut generated
mutants_x__format_cores__mutmut['x__format_cores__mutmut_11'] = x__format_cores__mutmut_11 # type: ignore # mutmut generated
mutants_x__format_bytes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__format_bytes__mutmut)
def _format_bytes(value: float) -> str:
    if abs(value) >= _BYTES_IN_GB:
        return f"{value / _BYTES_IN_GB:.2f} GB"
    if abs(value) >= _BYTES_IN_MB:
        return f"{value / _BYTES_IN_MB:.2f} MB"
    if abs(value) >= _BYTES_IN_KB:
        return f"{value / _BYTES_IN_KB:.2f} KB"
    return f"{value:g} B"


def x__format_bytes__mutmut_orig(value: float) -> str:
    if abs(value) >= _BYTES_IN_GB:
        return f"{value / _BYTES_IN_GB:.2f} GB"
    if abs(value) >= _BYTES_IN_MB:
        return f"{value / _BYTES_IN_MB:.2f} MB"
    if abs(value) >= _BYTES_IN_KB:
        return f"{value / _BYTES_IN_KB:.2f} KB"
    return f"{value:g} B"


def x__format_bytes__mutmut_1(value: float) -> str:
    if abs(None) >= _BYTES_IN_GB:
        return f"{value / _BYTES_IN_GB:.2f} GB"
    if abs(value) >= _BYTES_IN_MB:
        return f"{value / _BYTES_IN_MB:.2f} MB"
    if abs(value) >= _BYTES_IN_KB:
        return f"{value / _BYTES_IN_KB:.2f} KB"
    return f"{value:g} B"


def x__format_bytes__mutmut_2(value: float) -> str:
    if abs(value) > _BYTES_IN_GB:
        return f"{value / _BYTES_IN_GB:.2f} GB"
    if abs(value) >= _BYTES_IN_MB:
        return f"{value / _BYTES_IN_MB:.2f} MB"
    if abs(value) >= _BYTES_IN_KB:
        return f"{value / _BYTES_IN_KB:.2f} KB"
    return f"{value:g} B"


def x__format_bytes__mutmut_3(value: float) -> str:
    if abs(value) >= _BYTES_IN_GB:
        return f"{value * _BYTES_IN_GB:.2f} GB"
    if abs(value) >= _BYTES_IN_MB:
        return f"{value / _BYTES_IN_MB:.2f} MB"
    if abs(value) >= _BYTES_IN_KB:
        return f"{value / _BYTES_IN_KB:.2f} KB"
    return f"{value:g} B"


def x__format_bytes__mutmut_4(value: float) -> str:
    if abs(value) >= _BYTES_IN_GB:
        return f"{value / _BYTES_IN_GB:.2f} GB"
    if abs(None) >= _BYTES_IN_MB:
        return f"{value / _BYTES_IN_MB:.2f} MB"
    if abs(value) >= _BYTES_IN_KB:
        return f"{value / _BYTES_IN_KB:.2f} KB"
    return f"{value:g} B"


def x__format_bytes__mutmut_5(value: float) -> str:
    if abs(value) >= _BYTES_IN_GB:
        return f"{value / _BYTES_IN_GB:.2f} GB"
    if abs(value) > _BYTES_IN_MB:
        return f"{value / _BYTES_IN_MB:.2f} MB"
    if abs(value) >= _BYTES_IN_KB:
        return f"{value / _BYTES_IN_KB:.2f} KB"
    return f"{value:g} B"


def x__format_bytes__mutmut_6(value: float) -> str:
    if abs(value) >= _BYTES_IN_GB:
        return f"{value / _BYTES_IN_GB:.2f} GB"
    if abs(value) >= _BYTES_IN_MB:
        return f"{value * _BYTES_IN_MB:.2f} MB"
    if abs(value) >= _BYTES_IN_KB:
        return f"{value / _BYTES_IN_KB:.2f} KB"
    return f"{value:g} B"


def x__format_bytes__mutmut_7(value: float) -> str:
    if abs(value) >= _BYTES_IN_GB:
        return f"{value / _BYTES_IN_GB:.2f} GB"
    if abs(value) >= _BYTES_IN_MB:
        return f"{value / _BYTES_IN_MB:.2f} MB"
    if abs(None) >= _BYTES_IN_KB:
        return f"{value / _BYTES_IN_KB:.2f} KB"
    return f"{value:g} B"


def x__format_bytes__mutmut_8(value: float) -> str:
    if abs(value) >= _BYTES_IN_GB:
        return f"{value / _BYTES_IN_GB:.2f} GB"
    if abs(value) >= _BYTES_IN_MB:
        return f"{value / _BYTES_IN_MB:.2f} MB"
    if abs(value) > _BYTES_IN_KB:
        return f"{value / _BYTES_IN_KB:.2f} KB"
    return f"{value:g} B"


def x__format_bytes__mutmut_9(value: float) -> str:
    if abs(value) >= _BYTES_IN_GB:
        return f"{value / _BYTES_IN_GB:.2f} GB"
    if abs(value) >= _BYTES_IN_MB:
        return f"{value / _BYTES_IN_MB:.2f} MB"
    if abs(value) >= _BYTES_IN_KB:
        return f"{value * _BYTES_IN_KB:.2f} KB"
    return f"{value:g} B"

mutants_x__format_bytes__mutmut['_mutmut_orig'] = x__format_bytes__mutmut_orig # type: ignore # mutmut generated
mutants_x__format_bytes__mutmut['x__format_bytes__mutmut_1'] = x__format_bytes__mutmut_1 # type: ignore # mutmut generated
mutants_x__format_bytes__mutmut['x__format_bytes__mutmut_2'] = x__format_bytes__mutmut_2 # type: ignore # mutmut generated
mutants_x__format_bytes__mutmut['x__format_bytes__mutmut_3'] = x__format_bytes__mutmut_3 # type: ignore # mutmut generated
mutants_x__format_bytes__mutmut['x__format_bytes__mutmut_4'] = x__format_bytes__mutmut_4 # type: ignore # mutmut generated
mutants_x__format_bytes__mutmut['x__format_bytes__mutmut_5'] = x__format_bytes__mutmut_5 # type: ignore # mutmut generated
mutants_x__format_bytes__mutmut['x__format_bytes__mutmut_6'] = x__format_bytes__mutmut_6 # type: ignore # mutmut generated
mutants_x__format_bytes__mutmut['x__format_bytes__mutmut_7'] = x__format_bytes__mutmut_7 # type: ignore # mutmut generated
mutants_x__format_bytes__mutmut['x__format_bytes__mutmut_8'] = x__format_bytes__mutmut_8 # type: ignore # mutmut generated
mutants_x__format_bytes__mutmut['x__format_bytes__mutmut_9'] = x__format_bytes__mutmut_9 # type: ignore # mutmut generated


def _format_raw(value: float) -> str:
    return f"{value:g}"
