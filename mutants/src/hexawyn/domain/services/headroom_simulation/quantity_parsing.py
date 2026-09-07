from __future__ import annotations

_BYTES_PER_GB = 1024.0**3


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_parse_cpu_quantity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_cpu_quantity__mutmut)
def parse_cpu_quantity(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_orig(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_1(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith(None):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_2(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("XXnXX"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_3(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("N"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_4(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") * 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_5(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(None, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_6(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, None) / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_7(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix("n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_8(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, ) / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_9(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "XXnXX") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_10(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "N") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_11(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1000000001
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_12(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith(None):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_13(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("XXuXX"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_14(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("U"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_15(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") * 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_16(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(None, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_17(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, None) / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_18(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix("u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_19(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, ) / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_20(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "XXuXX") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_21(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "U") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_22(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1000001
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_23(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith(None):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_24(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("XXmXX"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_25(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("M"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_26(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") * 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_27(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(None, "m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_28(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, None) / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_29(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix("m") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_30(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, ) / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_31(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "XXmXX") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_32(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "M") / 1_000
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_33(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1001
    return _safe_float(value)


def x_parse_cpu_quantity__mutmut_34(value: str) -> float:
    """Parses a human-typed K8s CPU quantity string (e.g. "500m", "2") into
    cores. Pure string parsing — no client objects involved, unlike the
    adapter-side parsers that read real K8s API node/pod objects."""
    if value.endswith("n"):
        return _float_prefix(value, "n") / 1_000_000_000
    if value.endswith("u"):
        return _float_prefix(value, "u") / 1_000_000
    if value.endswith("m"):
        return _float_prefix(value, "m") / 1_000
    return _safe_float(None)

mutants_x_parse_cpu_quantity__mutmut['_mutmut_orig'] = x_parse_cpu_quantity__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_1'] = x_parse_cpu_quantity__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_2'] = x_parse_cpu_quantity__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_3'] = x_parse_cpu_quantity__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_4'] = x_parse_cpu_quantity__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_5'] = x_parse_cpu_quantity__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_6'] = x_parse_cpu_quantity__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_7'] = x_parse_cpu_quantity__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_8'] = x_parse_cpu_quantity__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_9'] = x_parse_cpu_quantity__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_10'] = x_parse_cpu_quantity__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_11'] = x_parse_cpu_quantity__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_12'] = x_parse_cpu_quantity__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_13'] = x_parse_cpu_quantity__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_14'] = x_parse_cpu_quantity__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_15'] = x_parse_cpu_quantity__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_16'] = x_parse_cpu_quantity__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_17'] = x_parse_cpu_quantity__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_18'] = x_parse_cpu_quantity__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_19'] = x_parse_cpu_quantity__mutmut_19 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_20'] = x_parse_cpu_quantity__mutmut_20 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_21'] = x_parse_cpu_quantity__mutmut_21 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_22'] = x_parse_cpu_quantity__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_23'] = x_parse_cpu_quantity__mutmut_23 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_24'] = x_parse_cpu_quantity__mutmut_24 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_25'] = x_parse_cpu_quantity__mutmut_25 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_26'] = x_parse_cpu_quantity__mutmut_26 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_27'] = x_parse_cpu_quantity__mutmut_27 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_28'] = x_parse_cpu_quantity__mutmut_28 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_29'] = x_parse_cpu_quantity__mutmut_29 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_30'] = x_parse_cpu_quantity__mutmut_30 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_31'] = x_parse_cpu_quantity__mutmut_31 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_32'] = x_parse_cpu_quantity__mutmut_32 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_33'] = x_parse_cpu_quantity__mutmut_33 # type: ignore # mutmut generated
mutants_x_parse_cpu_quantity__mutmut['x_parse_cpu_quantity__mutmut_34'] = x_parse_cpu_quantity__mutmut_34 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_memory_quantity__mutmut)
def parse_memory_quantity(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_orig(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_1(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = None
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_2(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"XXKiXX": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_3(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_4(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"KI": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_5(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1025.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_6(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "XXMiXX": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_7(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_8(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "MI": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_9(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0 * 2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_10(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1025.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_11(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**3, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_12(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "XXGiXX": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_13(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_14(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "GI": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_15(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0 * 3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_16(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1025.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_17(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**4, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_18(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "XXTiXX": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_19(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_20(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "TI": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_21(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0 * 4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_22(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1025.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_23(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**5}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_24(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(None):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_25(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier * _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_26(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) / multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_27(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(None, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_28(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, None) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_29(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_30(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, ) * multiplier / _BYTES_PER_GB
    return _safe_float(value) / _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_31(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(value) * _BYTES_PER_GB


def x_parse_memory_quantity__mutmut_32(value: str) -> float:
    """Parses a human-typed K8s memory quantity string (e.g. "512Mi", "2Gi")
    into GB (not bytes — this feature's domain model works in GB throughout)."""
    multipliers = {"Ki": 1024.0, "Mi": 1024.0**2, "Gi": 1024.0**3, "Ti": 1024.0**4}
    for suffix, multiplier in multipliers.items():
        if value.endswith(suffix):
            return _float_prefix(value, suffix) * multiplier / _BYTES_PER_GB
    return _safe_float(None) / _BYTES_PER_GB

mutants_x_parse_memory_quantity__mutmut['_mutmut_orig'] = x_parse_memory_quantity__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_1'] = x_parse_memory_quantity__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_2'] = x_parse_memory_quantity__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_3'] = x_parse_memory_quantity__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_4'] = x_parse_memory_quantity__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_5'] = x_parse_memory_quantity__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_6'] = x_parse_memory_quantity__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_7'] = x_parse_memory_quantity__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_8'] = x_parse_memory_quantity__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_9'] = x_parse_memory_quantity__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_10'] = x_parse_memory_quantity__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_11'] = x_parse_memory_quantity__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_12'] = x_parse_memory_quantity__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_13'] = x_parse_memory_quantity__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_14'] = x_parse_memory_quantity__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_15'] = x_parse_memory_quantity__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_16'] = x_parse_memory_quantity__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_17'] = x_parse_memory_quantity__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_18'] = x_parse_memory_quantity__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_19'] = x_parse_memory_quantity__mutmut_19 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_20'] = x_parse_memory_quantity__mutmut_20 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_21'] = x_parse_memory_quantity__mutmut_21 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_22'] = x_parse_memory_quantity__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_23'] = x_parse_memory_quantity__mutmut_23 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_24'] = x_parse_memory_quantity__mutmut_24 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_25'] = x_parse_memory_quantity__mutmut_25 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_26'] = x_parse_memory_quantity__mutmut_26 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_27'] = x_parse_memory_quantity__mutmut_27 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_28'] = x_parse_memory_quantity__mutmut_28 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_29'] = x_parse_memory_quantity__mutmut_29 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_30'] = x_parse_memory_quantity__mutmut_30 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_31'] = x_parse_memory_quantity__mutmut_31 # type: ignore # mutmut generated
mutants_x_parse_memory_quantity__mutmut['x_parse_memory_quantity__mutmut_32'] = x_parse_memory_quantity__mutmut_32 # type: ignore # mutmut generated
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
