import os
from importlib.metadata import EntryPoint, entry_points
from typing import cast

from hexawyn.adapters.provider_registry import CloudProvider
from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort

ENTRY_POINT_GROUP = "hexawyn.providers"


def _discover_entry_points() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = cast(dict[str, list[EntryPoint]], entry_points())
        return list(all_eps.get(ENTRY_POINT_GROUP, []))


def build_adapters(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter  # hexa-lazy-import

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "name": cluster_name,
        "cluster": cluster_name,
        "provider": "unknown",
        "namespace": "default",
    }

    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], ep.load())
            if provider_cls.supports(context):
                return provider_cls.build(context)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def list_installed_providers() -> list[type[CloudProvider]]:
    """Return all installed CloudProvider classes (used by /config providers)."""
    providers: list[type[CloudProvider]] = []
    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], ep.load())
            providers.append(provider_cls)
        except Exception:
            continue
    return providers
