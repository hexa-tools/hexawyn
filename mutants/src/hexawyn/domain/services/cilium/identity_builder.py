"""Pure Cilium security-identity listing — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import (
    CiliumIdentitiesResult,
    CiliumIdentityInfo,
)

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


def _as_dict(value: object) -> dict[str, object]:
    return value if isinstance(value, dict) else {}
mutants_x_build_identities_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_identities_result__mutmut)
def build_identities_result(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_orig(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_1(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = None
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_2(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(None)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_3(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = None
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_4(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = None
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_5(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(None)
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_6(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get(None))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_7(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("XXmetadataXX"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_8(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("METADATA"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_9(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = None
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_10(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(None)
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_11(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get(None))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_12(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("XXspecXX"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_13(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("SPEC"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_14(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = None
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_15(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(None)
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_16(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get(None, ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_17(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", None))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_18(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get(""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_19(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_20(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("XXnameXX", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_21(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("NAME", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_22(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", "XXXX"))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_23(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            None
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_24(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=None,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_25(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=None,
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_26(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=None,
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_27(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_28(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_29(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_30(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(None, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_31(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, None),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_32(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_33(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, ),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_34(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(None, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_35(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, None),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_36(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_37(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, ),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_38(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 1),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_39(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=None,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_40(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status=None,
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_41(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=None,
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_42(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=None,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_43(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None,
    )


def x_build_identities_result__mutmut_44(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_45(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_46(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_47(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_48(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        )


def x_build_identities_result__mutmut_49(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=False,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_50(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="XXpresentXX" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_51(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="PRESENT" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_52(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "XXemptyXX",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_53(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "EMPTY",
        total_identities=len(built),
        identities=built,
        note=None if built else "No Cilium identities found",
    )


def x_build_identities_result__mutmut_54(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "XXNo Cilium identities foundXX",
    )


def x_build_identities_result__mutmut_55(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "no cilium identities found",
    )


def x_build_identities_result__mutmut_56(
    identities: list[dict[str, object]],
    endpoints: list[dict[str, object]],
) -> CiliumIdentitiesResult:
    """Build the identity list, counting associated CiliumEndpoint ids."""
    counts = _count_endpoint_ids(endpoints)
    built: list[CiliumIdentityInfo] = []
    for raw in identities:
        metadata = _as_dict(raw.get("metadata"))
        spec = _as_dict(raw.get("spec"))
        identity_id = str(metadata.get("name", ""))
        built.append(
            CiliumIdentityInfo(
                id=identity_id,
                labels=_extract_labels(spec, metadata),
                endpoint_count=counts.get(identity_id, 0),
            )
        )
    return CiliumIdentitiesResult(
        installed=True,
        status="present" if built else "empty",
        total_identities=len(built),
        identities=built,
        note=None if built else "NO CILIUM IDENTITIES FOUND",
    )

mutants_x_build_identities_result__mutmut['_mutmut_orig'] = x_build_identities_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_1'] = x_build_identities_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_2'] = x_build_identities_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_3'] = x_build_identities_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_4'] = x_build_identities_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_5'] = x_build_identities_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_6'] = x_build_identities_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_7'] = x_build_identities_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_8'] = x_build_identities_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_9'] = x_build_identities_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_10'] = x_build_identities_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_11'] = x_build_identities_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_12'] = x_build_identities_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_13'] = x_build_identities_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_14'] = x_build_identities_result__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_15'] = x_build_identities_result__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_16'] = x_build_identities_result__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_17'] = x_build_identities_result__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_18'] = x_build_identities_result__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_19'] = x_build_identities_result__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_20'] = x_build_identities_result__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_21'] = x_build_identities_result__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_22'] = x_build_identities_result__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_23'] = x_build_identities_result__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_24'] = x_build_identities_result__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_25'] = x_build_identities_result__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_26'] = x_build_identities_result__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_27'] = x_build_identities_result__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_28'] = x_build_identities_result__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_29'] = x_build_identities_result__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_30'] = x_build_identities_result__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_31'] = x_build_identities_result__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_32'] = x_build_identities_result__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_33'] = x_build_identities_result__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_34'] = x_build_identities_result__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_35'] = x_build_identities_result__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_36'] = x_build_identities_result__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_37'] = x_build_identities_result__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_38'] = x_build_identities_result__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_39'] = x_build_identities_result__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_40'] = x_build_identities_result__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_41'] = x_build_identities_result__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_42'] = x_build_identities_result__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_43'] = x_build_identities_result__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_44'] = x_build_identities_result__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_45'] = x_build_identities_result__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_46'] = x_build_identities_result__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_47'] = x_build_identities_result__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_48'] = x_build_identities_result__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_49'] = x_build_identities_result__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_50'] = x_build_identities_result__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_51'] = x_build_identities_result__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_52'] = x_build_identities_result__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_53'] = x_build_identities_result__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_54'] = x_build_identities_result__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_55'] = x_build_identities_result__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_identities_result__mutmut['x_build_identities_result__mutmut_56'] = x_build_identities_result__mutmut_56 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_not_installed_identities_result__mutmut)
def not_installed_identities_result() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status="not_installed",
        total_identities=0,
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_orig() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status="not_installed",
        total_identities=0,
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_1() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=None,
        status="not_installed",
        total_identities=0,
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_2() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status=None,
        total_identities=0,
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_3() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status="not_installed",
        total_identities=None,
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_4() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status="not_installed",
        total_identities=0,
        identities=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_5() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status="not_installed",
        total_identities=0,
        identities=[],
        note=None,
    )


def x_not_installed_identities_result__mutmut_6() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        status="not_installed",
        total_identities=0,
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_7() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        total_identities=0,
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_8() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status="not_installed",
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_9() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status="not_installed",
        total_identities=0,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_10() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status="not_installed",
        total_identities=0,
        identities=[],
        )


def x_not_installed_identities_result__mutmut_11() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=True,
        status="not_installed",
        total_identities=0,
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_12() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status="XXnot_installedXX",
        total_identities=0,
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_13() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status="NOT_INSTALLED",
        total_identities=0,
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_identities_result__mutmut_14() -> CiliumIdentitiesResult:
    """Honest NOT_INSTALLED marker — no fabricated identities."""
    return CiliumIdentitiesResult(
        installed=False,
        status="not_installed",
        total_identities=1,
        identities=[],
        note=_NOT_INSTALLED_NOTE,
    )

mutants_x_not_installed_identities_result__mutmut['_mutmut_orig'] = x_not_installed_identities_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_1'] = x_not_installed_identities_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_2'] = x_not_installed_identities_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_3'] = x_not_installed_identities_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_4'] = x_not_installed_identities_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_5'] = x_not_installed_identities_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_6'] = x_not_installed_identities_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_7'] = x_not_installed_identities_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_8'] = x_not_installed_identities_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_9'] = x_not_installed_identities_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_10'] = x_not_installed_identities_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_11'] = x_not_installed_identities_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_12'] = x_not_installed_identities_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_13'] = x_not_installed_identities_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_not_installed_identities_result__mutmut['x_not_installed_identities_result__mutmut_14'] = x_not_installed_identities_result__mutmut_14 # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_labels__mutmut)
def _extract_labels(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("labels")
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = metadata.get("labels")
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def x__extract_labels__mutmut_orig(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("labels")
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = metadata.get("labels")
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def x__extract_labels__mutmut_1(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = None
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = metadata.get("labels")
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def x__extract_labels__mutmut_2(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get(None)
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = metadata.get("labels")
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def x__extract_labels__mutmut_3(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("XXlabelsXX")
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = metadata.get("labels")
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def x__extract_labels__mutmut_4(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("LABELS")
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = metadata.get("labels")
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def x__extract_labels__mutmut_5(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("labels")
    if isinstance(spec_labels, list):
        return tuple(None)
    meta_labels = metadata.get("labels")
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def x__extract_labels__mutmut_6(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("labels")
    if isinstance(spec_labels, list):
        return tuple(str(None) for value in spec_labels)
    meta_labels = metadata.get("labels")
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def x__extract_labels__mutmut_7(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("labels")
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = None
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def x__extract_labels__mutmut_8(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("labels")
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = metadata.get(None)
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def x__extract_labels__mutmut_9(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("labels")
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = metadata.get("XXlabelsXX")
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def x__extract_labels__mutmut_10(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("labels")
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = metadata.get("LABELS")
    if isinstance(meta_labels, dict):
        return tuple(sorted(f"{key}={value}" for key, value in meta_labels.items()))
    return ()


def x__extract_labels__mutmut_11(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("labels")
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = metadata.get("labels")
    if isinstance(meta_labels, dict):
        return tuple(None)
    return ()


def x__extract_labels__mutmut_12(spec: dict[str, object], metadata: dict[str, object]) -> tuple[str, ...]:
    spec_labels = spec.get("labels")
    if isinstance(spec_labels, list):
        return tuple(str(value) for value in spec_labels)
    meta_labels = metadata.get("labels")
    if isinstance(meta_labels, dict):
        return tuple(sorted(None))
    return ()

mutants_x__extract_labels__mutmut['_mutmut_orig'] = x__extract_labels__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut['x__extract_labels__mutmut_1'] = x__extract_labels__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut['x__extract_labels__mutmut_2'] = x__extract_labels__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut['x__extract_labels__mutmut_3'] = x__extract_labels__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut['x__extract_labels__mutmut_4'] = x__extract_labels__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut['x__extract_labels__mutmut_5'] = x__extract_labels__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut['x__extract_labels__mutmut_6'] = x__extract_labels__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut['x__extract_labels__mutmut_7'] = x__extract_labels__mutmut_7 # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut['x__extract_labels__mutmut_8'] = x__extract_labels__mutmut_8 # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut['x__extract_labels__mutmut_9'] = x__extract_labels__mutmut_9 # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut['x__extract_labels__mutmut_10'] = x__extract_labels__mutmut_10 # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut['x__extract_labels__mutmut_11'] = x__extract_labels__mutmut_11 # type: ignore # mutmut generated
mutants_x__extract_labels__mutmut['x__extract_labels__mutmut_12'] = x__extract_labels__mutmut_12 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__count_endpoint_ids__mutmut)
def _count_endpoint_ids(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(identity_id, 0) + 1
    return counts


def x__count_endpoint_ids__mutmut_orig(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(identity_id, 0) + 1
    return counts


def x__count_endpoint_ids__mutmut_1(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = None
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(identity_id, 0) + 1
    return counts


def x__count_endpoint_ids__mutmut_2(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = None
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(identity_id, 0) + 1
    return counts


def x__count_endpoint_ids__mutmut_3(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(None)
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(identity_id, 0) + 1
    return counts


def x__count_endpoint_ids__mutmut_4(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is not None:
            continue
        counts[identity_id] = counts.get(identity_id, 0) + 1
    return counts


def x__count_endpoint_ids__mutmut_5(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            break
        counts[identity_id] = counts.get(identity_id, 0) + 1
    return counts


def x__count_endpoint_ids__mutmut_6(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            continue
        counts[identity_id] = None
    return counts


def x__count_endpoint_ids__mutmut_7(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(identity_id, 0) - 1
    return counts


def x__count_endpoint_ids__mutmut_8(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(None, 0) + 1
    return counts


def x__count_endpoint_ids__mutmut_9(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(identity_id, None) + 1
    return counts


def x__count_endpoint_ids__mutmut_10(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(0) + 1
    return counts


def x__count_endpoint_ids__mutmut_11(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(identity_id, ) + 1
    return counts


def x__count_endpoint_ids__mutmut_12(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(identity_id, 1) + 1
    return counts


def x__count_endpoint_ids__mutmut_13(endpoints: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for endpoint in endpoints:
        identity_id = _endpoint_identity_id(endpoint)
        if identity_id is None:
            continue
        counts[identity_id] = counts.get(identity_id, 0) + 2
    return counts

mutants_x__count_endpoint_ids__mutmut['_mutmut_orig'] = x__count_endpoint_ids__mutmut_orig # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_1'] = x__count_endpoint_ids__mutmut_1 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_2'] = x__count_endpoint_ids__mutmut_2 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_3'] = x__count_endpoint_ids__mutmut_3 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_4'] = x__count_endpoint_ids__mutmut_4 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_5'] = x__count_endpoint_ids__mutmut_5 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_6'] = x__count_endpoint_ids__mutmut_6 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_7'] = x__count_endpoint_ids__mutmut_7 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_8'] = x__count_endpoint_ids__mutmut_8 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_9'] = x__count_endpoint_ids__mutmut_9 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_10'] = x__count_endpoint_ids__mutmut_10 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_11'] = x__count_endpoint_ids__mutmut_11 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_12'] = x__count_endpoint_ids__mutmut_12 # type: ignore # mutmut generated
mutants_x__count_endpoint_ids__mutmut['x__count_endpoint_ids__mutmut_13'] = x__count_endpoint_ids__mutmut_13 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__endpoint_identity_id__mutmut)
def _endpoint_identity_id(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_orig(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_1(endpoint: dict[str, object]) -> str | None:
    status = None
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_2(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(None)
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_3(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get(None))
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_4(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("XXstatusXX"))
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_5(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("STATUS"))
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_6(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = None
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_7(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get(None)
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_8(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get("XXidentityXX")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_9(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get("IDENTITY")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_10(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get("identity")
    if isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_11(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = None
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_12(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get(None)
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_13(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("XXidXX")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_14(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("ID")
    return str(raw_id) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_15(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(None) if raw_id is not None else None


def x__endpoint_identity_id__mutmut_16(endpoint: dict[str, object]) -> str | None:
    status = _as_dict(endpoint.get("status"))
    identity = status.get("identity")
    if not isinstance(identity, dict):
        return None
    raw_id = identity.get("id")
    return str(raw_id) if raw_id is None else None

mutants_x__endpoint_identity_id__mutmut['_mutmut_orig'] = x__endpoint_identity_id__mutmut_orig # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_1'] = x__endpoint_identity_id__mutmut_1 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_2'] = x__endpoint_identity_id__mutmut_2 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_3'] = x__endpoint_identity_id__mutmut_3 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_4'] = x__endpoint_identity_id__mutmut_4 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_5'] = x__endpoint_identity_id__mutmut_5 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_6'] = x__endpoint_identity_id__mutmut_6 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_7'] = x__endpoint_identity_id__mutmut_7 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_8'] = x__endpoint_identity_id__mutmut_8 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_9'] = x__endpoint_identity_id__mutmut_9 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_10'] = x__endpoint_identity_id__mutmut_10 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_11'] = x__endpoint_identity_id__mutmut_11 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_12'] = x__endpoint_identity_id__mutmut_12 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_13'] = x__endpoint_identity_id__mutmut_13 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_14'] = x__endpoint_identity_id__mutmut_14 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_15'] = x__endpoint_identity_id__mutmut_15 # type: ignore # mutmut generated
mutants_x__endpoint_identity_id__mutmut['x__endpoint_identity_id__mutmut_16'] = x__endpoint_identity_id__mutmut_16 # type: ignore # mutmut generated
