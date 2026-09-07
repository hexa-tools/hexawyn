from __future__ import annotations

from hexawyn.application.ports.driven.drift_detection_port import ResourceManifestRaw
from hexawyn.application.ports.driven.image_drift_port import ResolvedContainerImageRaw


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_index_resolved_images__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_index_resolved_images__mutmut)
def index_resolved_images(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["container"]): item["image_id"] for item in resolved}


def x_index_resolved_images__mutmut_orig(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["container"]): item["image_id"] for item in resolved}


def x_index_resolved_images__mutmut_1(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["XXdeploymentXX"], item["container"]): item["image_id"] for item in resolved}


def x_index_resolved_images__mutmut_2(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["DEPLOYMENT"], item["container"]): item["image_id"] for item in resolved}


def x_index_resolved_images__mutmut_3(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["XXcontainerXX"]): item["image_id"] for item in resolved}


def x_index_resolved_images__mutmut_4(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["CONTAINER"]): item["image_id"] for item in resolved}


def x_index_resolved_images__mutmut_5(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["container"]): item["XXimage_idXX"] for item in resolved}


def x_index_resolved_images__mutmut_6(
    resolved: list[ResolvedContainerImageRaw],
) -> dict[tuple[str, str], str]:
    return {(item["deployment"], item["container"]): item["IMAGE_ID"] for item in resolved}

mutants_x_index_resolved_images__mutmut['_mutmut_orig'] = x_index_resolved_images__mutmut_orig # type: ignore # mutmut generated
mutants_x_index_resolved_images__mutmut['x_index_resolved_images__mutmut_1'] = x_index_resolved_images__mutmut_1 # type: ignore # mutmut generated
mutants_x_index_resolved_images__mutmut['x_index_resolved_images__mutmut_2'] = x_index_resolved_images__mutmut_2 # type: ignore # mutmut generated
mutants_x_index_resolved_images__mutmut['x_index_resolved_images__mutmut_3'] = x_index_resolved_images__mutmut_3 # type: ignore # mutmut generated
mutants_x_index_resolved_images__mutmut['x_index_resolved_images__mutmut_4'] = x_index_resolved_images__mutmut_4 # type: ignore # mutmut generated
mutants_x_index_resolved_images__mutmut['x_index_resolved_images__mutmut_5'] = x_index_resolved_images__mutmut_5 # type: ignore # mutmut generated
mutants_x_index_resolved_images__mutmut['x_index_resolved_images__mutmut_6'] = x_index_resolved_images__mutmut_6 # type: ignore # mutmut generated
mutants_x_find_matching__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_find_matching__mutmut)
def find_matching(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["name"] == name:
            return raw
    return None


def x_find_matching__mutmut_orig(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["name"] == name:
            return raw
    return None


def x_find_matching__mutmut_1(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind or raw["name"] == name:
            return raw
    return None


def x_find_matching__mutmut_2(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["XXkindXX"] == kind and raw["name"] == name:
            return raw
    return None


def x_find_matching__mutmut_3(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["KIND"] == kind and raw["name"] == name:
            return raw
    return None


def x_find_matching__mutmut_4(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] != kind and raw["name"] == name:
            return raw
    return None


def x_find_matching__mutmut_5(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["XXnameXX"] == name:
            return raw
    return None


def x_find_matching__mutmut_6(
    manifests: list[ResourceManifestRaw], kind: str, name: str
) -> ResourceManifestRaw | None:
    for raw in manifests:
        if raw["kind"] == kind and raw["NAME"] == name:
            return raw
    return None


def x_find_matching__mutmut_7(
    manifests: list[ResourceManifestRaw], kind: str, name: str
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
