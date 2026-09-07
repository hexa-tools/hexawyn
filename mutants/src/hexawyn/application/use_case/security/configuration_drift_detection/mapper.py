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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_find_matching__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_find_matching__mutmut)
def find_matching(
    manifests: list[ResourceManifestRaw],
    kind: str,
    name: str,
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["name"] == name:
            return raw
    return None


def x_find_matching__mutmut_orig(
    manifests: list[ResourceManifestRaw],
    kind: str,
    name: str,
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["name"] == name:
            return raw
    return None


def x_find_matching__mutmut_1(
    manifests: list[ResourceManifestRaw],
    kind: str,
    name: str,
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind or raw["name"] == name:
            return raw
    return None


def x_find_matching__mutmut_2(
    manifests: list[ResourceManifestRaw],
    kind: str,
    name: str,
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["XXkindXX"] == kind and raw["name"] == name:
            return raw
    return None


def x_find_matching__mutmut_3(
    manifests: list[ResourceManifestRaw],
    kind: str,
    name: str,
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["KIND"] == kind and raw["name"] == name:
            return raw
    return None


def x_find_matching__mutmut_4(
    manifests: list[ResourceManifestRaw],
    kind: str,
    name: str,
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] != kind and raw["name"] == name:
            return raw
    return None


def x_find_matching__mutmut_5(
    manifests: list[ResourceManifestRaw],
    kind: str,
    name: str,
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["XXnameXX"] == name:
            return raw
    return None


def x_find_matching__mutmut_6(
    manifests: list[ResourceManifestRaw],
    kind: str,
    name: str,
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["NAME"] == name:
            return raw
    return None


def x_find_matching__mutmut_7(
    manifests: list[ResourceManifestRaw],
    kind: str,
    name: str,
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["name"] != name:
            return raw
    return None

mutants_x_find_matching__mutmut['_mutmut_orig'] = x_find_matching__mutmut_orig # type: ignore # mutmut generated
mutants_x_find_matching__mutmut['x_find_matching__mutmut_1'] = x_find_matching__mutmut_1 # type: ignore # mutmut generated
mutants_x_find_matching__mutmut['x_find_matching__mutmut_2'] = x_find_matching__mutmut_2 # type: ignore # mutmut generated
mutants_x_find_matching__mutmut['x_find_matching__mutmut_3'] = x_find_matching__mutmut_3 # type: ignore # mutmut generated
mutants_x_find_matching__mutmut['x_find_matching__mutmut_4'] = x_find_matching__mutmut_4 # type: ignore # mutmut generated
mutants_x_find_matching__mutmut['x_find_matching__mutmut_5'] = x_find_matching__mutmut_5 # type: ignore # mutmut generated
mutants_x_find_matching__mutmut['x_find_matching__mutmut_6'] = x_find_matching__mutmut_6 # type: ignore # mutmut generated
mutants_x_find_matching__mutmut['x_find_matching__mutmut_7'] = x_find_matching__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_manifest__mutmut)
def to_manifest(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["name"],
        namespace=raw["namespace"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_orig(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["name"],
        namespace=raw["namespace"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_1(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=None,
        name=raw["name"],
        namespace=raw["namespace"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_2(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=None,
        namespace=raw["namespace"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_3(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["name"],
        namespace=None,
        data=raw["data"],
    )


def x_to_manifest__mutmut_4(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["name"],
        namespace=raw["namespace"],
        data=None,
    )


def x_to_manifest__mutmut_5(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        name=raw["name"],
        namespace=raw["namespace"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_6(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        namespace=raw["namespace"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_7(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["name"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_8(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["name"],
        namespace=raw["namespace"],
        )


def x_to_manifest__mutmut_9(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["XXkindXX"],
        name=raw["name"],
        namespace=raw["namespace"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_10(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["KIND"],
        name=raw["name"],
        namespace=raw["namespace"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_11(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["XXnameXX"],
        namespace=raw["namespace"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_12(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["NAME"],
        namespace=raw["namespace"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_13(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["name"],
        namespace=raw["XXnamespaceXX"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_14(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["name"],
        namespace=raw["NAMESPACE"],
        data=raw["data"],
    )


def x_to_manifest__mutmut_15(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["name"],
        namespace=raw["namespace"],
        data=raw["XXdataXX"],
    )


def x_to_manifest__mutmut_16(raw: ResourceManifestRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=raw["kind"],
        name=raw["name"],
        namespace=raw["namespace"],
        data=raw["DATA"],
    )

mutants_x_to_manifest__mutmut['_mutmut_orig'] = x_to_manifest__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_1'] = x_to_manifest__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_2'] = x_to_manifest__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_3'] = x_to_manifest__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_4'] = x_to_manifest__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_5'] = x_to_manifest__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_6'] = x_to_manifest__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_7'] = x_to_manifest__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_8'] = x_to_manifest__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_9'] = x_to_manifest__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_10'] = x_to_manifest__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_11'] = x_to_manifest__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_12'] = x_to_manifest__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_13'] = x_to_manifest__mutmut_13 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_14'] = x_to_manifest__mutmut_14 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_15'] = x_to_manifest__mutmut_15 # type: ignore # mutmut generated
mutants_x_to_manifest__mutmut['x_to_manifest__mutmut_16'] = x_to_manifest__mutmut_16 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_live_manifest__mutmut)
def to_live_manifest(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["name"],
        namespace=live["namespace"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_orig(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["name"],
        namespace=live["namespace"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_1(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=None,
        name=live["name"],
        namespace=live["namespace"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_2(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=None,
        namespace=live["namespace"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_3(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["name"],
        namespace=None,
        data=live["data"],
    )


def x_to_live_manifest__mutmut_4(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["name"],
        namespace=live["namespace"],
        data=None,
    )


def x_to_live_manifest__mutmut_5(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        name=live["name"],
        namespace=live["namespace"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_6(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        namespace=live["namespace"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_7(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["name"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_8(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["name"],
        namespace=live["namespace"],
        )


def x_to_live_manifest__mutmut_9(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["XXkindXX"],
        name=live["name"],
        namespace=live["namespace"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_10(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["KIND"],
        name=live["name"],
        namespace=live["namespace"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_11(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["XXnameXX"],
        namespace=live["namespace"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_12(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["NAME"],
        namespace=live["namespace"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_13(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["name"],
        namespace=live["XXnamespaceXX"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_14(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["name"],
        namespace=live["NAMESPACE"],
        data=live["data"],
    )


def x_to_live_manifest__mutmut_15(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["name"],
        namespace=live["namespace"],
        data=live["XXdataXX"],
    )


def x_to_live_manifest__mutmut_16(live: LiveResourceRaw) -> ResourceManifest:
    return ResourceManifest(
        kind=live["kind"],
        name=live["name"],
        namespace=live["namespace"],
        data=live["DATA"],
    )

mutants_x_to_live_manifest__mutmut['_mutmut_orig'] = x_to_live_manifest__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_1'] = x_to_live_manifest__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_2'] = x_to_live_manifest__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_3'] = x_to_live_manifest__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_4'] = x_to_live_manifest__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_5'] = x_to_live_manifest__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_6'] = x_to_live_manifest__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_7'] = x_to_live_manifest__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_8'] = x_to_live_manifest__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_9'] = x_to_live_manifest__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_10'] = x_to_live_manifest__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_11'] = x_to_live_manifest__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_12'] = x_to_live_manifest__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_13'] = x_to_live_manifest__mutmut_13 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_14'] = x_to_live_manifest__mutmut_14 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_15'] = x_to_live_manifest__mutmut_15 # type: ignore # mutmut generated
mutants_x_to_live_manifest__mutmut['x_to_live_manifest__mutmut_16'] = x_to_live_manifest__mutmut_16 # type: ignore # mutmut generated
mutants_x_to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_response__mutmut)
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


def x_to_response__mutmut_orig(
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


def x_to_response__mutmut_1(
    report: ConfigurationDriftReport,
) -> ConfigurationDriftDetectionResponse:
    from hexawyn.application.use_case.security.configuration_drift_detection.response import (  # noqa: E501
        ConfigurationDriftDetectionResponse,
    )

    return ConfigurationDriftDetectionResponse(
        drifted_resources=None,
        drifted_by_namespace={
            ns: [_to_result_dict(r) for r in results]
            for ns, results in report.drifted_by_namespace.items()
        },
        in_sync_count=report.in_sync_count,
        excluded_resources=report.excluded_resources,  # type: ignore
        total_checked=report.total_checked,
        summary=report.summary,
    )


def x_to_response__mutmut_2(
    report: ConfigurationDriftReport,
) -> ConfigurationDriftDetectionResponse:
    from hexawyn.application.use_case.security.configuration_drift_detection.response import (  # noqa: E501
        ConfigurationDriftDetectionResponse,
    )

    return ConfigurationDriftDetectionResponse(
        drifted_resources=[_to_result_dict(r) for r in report.drifted_resources],
        drifted_by_namespace=None,
        in_sync_count=report.in_sync_count,
        excluded_resources=report.excluded_resources,  # type: ignore
        total_checked=report.total_checked,
        summary=report.summary,
    )


def x_to_response__mutmut_3(
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
        in_sync_count=None,
        excluded_resources=report.excluded_resources,  # type: ignore
        total_checked=report.total_checked,
        summary=report.summary,
    )


def x_to_response__mutmut_4(
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
        excluded_resources=None,  # type: ignore
        total_checked=report.total_checked,
        summary=report.summary,
    )


def x_to_response__mutmut_5(
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
        total_checked=None,
        summary=report.summary,
    )


def x_to_response__mutmut_6(
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
        summary=None,
    )


def x_to_response__mutmut_7(
    report: ConfigurationDriftReport,
) -> ConfigurationDriftDetectionResponse:
    from hexawyn.application.use_case.security.configuration_drift_detection.response import (  # noqa: E501
        ConfigurationDriftDetectionResponse,
    )

    return ConfigurationDriftDetectionResponse(
        drifted_by_namespace={
            ns: [_to_result_dict(r) for r in results]
            for ns, results in report.drifted_by_namespace.items()
        },
        in_sync_count=report.in_sync_count,
        excluded_resources=report.excluded_resources,  # type: ignore
        total_checked=report.total_checked,
        summary=report.summary,
    )


def x_to_response__mutmut_8(
    report: ConfigurationDriftReport,
) -> ConfigurationDriftDetectionResponse:
    from hexawyn.application.use_case.security.configuration_drift_detection.response import (  # noqa: E501
        ConfigurationDriftDetectionResponse,
    )

    return ConfigurationDriftDetectionResponse(
        drifted_resources=[_to_result_dict(r) for r in report.drifted_resources],
        in_sync_count=report.in_sync_count,
        excluded_resources=report.excluded_resources,  # type: ignore
        total_checked=report.total_checked,
        summary=report.summary,
    )


def x_to_response__mutmut_9(
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
        excluded_resources=report.excluded_resources,  # type: ignore
        total_checked=report.total_checked,
        summary=report.summary,
    )


def x_to_response__mutmut_10(
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
        total_checked=report.total_checked,
        summary=report.summary,
    )


def x_to_response__mutmut_11(
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
        summary=report.summary,
    )


def x_to_response__mutmut_12(
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
        )


def x_to_response__mutmut_13(
    report: ConfigurationDriftReport,
) -> ConfigurationDriftDetectionResponse:
    from hexawyn.application.use_case.security.configuration_drift_detection.response import (  # noqa: E501
        ConfigurationDriftDetectionResponse,
    )

    return ConfigurationDriftDetectionResponse(
        drifted_resources=[_to_result_dict(None) for r in report.drifted_resources],
        drifted_by_namespace={
            ns: [_to_result_dict(r) for r in results]
            for ns, results in report.drifted_by_namespace.items()
        },
        in_sync_count=report.in_sync_count,
        excluded_resources=report.excluded_resources,  # type: ignore
        total_checked=report.total_checked,
        summary=report.summary,
    )


def x_to_response__mutmut_14(
    report: ConfigurationDriftReport,
) -> ConfigurationDriftDetectionResponse:
    from hexawyn.application.use_case.security.configuration_drift_detection.response import (  # noqa: E501
        ConfigurationDriftDetectionResponse,
    )

    return ConfigurationDriftDetectionResponse(
        drifted_resources=[_to_result_dict(r) for r in report.drifted_resources],
        drifted_by_namespace={
            ns: [_to_result_dict(None) for r in results]
            for ns, results in report.drifted_by_namespace.items()
        },
        in_sync_count=report.in_sync_count,
        excluded_resources=report.excluded_resources,  # type: ignore
        total_checked=report.total_checked,
        summary=report.summary,
    )

mutants_x_to_response__mutmut['_mutmut_orig'] = x_to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_1'] = x_to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_2'] = x_to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_3'] = x_to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_4'] = x_to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_5'] = x_to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_6'] = x_to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_7'] = x_to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_8'] = x_to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_9'] = x_to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_10'] = x_to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_11'] = x_to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_12'] = x_to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_13'] = x_to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_14'] = x_to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_result_dict__mutmut)
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


def x__to_result_dict__mutmut_orig(result: DriftResult) -> DriftResultDict:
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


def x__to_result_dict__mutmut_1(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=None,
        name=result.name,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_2(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=None,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_3(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=None,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_4(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        managed_by=None,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_5(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=None,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_6(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=None,
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_7(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=None,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_8(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=None,
    )


def x__to_result_dict__mutmut_9(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        name=result.name,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_10(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_11(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_12(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_13(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        managed_by=result.managed_by,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_14(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_15(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        is_orphaned=result.is_orphaned,
    )


def x__to_result_dict__mutmut_16(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(f) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        )


def x__to_result_dict__mutmut_17(result: DriftResult) -> DriftResultDict:
    return DriftResultDict(
        kind=result.kind,
        name=result.name,
        namespace=result.namespace,
        managed_by=result.managed_by,
        release_or_source=result.release_or_source,
        drifted_fields=[_to_field_dict(None) for f in result.drifted_fields],
        has_critical_drift=result.has_critical_drift,
        is_orphaned=result.is_orphaned,
    )

mutants_x__to_result_dict__mutmut['_mutmut_orig'] = x__to_result_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_1'] = x__to_result_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_2'] = x__to_result_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_3'] = x__to_result_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_4'] = x__to_result_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_5'] = x__to_result_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_6'] = x__to_result_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_7'] = x__to_result_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_8'] = x__to_result_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_9'] = x__to_result_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_10'] = x__to_result_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_11'] = x__to_result_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_12'] = x__to_result_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_13'] = x__to_result_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_14'] = x__to_result_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_15'] = x__to_result_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_16'] = x__to_result_dict__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_result_dict__mutmut['x__to_result_dict__mutmut_17'] = x__to_result_dict__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_field_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_field_dict__mutmut)
def _to_field_dict(field: DriftedField) -> DriftedFieldDict:
    return DriftedFieldDict(
        field_path=field.field_path,
        desired_value=field.desired_value,
        live_value=field.live_value,
        severity=field.severity,
    )


def x__to_field_dict__mutmut_orig(field: DriftedField) -> DriftedFieldDict:
    return DriftedFieldDict(
        field_path=field.field_path,
        desired_value=field.desired_value,
        live_value=field.live_value,
        severity=field.severity,
    )


def x__to_field_dict__mutmut_1(field: DriftedField) -> DriftedFieldDict:
    return DriftedFieldDict(
        field_path=None,
        desired_value=field.desired_value,
        live_value=field.live_value,
        severity=field.severity,
    )


def x__to_field_dict__mutmut_2(field: DriftedField) -> DriftedFieldDict:
    return DriftedFieldDict(
        field_path=field.field_path,
        desired_value=None,
        live_value=field.live_value,
        severity=field.severity,
    )


def x__to_field_dict__mutmut_3(field: DriftedField) -> DriftedFieldDict:
    return DriftedFieldDict(
        field_path=field.field_path,
        desired_value=field.desired_value,
        live_value=None,
        severity=field.severity,
    )


def x__to_field_dict__mutmut_4(field: DriftedField) -> DriftedFieldDict:
    return DriftedFieldDict(
        field_path=field.field_path,
        desired_value=field.desired_value,
        live_value=field.live_value,
        severity=None,
    )


def x__to_field_dict__mutmut_5(field: DriftedField) -> DriftedFieldDict:
    return DriftedFieldDict(
        desired_value=field.desired_value,
        live_value=field.live_value,
        severity=field.severity,
    )


def x__to_field_dict__mutmut_6(field: DriftedField) -> DriftedFieldDict:
    return DriftedFieldDict(
        field_path=field.field_path,
        live_value=field.live_value,
        severity=field.severity,
    )


def x__to_field_dict__mutmut_7(field: DriftedField) -> DriftedFieldDict:
    return DriftedFieldDict(
        field_path=field.field_path,
        desired_value=field.desired_value,
        severity=field.severity,
    )


def x__to_field_dict__mutmut_8(field: DriftedField) -> DriftedFieldDict:
    return DriftedFieldDict(
        field_path=field.field_path,
        desired_value=field.desired_value,
        live_value=field.live_value,
        )

mutants_x__to_field_dict__mutmut['_mutmut_orig'] = x__to_field_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_field_dict__mutmut['x__to_field_dict__mutmut_1'] = x__to_field_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_field_dict__mutmut['x__to_field_dict__mutmut_2'] = x__to_field_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_field_dict__mutmut['x__to_field_dict__mutmut_3'] = x__to_field_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_field_dict__mutmut['x__to_field_dict__mutmut_4'] = x__to_field_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_field_dict__mutmut['x__to_field_dict__mutmut_5'] = x__to_field_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_field_dict__mutmut['x__to_field_dict__mutmut_6'] = x__to_field_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_field_dict__mutmut['x__to_field_dict__mutmut_7'] = x__to_field_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_field_dict__mutmut['x__to_field_dict__mutmut_8'] = x__to_field_dict__mutmut_8 # type: ignore # mutmut generated
