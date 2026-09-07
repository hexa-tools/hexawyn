"""MCP tool: calico_encryption_status — Calico WireGuard encryption status."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.calico.calico_encryption_status.calico_encryption_status_use_case import (  # noqa: E501
    CalicoEncryptionStatusUseCase,
)
from hexawyn.application.use_case.calico.calico_encryption_status.command import (
    CalicoEncryptionStatusCommand,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__node_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__node_dict__mutmut)
def _node_dict(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_orig(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_1(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "XXnodeXX": getattr(node, "node", None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_2(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "NODE": getattr(node, "node", None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_3(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(None, "node", None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_4(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, None, None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_5(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr("node", None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_6(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_7(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", ),
        "wireguard_enabled": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_8(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "XXnodeXX", None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_9(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "NODE", None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_10(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "XXwireguard_enabledXX": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_11(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "WIREGUARD_ENABLED": getattr(node, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_12(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "wireguard_enabled": getattr(None, "wireguard_enabled", False),
    }


def x__node_dict__mutmut_13(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "wireguard_enabled": getattr(node, None, False),
    }


def x__node_dict__mutmut_14(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", None),
    }


def x__node_dict__mutmut_15(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "wireguard_enabled": getattr("wireguard_enabled", False),
    }


def x__node_dict__mutmut_16(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "wireguard_enabled": getattr(node, False),
    }


def x__node_dict__mutmut_17(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", ),
    }


def x__node_dict__mutmut_18(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "wireguard_enabled": getattr(node, "XXwireguard_enabledXX", False),
    }


def x__node_dict__mutmut_19(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "wireguard_enabled": getattr(node, "WIREGUARD_ENABLED", False),
    }


def x__node_dict__mutmut_20(node: object) -> dict[str, object]:
    """Project a CalicoEncryptionNodeStatus into a plain, serialisable dict."""
    return {
        "node": getattr(node, "node", None),
        "wireguard_enabled": getattr(node, "wireguard_enabled", True),
    }

mutants_x__node_dict__mutmut['_mutmut_orig'] = x__node_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_1'] = x__node_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_2'] = x__node_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_3'] = x__node_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_4'] = x__node_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_5'] = x__node_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_6'] = x__node_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_7'] = x__node_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_8'] = x__node_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_9'] = x__node_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_10'] = x__node_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_11'] = x__node_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_12'] = x__node_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_13'] = x__node_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_14'] = x__node_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_15'] = x__node_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_16'] = x__node_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_17'] = x__node_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_18'] = x__node_dict__mutmut_18 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_19'] = x__node_dict__mutmut_19 # type: ignore # mutmut generated
mutants_x__node_dict__mutmut['x__node_dict__mutmut_20'] = x__node_dict__mutmut_20 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calico_encryption_status__mutmut)
def calico_encryption_status() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_orig() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_1() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = None
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_2() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=None)
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_3() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = None
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_4() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_5() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "XXinstalledXX": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_6() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "INSTALLED": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_7() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "XXnot_installed_markerXX": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_8() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "NOT_INSTALLED_MARKER": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_9() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "XXwireguard_enabledXX": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_10() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "WIREGUARD_ENABLED": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_11() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "XXmodeXX": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_12() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "MODE": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_13() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "XXper_nodeXX": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_14() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "PER_NODE": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_15() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(None) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_16() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "XXsummaryXX": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_17() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "SUMMARY": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_18() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_19() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_20() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_21() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_22() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_23() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXnot_installed_markerXX": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_24() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "NOT_INSTALLED_MARKER": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_25() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "XXNOT_INSTALLEDXX",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_26() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "not_installed",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_27() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "XXwireguard_enabledXX": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_28() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "WIREGUARD_ENABLED": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_29() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "XXmodeXX": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_30() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "MODE": None,
            "per_node": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_31() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "XXper_nodeXX": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_32() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "PER_NODE": [],
            "summary": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_33() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "XXsummaryXX": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_34() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "SUMMARY": None,
            "error": str(exc),
        }


def x_calico_encryption_status__mutmut_35() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "XXerrorXX": str(exc),
        }


def x_calico_encryption_status__mutmut_36() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "ERROR": str(exc),
        }


def x_calico_encryption_status__mutmut_37() -> dict[str, object]:
    from hexawyn.mcp.server import build_calico_adapter

    try:
        use_case = CalicoEncryptionStatusUseCase(port=build_calico_adapter())
        result = use_case.execute(CalicoEncryptionStatusCommand())
        return {
            "installed": result.installed,
            "not_installed_marker": result.not_installed_marker,
            "wireguard_enabled": result.wireguard_enabled,
            "mode": result.mode,
            "per_node": [_node_dict(node) for node in result.per_node],
            "summary": result.summary,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "not_installed_marker": "NOT_INSTALLED",
            "wireguard_enabled": None,
            "mode": None,
            "per_node": [],
            "summary": None,
            "error": str(None),
        }

mutants_x_calico_encryption_status__mutmut['_mutmut_orig'] = x_calico_encryption_status__mutmut_orig # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_1'] = x_calico_encryption_status__mutmut_1 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_2'] = x_calico_encryption_status__mutmut_2 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_3'] = x_calico_encryption_status__mutmut_3 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_4'] = x_calico_encryption_status__mutmut_4 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_5'] = x_calico_encryption_status__mutmut_5 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_6'] = x_calico_encryption_status__mutmut_6 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_7'] = x_calico_encryption_status__mutmut_7 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_8'] = x_calico_encryption_status__mutmut_8 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_9'] = x_calico_encryption_status__mutmut_9 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_10'] = x_calico_encryption_status__mutmut_10 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_11'] = x_calico_encryption_status__mutmut_11 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_12'] = x_calico_encryption_status__mutmut_12 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_13'] = x_calico_encryption_status__mutmut_13 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_14'] = x_calico_encryption_status__mutmut_14 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_15'] = x_calico_encryption_status__mutmut_15 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_16'] = x_calico_encryption_status__mutmut_16 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_17'] = x_calico_encryption_status__mutmut_17 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_18'] = x_calico_encryption_status__mutmut_18 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_19'] = x_calico_encryption_status__mutmut_19 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_20'] = x_calico_encryption_status__mutmut_20 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_21'] = x_calico_encryption_status__mutmut_21 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_22'] = x_calico_encryption_status__mutmut_22 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_23'] = x_calico_encryption_status__mutmut_23 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_24'] = x_calico_encryption_status__mutmut_24 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_25'] = x_calico_encryption_status__mutmut_25 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_26'] = x_calico_encryption_status__mutmut_26 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_27'] = x_calico_encryption_status__mutmut_27 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_28'] = x_calico_encryption_status__mutmut_28 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_29'] = x_calico_encryption_status__mutmut_29 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_30'] = x_calico_encryption_status__mutmut_30 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_31'] = x_calico_encryption_status__mutmut_31 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_32'] = x_calico_encryption_status__mutmut_32 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_33'] = x_calico_encryption_status__mutmut_33 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_34'] = x_calico_encryption_status__mutmut_34 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_35'] = x_calico_encryption_status__mutmut_35 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_36'] = x_calico_encryption_status__mutmut_36 # type: ignore # mutmut generated
mutants_x_calico_encryption_status__mutmut['x_calico_encryption_status__mutmut_37'] = x_calico_encryption_status__mutmut_37 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(calico_encryption_status)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(calico_encryption_status)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
