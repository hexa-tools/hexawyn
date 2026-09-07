"""MCP tool: resource_yaml — Get YAML definition of a k8s resource with secrets redacted."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.cluster.resource_yaml.command import (
    ResourceYamlCommand,
)
from hexawyn.application.use_case.cluster.resource_yaml.resource_yaml_use_case import (
    ResourceYAMLUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_resource_yaml__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_resource_yaml__mutmut)
def resource_yaml(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_orig(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_1(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = None
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_2(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = None
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_3(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            None  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_4(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=None).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_5(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=None, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_6(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=None, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_7(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=None)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_8(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_9(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_10(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, )  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_11(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "XXresource_nameXX": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_12(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "RESOURCE_NAME": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_13(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "XXnamespaceXX": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_14(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "NAMESPACE": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_15(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "XXkindXX": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_16(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "KIND": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_17(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "XXresource_foundXX": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_18(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "RESOURCE_FOUND": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_19(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "XXyaml_dataXX": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_20(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "YAML_DATA": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_21(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "XXimage_tagsXX": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_22(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "IMAGE_TAGS": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_23(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "XXresource_limitsXX": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_24(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "RESOURCE_LIMITS": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_25(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_26(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_27(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXresource_nameXX": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_28(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"RESOURCE_NAME": resource_name, "error": str(exc)}


def x_resource_yaml__mutmut_29(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "XXerrorXX": str(exc)}


def x_resource_yaml__mutmut_30(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "ERROR": str(exc)}


def x_resource_yaml__mutmut_31(resource_name: str, namespace: str, kind: str) -> dict[str, object]:
    from hexawyn.mcp.server import build_resource_yaml_adapter

    try:
        a = build_resource_yaml_adapter()
        r = ResourceYAMLUseCase(port=a).execute(
            ResourceYamlCommand(resource_name=resource_name, namespace=namespace, kind=kind)  # type: ignore
        )
        return {
            "resource_name": r.resource_name,
            "namespace": r.namespace,
            "kind": r.kind,
            "resource_found": r.resource_found,
            "yaml_data": r.yaml_data,
            "image_tags": r.image_tags,
            "resource_limits": r.resource_limits,
            "error": r.error,
        }
    except Exception as exc:
        return {"resource_name": resource_name, "error": str(None)}

mutants_x_resource_yaml__mutmut['_mutmut_orig'] = x_resource_yaml__mutmut_orig # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_1'] = x_resource_yaml__mutmut_1 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_2'] = x_resource_yaml__mutmut_2 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_3'] = x_resource_yaml__mutmut_3 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_4'] = x_resource_yaml__mutmut_4 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_5'] = x_resource_yaml__mutmut_5 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_6'] = x_resource_yaml__mutmut_6 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_7'] = x_resource_yaml__mutmut_7 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_8'] = x_resource_yaml__mutmut_8 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_9'] = x_resource_yaml__mutmut_9 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_10'] = x_resource_yaml__mutmut_10 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_11'] = x_resource_yaml__mutmut_11 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_12'] = x_resource_yaml__mutmut_12 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_13'] = x_resource_yaml__mutmut_13 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_14'] = x_resource_yaml__mutmut_14 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_15'] = x_resource_yaml__mutmut_15 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_16'] = x_resource_yaml__mutmut_16 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_17'] = x_resource_yaml__mutmut_17 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_18'] = x_resource_yaml__mutmut_18 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_19'] = x_resource_yaml__mutmut_19 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_20'] = x_resource_yaml__mutmut_20 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_21'] = x_resource_yaml__mutmut_21 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_22'] = x_resource_yaml__mutmut_22 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_23'] = x_resource_yaml__mutmut_23 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_24'] = x_resource_yaml__mutmut_24 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_25'] = x_resource_yaml__mutmut_25 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_26'] = x_resource_yaml__mutmut_26 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_27'] = x_resource_yaml__mutmut_27 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_28'] = x_resource_yaml__mutmut_28 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_29'] = x_resource_yaml__mutmut_29 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_30'] = x_resource_yaml__mutmut_30 # type: ignore # mutmut generated
mutants_x_resource_yaml__mutmut['x_resource_yaml__mutmut_31'] = x_resource_yaml__mutmut_31 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(resource_yaml)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(resource_yaml)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
