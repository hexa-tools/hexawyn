from __future__ import annotations

from hexawyn.application.ports.driven.drift_detection_port import (
    ResourceManifestRaw,
)
from hexawyn.application.ports.driven.live_resource_port import LiveResourceRaw
from hexawyn.application.use_case.security.configuration_drift_detection.response import (
    ConfigurationDriftDetectionResponse,
    DriftedFieldDict,
    DriftResultDict,
)
from hexawyn.domain.models.configuration_drift import (
    ConfigurationDriftReport,
    DriftedField,
    DriftResult,
    ResourceManifest,
)


def find_matching(
    manifests: list[ResourceManifestRaw],
    kind: str,
    name: str,
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["name"] == name:
            return raw
    return None


def to_manifest(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["name"],
        namespace=raw["namespace"],
        data=raw["data"],
    )


def to_live_manifest(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["name"],
        namespace=live["namespace"],
        data=live["data"],
    )


def to_response(
    report: ConfigurationDriftReport,
) -> ConfigurationDriftDetectionResponse:
    from hexawyn.application.use_case.security.configuration_drift_detection.response import (  # noqa: E501
        ConfigurationDriftDetectionResponse,
    )

    return ConfigurationDriftDetectionResponse(
        drifted_resources=[_to_result_dict(r) for r in report.drifted_resources],
        drifted_by_namespace={
            ns: [_to_result_dict(r) for r in results]
            for ns, results in report.drifted_by_namespace.items()
        },
        in_sync_count=report.in_sync_count,
        excluded_resources=report.excluded_resources,  # type: ignore
        total_checked=report.total_checked,
        summary=report.summary,
    )


def _to_result_dict(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def _to_field_dict(field: DriftedField) -> DriftedFieldDict:
    return DriftedFieldDict(
        field_path=field.field_path,
        desired_value=field.desired_value,
        live_value=field.live_value,
        severity=field.severity,
    )
