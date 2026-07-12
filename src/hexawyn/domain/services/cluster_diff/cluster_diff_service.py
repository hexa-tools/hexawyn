from __future__ import annotations

from hexawyn.application.ports.driven.cluster_diff_port import (
    ClusterInventoryData,
    ResourceInventoryRaw,
)
from hexawyn.domain.models.cluster_diff import (
    ClusterDiffReport,
    PromotionChecklist,
    ResourceDiff,
)


def compute_diff(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason != "secret_manual"]
    review = [diff.resource for diff in version_mismatches]

    sync = "in_sync" if not in_staging_not_prod and not prod_only else "out_of_sync"

    return ClusterDiffReport(
        source_cluster=staging["cluster_name"],
        target_cluster=prod["cluster_name"],
        in_staging_not_prod=missing,
        version_mismatches=version_mismatches,
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def _key(resource: ResourceInventoryRaw) -> str:
    return f"{resource['kind']}/{resource['name']}/{resource['namespace']}"


def _spec(resource: ResourceInventoryRaw) -> str:
    return f"{resource['kind']}/{resource['name']}"


def _index_by_key(
    resources: list[ResourceInventoryRaw],
) -> dict[str, ResourceInventoryRaw]:
    return {_key(resource): resource for resource in resources}


def _missing(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in resources:
        key = _key(resource)
        if key not in target_map:
            is_secret = resource.get("is_secret", False)
            diffs.append(
                ResourceDiff(
                    resource=_spec(resource),
                    namespace=str(resource["namespace"]),
                    reason="secret_manual" if is_secret else "never_promoted",
                    priority=priority,
                    staging_value=str(resource.get("image_tag", "")),
                    prod_value="",
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def _version_mismatches(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(key)
        if prod_resource is None:
            continue
        image_staging = str(resource.get("image_tag", ""))
        image_prod = str(prod_resource.get("image_tag", ""))
        replicas_staging = int(str(resource.get("replicas", "0")))
        replicas_prod = int(str(prod_resource.get("replicas", "0")))

        if image_staging != image_prod:
            diffs.append(
                ResourceDiff(
                    resource=_spec(resource),
                    namespace=str(resource["namespace"]),
                    reason="version_mismatch",
                    priority="blocking",
                    staging_value=image_staging,
                    prod_value=image_prod,
                    detail=f"Image version differs: staging={image_staging}, prod={image_prod}",
                )
            )
        elif replicas_staging != replicas_prod:
            diffs.append(
                ResourceDiff(
                    resource=_spec(resource),
                    namespace=str(resource["namespace"]),
                    reason="version_mismatch",
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",
                )
            )
    return diffs
