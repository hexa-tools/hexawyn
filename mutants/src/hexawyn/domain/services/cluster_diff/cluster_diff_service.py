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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_diff__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_diff__mutmut)
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


def x_compute_diff__mutmut_orig(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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


def x_compute_diff__mutmut_1(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = None
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


def x_compute_diff__mutmut_2(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(None)
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


def x_compute_diff__mutmut_3(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["XXresourcesXX"])
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


def x_compute_diff__mutmut_4(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["RESOURCES"])
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


def x_compute_diff__mutmut_5(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = None

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


def x_compute_diff__mutmut_6(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(None)

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


def x_compute_diff__mutmut_7(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["XXresourcesXX"])

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


def x_compute_diff__mutmut_8(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["RESOURCES"])

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


def x_compute_diff__mutmut_9(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = None
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


def x_compute_diff__mutmut_10(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(None, prod_map, priority="blocking")
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


def x_compute_diff__mutmut_11(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], None, priority="blocking")
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


def x_compute_diff__mutmut_12(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority=None)
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


def x_compute_diff__mutmut_13(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(prod_map, priority="blocking")
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


def x_compute_diff__mutmut_14(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], priority="blocking")
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


def x_compute_diff__mutmut_15(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, )
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


def x_compute_diff__mutmut_16(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["XXresourcesXX"], prod_map, priority="blocking")
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


def x_compute_diff__mutmut_17(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["RESOURCES"], prod_map, priority="blocking")
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


def x_compute_diff__mutmut_18(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="XXblockingXX")
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


def x_compute_diff__mutmut_19(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="BLOCKING")
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


def x_compute_diff__mutmut_20(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = None
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


def x_compute_diff__mutmut_21(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(None, prod_map)
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


def x_compute_diff__mutmut_22(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], None)
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


def x_compute_diff__mutmut_23(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(prod_map)
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


def x_compute_diff__mutmut_24(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], )
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


def x_compute_diff__mutmut_25(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["XXresourcesXX"], prod_map)
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


def x_compute_diff__mutmut_26(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["RESOURCES"], prod_map)
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


def x_compute_diff__mutmut_27(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = None

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


def x_compute_diff__mutmut_28(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(None, staging_map, priority="informational")

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


def x_compute_diff__mutmut_29(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], None, priority="informational")

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


def x_compute_diff__mutmut_30(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority=None)

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


def x_compute_diff__mutmut_31(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(staging_map, priority="informational")

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


def x_compute_diff__mutmut_32(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], priority="informational")

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


def x_compute_diff__mutmut_33(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, )

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


def x_compute_diff__mutmut_34(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["XXresourcesXX"], staging_map, priority="informational")

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


def x_compute_diff__mutmut_35(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["RESOURCES"], staging_map, priority="informational")

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


def x_compute_diff__mutmut_36(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="XXinformationalXX")

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


def x_compute_diff__mutmut_37(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="INFORMATIONAL")

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


def x_compute_diff__mutmut_38(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = None

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


def x_compute_diff__mutmut_39(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing - version_mismatches

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


def x_compute_diff__mutmut_40(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = None
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


def x_compute_diff__mutmut_41(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason == "secret_manual"]
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


def x_compute_diff__mutmut_42(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason != "XXsecret_manualXX"]
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


def x_compute_diff__mutmut_43(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason != "SECRET_MANUAL"]
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


def x_compute_diff__mutmut_44(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason != "secret_manual"]
    review = None

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


def x_compute_diff__mutmut_45(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason != "secret_manual"]
    review = [diff.resource for diff in version_mismatches]

    sync = None

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


def x_compute_diff__mutmut_46(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason != "secret_manual"]
    review = [diff.resource for diff in version_mismatches]

    sync = "XXin_syncXX" if not in_staging_not_prod and not prod_only else "out_of_sync"

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


def x_compute_diff__mutmut_47(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason != "secret_manual"]
    review = [diff.resource for diff in version_mismatches]

    sync = "IN_SYNC" if not in_staging_not_prod and not prod_only else "out_of_sync"

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


def x_compute_diff__mutmut_48(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason != "secret_manual"]
    review = [diff.resource for diff in version_mismatches]

    sync = "in_sync" if not in_staging_not_prod or not prod_only else "out_of_sync"

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


def x_compute_diff__mutmut_49(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason != "secret_manual"]
    review = [diff.resource for diff in version_mismatches]

    sync = "in_sync" if in_staging_not_prod and not prod_only else "out_of_sync"

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


def x_compute_diff__mutmut_50(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason != "secret_manual"]
    review = [diff.resource for diff in version_mismatches]

    sync = "in_sync" if not in_staging_not_prod and prod_only else "out_of_sync"

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


def x_compute_diff__mutmut_51(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason != "secret_manual"]
    review = [diff.resource for diff in version_mismatches]

    sync = "in_sync" if not in_staging_not_prod and not prod_only else "XXout_of_syncXX"

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


def x_compute_diff__mutmut_52(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
    prod_map = _index_by_key(prod["resources"])
    staging_map = _index_by_key(staging["resources"])

    missing = _missing(staging["resources"], prod_map, priority="blocking")
    version_mismatches = _version_mismatches(staging["resources"], prod_map)
    prod_only = _missing(prod["resources"], staging_map, priority="informational")

    in_staging_not_prod = missing + version_mismatches

    ready = [diff.resource for diff in missing if diff.reason != "secret_manual"]
    review = [diff.resource for diff in version_mismatches]

    sync = "in_sync" if not in_staging_not_prod and not prod_only else "OUT_OF_SYNC"

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


def x_compute_diff__mutmut_53(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        source_cluster=None,
        target_cluster=prod["cluster_name"],
        in_staging_not_prod=missing,
        version_mismatches=version_mismatches,
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_54(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        target_cluster=None,
        in_staging_not_prod=missing,
        version_mismatches=version_mismatches,
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_55(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        in_staging_not_prod=None,
        version_mismatches=version_mismatches,
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_56(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        version_mismatches=None,
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_57(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        prod_only=None,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_58(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        promotion_checklist=None,
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_59(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        sync_status=None,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_60(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        total_differences=None,
        has_data=True,
    )


def x_compute_diff__mutmut_61(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        has_data=None,
    )


def x_compute_diff__mutmut_62(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        target_cluster=prod["cluster_name"],
        in_staging_not_prod=missing,
        version_mismatches=version_mismatches,
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_63(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        in_staging_not_prod=missing,
        version_mismatches=version_mismatches,
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_64(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        version_mismatches=version_mismatches,
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_65(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_66(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_67(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_68(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_69(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        has_data=True,
    )


def x_compute_diff__mutmut_70(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        )


def x_compute_diff__mutmut_71(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        source_cluster=staging["XXcluster_nameXX"],
        target_cluster=prod["cluster_name"],
        in_staging_not_prod=missing,
        version_mismatches=version_mismatches,
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_72(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        source_cluster=staging["CLUSTER_NAME"],
        target_cluster=prod["cluster_name"],
        in_staging_not_prod=missing,
        version_mismatches=version_mismatches,
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_73(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        target_cluster=prod["XXcluster_nameXX"],
        in_staging_not_prod=missing,
        version_mismatches=version_mismatches,
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_74(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        target_cluster=prod["CLUSTER_NAME"],
        in_staging_not_prod=missing,
        version_mismatches=version_mismatches,
        prod_only=prod_only,
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_75(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        promotion_checklist=PromotionChecklist(ready_to_promote=None, requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_76(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, requires_review=None),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_77(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        promotion_checklist=PromotionChecklist(requires_review=review),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_78(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        promotion_checklist=PromotionChecklist(ready_to_promote=ready, ),
        sync_status=sync,
        total_differences=len(in_staging_not_prod) + len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_79(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        total_differences=len(in_staging_not_prod) - len(prod_only),
        has_data=True,
    )


def x_compute_diff__mutmut_80(staging: ClusterInventoryData, prod: ClusterInventoryData) -> ClusterDiffReport:
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
        has_data=False,
    )

mutants_x_compute_diff__mutmut['_mutmut_orig'] = x_compute_diff__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_1'] = x_compute_diff__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_2'] = x_compute_diff__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_3'] = x_compute_diff__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_4'] = x_compute_diff__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_5'] = x_compute_diff__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_6'] = x_compute_diff__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_7'] = x_compute_diff__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_8'] = x_compute_diff__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_9'] = x_compute_diff__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_10'] = x_compute_diff__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_11'] = x_compute_diff__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_12'] = x_compute_diff__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_13'] = x_compute_diff__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_14'] = x_compute_diff__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_15'] = x_compute_diff__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_16'] = x_compute_diff__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_17'] = x_compute_diff__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_18'] = x_compute_diff__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_19'] = x_compute_diff__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_20'] = x_compute_diff__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_21'] = x_compute_diff__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_22'] = x_compute_diff__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_23'] = x_compute_diff__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_24'] = x_compute_diff__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_25'] = x_compute_diff__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_26'] = x_compute_diff__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_27'] = x_compute_diff__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_28'] = x_compute_diff__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_29'] = x_compute_diff__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_30'] = x_compute_diff__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_31'] = x_compute_diff__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_32'] = x_compute_diff__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_33'] = x_compute_diff__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_34'] = x_compute_diff__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_35'] = x_compute_diff__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_36'] = x_compute_diff__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_37'] = x_compute_diff__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_38'] = x_compute_diff__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_39'] = x_compute_diff__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_40'] = x_compute_diff__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_41'] = x_compute_diff__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_42'] = x_compute_diff__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_43'] = x_compute_diff__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_44'] = x_compute_diff__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_45'] = x_compute_diff__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_46'] = x_compute_diff__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_47'] = x_compute_diff__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_48'] = x_compute_diff__mutmut_48 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_49'] = x_compute_diff__mutmut_49 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_50'] = x_compute_diff__mutmut_50 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_51'] = x_compute_diff__mutmut_51 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_52'] = x_compute_diff__mutmut_52 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_53'] = x_compute_diff__mutmut_53 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_54'] = x_compute_diff__mutmut_54 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_55'] = x_compute_diff__mutmut_55 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_56'] = x_compute_diff__mutmut_56 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_57'] = x_compute_diff__mutmut_57 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_58'] = x_compute_diff__mutmut_58 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_59'] = x_compute_diff__mutmut_59 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_60'] = x_compute_diff__mutmut_60 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_61'] = x_compute_diff__mutmut_61 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_62'] = x_compute_diff__mutmut_62 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_63'] = x_compute_diff__mutmut_63 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_64'] = x_compute_diff__mutmut_64 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_65'] = x_compute_diff__mutmut_65 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_66'] = x_compute_diff__mutmut_66 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_67'] = x_compute_diff__mutmut_67 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_68'] = x_compute_diff__mutmut_68 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_69'] = x_compute_diff__mutmut_69 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_70'] = x_compute_diff__mutmut_70 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_71'] = x_compute_diff__mutmut_71 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_72'] = x_compute_diff__mutmut_72 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_73'] = x_compute_diff__mutmut_73 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_74'] = x_compute_diff__mutmut_74 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_75'] = x_compute_diff__mutmut_75 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_76'] = x_compute_diff__mutmut_76 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_77'] = x_compute_diff__mutmut_77 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_78'] = x_compute_diff__mutmut_78 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_79'] = x_compute_diff__mutmut_79 # type: ignore # mutmut generated
mutants_x_compute_diff__mutmut['x_compute_diff__mutmut_80'] = x_compute_diff__mutmut_80 # type: ignore # mutmut generated
mutants_x__key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__key__mutmut)
def _key(resource: ResourceInventoryRaw) -> str:
    return f"{resource['kind']}/{resource['name']}/{resource['namespace']}"


def x__key__mutmut_orig(resource: ResourceInventoryRaw) -> str:
    return f"{resource['kind']}/{resource['name']}/{resource['namespace']}"


def x__key__mutmut_1(resource: ResourceInventoryRaw) -> str:
    return f"{resource['XXkindXX']}/{resource['name']}/{resource['namespace']}"


def x__key__mutmut_2(resource: ResourceInventoryRaw) -> str:
    return f"{resource['KIND']}/{resource['name']}/{resource['namespace']}"


def x__key__mutmut_3(resource: ResourceInventoryRaw) -> str:
    return f"{resource['kind']}/{resource['XXnameXX']}/{resource['namespace']}"


def x__key__mutmut_4(resource: ResourceInventoryRaw) -> str:
    return f"{resource['kind']}/{resource['NAME']}/{resource['namespace']}"


def x__key__mutmut_5(resource: ResourceInventoryRaw) -> str:
    return f"{resource['kind']}/{resource['name']}/{resource['XXnamespaceXX']}"


def x__key__mutmut_6(resource: ResourceInventoryRaw) -> str:
    return f"{resource['kind']}/{resource['name']}/{resource['NAMESPACE']}"

mutants_x__key__mutmut['_mutmut_orig'] = x__key__mutmut_orig # type: ignore # mutmut generated
mutants_x__key__mutmut['x__key__mutmut_1'] = x__key__mutmut_1 # type: ignore # mutmut generated
mutants_x__key__mutmut['x__key__mutmut_2'] = x__key__mutmut_2 # type: ignore # mutmut generated
mutants_x__key__mutmut['x__key__mutmut_3'] = x__key__mutmut_3 # type: ignore # mutmut generated
mutants_x__key__mutmut['x__key__mutmut_4'] = x__key__mutmut_4 # type: ignore # mutmut generated
mutants_x__key__mutmut['x__key__mutmut_5'] = x__key__mutmut_5 # type: ignore # mutmut generated
mutants_x__key__mutmut['x__key__mutmut_6'] = x__key__mutmut_6 # type: ignore # mutmut generated
mutants_x__spec__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__spec__mutmut)
def _spec(resource: ResourceInventoryRaw) -> str:
    return f"{resource['kind']}/{resource['name']}"


def x__spec__mutmut_orig(resource: ResourceInventoryRaw) -> str:
    return f"{resource['kind']}/{resource['name']}"


def x__spec__mutmut_1(resource: ResourceInventoryRaw) -> str:
    return f"{resource['XXkindXX']}/{resource['name']}"


def x__spec__mutmut_2(resource: ResourceInventoryRaw) -> str:
    return f"{resource['KIND']}/{resource['name']}"


def x__spec__mutmut_3(resource: ResourceInventoryRaw) -> str:
    return f"{resource['kind']}/{resource['XXnameXX']}"


def x__spec__mutmut_4(resource: ResourceInventoryRaw) -> str:
    return f"{resource['kind']}/{resource['NAME']}"

mutants_x__spec__mutmut['_mutmut_orig'] = x__spec__mutmut_orig # type: ignore # mutmut generated
mutants_x__spec__mutmut['x__spec__mutmut_1'] = x__spec__mutmut_1 # type: ignore # mutmut generated
mutants_x__spec__mutmut['x__spec__mutmut_2'] = x__spec__mutmut_2 # type: ignore # mutmut generated
mutants_x__spec__mutmut['x__spec__mutmut_3'] = x__spec__mutmut_3 # type: ignore # mutmut generated
mutants_x__spec__mutmut['x__spec__mutmut_4'] = x__spec__mutmut_4 # type: ignore # mutmut generated
mutants_x__index_by_key__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__index_by_key__mutmut)
def _index_by_key(
    resources: list[ResourceInventoryRaw],
) -> dict[str, ResourceInventoryRaw]:
    return {_key(resource): resource for resource in resources}


def x__index_by_key__mutmut_orig(
    resources: list[ResourceInventoryRaw],
) -> dict[str, ResourceInventoryRaw]:
    return {_key(resource): resource for resource in resources}


def x__index_by_key__mutmut_1(
    resources: list[ResourceInventoryRaw],
) -> dict[str, ResourceInventoryRaw]:
    return {_key(None): resource for resource in resources}

mutants_x__index_by_key__mutmut['_mutmut_orig'] = x__index_by_key__mutmut_orig # type: ignore # mutmut generated
mutants_x__index_by_key__mutmut['x__index_by_key__mutmut_1'] = x__index_by_key__mutmut_1 # type: ignore # mutmut generated
mutants_x__missing__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__missing__mutmut)
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


def x__missing__mutmut_orig(
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


def x__missing__mutmut_1(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "XXblockingXX",
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


def x__missing__mutmut_2(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "BLOCKING",
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


def x__missing__mutmut_3(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = None
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


def x__missing__mutmut_4(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in resources:
        key = None
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


def x__missing__mutmut_5(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in resources:
        key = _key(None)
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


def x__missing__mutmut_6(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in resources:
        key = _key(resource)
        if key in target_map:
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


def x__missing__mutmut_7(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in resources:
        key = _key(resource)
        if key not in target_map:
            is_secret = None
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


def x__missing__mutmut_8(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in resources:
        key = _key(resource)
        if key not in target_map:
            is_secret = resource.get(None, False)
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


def x__missing__mutmut_9(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in resources:
        key = _key(resource)
        if key not in target_map:
            is_secret = resource.get("is_secret", None)
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


def x__missing__mutmut_10(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in resources:
        key = _key(resource)
        if key not in target_map:
            is_secret = resource.get(False)
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


def x__missing__mutmut_11(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in resources:
        key = _key(resource)
        if key not in target_map:
            is_secret = resource.get("is_secret", )
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


def x__missing__mutmut_12(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in resources:
        key = _key(resource)
        if key not in target_map:
            is_secret = resource.get("XXis_secretXX", False)
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


def x__missing__mutmut_13(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in resources:
        key = _key(resource)
        if key not in target_map:
            is_secret = resource.get("IS_SECRET", False)
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


def x__missing__mutmut_14(
    resources: list[ResourceInventoryRaw],
    target_map: dict[str, ResourceInventoryRaw],
    priority: str = "blocking",
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in resources:
        key = _key(resource)
        if key not in target_map:
            is_secret = resource.get("is_secret", True)
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


def x__missing__mutmut_15(
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
                None
            )
    return diffs


def x__missing__mutmut_16(
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
                    resource=None,
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


def x__missing__mutmut_17(
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
                    namespace=None,
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


def x__missing__mutmut_18(
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
                    reason=None,
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


def x__missing__mutmut_19(
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
                    priority=None,
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


def x__missing__mutmut_20(
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
                    staging_value=None,
                    prod_value="",
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_21(
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
                    prod_value=None,
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_22(
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
                    detail=None,
                )
            )
    return diffs


def x__missing__mutmut_23(
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


def x__missing__mutmut_24(
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


def x__missing__mutmut_25(
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


def x__missing__mutmut_26(
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


def x__missing__mutmut_27(
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
                    prod_value="",
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_28(
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
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_29(
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
                    )
            )
    return diffs


def x__missing__mutmut_30(
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
                    resource=_spec(None),
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


def x__missing__mutmut_31(
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
                    namespace=str(None),
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


def x__missing__mutmut_32(
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
                    namespace=str(resource["XXnamespaceXX"]),
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


def x__missing__mutmut_33(
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
                    namespace=str(resource["NAMESPACE"]),
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


def x__missing__mutmut_34(
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
                    reason="XXsecret_manualXX" if is_secret else "never_promoted",
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


def x__missing__mutmut_35(
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
                    reason="SECRET_MANUAL" if is_secret else "never_promoted",
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


def x__missing__mutmut_36(
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
                    reason="secret_manual" if is_secret else "XXnever_promotedXX",
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


def x__missing__mutmut_37(
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
                    reason="secret_manual" if is_secret else "NEVER_PROMOTED",
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


def x__missing__mutmut_38(
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
                    staging_value=str(None),
                    prod_value="",
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_39(
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
                    staging_value=str(resource.get(None, "")),
                    prod_value="",
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_40(
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
                    staging_value=str(resource.get("image_tag", None)),
                    prod_value="",
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_41(
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
                    staging_value=str(resource.get("")),
                    prod_value="",
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_42(
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
                    staging_value=str(resource.get("image_tag", )),
                    prod_value="",
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_43(
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
                    staging_value=str(resource.get("XXimage_tagXX", "")),
                    prod_value="",
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_44(
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
                    staging_value=str(resource.get("IMAGE_TAG", "")),
                    prod_value="",
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_45(
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
                    staging_value=str(resource.get("image_tag", "XXXX")),
                    prod_value="",
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_46(
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
                    prod_value="XXXX",
                    detail=(
                        "Secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_47(
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
                        "XXSecret requires manual promotionXX"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_48(
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
                        "secret requires manual promotion"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_49(
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
                        "SECRET REQUIRES MANUAL PROMOTION"
                        if is_secret
                        else "Resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_50(
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
                        else "XXResource present in staging, absent in productionXX"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_51(
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
                        else "resource present in staging, absent in production"
                    ),
                )
            )
    return diffs


def x__missing__mutmut_52(
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
                        else "RESOURCE PRESENT IN STAGING, ABSENT IN PRODUCTION"
                    ),
                )
            )
    return diffs

mutants_x__missing__mutmut['_mutmut_orig'] = x__missing__mutmut_orig # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_1'] = x__missing__mutmut_1 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_2'] = x__missing__mutmut_2 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_3'] = x__missing__mutmut_3 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_4'] = x__missing__mutmut_4 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_5'] = x__missing__mutmut_5 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_6'] = x__missing__mutmut_6 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_7'] = x__missing__mutmut_7 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_8'] = x__missing__mutmut_8 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_9'] = x__missing__mutmut_9 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_10'] = x__missing__mutmut_10 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_11'] = x__missing__mutmut_11 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_12'] = x__missing__mutmut_12 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_13'] = x__missing__mutmut_13 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_14'] = x__missing__mutmut_14 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_15'] = x__missing__mutmut_15 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_16'] = x__missing__mutmut_16 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_17'] = x__missing__mutmut_17 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_18'] = x__missing__mutmut_18 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_19'] = x__missing__mutmut_19 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_20'] = x__missing__mutmut_20 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_21'] = x__missing__mutmut_21 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_22'] = x__missing__mutmut_22 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_23'] = x__missing__mutmut_23 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_24'] = x__missing__mutmut_24 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_25'] = x__missing__mutmut_25 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_26'] = x__missing__mutmut_26 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_27'] = x__missing__mutmut_27 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_28'] = x__missing__mutmut_28 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_29'] = x__missing__mutmut_29 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_30'] = x__missing__mutmut_30 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_31'] = x__missing__mutmut_31 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_32'] = x__missing__mutmut_32 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_33'] = x__missing__mutmut_33 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_34'] = x__missing__mutmut_34 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_35'] = x__missing__mutmut_35 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_36'] = x__missing__mutmut_36 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_37'] = x__missing__mutmut_37 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_38'] = x__missing__mutmut_38 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_39'] = x__missing__mutmut_39 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_40'] = x__missing__mutmut_40 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_41'] = x__missing__mutmut_41 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_42'] = x__missing__mutmut_42 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_43'] = x__missing__mutmut_43 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_44'] = x__missing__mutmut_44 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_45'] = x__missing__mutmut_45 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_46'] = x__missing__mutmut_46 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_47'] = x__missing__mutmut_47 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_48'] = x__missing__mutmut_48 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_49'] = x__missing__mutmut_49 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_50'] = x__missing__mutmut_50 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_51'] = x__missing__mutmut_51 # type: ignore # mutmut generated
mutants_x__missing__mutmut['x__missing__mutmut_52'] = x__missing__mutmut_52 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__version_mismatches__mutmut)
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_orig(
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_1(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = None
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_2(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = None
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_3(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(None)
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_4(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = None
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_5(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(None)
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_6(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(key)
        if prod_resource is not None:
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_7(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(key)
        if prod_resource is None:
            break
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_8(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(key)
        if prod_resource is None:
            continue
        image_staging = None
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_9(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(key)
        if prod_resource is None:
            continue
        image_staging = str(None)
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_10(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(key)
        if prod_resource is None:
            continue
        image_staging = str(resource.get(None, ""))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_11(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(key)
        if prod_resource is None:
            continue
        image_staging = str(resource.get("image_tag", None))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_12(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(key)
        if prod_resource is None:
            continue
        image_staging = str(resource.get(""))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_13(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(key)
        if prod_resource is None:
            continue
        image_staging = str(resource.get("image_tag", ))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_14(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(key)
        if prod_resource is None:
            continue
        image_staging = str(resource.get("XXimage_tagXX", ""))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_15(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(key)
        if prod_resource is None:
            continue
        image_staging = str(resource.get("IMAGE_TAG", ""))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_16(
    staging_resources: list[ResourceInventoryRaw],
    prod_map: dict[str, ResourceInventoryRaw],
) -> list[ResourceDiff]:
    diffs: list[ResourceDiff] = []
    for resource in staging_resources:
        key = _key(resource)
        prod_resource = prod_map.get(key)
        if prod_resource is None:
            continue
        image_staging = str(resource.get("image_tag", "XXXX"))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_17(
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
        image_prod = None
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_18(
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
        image_prod = str(None)
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_19(
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
        image_prod = str(prod_resource.get(None, ""))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_20(
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
        image_prod = str(prod_resource.get("image_tag", None))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_21(
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
        image_prod = str(prod_resource.get(""))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_22(
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
        image_prod = str(prod_resource.get("image_tag", ))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_23(
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
        image_prod = str(prod_resource.get("XXimage_tagXX", ""))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_24(
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
        image_prod = str(prod_resource.get("IMAGE_TAG", ""))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_25(
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
        image_prod = str(prod_resource.get("image_tag", "XXXX"))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_26(
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
        replicas_staging = None
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_27(
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
        replicas_staging = int(None)
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_28(
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
        replicas_staging = int(str(None))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_29(
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
        replicas_staging = int(str(resource.get(None, "0")))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_30(
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
        replicas_staging = int(str(resource.get("replicas", None)))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_31(
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
        replicas_staging = int(str(resource.get("0")))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_32(
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
        replicas_staging = int(str(resource.get("replicas", )))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_33(
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
        replicas_staging = int(str(resource.get("XXreplicasXX", "0")))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_34(
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
        replicas_staging = int(str(resource.get("REPLICAS", "0")))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_35(
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
        replicas_staging = int(str(resource.get("replicas", "XX0XX")))
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_36(
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
        replicas_prod = None

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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_37(
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
        replicas_prod = int(None)

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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_38(
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
        replicas_prod = int(str(None))

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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_39(
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
        replicas_prod = int(str(prod_resource.get(None, "0")))

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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_40(
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
        replicas_prod = int(str(prod_resource.get("replicas", None)))

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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_41(
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
        replicas_prod = int(str(prod_resource.get("0")))

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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_42(
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
        replicas_prod = int(str(prod_resource.get("replicas", )))

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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_43(
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
        replicas_prod = int(str(prod_resource.get("XXreplicasXX", "0")))

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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_44(
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
        replicas_prod = int(str(prod_resource.get("REPLICAS", "0")))

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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_45(
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
        replicas_prod = int(str(prod_resource.get("replicas", "XX0XX")))

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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_46(
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

        if image_staging == image_prod:
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_47(
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
                None
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_48(
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
                    resource=None,
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_49(
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
                    namespace=None,
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_50(
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
                    reason=None,
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_51(
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
                    priority=None,
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_52(
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
                    staging_value=None,
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_53(
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
                    prod_value=None,
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_54(
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
                    detail=None,
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_55(
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_56(
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_57(
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_58(
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_59(
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_60(
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_61(
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_62(
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
                    resource=_spec(None),
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_63(
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
                    namespace=str(None),
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_64(
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
                    namespace=str(resource["XXnamespaceXX"]),
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_65(
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
                    namespace=str(resource["NAMESPACE"]),
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_66(
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
                    reason="XXversion_mismatchXX",
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_67(
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
                    reason="VERSION_MISMATCH",
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_68(
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
                    priority="XXblockingXX",
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_69(
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
                    priority="BLOCKING",
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_70(
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
        elif replicas_staging == replicas_prod:
            diffs.append(
                ResourceDiff(
                    resource=_spec(resource),
                    namespace=str(resource["namespace"]),
                    reason="version_mismatch",
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_71(
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
                None
            )
    return diffs


def x__version_mismatches__mutmut_72(
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
                    resource=None,
                    namespace=str(resource["namespace"]),
                    reason="version_mismatch",
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_73(
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
                    namespace=None,
                    reason="version_mismatch",
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_74(
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
                    reason=None,
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_75(
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
                    priority=None,
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_76(
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
                    staging_value=None,
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_77(
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
                    prod_value=None,
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_78(
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
                    detail=None,  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_79(
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
                    namespace=str(resource["namespace"]),
                    reason="version_mismatch",
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_80(
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
                    reason="version_mismatch",
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_81(
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
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_82(
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
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_83(
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
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_84(
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
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_85(
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
                    )
            )
    return diffs


def x__version_mismatches__mutmut_86(
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
                    resource=_spec(None),
                    namespace=str(resource["namespace"]),
                    reason="version_mismatch",
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_87(
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
                    namespace=str(None),
                    reason="version_mismatch",
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_88(
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
                    namespace=str(resource["XXnamespaceXX"]),
                    reason="version_mismatch",
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_89(
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
                    namespace=str(resource["NAMESPACE"]),
                    reason="version_mismatch",
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_90(
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
                    reason="XXversion_mismatchXX",
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_91(
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
                    reason="VERSION_MISMATCH",
                    priority="informational",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_92(
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
                    priority="XXinformationalXX",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_93(
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
                    priority="INFORMATIONAL",
                    staging_value=str(replicas_staging),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_94(
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
                    staging_value=str(None),
                    prod_value=str(replicas_prod),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs


def x__version_mismatches__mutmut_95(
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
                    prod_value=str(None),
                    detail=f"Replica count differs: staging={replicas_staging}, prod={replicas_prod}",  # noqa: E501
                )
            )
    return diffs

mutants_x__version_mismatches__mutmut['_mutmut_orig'] = x__version_mismatches__mutmut_orig # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_1'] = x__version_mismatches__mutmut_1 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_2'] = x__version_mismatches__mutmut_2 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_3'] = x__version_mismatches__mutmut_3 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_4'] = x__version_mismatches__mutmut_4 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_5'] = x__version_mismatches__mutmut_5 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_6'] = x__version_mismatches__mutmut_6 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_7'] = x__version_mismatches__mutmut_7 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_8'] = x__version_mismatches__mutmut_8 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_9'] = x__version_mismatches__mutmut_9 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_10'] = x__version_mismatches__mutmut_10 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_11'] = x__version_mismatches__mutmut_11 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_12'] = x__version_mismatches__mutmut_12 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_13'] = x__version_mismatches__mutmut_13 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_14'] = x__version_mismatches__mutmut_14 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_15'] = x__version_mismatches__mutmut_15 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_16'] = x__version_mismatches__mutmut_16 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_17'] = x__version_mismatches__mutmut_17 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_18'] = x__version_mismatches__mutmut_18 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_19'] = x__version_mismatches__mutmut_19 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_20'] = x__version_mismatches__mutmut_20 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_21'] = x__version_mismatches__mutmut_21 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_22'] = x__version_mismatches__mutmut_22 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_23'] = x__version_mismatches__mutmut_23 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_24'] = x__version_mismatches__mutmut_24 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_25'] = x__version_mismatches__mutmut_25 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_26'] = x__version_mismatches__mutmut_26 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_27'] = x__version_mismatches__mutmut_27 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_28'] = x__version_mismatches__mutmut_28 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_29'] = x__version_mismatches__mutmut_29 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_30'] = x__version_mismatches__mutmut_30 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_31'] = x__version_mismatches__mutmut_31 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_32'] = x__version_mismatches__mutmut_32 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_33'] = x__version_mismatches__mutmut_33 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_34'] = x__version_mismatches__mutmut_34 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_35'] = x__version_mismatches__mutmut_35 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_36'] = x__version_mismatches__mutmut_36 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_37'] = x__version_mismatches__mutmut_37 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_38'] = x__version_mismatches__mutmut_38 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_39'] = x__version_mismatches__mutmut_39 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_40'] = x__version_mismatches__mutmut_40 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_41'] = x__version_mismatches__mutmut_41 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_42'] = x__version_mismatches__mutmut_42 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_43'] = x__version_mismatches__mutmut_43 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_44'] = x__version_mismatches__mutmut_44 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_45'] = x__version_mismatches__mutmut_45 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_46'] = x__version_mismatches__mutmut_46 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_47'] = x__version_mismatches__mutmut_47 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_48'] = x__version_mismatches__mutmut_48 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_49'] = x__version_mismatches__mutmut_49 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_50'] = x__version_mismatches__mutmut_50 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_51'] = x__version_mismatches__mutmut_51 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_52'] = x__version_mismatches__mutmut_52 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_53'] = x__version_mismatches__mutmut_53 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_54'] = x__version_mismatches__mutmut_54 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_55'] = x__version_mismatches__mutmut_55 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_56'] = x__version_mismatches__mutmut_56 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_57'] = x__version_mismatches__mutmut_57 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_58'] = x__version_mismatches__mutmut_58 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_59'] = x__version_mismatches__mutmut_59 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_60'] = x__version_mismatches__mutmut_60 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_61'] = x__version_mismatches__mutmut_61 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_62'] = x__version_mismatches__mutmut_62 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_63'] = x__version_mismatches__mutmut_63 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_64'] = x__version_mismatches__mutmut_64 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_65'] = x__version_mismatches__mutmut_65 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_66'] = x__version_mismatches__mutmut_66 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_67'] = x__version_mismatches__mutmut_67 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_68'] = x__version_mismatches__mutmut_68 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_69'] = x__version_mismatches__mutmut_69 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_70'] = x__version_mismatches__mutmut_70 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_71'] = x__version_mismatches__mutmut_71 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_72'] = x__version_mismatches__mutmut_72 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_73'] = x__version_mismatches__mutmut_73 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_74'] = x__version_mismatches__mutmut_74 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_75'] = x__version_mismatches__mutmut_75 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_76'] = x__version_mismatches__mutmut_76 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_77'] = x__version_mismatches__mutmut_77 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_78'] = x__version_mismatches__mutmut_78 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_79'] = x__version_mismatches__mutmut_79 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_80'] = x__version_mismatches__mutmut_80 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_81'] = x__version_mismatches__mutmut_81 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_82'] = x__version_mismatches__mutmut_82 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_83'] = x__version_mismatches__mutmut_83 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_84'] = x__version_mismatches__mutmut_84 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_85'] = x__version_mismatches__mutmut_85 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_86'] = x__version_mismatches__mutmut_86 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_87'] = x__version_mismatches__mutmut_87 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_88'] = x__version_mismatches__mutmut_88 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_89'] = x__version_mismatches__mutmut_89 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_90'] = x__version_mismatches__mutmut_90 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_91'] = x__version_mismatches__mutmut_91 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_92'] = x__version_mismatches__mutmut_92 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_93'] = x__version_mismatches__mutmut_93 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_94'] = x__version_mismatches__mutmut_94 # type: ignore # mutmut generated
mutants_x__version_mismatches__mutmut['x__version_mismatches__mutmut_95'] = x__version_mismatches__mutmut_95 # type: ignore # mutmut generated
