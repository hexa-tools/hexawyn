"""MCP tool: detect_cilium_denials — detect Cilium policy denials via Hubble."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.detect_cilium_denials.command import (
    DetectCiliumDenialsCommand,
)
from hexawyn.application.use_case.cilium.detect_cilium_denials.detect_cilium_denials_use_case import (  # noqa: E501
    DetectCiliumDenialsUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_detect_cilium_denials__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_detect_cilium_denials__mutmut)
def detect_cilium_denials(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_orig(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_1(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 6,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_2(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 101,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_3(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = None
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_4(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = None
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_5(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=None)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_6(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = None
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_7(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            None
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_8(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=None,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_9(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=None,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_10(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=None,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_11(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_12(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_13(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_14(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "XXinstalledXX": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_15(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "INSTALLED": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_16(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "XXstatusXX": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_17(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "STATUS": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_18(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "XXtotal_denialsXX": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_19(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "TOTAL_DENIALS": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_20(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "XXgroupsXX": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_21(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "GROUPS": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_22(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "XXnoteXX": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_23(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "NOTE": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_24(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_25(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_26(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_27(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_28(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_29(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXstatusXX": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_30(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "STATUS": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_31(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "XXunknownXX",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_32(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "UNKNOWN",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_33(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "XXtotal_denialsXX": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_34(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "TOTAL_DENIALS": 0,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_35(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 1,
            "groups": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_36(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "XXgroupsXX": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_37(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "GROUPS": [],
            "note": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_38(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "XXnoteXX": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_39(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "NOTE": None,
            "error": str(exc),
        }


def x_detect_cilium_denials__mutmut_40(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "XXerrorXX": str(exc),
        }


def x_detect_cilium_denials__mutmut_41(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "ERROR": str(exc),
        }


def x_detect_cilium_denials__mutmut_42(  # noqa: PLR0913
    namespace: str | None = None,
    window_minutes: int = 5,
    limit: int = 100,
) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_hubble_adapter

    try:
        adapter = build_cilium_hubble_adapter()
        use_case = DetectCiliumDenialsUseCase(port=adapter)
        result = use_case.execute(
            DetectCiliumDenialsCommand(
                namespace=namespace,
                window_minutes=window_minutes,
                limit=limit,
            )
        )
        return {
            "installed": result.installed,
            "status": result.status,
            "total_denials": result.total_denials,
            "groups": result.groups,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "total_denials": 0,
            "groups": [],
            "note": None,
            "error": str(None),
        }

mutants_x_detect_cilium_denials__mutmut['_mutmut_orig'] = x_detect_cilium_denials__mutmut_orig # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_1'] = x_detect_cilium_denials__mutmut_1 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_2'] = x_detect_cilium_denials__mutmut_2 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_3'] = x_detect_cilium_denials__mutmut_3 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_4'] = x_detect_cilium_denials__mutmut_4 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_5'] = x_detect_cilium_denials__mutmut_5 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_6'] = x_detect_cilium_denials__mutmut_6 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_7'] = x_detect_cilium_denials__mutmut_7 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_8'] = x_detect_cilium_denials__mutmut_8 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_9'] = x_detect_cilium_denials__mutmut_9 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_10'] = x_detect_cilium_denials__mutmut_10 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_11'] = x_detect_cilium_denials__mutmut_11 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_12'] = x_detect_cilium_denials__mutmut_12 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_13'] = x_detect_cilium_denials__mutmut_13 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_14'] = x_detect_cilium_denials__mutmut_14 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_15'] = x_detect_cilium_denials__mutmut_15 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_16'] = x_detect_cilium_denials__mutmut_16 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_17'] = x_detect_cilium_denials__mutmut_17 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_18'] = x_detect_cilium_denials__mutmut_18 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_19'] = x_detect_cilium_denials__mutmut_19 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_20'] = x_detect_cilium_denials__mutmut_20 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_21'] = x_detect_cilium_denials__mutmut_21 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_22'] = x_detect_cilium_denials__mutmut_22 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_23'] = x_detect_cilium_denials__mutmut_23 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_24'] = x_detect_cilium_denials__mutmut_24 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_25'] = x_detect_cilium_denials__mutmut_25 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_26'] = x_detect_cilium_denials__mutmut_26 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_27'] = x_detect_cilium_denials__mutmut_27 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_28'] = x_detect_cilium_denials__mutmut_28 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_29'] = x_detect_cilium_denials__mutmut_29 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_30'] = x_detect_cilium_denials__mutmut_30 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_31'] = x_detect_cilium_denials__mutmut_31 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_32'] = x_detect_cilium_denials__mutmut_32 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_33'] = x_detect_cilium_denials__mutmut_33 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_34'] = x_detect_cilium_denials__mutmut_34 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_35'] = x_detect_cilium_denials__mutmut_35 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_36'] = x_detect_cilium_denials__mutmut_36 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_37'] = x_detect_cilium_denials__mutmut_37 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_38'] = x_detect_cilium_denials__mutmut_38 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_39'] = x_detect_cilium_denials__mutmut_39 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_40'] = x_detect_cilium_denials__mutmut_40 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_41'] = x_detect_cilium_denials__mutmut_41 # type: ignore # mutmut generated
mutants_x_detect_cilium_denials__mutmut['x_detect_cilium_denials__mutmut_42'] = x_detect_cilium_denials__mutmut_42 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(detect_cilium_denials)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(detect_cilium_denials)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
