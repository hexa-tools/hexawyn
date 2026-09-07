"""MCP tool: configuration_drift_detection — compares live Kubernetes
resources against their rendered Helm/Kustomize desired state, flagging
drifted fields and orphaned resources."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.configuration_drift_detection.command import (
    ConfigurationDriftDetectionCommand,
)
from hexawyn.application.use_case.security.configuration_drift_detection.configuration_drift_detection_use_case import (  # noqa: E501
    ConfigurationDriftDetectionUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_configuration_drift_detection__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_configuration_drift_detection__mutmut)
def configuration_drift_detection(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_orig(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_1(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = None
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_2(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=None,
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_3(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=None,
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_4(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=None,
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_5(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_6(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_7(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_8(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = None  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_9(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=None)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_10(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = None
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_11(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            None
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_12(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=None, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_13(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=None
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_14(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_15(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_16(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths and []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_17(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "XXdrifted_resourcesXX": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_18(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "DRIFTED_RESOURCES": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_19(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "XXdrifted_by_namespaceXX": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_20(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "DRIFTED_BY_NAMESPACE": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_21(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "XXin_sync_countXX": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_22(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "IN_SYNC_COUNT": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_23(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "XXexcluded_resourcesXX": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_24(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "EXCLUDED_RESOURCES": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_25(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "XXtotal_checkedXX": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_26(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "TOTAL_CHECKED": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_27(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "XXsummaryXX": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_28(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "SUMMARY": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_29(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "XXerrorXX": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_30(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "ERROR": r.error,
        }
    except Exception as exc:
        return {"error": str(exc)}


def x_configuration_drift_detection__mutmut_31(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"XXerrorXX": str(exc)}


def x_configuration_drift_detection__mutmut_32(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"ERROR": str(exc)}


def x_configuration_drift_detection__mutmut_33(
    namespace: str, kustomize_paths: list[str] | None = None
) -> dict[str, object]:
    from hexawyn.mcp.server import (
        build_helm_drift_adapter,
        build_kustomize_drift_adapter,
        build_live_resource_adapter,
    )

    try:
        service = ConfigurationDriftDetectionUseCase(
            live_resource_port=build_live_resource_adapter(),
            helm_adapter=build_helm_drift_adapter(),
            kustomize_adapter=build_kustomize_drift_adapter(),
        )
        use_case = ConfigurationDriftDetectionUseCase(service=service)  # type: ignore
        r = use_case.execute(  # type: ignore
            ConfigurationDriftDetectionCommand(
                namespace=namespace, kustomize_paths=kustomize_paths or []
            )
        )
        return {
            "drifted_resources": r.drifted_resources,
            "drifted_by_namespace": r.drifted_by_namespace,
            "in_sync_count": r.in_sync_count,
            "excluded_resources": r.excluded_resources,
            "total_checked": r.total_checked,
            "summary": r.summary,
            "error": r.error,
        }
    except Exception as exc:
        return {"error": str(None)}

mutants_x_configuration_drift_detection__mutmut['_mutmut_orig'] = x_configuration_drift_detection__mutmut_orig # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_1'] = x_configuration_drift_detection__mutmut_1 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_2'] = x_configuration_drift_detection__mutmut_2 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_3'] = x_configuration_drift_detection__mutmut_3 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_4'] = x_configuration_drift_detection__mutmut_4 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_5'] = x_configuration_drift_detection__mutmut_5 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_6'] = x_configuration_drift_detection__mutmut_6 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_7'] = x_configuration_drift_detection__mutmut_7 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_8'] = x_configuration_drift_detection__mutmut_8 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_9'] = x_configuration_drift_detection__mutmut_9 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_10'] = x_configuration_drift_detection__mutmut_10 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_11'] = x_configuration_drift_detection__mutmut_11 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_12'] = x_configuration_drift_detection__mutmut_12 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_13'] = x_configuration_drift_detection__mutmut_13 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_14'] = x_configuration_drift_detection__mutmut_14 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_15'] = x_configuration_drift_detection__mutmut_15 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_16'] = x_configuration_drift_detection__mutmut_16 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_17'] = x_configuration_drift_detection__mutmut_17 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_18'] = x_configuration_drift_detection__mutmut_18 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_19'] = x_configuration_drift_detection__mutmut_19 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_20'] = x_configuration_drift_detection__mutmut_20 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_21'] = x_configuration_drift_detection__mutmut_21 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_22'] = x_configuration_drift_detection__mutmut_22 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_23'] = x_configuration_drift_detection__mutmut_23 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_24'] = x_configuration_drift_detection__mutmut_24 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_25'] = x_configuration_drift_detection__mutmut_25 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_26'] = x_configuration_drift_detection__mutmut_26 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_27'] = x_configuration_drift_detection__mutmut_27 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_28'] = x_configuration_drift_detection__mutmut_28 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_29'] = x_configuration_drift_detection__mutmut_29 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_30'] = x_configuration_drift_detection__mutmut_30 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_31'] = x_configuration_drift_detection__mutmut_31 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_32'] = x_configuration_drift_detection__mutmut_32 # type: ignore # mutmut generated
mutants_x_configuration_drift_detection__mutmut['x_configuration_drift_detection__mutmut_33'] = x_configuration_drift_detection__mutmut_33 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(configuration_drift_detection)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(configuration_drift_detection)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
