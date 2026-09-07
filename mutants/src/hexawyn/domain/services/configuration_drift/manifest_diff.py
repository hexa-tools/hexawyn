from __future__ import annotations

from hexawyn.domain.models.configuration_drift import DriftResult, ManagedBy, ResourceManifest
from hexawyn.domain.services.configuration_drift.field_comparison import (
    compare_dict_field,
    compare_scalar_field,
    get_configmap_data,
    get_env_vars,
    get_image,
    get_labels,
    get_replicas,
    get_resource_limits,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compare_resource__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compare_resource__mutmut)
def compare_resource(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_orig(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_1(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is not None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_2(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=None,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_3(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=None,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_4(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=None,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_5(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=None,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_6(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=None,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_7(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=None,
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_8(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=None,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_9(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=None,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_10(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_11(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_12(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_13(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_14(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_15(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_16(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_17(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_18(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=True,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_19(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=False,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_20(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = None
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_21(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field(None, get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_22(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", None, get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_23(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), None, live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_24(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), None),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_25(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field(get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_26(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_27(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_28(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), ),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_29(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("XXimageXX", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_30(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("IMAGE", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_31(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(None), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_32(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(None), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_33(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            None, get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_34(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", None, get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_35(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), None, live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_36(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), None
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_37(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_38(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_39(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_40(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_41(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "XXreplicasXX", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_42(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "REPLICAS", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_43(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(None), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_44(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(None), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_45(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            None, get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_46(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", None, get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_47(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), None, live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_48(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), None
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_49(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_50(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_51(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_52(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_53(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "XXenv_varsXX", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_54(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "ENV_VARS", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_55(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(None), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_56(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(None), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_57(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            None,
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_58(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            None,
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_59(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            None,
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_60(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            None,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_61(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_62(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_63(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_64(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_65(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "XXresource_limitsXX",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_66(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "RESOURCE_LIMITS",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_67(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(None),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_68(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(None),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_69(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field(None, get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_70(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", None, get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_71(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), None, live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_72(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), None),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_73(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field(get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_74(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_75(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_76(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), ),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_77(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("XXlabelsXX", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_78(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("LABELS", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_79(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(None), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_80(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(None), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_81(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind != "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_82(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "XXConfigMapXX":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_83(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "configmap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_84(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "CONFIGMAP":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_85(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields = compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_86(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields -= compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_87(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            None,
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_88(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            None,
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_89(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            None,
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_90(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            None,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_91(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_92(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_93(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_94(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_95(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "XXconfigmap_dataXX",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_96(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "CONFIGMAP_DATA",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_97(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(None),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_98(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(None),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_99(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=None,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_100(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=None,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_101(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=None,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_102(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=None,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_103(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=None,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_104(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=None,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_105(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=None,
        is_orphaned=False,
    )


def x_compare_resource__mutmut_106(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=None,
    )


def x_compare_resource__mutmut_107(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_108(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_109(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_110(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_111(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_112(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_113(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        is_orphaned=False,
    )


def x_compare_resource__mutmut_114(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        )


def x_compare_resource__mutmut_115(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(None),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_116(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity != "critical" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_117(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "XXcriticalXX" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_118(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "CRITICAL" for field in fields),
        is_orphaned=False,
    )


def x_compare_resource__mutmut_119(
    desired: ResourceManifest | None,
    live: ResourceManifest,
    managed_by: ManagedBy,
    release_or_source: str,
) -> DriftResult:
    """A missing desired manifest means the resource's owning Helm release
    (or Kustomize source) no longer exists — orphaned, not "no drift"."""
    if desired is None:
        return DriftResult(
            kind=live.kind,
            name=live.name,
            namespace=live.namespace,
            managed_by=managed_by,
            release_or_source=release_or_source,
            drifted_fields=[],
            has_critical_drift=False,
            is_orphaned=True,
        )

    fields = [
        *compare_scalar_field("image", get_image(desired.data), get_image(live.data), live.kind),
        *compare_scalar_field(
            "replicas", get_replicas(desired.data), get_replicas(live.data), live.kind
        ),
        *compare_dict_field(
            "env_vars", get_env_vars(desired.data), get_env_vars(live.data), live.kind
        ),
        *compare_dict_field(
            "resource_limits",
            get_resource_limits(desired.data),
            get_resource_limits(live.data),
            live.kind,
        ),
        *compare_dict_field("labels", get_labels(desired.data), get_labels(live.data), live.kind),
    ]
    if live.kind == "ConfigMap":
        fields += compare_dict_field(
            "configmap_data",
            get_configmap_data(desired.data),
            get_configmap_data(live.data),
            live.kind,
        )

    return DriftResult(
        kind=live.kind,
        name=live.name,
        namespace=live.namespace,
        managed_by=managed_by,
        release_or_source=release_or_source,
        drifted_fields=fields,
        has_critical_drift=any(field.severity == "critical" for field in fields),
        is_orphaned=True,
    )

mutants_x_compare_resource__mutmut['_mutmut_orig'] = x_compare_resource__mutmut_orig # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_1'] = x_compare_resource__mutmut_1 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_2'] = x_compare_resource__mutmut_2 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_3'] = x_compare_resource__mutmut_3 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_4'] = x_compare_resource__mutmut_4 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_5'] = x_compare_resource__mutmut_5 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_6'] = x_compare_resource__mutmut_6 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_7'] = x_compare_resource__mutmut_7 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_8'] = x_compare_resource__mutmut_8 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_9'] = x_compare_resource__mutmut_9 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_10'] = x_compare_resource__mutmut_10 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_11'] = x_compare_resource__mutmut_11 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_12'] = x_compare_resource__mutmut_12 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_13'] = x_compare_resource__mutmut_13 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_14'] = x_compare_resource__mutmut_14 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_15'] = x_compare_resource__mutmut_15 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_16'] = x_compare_resource__mutmut_16 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_17'] = x_compare_resource__mutmut_17 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_18'] = x_compare_resource__mutmut_18 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_19'] = x_compare_resource__mutmut_19 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_20'] = x_compare_resource__mutmut_20 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_21'] = x_compare_resource__mutmut_21 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_22'] = x_compare_resource__mutmut_22 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_23'] = x_compare_resource__mutmut_23 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_24'] = x_compare_resource__mutmut_24 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_25'] = x_compare_resource__mutmut_25 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_26'] = x_compare_resource__mutmut_26 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_27'] = x_compare_resource__mutmut_27 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_28'] = x_compare_resource__mutmut_28 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_29'] = x_compare_resource__mutmut_29 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_30'] = x_compare_resource__mutmut_30 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_31'] = x_compare_resource__mutmut_31 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_32'] = x_compare_resource__mutmut_32 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_33'] = x_compare_resource__mutmut_33 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_34'] = x_compare_resource__mutmut_34 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_35'] = x_compare_resource__mutmut_35 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_36'] = x_compare_resource__mutmut_36 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_37'] = x_compare_resource__mutmut_37 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_38'] = x_compare_resource__mutmut_38 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_39'] = x_compare_resource__mutmut_39 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_40'] = x_compare_resource__mutmut_40 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_41'] = x_compare_resource__mutmut_41 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_42'] = x_compare_resource__mutmut_42 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_43'] = x_compare_resource__mutmut_43 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_44'] = x_compare_resource__mutmut_44 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_45'] = x_compare_resource__mutmut_45 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_46'] = x_compare_resource__mutmut_46 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_47'] = x_compare_resource__mutmut_47 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_48'] = x_compare_resource__mutmut_48 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_49'] = x_compare_resource__mutmut_49 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_50'] = x_compare_resource__mutmut_50 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_51'] = x_compare_resource__mutmut_51 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_52'] = x_compare_resource__mutmut_52 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_53'] = x_compare_resource__mutmut_53 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_54'] = x_compare_resource__mutmut_54 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_55'] = x_compare_resource__mutmut_55 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_56'] = x_compare_resource__mutmut_56 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_57'] = x_compare_resource__mutmut_57 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_58'] = x_compare_resource__mutmut_58 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_59'] = x_compare_resource__mutmut_59 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_60'] = x_compare_resource__mutmut_60 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_61'] = x_compare_resource__mutmut_61 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_62'] = x_compare_resource__mutmut_62 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_63'] = x_compare_resource__mutmut_63 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_64'] = x_compare_resource__mutmut_64 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_65'] = x_compare_resource__mutmut_65 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_66'] = x_compare_resource__mutmut_66 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_67'] = x_compare_resource__mutmut_67 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_68'] = x_compare_resource__mutmut_68 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_69'] = x_compare_resource__mutmut_69 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_70'] = x_compare_resource__mutmut_70 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_71'] = x_compare_resource__mutmut_71 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_72'] = x_compare_resource__mutmut_72 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_73'] = x_compare_resource__mutmut_73 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_74'] = x_compare_resource__mutmut_74 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_75'] = x_compare_resource__mutmut_75 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_76'] = x_compare_resource__mutmut_76 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_77'] = x_compare_resource__mutmut_77 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_78'] = x_compare_resource__mutmut_78 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_79'] = x_compare_resource__mutmut_79 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_80'] = x_compare_resource__mutmut_80 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_81'] = x_compare_resource__mutmut_81 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_82'] = x_compare_resource__mutmut_82 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_83'] = x_compare_resource__mutmut_83 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_84'] = x_compare_resource__mutmut_84 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_85'] = x_compare_resource__mutmut_85 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_86'] = x_compare_resource__mutmut_86 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_87'] = x_compare_resource__mutmut_87 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_88'] = x_compare_resource__mutmut_88 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_89'] = x_compare_resource__mutmut_89 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_90'] = x_compare_resource__mutmut_90 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_91'] = x_compare_resource__mutmut_91 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_92'] = x_compare_resource__mutmut_92 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_93'] = x_compare_resource__mutmut_93 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_94'] = x_compare_resource__mutmut_94 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_95'] = x_compare_resource__mutmut_95 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_96'] = x_compare_resource__mutmut_96 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_97'] = x_compare_resource__mutmut_97 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_98'] = x_compare_resource__mutmut_98 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_99'] = x_compare_resource__mutmut_99 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_100'] = x_compare_resource__mutmut_100 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_101'] = x_compare_resource__mutmut_101 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_102'] = x_compare_resource__mutmut_102 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_103'] = x_compare_resource__mutmut_103 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_104'] = x_compare_resource__mutmut_104 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_105'] = x_compare_resource__mutmut_105 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_106'] = x_compare_resource__mutmut_106 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_107'] = x_compare_resource__mutmut_107 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_108'] = x_compare_resource__mutmut_108 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_109'] = x_compare_resource__mutmut_109 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_110'] = x_compare_resource__mutmut_110 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_111'] = x_compare_resource__mutmut_111 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_112'] = x_compare_resource__mutmut_112 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_113'] = x_compare_resource__mutmut_113 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_114'] = x_compare_resource__mutmut_114 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_115'] = x_compare_resource__mutmut_115 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_116'] = x_compare_resource__mutmut_116 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_117'] = x_compare_resource__mutmut_117 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_118'] = x_compare_resource__mutmut_118 # type: ignore # mutmut generated
mutants_x_compare_resource__mutmut['x_compare_resource__mutmut_119'] = x_compare_resource__mutmut_119 # type: ignore # mutmut generated
