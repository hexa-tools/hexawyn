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
