"""MCP tool: get_cilium_network_policy — full detail of one Cilium policy."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cilium.get_cilium_network_policy.command import (
    GetCiliumNetworkPolicyCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_network_policy.get_cilium_network_policy_use_case import (  # noqa: E501
    GetCiliumNetworkPolicyUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_cilium_network_policy__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_cilium_network_policy__mutmut)
def get_cilium_network_policy(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_orig(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_1(name: str = "XXXX", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_2(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = None
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_3(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = None
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_4(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=None)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_5(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = None
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_6(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(None)
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_7(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=None, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_8(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=None))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_9(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_10(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, ))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_11(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "XXinstalledXX": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_12(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "INSTALLED": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_13(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "XXstatusXX": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_14(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "STATUS": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_15(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "XXkindXX": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_16(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "KIND": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_17(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "XXnameXX": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_18(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "NAME": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_19(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "XXnamespaceXX": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_20(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "NAMESPACE": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_21(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "XXendpoint_selectorXX": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_22(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "ENDPOINT_SELECTOR": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_23(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "XXingress_rulesXX": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_24(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "INGRESS_RULES": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_25(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "XXegress_rulesXX": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_26(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "EGRESS_RULES": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_27(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "XXl7_protocolsXX": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_28(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "L7_PROTOCOLS": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_29(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "XXspecXX": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_30(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "SPEC": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_31(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "XXnoteXX": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_32(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "NOTE": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_33(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "XXerrorXX": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_34(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "ERROR": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_35(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "XXinstalledXX": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_36(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "INSTALLED": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_37(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": True,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_38(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "XXstatusXX": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_39(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "STATUS": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_40(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "XXunknownXX",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_41(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "UNKNOWN",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_42(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "XXkindXX": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_43(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "KIND": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_44(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "XXXX",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_45(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "XXnameXX": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_46(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "NAME": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_47(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "XXXX",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_48(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "XXnamespaceXX": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_49(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "NAMESPACE": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_50(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "XXendpoint_selectorXX": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_51(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "ENDPOINT_SELECTOR": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_52(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "XXXX",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_53(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "XXingress_rulesXX": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_54(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "INGRESS_RULES": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_55(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "XXegress_rulesXX": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_56(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "EGRESS_RULES": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_57(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "XXl7_protocolsXX": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_58(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "L7_PROTOCOLS": [],
            "spec": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_59(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "XXspecXX": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_60(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "SPEC": {},
            "note": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_61(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "XXnoteXX": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_62(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "NOTE": None,
            "error": str(exc),
        }


def x_get_cilium_network_policy__mutmut_63(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "XXerrorXX": str(exc),
        }


def x_get_cilium_network_policy__mutmut_64(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "ERROR": str(exc),
        }


def x_get_cilium_network_policy__mutmut_65(name: str = "", namespace: str | None = None) -> dict[str, object]:
    from hexawyn.mcp.server import build_cilium_adapter

    try:
        adapter = build_cilium_adapter()
        use_case = GetCiliumNetworkPolicyUseCase(port=adapter)
        result = use_case.execute(GetCiliumNetworkPolicyCommand(name=name, namespace=namespace))
        return {
            "installed": result.installed,
            "status": result.status,
            "kind": result.kind,
            "name": result.name,
            "namespace": result.namespace,
            "endpoint_selector": result.endpoint_selector,
            "ingress_rules": result.ingress_rules,
            "egress_rules": result.egress_rules,
            "l7_protocols": result.l7_protocols,
            "spec": result.spec,
            "note": result.note,
            "error": result.error,
        }
    except Exception as exc:
        return {
            "installed": False,
            "status": "unknown",
            "kind": "",
            "name": "",
            "namespace": None,
            "endpoint_selector": "",
            "ingress_rules": [],
            "egress_rules": [],
            "l7_protocols": [],
            "spec": {},
            "note": None,
            "error": str(None),
        }

mutants_x_get_cilium_network_policy__mutmut['_mutmut_orig'] = x_get_cilium_network_policy__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_1'] = x_get_cilium_network_policy__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_2'] = x_get_cilium_network_policy__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_3'] = x_get_cilium_network_policy__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_4'] = x_get_cilium_network_policy__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_5'] = x_get_cilium_network_policy__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_6'] = x_get_cilium_network_policy__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_7'] = x_get_cilium_network_policy__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_8'] = x_get_cilium_network_policy__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_9'] = x_get_cilium_network_policy__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_10'] = x_get_cilium_network_policy__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_11'] = x_get_cilium_network_policy__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_12'] = x_get_cilium_network_policy__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_13'] = x_get_cilium_network_policy__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_14'] = x_get_cilium_network_policy__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_15'] = x_get_cilium_network_policy__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_16'] = x_get_cilium_network_policy__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_17'] = x_get_cilium_network_policy__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_18'] = x_get_cilium_network_policy__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_19'] = x_get_cilium_network_policy__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_20'] = x_get_cilium_network_policy__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_21'] = x_get_cilium_network_policy__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_22'] = x_get_cilium_network_policy__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_23'] = x_get_cilium_network_policy__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_24'] = x_get_cilium_network_policy__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_25'] = x_get_cilium_network_policy__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_26'] = x_get_cilium_network_policy__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_27'] = x_get_cilium_network_policy__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_28'] = x_get_cilium_network_policy__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_29'] = x_get_cilium_network_policy__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_30'] = x_get_cilium_network_policy__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_31'] = x_get_cilium_network_policy__mutmut_31 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_32'] = x_get_cilium_network_policy__mutmut_32 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_33'] = x_get_cilium_network_policy__mutmut_33 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_34'] = x_get_cilium_network_policy__mutmut_34 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_35'] = x_get_cilium_network_policy__mutmut_35 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_36'] = x_get_cilium_network_policy__mutmut_36 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_37'] = x_get_cilium_network_policy__mutmut_37 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_38'] = x_get_cilium_network_policy__mutmut_38 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_39'] = x_get_cilium_network_policy__mutmut_39 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_40'] = x_get_cilium_network_policy__mutmut_40 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_41'] = x_get_cilium_network_policy__mutmut_41 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_42'] = x_get_cilium_network_policy__mutmut_42 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_43'] = x_get_cilium_network_policy__mutmut_43 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_44'] = x_get_cilium_network_policy__mutmut_44 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_45'] = x_get_cilium_network_policy__mutmut_45 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_46'] = x_get_cilium_network_policy__mutmut_46 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_47'] = x_get_cilium_network_policy__mutmut_47 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_48'] = x_get_cilium_network_policy__mutmut_48 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_49'] = x_get_cilium_network_policy__mutmut_49 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_50'] = x_get_cilium_network_policy__mutmut_50 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_51'] = x_get_cilium_network_policy__mutmut_51 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_52'] = x_get_cilium_network_policy__mutmut_52 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_53'] = x_get_cilium_network_policy__mutmut_53 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_54'] = x_get_cilium_network_policy__mutmut_54 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_55'] = x_get_cilium_network_policy__mutmut_55 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_56'] = x_get_cilium_network_policy__mutmut_56 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_57'] = x_get_cilium_network_policy__mutmut_57 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_58'] = x_get_cilium_network_policy__mutmut_58 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_59'] = x_get_cilium_network_policy__mutmut_59 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_60'] = x_get_cilium_network_policy__mutmut_60 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_61'] = x_get_cilium_network_policy__mutmut_61 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_62'] = x_get_cilium_network_policy__mutmut_62 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_63'] = x_get_cilium_network_policy__mutmut_63 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_64'] = x_get_cilium_network_policy__mutmut_64 # type: ignore # mutmut generated
mutants_x_get_cilium_network_policy__mutmut['x_get_cilium_network_policy__mutmut_65'] = x_get_cilium_network_policy__mutmut_65 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(get_cilium_network_policy)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(get_cilium_network_policy)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
