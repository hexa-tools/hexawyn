"""MCP tool: gitops_app_get — Get ArgoCD/Flux application details."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.gitops.gitops_app_get.command import GitopsAppGetCommand
from hexawyn.application.use_case.gitops.gitops_app_get.gitops_app_get_use_case import (
    GitopsAppGetUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_gitops_app_get__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_gitops_app_get__mutmut)
def gitops_app_get(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_orig(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_1(name: str, namespace: str = "XXdefaultXX") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_2(name: str, namespace: str = "DEFAULT") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_3(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = None
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_4(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=None)
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_5(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = None
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_6(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(None)
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_7(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=None, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_8(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=None))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_9(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_10(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, ))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_11(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "XXnameXX": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_12(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "NAME": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_13(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "XXnamespaceXX": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_14(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "NAMESPACE": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_15(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "XXengineXX": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_16(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "ENGINE": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_17(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "XXkindXX": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_18(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "KIND": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_19(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "XXsync_statusXX": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_20(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "SYNC_STATUS": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_21(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "XXhealth_statusXX": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_22(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "HEALTH_STATUS": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_23(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "XXerrorXX": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_24(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "ERROR": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_25(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "XXnameXX": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_26(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "NAME": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_27(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "XXnamespaceXX": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_28(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "NAMESPACE": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_29(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "XXengineXX": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_30(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "ENGINE": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_31(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "XXXX",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_32(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "XXkindXX": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_33(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "KIND": "",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_34(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "XXXX",
            "sync_status": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_35(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "XXsync_statusXX": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_36(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "SYNC_STATUS": "",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_37(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "XXXX",
            "health_status": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_38(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "XXhealth_statusXX": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_39(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "HEALTH_STATUS": "",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_40(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "XXXX",
            "error": str(exc),
        }


def x_gitops_app_get__mutmut_41(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "XXerrorXX": str(exc),
        }


def x_gitops_app_get__mutmut_42(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "ERROR": str(exc),
        }


def x_gitops_app_get__mutmut_43(name: str, namespace: str = "default") -> dict[str, object]:
    """Get full details of a GitOps application (ArgoCD or Flux).

    Args:
        name: Application name.
        namespace: Kubernetes namespace (default: default).
    """
    from hexawyn.mcp.server import build_gitops_adapter

    try:
        use_case = GitopsAppGetUseCase(gitops_port=build_gitops_adapter())
        response = use_case.execute(GitopsAppGetCommand(name=name, namespace=namespace))
        return {
            "name": response.name,
            "namespace": response.namespace,
            "engine": response.engine,
            "kind": response.kind,
            "sync_status": response.sync_status,
            "health_status": response.health_status,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "name": name,
            "namespace": namespace,
            "engine": "",
            "kind": "",
            "sync_status": "",
            "health_status": "",
            "error": str(None),
        }

mutants_x_gitops_app_get__mutmut['_mutmut_orig'] = x_gitops_app_get__mutmut_orig # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_1'] = x_gitops_app_get__mutmut_1 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_2'] = x_gitops_app_get__mutmut_2 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_3'] = x_gitops_app_get__mutmut_3 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_4'] = x_gitops_app_get__mutmut_4 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_5'] = x_gitops_app_get__mutmut_5 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_6'] = x_gitops_app_get__mutmut_6 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_7'] = x_gitops_app_get__mutmut_7 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_8'] = x_gitops_app_get__mutmut_8 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_9'] = x_gitops_app_get__mutmut_9 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_10'] = x_gitops_app_get__mutmut_10 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_11'] = x_gitops_app_get__mutmut_11 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_12'] = x_gitops_app_get__mutmut_12 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_13'] = x_gitops_app_get__mutmut_13 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_14'] = x_gitops_app_get__mutmut_14 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_15'] = x_gitops_app_get__mutmut_15 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_16'] = x_gitops_app_get__mutmut_16 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_17'] = x_gitops_app_get__mutmut_17 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_18'] = x_gitops_app_get__mutmut_18 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_19'] = x_gitops_app_get__mutmut_19 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_20'] = x_gitops_app_get__mutmut_20 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_21'] = x_gitops_app_get__mutmut_21 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_22'] = x_gitops_app_get__mutmut_22 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_23'] = x_gitops_app_get__mutmut_23 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_24'] = x_gitops_app_get__mutmut_24 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_25'] = x_gitops_app_get__mutmut_25 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_26'] = x_gitops_app_get__mutmut_26 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_27'] = x_gitops_app_get__mutmut_27 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_28'] = x_gitops_app_get__mutmut_28 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_29'] = x_gitops_app_get__mutmut_29 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_30'] = x_gitops_app_get__mutmut_30 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_31'] = x_gitops_app_get__mutmut_31 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_32'] = x_gitops_app_get__mutmut_32 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_33'] = x_gitops_app_get__mutmut_33 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_34'] = x_gitops_app_get__mutmut_34 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_35'] = x_gitops_app_get__mutmut_35 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_36'] = x_gitops_app_get__mutmut_36 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_37'] = x_gitops_app_get__mutmut_37 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_38'] = x_gitops_app_get__mutmut_38 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_39'] = x_gitops_app_get__mutmut_39 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_40'] = x_gitops_app_get__mutmut_40 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_41'] = x_gitops_app_get__mutmut_41 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_42'] = x_gitops_app_get__mutmut_42 # type: ignore # mutmut generated
mutants_x_gitops_app_get__mutmut['x_gitops_app_get__mutmut_43'] = x_gitops_app_get__mutmut_43 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(gitops_app_get)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(gitops_app_get)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
