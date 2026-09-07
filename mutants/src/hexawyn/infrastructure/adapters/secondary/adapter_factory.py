import os
from importlib.metadata import EntryPoint, entry_points
from typing import cast

from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort
from hexawyn.infrastructure.adapters.provider_registry import CloudProvider

ENTRY_POINT_GROUP = "hexawyn.providers"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__discover_entry_points__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__discover_entry_points__mutmut)
def _discover_entry_points() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = cast(dict[str, list[EntryPoint]], entry_points())
        return list(all_eps.get(ENTRY_POINT_GROUP, []))


def x__discover_entry_points__mutmut_orig() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = cast(dict[str, list[EntryPoint]], entry_points())
        return list(all_eps.get(ENTRY_POINT_GROUP, []))


def x__discover_entry_points__mutmut_1() -> list[EntryPoint]:
    try:
        return list(None)
    except TypeError:
        all_eps = cast(dict[str, list[EntryPoint]], entry_points())
        return list(all_eps.get(ENTRY_POINT_GROUP, []))


def x__discover_entry_points__mutmut_2() -> list[EntryPoint]:
    try:
        return list(entry_points(group=None))
    except TypeError:
        all_eps = cast(dict[str, list[EntryPoint]], entry_points())
        return list(all_eps.get(ENTRY_POINT_GROUP, []))


def x__discover_entry_points__mutmut_3() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = None
        return list(all_eps.get(ENTRY_POINT_GROUP, []))


def x__discover_entry_points__mutmut_4() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = cast(None, entry_points())
        return list(all_eps.get(ENTRY_POINT_GROUP, []))


def x__discover_entry_points__mutmut_5() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = cast(dict[str, list[EntryPoint]], None)
        return list(all_eps.get(ENTRY_POINT_GROUP, []))


def x__discover_entry_points__mutmut_6() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = cast(entry_points())
        return list(all_eps.get(ENTRY_POINT_GROUP, []))


def x__discover_entry_points__mutmut_7() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = cast(dict[str, list[EntryPoint]], )
        return list(all_eps.get(ENTRY_POINT_GROUP, []))


def x__discover_entry_points__mutmut_8() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = cast(dict[str, list[EntryPoint]], entry_points())
        return list(None)


def x__discover_entry_points__mutmut_9() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = cast(dict[str, list[EntryPoint]], entry_points())
        return list(all_eps.get(None, []))


def x__discover_entry_points__mutmut_10() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = cast(dict[str, list[EntryPoint]], entry_points())
        return list(all_eps.get(ENTRY_POINT_GROUP, None))


def x__discover_entry_points__mutmut_11() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = cast(dict[str, list[EntryPoint]], entry_points())
        return list(all_eps.get([]))


def x__discover_entry_points__mutmut_12() -> list[EntryPoint]:
    try:
        return list(entry_points(group=ENTRY_POINT_GROUP))
    except TypeError:
        all_eps = cast(dict[str, list[EntryPoint]], entry_points())
        return list(all_eps.get(ENTRY_POINT_GROUP, ))

mutants_x__discover_entry_points__mutmut['_mutmut_orig'] = x__discover_entry_points__mutmut_orig # type: ignore # mutmut generated
mutants_x__discover_entry_points__mutmut['x__discover_entry_points__mutmut_1'] = x__discover_entry_points__mutmut_1 # type: ignore # mutmut generated
mutants_x__discover_entry_points__mutmut['x__discover_entry_points__mutmut_2'] = x__discover_entry_points__mutmut_2 # type: ignore # mutmut generated
mutants_x__discover_entry_points__mutmut['x__discover_entry_points__mutmut_3'] = x__discover_entry_points__mutmut_3 # type: ignore # mutmut generated
mutants_x__discover_entry_points__mutmut['x__discover_entry_points__mutmut_4'] = x__discover_entry_points__mutmut_4 # type: ignore # mutmut generated
mutants_x__discover_entry_points__mutmut['x__discover_entry_points__mutmut_5'] = x__discover_entry_points__mutmut_5 # type: ignore # mutmut generated
mutants_x__discover_entry_points__mutmut['x__discover_entry_points__mutmut_6'] = x__discover_entry_points__mutmut_6 # type: ignore # mutmut generated
mutants_x__discover_entry_points__mutmut['x__discover_entry_points__mutmut_7'] = x__discover_entry_points__mutmut_7 # type: ignore # mutmut generated
mutants_x__discover_entry_points__mutmut['x__discover_entry_points__mutmut_8'] = x__discover_entry_points__mutmut_8 # type: ignore # mutmut generated
mutants_x__discover_entry_points__mutmut['x__discover_entry_points__mutmut_9'] = x__discover_entry_points__mutmut_9 # type: ignore # mutmut generated
mutants_x__discover_entry_points__mutmut['x__discover_entry_points__mutmut_10'] = x__discover_entry_points__mutmut_10 # type: ignore # mutmut generated
mutants_x__discover_entry_points__mutmut['x__discover_entry_points__mutmut_11'] = x__discover_entry_points__mutmut_11 # type: ignore # mutmut generated
mutants_x__discover_entry_points__mutmut['x__discover_entry_points__mutmut_12'] = x__discover_entry_points__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_adapters__mutmut)
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
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_orig(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_1(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = None
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_2(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").upper() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_3(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get(None, "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_4(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", None).lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_5(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_6(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", ).lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_7(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("XXHEXAWYN_DEMO_MODEXX", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_8(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("hexawyn_demo_mode", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_9(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "XXfalseXX").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_10(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "FALSE").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_11(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() != "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_12(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "XXtrueXX"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_13(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "TRUE"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_14(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = None
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_15(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get(None, "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_16(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", None)
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_17(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_18(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", )
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_19(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("XXHEXAWYN_DEMO_SCENARIOXX", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_20(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("hexawyn_demo_scenario", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_21(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "XXaws_eksXX")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_22(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "AWS_EKS")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_23(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=None)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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


def x_build_adapters__mutmut_24(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = None

    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], ep.load())
            if provider_cls.supports(context):
                return provider_cls.build(context)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_25(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "XXnameXX": cluster_name,
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


def x_build_adapters__mutmut_26(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "NAME": cluster_name,
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


def x_build_adapters__mutmut_27(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "name": cluster_name,
        "XXclusterXX": cluster_name,
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


def x_build_adapters__mutmut_28(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "name": cluster_name,
        "CLUSTER": cluster_name,
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


def x_build_adapters__mutmut_29(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "name": cluster_name,
        "cluster": cluster_name,
        "XXproviderXX": "unknown",
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


def x_build_adapters__mutmut_30(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "name": cluster_name,
        "cluster": cluster_name,
        "PROVIDER": "unknown",
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


def x_build_adapters__mutmut_31(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "name": cluster_name,
        "cluster": cluster_name,
        "provider": "XXunknownXX",
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


def x_build_adapters__mutmut_32(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "name": cluster_name,
        "cluster": cluster_name,
        "provider": "UNKNOWN",
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


def x_build_adapters__mutmut_33(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "name": cluster_name,
        "cluster": cluster_name,
        "provider": "unknown",
        "XXnamespaceXX": "default",
    }

    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], ep.load())
            if provider_cls.supports(context):
                return provider_cls.build(context)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_34(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "name": cluster_name,
        "cluster": cluster_name,
        "provider": "unknown",
        "NAMESPACE": "default",
    }

    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], ep.load())
            if provider_cls.supports(context):
                return provider_cls.build(context)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_35(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "name": cluster_name,
        "cluster": cluster_name,
        "provider": "unknown",
        "namespace": "XXdefaultXX",
    }

    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], ep.load())
            if provider_cls.supports(context):
                return provider_cls.build(context)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_36(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
        VanillaAdapter,  # hexa-lazy-import
    )

    context: ClusterContext = {
        "name": cluster_name,
        "cluster": cluster_name,
        "provider": "unknown",
        "namespace": "DEFAULT",
    }

    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], ep.load())
            if provider_cls.supports(context):
                return provider_cls.build(context)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_37(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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
            provider_cls = None
            if provider_cls.supports(context):
                return provider_cls.build(context)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_38(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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
            provider_cls = cast(None, ep.load())
            if provider_cls.supports(context):
                return provider_cls.build(context)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_39(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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
            provider_cls = cast(type[CloudProvider], None)
            if provider_cls.supports(context):
                return provider_cls.build(context)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_40(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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
            provider_cls = cast(ep.load())
            if provider_cls.supports(context):
                return provider_cls.build(context)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_41(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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
            provider_cls = cast(type[CloudProvider], )
            if provider_cls.supports(context):
                return provider_cls.build(context)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_42(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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
            if provider_cls.supports(None):
                return provider_cls.build(context)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_43(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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
                return provider_cls.build(None)
        except Exception:
            continue

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_44(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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
            break

    return VanillaAdapter(cluster_name)


def x_build_adapters__mutmut_45(cluster_name: str) -> K8sPort:
    """
    Select and return the appropriate adapter for the given cluster.

    Priority:
    1. HEXAWYN_DEMO_MODE=true → DemoAdapter (always wins)
    2. Entry points discovery → any installed CloudProvider
    3. VanillaAdapter → always available as fallback
    """
    demo_mode = os.environ.get("HEXAWYN_DEMO_MODE", "false").lower() == "true"
    if demo_mode:
        from hexawyn.infrastructure.adapters.secondary.mock.demo_adapter import (
            DemoAdapter,  # hexa-lazy-import
        )

        scenario = os.environ.get("HEXAWYN_DEMO_SCENARIO", "aws_eks")
        return DemoAdapter(scenario=scenario)

    from hexawyn.infrastructure.adapters.secondary.vanilla.vanilla_adapter import (
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

    return VanillaAdapter(None)

mutants_x_build_adapters__mutmut['_mutmut_orig'] = x_build_adapters__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_1'] = x_build_adapters__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_2'] = x_build_adapters__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_3'] = x_build_adapters__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_4'] = x_build_adapters__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_5'] = x_build_adapters__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_6'] = x_build_adapters__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_7'] = x_build_adapters__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_8'] = x_build_adapters__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_9'] = x_build_adapters__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_10'] = x_build_adapters__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_11'] = x_build_adapters__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_12'] = x_build_adapters__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_13'] = x_build_adapters__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_14'] = x_build_adapters__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_15'] = x_build_adapters__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_16'] = x_build_adapters__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_17'] = x_build_adapters__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_18'] = x_build_adapters__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_19'] = x_build_adapters__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_20'] = x_build_adapters__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_21'] = x_build_adapters__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_22'] = x_build_adapters__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_23'] = x_build_adapters__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_24'] = x_build_adapters__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_25'] = x_build_adapters__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_26'] = x_build_adapters__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_27'] = x_build_adapters__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_28'] = x_build_adapters__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_29'] = x_build_adapters__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_30'] = x_build_adapters__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_31'] = x_build_adapters__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_32'] = x_build_adapters__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_33'] = x_build_adapters__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_34'] = x_build_adapters__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_35'] = x_build_adapters__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_36'] = x_build_adapters__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_37'] = x_build_adapters__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_38'] = x_build_adapters__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_39'] = x_build_adapters__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_40'] = x_build_adapters__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_41'] = x_build_adapters__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_42'] = x_build_adapters__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_43'] = x_build_adapters__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_44'] = x_build_adapters__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_adapters__mutmut['x_build_adapters__mutmut_45'] = x_build_adapters__mutmut_45 # type: ignore # mutmut generated
mutants_x_list_installed_providers__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_installed_providers__mutmut)
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


def x_list_installed_providers__mutmut_orig() -> list[type[CloudProvider]]:
    """Return all installed CloudProvider classes (used by /config providers)."""
    providers: list[type[CloudProvider]] = []
    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], ep.load())
            providers.append(provider_cls)
        except Exception:
            continue
    return providers


def x_list_installed_providers__mutmut_1() -> list[type[CloudProvider]]:
    """Return all installed CloudProvider classes (used by /config providers)."""
    providers: list[type[CloudProvider]] = None
    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], ep.load())
            providers.append(provider_cls)
        except Exception:
            continue
    return providers


def x_list_installed_providers__mutmut_2() -> list[type[CloudProvider]]:
    """Return all installed CloudProvider classes (used by /config providers)."""
    providers: list[type[CloudProvider]] = []
    for ep in _discover_entry_points():
        try:
            provider_cls = None
            providers.append(provider_cls)
        except Exception:
            continue
    return providers


def x_list_installed_providers__mutmut_3() -> list[type[CloudProvider]]:
    """Return all installed CloudProvider classes (used by /config providers)."""
    providers: list[type[CloudProvider]] = []
    for ep in _discover_entry_points():
        try:
            provider_cls = cast(None, ep.load())
            providers.append(provider_cls)
        except Exception:
            continue
    return providers


def x_list_installed_providers__mutmut_4() -> list[type[CloudProvider]]:
    """Return all installed CloudProvider classes (used by /config providers)."""
    providers: list[type[CloudProvider]] = []
    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], None)
            providers.append(provider_cls)
        except Exception:
            continue
    return providers


def x_list_installed_providers__mutmut_5() -> list[type[CloudProvider]]:
    """Return all installed CloudProvider classes (used by /config providers)."""
    providers: list[type[CloudProvider]] = []
    for ep in _discover_entry_points():
        try:
            provider_cls = cast(ep.load())
            providers.append(provider_cls)
        except Exception:
            continue
    return providers


def x_list_installed_providers__mutmut_6() -> list[type[CloudProvider]]:
    """Return all installed CloudProvider classes (used by /config providers)."""
    providers: list[type[CloudProvider]] = []
    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], )
            providers.append(provider_cls)
        except Exception:
            continue
    return providers


def x_list_installed_providers__mutmut_7() -> list[type[CloudProvider]]:
    """Return all installed CloudProvider classes (used by /config providers)."""
    providers: list[type[CloudProvider]] = []
    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], ep.load())
            providers.append(None)
        except Exception:
            continue
    return providers


def x_list_installed_providers__mutmut_8() -> list[type[CloudProvider]]:
    """Return all installed CloudProvider classes (used by /config providers)."""
    providers: list[type[CloudProvider]] = []
    for ep in _discover_entry_points():
        try:
            provider_cls = cast(type[CloudProvider], ep.load())
            providers.append(provider_cls)
        except Exception:
            break
    return providers

mutants_x_list_installed_providers__mutmut['_mutmut_orig'] = x_list_installed_providers__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_installed_providers__mutmut['x_list_installed_providers__mutmut_1'] = x_list_installed_providers__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_installed_providers__mutmut['x_list_installed_providers__mutmut_2'] = x_list_installed_providers__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_installed_providers__mutmut['x_list_installed_providers__mutmut_3'] = x_list_installed_providers__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_installed_providers__mutmut['x_list_installed_providers__mutmut_4'] = x_list_installed_providers__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_installed_providers__mutmut['x_list_installed_providers__mutmut_5'] = x_list_installed_providers__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_installed_providers__mutmut['x_list_installed_providers__mutmut_6'] = x_list_installed_providers__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_installed_providers__mutmut['x_list_installed_providers__mutmut_7'] = x_list_installed_providers__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_installed_providers__mutmut['x_list_installed_providers__mutmut_8'] = x_list_installed_providers__mutmut_8 # type: ignore # mutmut generated
