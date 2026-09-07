"""MCP tool: calico_segmentation_audit — Calico east-west matrix."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_segmentation_audit.calico_segmentation_audit_use_case import (  # noqa: E501
    CalicoSegmentationAuditUseCase,
)
from hexawyn.application.use_case.calico.calico_segmentation_audit.command import (
    CalicoSegmentationAuditCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__edge_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__edge_dict__mutmut)
def _edge_dict(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_orig(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_1(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "XXsourceXX": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_2(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "SOURCE": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_3(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(None, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_4(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, None, None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_5(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr("source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_6(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_7(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", ),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_8(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "XXsourceXX", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_9(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "SOURCE", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_10(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "XXdestinationXX": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_11(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "DESTINATION": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_12(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(None, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_13(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, None, None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_14(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr("destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_15(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_16(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", ),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_17(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "XXdestinationXX", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_18(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "DESTINATION", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_19(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "XXrestrictedXX": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_20(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "RESTRICTED": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_21(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(None, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_22(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, None, False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_23(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", None),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_24(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr("restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_25(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_26(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", ),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_27(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "XXrestrictedXX", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_28(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "RESTRICTED", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_29(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", True),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_30(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "XXselectorsXX": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_31(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "SELECTORS": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_32(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(None),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_33(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(None, "selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_34(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, None, ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_35(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", None)),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_36(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr("selectors", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_37(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_38(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", )),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_39(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "XXselectorsXX", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_40(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "SELECTORS", ())),
        "note": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_41(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "XXnoteXX": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_42(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "NOTE": getattr(edge, "note", None),
    }


def x__edge_dict__mutmut_43(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(None, "note", None),
    }


def x__edge_dict__mutmut_44(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, None, None),
    }


def x__edge_dict__mutmut_45(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr("note", None),
    }


def x__edge_dict__mutmut_46(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, None),
    }


def x__edge_dict__mutmut_47(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "note", ),
    }


def x__edge_dict__mutmut_48(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "XXnoteXX", None),
    }


def x__edge_dict__mutmut_49(edge: object) -> dict[str, object]:
    """Project a CalicoSegmentationEdge into a plain, serialisable dict."""
    return {
        "source": getattr(edge, "source", None),
        "destination": getattr(edge, "destination", None),
        "restricted": getattr(edge, "restricted", False),
        "selectors": list(getattr(edge, "selectors", ())),
        "note": getattr(edge, "NOTE", None),
    }

mutants_x__edge_dict__mutmut['_mutmut_orig'] = x__edge_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_1'] = x__edge_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_2'] = x__edge_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_3'] = x__edge_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_4'] = x__edge_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_5'] = x__edge_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_6'] = x__edge_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_7'] = x__edge_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_8'] = x__edge_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_9'] = x__edge_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_10'] = x__edge_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_11'] = x__edge_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_12'] = x__edge_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_13'] = x__edge_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_14'] = x__edge_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_15'] = x__edge_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_16'] = x__edge_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_17'] = x__edge_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_18'] = x__edge_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_19'] = x__edge_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_20'] = x__edge_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_21'] = x__edge_dict__mutmut_21 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_22'] = x__edge_dict__mutmut_22 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_23'] = x__edge_dict__mutmut_23 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_24'] = x__edge_dict__mutmut_24 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_25'] = x__edge_dict__mutmut_25 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_26'] = x__edge_dict__mutmut_26 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_27'] = x__edge_dict__mutmut_27 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_28'] = x__edge_dict__mutmut_28 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_29'] = x__edge_dict__mutmut_29 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_30'] = x__edge_dict__mutmut_30 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_31'] = x__edge_dict__mutmut_31 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_32'] = x__edge_dict__mutmut_32 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_33'] = x__edge_dict__mutmut_33 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_34'] = x__edge_dict__mutmut_34 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_35'] = x__edge_dict__mutmut_35 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_36'] = x__edge_dict__mutmut_36 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_37'] = x__edge_dict__mutmut_37 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_38'] = x__edge_dict__mutmut_38 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_39'] = x__edge_dict__mutmut_39 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_40'] = x__edge_dict__mutmut_40 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_41'] = x__edge_dict__mutmut_41 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_42'] = x__edge_dict__mutmut_42 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_43'] = x__edge_dict__mutmut_43 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_44'] = x__edge_dict__mutmut_44 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_45'] = x__edge_dict__mutmut_45 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_46'] = x__edge_dict__mutmut_46 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_47'] = x__edge_dict__mutmut_47 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_48'] = x__edge_dict__mutmut_48 # type: ignore # mutmut generated
mutants_x__edge_dict__mutmut['x__edge_dict__mutmut_49'] = x__edge_dict__mutmut_49 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calico_segmentation_audit__mutmut)
def calico_segmentation_audit(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_orig(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_1(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = None
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_2(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=None)
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_3(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = None
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_4(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=None,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_5(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=None,
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_6(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_7(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_8(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces and (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_9(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = None
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_10(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_11(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "XXinstalledXX": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_12(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "INSTALLED": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_13(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "XXnot_installed_markerXX": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_14(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "NOT_INSTALLED_MARKER": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_15(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "XXviewXX": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_16(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "VIEW": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_17(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "XXtiersXX": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_18(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "TIERS": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_19(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(None),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_20(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "XXedgesXX": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_21(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "EDGES": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_22(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(None) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_23(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "XXgap_countXX": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_24(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "GAP_COUNT": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_25(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "XXtotal_pathsXX": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_26(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "TOTAL_PATHS": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_27(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "XXsummaryXX": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_28(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "SUMMARY": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_29(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_30(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_31(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_32(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_33(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_34(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXnot_installed_markerXX": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_35(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "NOT_INSTALLED_MARKER": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_36(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "XXNOT_INSTALLEDXX",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_37(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "not_installed",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_38(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "XXviewXX": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_39(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "VIEW": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_40(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "XXvanillaXX",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_41(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "VANILLA",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_42(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "XXtiersXX": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_43(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "TIERS": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_44(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "XXedgesXX": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_45(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "EDGES": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_46(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "XXgap_countXX": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_47(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "GAP_COUNT": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_48(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 1,
            "total_paths": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_49(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "XXtotal_pathsXX": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_50(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "TOTAL_PATHS": 0,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_51(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 1,
            "summary": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_52(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "XXsummaryXX": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_53(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "SUMMARY": None,
            "error": str(exc),
        }


def x_calico_segmentation_audit__mutmut_54(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "XXerrorXX": str(exc),
        }


def x_calico_segmentation_audit__mutmut_55(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "ERROR": str(exc),
        }


def x_calico_segmentation_audit__mutmut_56(
    namespace: str | None = None, excluded_namespaces: tuple[str, ...] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoSegmentationAuditUseCase(port=build_calico_adapter())
        command = CalicoSegmentationAuditCommand(
            namespace=namespace,
            excluded_namespaces=excluded_namespaces or (),
        )
        result = use_case.execute(command)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "view": result.view,
            "tiers": list(result.tiers),
            "edges": [_edge_dict(edge) for edge in result.edges],
            "gap_count": result.gap_count,
            "total_paths": result.total_paths,
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "view": "vanilla",
            "tiers": [],
            "edges": [],
            "gap_count": 0,
            "total_paths": 0,
            "summary": None,
            "error": str(None),
        }

mutants_x_calico_segmentation_audit__mutmut['_mutmut_orig'] = x_calico_segmentation_audit__mutmut_orig # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_1'] = x_calico_segmentation_audit__mutmut_1 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_2'] = x_calico_segmentation_audit__mutmut_2 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_3'] = x_calico_segmentation_audit__mutmut_3 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_4'] = x_calico_segmentation_audit__mutmut_4 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_5'] = x_calico_segmentation_audit__mutmut_5 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_6'] = x_calico_segmentation_audit__mutmut_6 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_7'] = x_calico_segmentation_audit__mutmut_7 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_8'] = x_calico_segmentation_audit__mutmut_8 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_9'] = x_calico_segmentation_audit__mutmut_9 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_10'] = x_calico_segmentation_audit__mutmut_10 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_11'] = x_calico_segmentation_audit__mutmut_11 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_12'] = x_calico_segmentation_audit__mutmut_12 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_13'] = x_calico_segmentation_audit__mutmut_13 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_14'] = x_calico_segmentation_audit__mutmut_14 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_15'] = x_calico_segmentation_audit__mutmut_15 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_16'] = x_calico_segmentation_audit__mutmut_16 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_17'] = x_calico_segmentation_audit__mutmut_17 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_18'] = x_calico_segmentation_audit__mutmut_18 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_19'] = x_calico_segmentation_audit__mutmut_19 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_20'] = x_calico_segmentation_audit__mutmut_20 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_21'] = x_calico_segmentation_audit__mutmut_21 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_22'] = x_calico_segmentation_audit__mutmut_22 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_23'] = x_calico_segmentation_audit__mutmut_23 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_24'] = x_calico_segmentation_audit__mutmut_24 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_25'] = x_calico_segmentation_audit__mutmut_25 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_26'] = x_calico_segmentation_audit__mutmut_26 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_27'] = x_calico_segmentation_audit__mutmut_27 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_28'] = x_calico_segmentation_audit__mutmut_28 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_29'] = x_calico_segmentation_audit__mutmut_29 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_30'] = x_calico_segmentation_audit__mutmut_30 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_31'] = x_calico_segmentation_audit__mutmut_31 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_32'] = x_calico_segmentation_audit__mutmut_32 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_33'] = x_calico_segmentation_audit__mutmut_33 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_34'] = x_calico_segmentation_audit__mutmut_34 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_35'] = x_calico_segmentation_audit__mutmut_35 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_36'] = x_calico_segmentation_audit__mutmut_36 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_37'] = x_calico_segmentation_audit__mutmut_37 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_38'] = x_calico_segmentation_audit__mutmut_38 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_39'] = x_calico_segmentation_audit__mutmut_39 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_40'] = x_calico_segmentation_audit__mutmut_40 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_41'] = x_calico_segmentation_audit__mutmut_41 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_42'] = x_calico_segmentation_audit__mutmut_42 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_43'] = x_calico_segmentation_audit__mutmut_43 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_44'] = x_calico_segmentation_audit__mutmut_44 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_45'] = x_calico_segmentation_audit__mutmut_45 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_46'] = x_calico_segmentation_audit__mutmut_46 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_47'] = x_calico_segmentation_audit__mutmut_47 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_48'] = x_calico_segmentation_audit__mutmut_48 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_49'] = x_calico_segmentation_audit__mutmut_49 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_50'] = x_calico_segmentation_audit__mutmut_50 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_51'] = x_calico_segmentation_audit__mutmut_51 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_52'] = x_calico_segmentation_audit__mutmut_52 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_53'] = x_calico_segmentation_audit__mutmut_53 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_54'] = x_calico_segmentation_audit__mutmut_54 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_55'] = x_calico_segmentation_audit__mutmut_55 # type: ignore # mutmut generated
mutants_x_calico_segmentation_audit__mutmut['x_calico_segmentation_audit__mutmut_56'] = x_calico_segmentation_audit__mutmut_56 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_segmentation_audit)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(calico_segmentation_audit)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
