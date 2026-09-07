"""Pure Hubble flow mapping and filtering — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumFlowEntry,
    CiliumFlowQuery,
    CiliumFlowsResult,
)

_NOT_INSTALLED_NOTE = "Hubble relay is not available in this cluster"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_flows__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_flows__mutmut)
def build_flows(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_orig(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_1(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = None
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_2(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = None
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_3(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(None)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_4(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(None, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_5(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, None):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_6(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_7(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, ):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_8(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(None)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_9(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit or len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_10(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) >= query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_11(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = None
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_12(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=None,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_13(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status=None,
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_14(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=None,
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_15(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=None,
        note=None,
    )


def x_build_flows__mutmut_16(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_17(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_18(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_19(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        note=None,
    )


def x_build_flows__mutmut_20(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        )


def x_build_flows__mutmut_21(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=False,
        status="present" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_22(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="XXpresentXX" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_23(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="PRESENT" if flows else "empty",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_24(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "XXemptyXX",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )


def x_build_flows__mutmut_25(raw_flows: list[dict[str, object]], query: CiliumFlowQuery) -> CiliumFlowsResult:
    """Map raw Hubble objects to flow entries, filter and clamp to the limit."""
    flows: list[CiliumFlowEntry] = []
    for raw in raw_flows:
        entry = _to_entry(raw)
        if _matches(entry, query):
            flows.append(entry)
    if query.limit and len(flows) > query.limit:
        flows = flows[: query.limit]
    return CiliumFlowsResult(
        installed=True,
        status="present" if flows else "EMPTY",
        total_flows=len(flows),
        flows=flows,
        note=None,
    )

mutants_x_build_flows__mutmut['_mutmut_orig'] = x_build_flows__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_1'] = x_build_flows__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_2'] = x_build_flows__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_3'] = x_build_flows__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_4'] = x_build_flows__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_5'] = x_build_flows__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_6'] = x_build_flows__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_7'] = x_build_flows__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_8'] = x_build_flows__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_9'] = x_build_flows__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_10'] = x_build_flows__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_11'] = x_build_flows__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_12'] = x_build_flows__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_13'] = x_build_flows__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_14'] = x_build_flows__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_15'] = x_build_flows__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_16'] = x_build_flows__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_17'] = x_build_flows__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_18'] = x_build_flows__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_19'] = x_build_flows__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_20'] = x_build_flows__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_21'] = x_build_flows__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_22'] = x_build_flows__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_23'] = x_build_flows__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_24'] = x_build_flows__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_flows__mutmut['x_build_flows__mutmut_25'] = x_build_flows__mutmut_25 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_not_installed_flows_result__mutmut)
def not_installed_flows_result() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status="not_installed",
        total_flows=0,
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_orig() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status="not_installed",
        total_flows=0,
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_1() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=None,
        status="not_installed",
        total_flows=0,
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_2() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status=None,
        total_flows=0,
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_3() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status="not_installed",
        total_flows=None,
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_4() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status="not_installed",
        total_flows=0,
        flows=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_5() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status="not_installed",
        total_flows=0,
        flows=[],
        note=None,
    )


def x_not_installed_flows_result__mutmut_6() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        status="not_installed",
        total_flows=0,
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_7() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        total_flows=0,
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_8() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status="not_installed",
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_9() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status="not_installed",
        total_flows=0,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_10() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status="not_installed",
        total_flows=0,
        flows=[],
        )


def x_not_installed_flows_result__mutmut_11() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=True,
        status="not_installed",
        total_flows=0,
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_12() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status="XXnot_installedXX",
        total_flows=0,
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_13() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status="NOT_INSTALLED",
        total_flows=0,
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_flows_result__mutmut_14() -> CiliumFlowsResult:
    """Honest NOT_INSTALLED marker — no fabricated flows."""
    return CiliumFlowsResult(
        installed=False,
        status="not_installed",
        total_flows=1,
        flows=[],
        note=_NOT_INSTALLED_NOTE,
    )

mutants_x_not_installed_flows_result__mutmut['_mutmut_orig'] = x_not_installed_flows_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_1'] = x_not_installed_flows_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_2'] = x_not_installed_flows_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_3'] = x_not_installed_flows_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_4'] = x_not_installed_flows_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_5'] = x_not_installed_flows_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_6'] = x_not_installed_flows_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_7'] = x_not_installed_flows_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_8'] = x_not_installed_flows_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_9'] = x_not_installed_flows_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_10'] = x_not_installed_flows_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_11'] = x_not_installed_flows_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_12'] = x_not_installed_flows_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_13'] = x_not_installed_flows_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_not_installed_flows_result__mutmut['x_not_installed_flows_result__mutmut_14'] = x_not_installed_flows_result__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_entry__mutmut)
def _to_entry(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_orig(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_1(raw: dict[str, object]) -> CiliumFlowEntry:
    source = None
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_2(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(None)
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_3(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get(None))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_4(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("XXsourceXX"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_5(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("SOURCE"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_6(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = None
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_7(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(None)
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_8(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get(None))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_9(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("XXdestinationXX"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_10(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("DESTINATION"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_11(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = None
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_12(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(None)
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_13(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get(None))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_14(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("XXipXX"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_15(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("IP"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_16(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = None
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_17(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(None)
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_18(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get(None))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_19(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("XXl4XX"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_20(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("L4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_21(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = None
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_22(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(None)
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_23(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get(None))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_24(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("XXl7XX"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_25(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("L7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_26(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = None
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_27(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(None)
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_28(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get(None))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_29(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("XXtcpXX"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_30(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("TCP"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_31(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = None
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_32(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(None)
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_33(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get(None))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_34(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("XXudpXX"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_35(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("UDP"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_36(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = None
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_37(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(None)
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_38(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") and "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_39(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") and udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_40(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get(None) or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_41(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("XXdestination_portXX") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_42(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("DESTINATION_PORT") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_43(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get(None) or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_44(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("XXdestination_portXX") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_45(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("DESTINATION_PORT") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_46(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "XXXX")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_47(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=None,
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_48(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=None,
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_49(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=None,
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_50(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=None,
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_51(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=None,
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_52(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=None,
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_53(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=None,
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_54(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=None,
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_55(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=None,
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_56(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol=None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_57(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_58(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=None,
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_59(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=None,
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_60(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=None,
    )


def x__to_entry__mutmut_61(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_62(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_63(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_64(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_65(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_66(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_67(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_68(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_69(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_70(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_71(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_72(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_73(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_74(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        )


def x__to_entry__mutmut_75(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(None),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_76(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") and ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_77(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get(None) or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_78(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("XXtimeXX") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_79(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("TIME") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_80(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or "XXXX"),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_81(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(None),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_82(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") and ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_83(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") and ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_84(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get(None) or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_85(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("XXpod_nameXX") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_86(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("POD_NAME") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_87(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get(None) or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_88(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("XXsourceXX") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_89(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("SOURCE") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_90(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or "XXXX"),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_91(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(None),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_92(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") and ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_93(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") and ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_94(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get(None) or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_95(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("XXpod_nameXX") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_96(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("POD_NAME") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_97(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get(None) or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_98(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("XXdestinationXX") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_99(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("DESTINATION") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_100(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or "XXXX"),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_101(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(None),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_102(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get(None)),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_103(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("XXnamespaceXX")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_104(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("NAMESPACE")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_105(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(None),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_106(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get(None)),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_107(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("XXnamespaceXX")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_108(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("NAMESPACE")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_109(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(None),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_110(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get(None)),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_111(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("XXidentityXX")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_112(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("IDENTITY")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_113(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(None),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_114(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get(None)),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_115(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("XXidentityXX")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_116(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("IDENTITY")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_117(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(None),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_118(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") and "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_119(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get(None) or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_120(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("XXverdictXX") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_121(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("VERDICT") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_122(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "XXUNKNOWNXX"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_123(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "unknown"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_124(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(None),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_125(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get(None)),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_126(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("XXdrop_reasonXX")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_127(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("DROP_REASON")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_128(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="XXtcpXX" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_129(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="TCP" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_130(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "XXudpXX" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_131(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "UDP" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_132(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port and None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_133(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(None),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_134(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get(None)),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_135(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("XXprotocolXX")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_136(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("PROTOCOL")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_137(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(None),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_138(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get(None)),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_139(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("XXdirectionXX")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_140(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("DIRECTION")),
        policy=_extract_policy(raw.get("labels")),
    )


def x__to_entry__mutmut_141(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(None),
    )


def x__to_entry__mutmut_142(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get(None)),
    )


def x__to_entry__mutmut_143(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("XXlabelsXX")),
    )


def x__to_entry__mutmut_144(raw: dict[str, object]) -> CiliumFlowEntry:
    source = _as_dict(raw.get("source"))
    destination = _as_dict(raw.get("destination"))
    ip = _as_dict(raw.get("ip"))
    l4 = _as_dict(raw.get("l4"))
    l7 = _as_dict(raw.get("l7"))
    tcp = _as_dict(l4.get("tcp"))
    udp = _as_dict(l4.get("udp"))
    destination_port = str(tcp.get("destination_port") or udp.get("destination_port") or "")
    return CiliumFlowEntry(
        timestamp=str(raw.get("time") or ""),
        source=str(source.get("pod_name") or ip.get("source") or ""),
        destination=str(destination.get("pod_name") or ip.get("destination") or ""),
        source_namespace=_as_str(source.get("namespace")),
        destination_namespace=_as_str(destination.get("namespace")),
        source_identity=_as_str(source.get("identity")),
        destination_identity=_as_str(destination.get("identity")),
        verdict=str(raw.get("verdict") or "UNKNOWN"),
        drop_reason=_as_str(raw.get("drop_reason")),
        protocol="tcp" if tcp else "udp" if udp else None,
        destination_port=destination_port or None,
        l7_protocol=_as_str(l7.get("protocol")),
        direction=_as_str(raw.get("direction")),
        policy=_extract_policy(raw.get("LABELS")),
    )

mutants_x__to_entry__mutmut['_mutmut_orig'] = x__to_entry__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_1'] = x__to_entry__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_2'] = x__to_entry__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_3'] = x__to_entry__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_4'] = x__to_entry__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_5'] = x__to_entry__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_6'] = x__to_entry__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_7'] = x__to_entry__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_8'] = x__to_entry__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_9'] = x__to_entry__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_10'] = x__to_entry__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_11'] = x__to_entry__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_12'] = x__to_entry__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_13'] = x__to_entry__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_14'] = x__to_entry__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_15'] = x__to_entry__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_16'] = x__to_entry__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_17'] = x__to_entry__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_18'] = x__to_entry__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_19'] = x__to_entry__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_20'] = x__to_entry__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_21'] = x__to_entry__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_22'] = x__to_entry__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_23'] = x__to_entry__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_24'] = x__to_entry__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_25'] = x__to_entry__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_26'] = x__to_entry__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_27'] = x__to_entry__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_28'] = x__to_entry__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_29'] = x__to_entry__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_30'] = x__to_entry__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_31'] = x__to_entry__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_32'] = x__to_entry__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_33'] = x__to_entry__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_34'] = x__to_entry__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_35'] = x__to_entry__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_36'] = x__to_entry__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_37'] = x__to_entry__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_38'] = x__to_entry__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_39'] = x__to_entry__mutmut_39 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_40'] = x__to_entry__mutmut_40 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_41'] = x__to_entry__mutmut_41 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_42'] = x__to_entry__mutmut_42 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_43'] = x__to_entry__mutmut_43 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_44'] = x__to_entry__mutmut_44 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_45'] = x__to_entry__mutmut_45 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_46'] = x__to_entry__mutmut_46 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_47'] = x__to_entry__mutmut_47 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_48'] = x__to_entry__mutmut_48 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_49'] = x__to_entry__mutmut_49 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_50'] = x__to_entry__mutmut_50 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_51'] = x__to_entry__mutmut_51 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_52'] = x__to_entry__mutmut_52 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_53'] = x__to_entry__mutmut_53 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_54'] = x__to_entry__mutmut_54 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_55'] = x__to_entry__mutmut_55 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_56'] = x__to_entry__mutmut_56 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_57'] = x__to_entry__mutmut_57 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_58'] = x__to_entry__mutmut_58 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_59'] = x__to_entry__mutmut_59 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_60'] = x__to_entry__mutmut_60 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_61'] = x__to_entry__mutmut_61 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_62'] = x__to_entry__mutmut_62 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_63'] = x__to_entry__mutmut_63 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_64'] = x__to_entry__mutmut_64 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_65'] = x__to_entry__mutmut_65 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_66'] = x__to_entry__mutmut_66 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_67'] = x__to_entry__mutmut_67 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_68'] = x__to_entry__mutmut_68 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_69'] = x__to_entry__mutmut_69 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_70'] = x__to_entry__mutmut_70 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_71'] = x__to_entry__mutmut_71 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_72'] = x__to_entry__mutmut_72 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_73'] = x__to_entry__mutmut_73 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_74'] = x__to_entry__mutmut_74 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_75'] = x__to_entry__mutmut_75 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_76'] = x__to_entry__mutmut_76 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_77'] = x__to_entry__mutmut_77 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_78'] = x__to_entry__mutmut_78 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_79'] = x__to_entry__mutmut_79 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_80'] = x__to_entry__mutmut_80 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_81'] = x__to_entry__mutmut_81 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_82'] = x__to_entry__mutmut_82 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_83'] = x__to_entry__mutmut_83 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_84'] = x__to_entry__mutmut_84 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_85'] = x__to_entry__mutmut_85 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_86'] = x__to_entry__mutmut_86 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_87'] = x__to_entry__mutmut_87 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_88'] = x__to_entry__mutmut_88 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_89'] = x__to_entry__mutmut_89 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_90'] = x__to_entry__mutmut_90 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_91'] = x__to_entry__mutmut_91 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_92'] = x__to_entry__mutmut_92 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_93'] = x__to_entry__mutmut_93 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_94'] = x__to_entry__mutmut_94 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_95'] = x__to_entry__mutmut_95 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_96'] = x__to_entry__mutmut_96 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_97'] = x__to_entry__mutmut_97 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_98'] = x__to_entry__mutmut_98 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_99'] = x__to_entry__mutmut_99 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_100'] = x__to_entry__mutmut_100 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_101'] = x__to_entry__mutmut_101 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_102'] = x__to_entry__mutmut_102 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_103'] = x__to_entry__mutmut_103 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_104'] = x__to_entry__mutmut_104 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_105'] = x__to_entry__mutmut_105 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_106'] = x__to_entry__mutmut_106 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_107'] = x__to_entry__mutmut_107 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_108'] = x__to_entry__mutmut_108 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_109'] = x__to_entry__mutmut_109 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_110'] = x__to_entry__mutmut_110 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_111'] = x__to_entry__mutmut_111 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_112'] = x__to_entry__mutmut_112 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_113'] = x__to_entry__mutmut_113 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_114'] = x__to_entry__mutmut_114 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_115'] = x__to_entry__mutmut_115 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_116'] = x__to_entry__mutmut_116 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_117'] = x__to_entry__mutmut_117 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_118'] = x__to_entry__mutmut_118 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_119'] = x__to_entry__mutmut_119 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_120'] = x__to_entry__mutmut_120 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_121'] = x__to_entry__mutmut_121 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_122'] = x__to_entry__mutmut_122 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_123'] = x__to_entry__mutmut_123 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_124'] = x__to_entry__mutmut_124 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_125'] = x__to_entry__mutmut_125 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_126'] = x__to_entry__mutmut_126 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_127'] = x__to_entry__mutmut_127 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_128'] = x__to_entry__mutmut_128 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_129'] = x__to_entry__mutmut_129 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_130'] = x__to_entry__mutmut_130 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_131'] = x__to_entry__mutmut_131 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_132'] = x__to_entry__mutmut_132 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_133'] = x__to_entry__mutmut_133 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_134'] = x__to_entry__mutmut_134 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_135'] = x__to_entry__mutmut_135 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_136'] = x__to_entry__mutmut_136 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_137'] = x__to_entry__mutmut_137 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_138'] = x__to_entry__mutmut_138 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_139'] = x__to_entry__mutmut_139 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_140'] = x__to_entry__mutmut_140 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_141'] = x__to_entry__mutmut_141 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_142'] = x__to_entry__mutmut_142 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_143'] = x__to_entry__mutmut_143 # type: ignore # mutmut generated
mutants_x__to_entry__mutmut['x__to_entry__mutmut_144'] = x__to_entry__mutmut_144 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_policy__mutmut)
def _extract_policy(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_orig(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_1(labels: object) -> str | None:
    if isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_2(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) and "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_3(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_4(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "XX=XX" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_5(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_6(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            break
        if "policy" not in label.lower():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_7(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "XXpolicyXX" not in label.lower():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_8(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "POLICY" not in label.lower():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_9(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" in label.lower():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_10(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.upper():
            continue
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_11(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            break
        value = label.split("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_12(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = None
        if value:
            return value
    return None


def x__extract_policy__mutmut_13(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split(None, 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_14(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("=", None)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_15(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split(1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_16(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("=", )[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_17(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.rsplit("=", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_18(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("XX=XX", 1)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_19(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("=", 2)[1]
        if value:
            return value
    return None


def x__extract_policy__mutmut_20(labels: object) -> str | None:
    if not isinstance(labels, list):
        return None
    for label in labels:
        if not isinstance(label, str) or "=" not in label:
            continue
        if "policy" not in label.lower():
            continue
        value = label.split("=", 1)[2]
        if value:
            return value
    return None

mutants_x__extract_policy__mutmut['_mutmut_orig'] = x__extract_policy__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_1'] = x__extract_policy__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_2'] = x__extract_policy__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_3'] = x__extract_policy__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_4'] = x__extract_policy__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_5'] = x__extract_policy__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_6'] = x__extract_policy__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_7'] = x__extract_policy__mutmut_7 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_8'] = x__extract_policy__mutmut_8 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_9'] = x__extract_policy__mutmut_9 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_10'] = x__extract_policy__mutmut_10 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_11'] = x__extract_policy__mutmut_11 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_12'] = x__extract_policy__mutmut_12 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_13'] = x__extract_policy__mutmut_13 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_14'] = x__extract_policy__mutmut_14 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_15'] = x__extract_policy__mutmut_15 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_16'] = x__extract_policy__mutmut_16 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_17'] = x__extract_policy__mutmut_17 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_18'] = x__extract_policy__mutmut_18 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_19'] = x__extract_policy__mutmut_19 # type: ignore # mutmut generated
mutants_x__extract_policy__mutmut['x__extract_policy__mutmut_20'] = x__extract_policy__mutmut_20 # type: ignore # mutmut generated
mutants_x__matches__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__matches__mutmut)
def _matches(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_orig(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_1(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace or not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_2(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_3(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(None, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_4(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, None):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_5(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_6(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, ):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_7(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return True
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_8(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod or query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_9(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_10(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return True
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_11(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction or query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_12(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.upper() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_13(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() == (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_14(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").upper():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_15(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction and "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_16(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "XXXX").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_17(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return True
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_18(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict or query.verdict.lower() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_19(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.upper() != entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_20(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() == entry.verdict.lower():
        return False
    return True


def x__matches__mutmut_21(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.upper():
        return False
    return True


def x__matches__mutmut_22(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return True
    return True


def x__matches__mutmut_23(entry: CiliumFlowEntry, query: CiliumFlowQuery) -> bool:
    if query.namespace and not _any_namespace(entry, query.namespace):
        return False
    if query.pod and query.pod not in (entry.source, entry.destination):
        return False
    if query.direction and query.direction.lower() != (entry.direction or "").lower():
        return False
    if query.verdict and query.verdict.lower() != entry.verdict.lower():
        return False
    return False

mutants_x__matches__mutmut['_mutmut_orig'] = x__matches__mutmut_orig # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_1'] = x__matches__mutmut_1 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_2'] = x__matches__mutmut_2 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_3'] = x__matches__mutmut_3 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_4'] = x__matches__mutmut_4 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_5'] = x__matches__mutmut_5 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_6'] = x__matches__mutmut_6 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_7'] = x__matches__mutmut_7 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_8'] = x__matches__mutmut_8 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_9'] = x__matches__mutmut_9 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_10'] = x__matches__mutmut_10 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_11'] = x__matches__mutmut_11 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_12'] = x__matches__mutmut_12 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_13'] = x__matches__mutmut_13 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_14'] = x__matches__mutmut_14 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_15'] = x__matches__mutmut_15 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_16'] = x__matches__mutmut_16 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_17'] = x__matches__mutmut_17 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_18'] = x__matches__mutmut_18 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_19'] = x__matches__mutmut_19 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_20'] = x__matches__mutmut_20 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_21'] = x__matches__mutmut_21 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_22'] = x__matches__mutmut_22 # type: ignore # mutmut generated
mutants_x__matches__mutmut['x__matches__mutmut_23'] = x__matches__mutmut_23 # type: ignore # mutmut generated
mutants_x__any_namespace__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__any_namespace__mutmut)
def _any_namespace(entry: CiliumFlowEntry, namespace: str) -> bool:
    return namespace in (entry.source_namespace, entry.destination_namespace)


def x__any_namespace__mutmut_orig(entry: CiliumFlowEntry, namespace: str) -> bool:
    return namespace in (entry.source_namespace, entry.destination_namespace)


def x__any_namespace__mutmut_1(entry: CiliumFlowEntry, namespace: str) -> bool:
    return namespace not in (entry.source_namespace, entry.destination_namespace)

mutants_x__any_namespace__mutmut['_mutmut_orig'] = x__any_namespace__mutmut_orig # type: ignore # mutmut generated
mutants_x__any_namespace__mutmut['x__any_namespace__mutmut_1'] = x__any_namespace__mutmut_1 # type: ignore # mutmut generated


def _as_dict(value: object) -> dict[str, object]:
    return value if isinstance(value, dict) else {}
mutants_x__as_str__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_str__mutmut)
def _as_str(value: object) -> str | None:
    return str(value) if value is not None else None


def x__as_str__mutmut_orig(value: object) -> str | None:
    return str(value) if value is not None else None


def x__as_str__mutmut_1(value: object) -> str | None:
    return str(None) if value is not None else None


def x__as_str__mutmut_2(value: object) -> str | None:
    return str(value) if value is None else None

mutants_x__as_str__mutmut['_mutmut_orig'] = x__as_str__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_str__mutmut['x__as_str__mutmut_1'] = x__as_str__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_str__mutmut['x__as_str__mutmut_2'] = x__as_str__mutmut_2 # type: ignore # mutmut generated
