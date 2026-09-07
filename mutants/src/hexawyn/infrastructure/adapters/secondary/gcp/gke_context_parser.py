from typing import TypedDict

_PREFIX = "gke_"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GKEContextInfo(TypedDict):
    project_id: str
    region: str
    cluster: str
mutants_x_parse_gke_context__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_gke_context__mutmut)
def parse_gke_context(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_orig(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_1(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_2(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(None):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_3(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = None
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_4(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split(None)
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_5(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("XX_XX")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_6(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) == 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_7(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_8(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = None
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_9(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region and not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_10(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id and not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_11(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_12(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_13(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_14(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"XXproject_idXX": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_15(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"PROJECT_ID": project_id, "region": region, "cluster": cluster}


def x_parse_gke_context__mutmut_16(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "XXregionXX": region, "cluster": cluster}


def x_parse_gke_context__mutmut_17(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "REGION": region, "cluster": cluster}


def x_parse_gke_context__mutmut_18(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "XXclusterXX": cluster}


def x_parse_gke_context__mutmut_19(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:  # noqa: PLR2004
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "CLUSTER": cluster}

mutants_x_parse_gke_context__mutmut['_mutmut_orig'] = x_parse_gke_context__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_1'] = x_parse_gke_context__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_2'] = x_parse_gke_context__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_3'] = x_parse_gke_context__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_4'] = x_parse_gke_context__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_5'] = x_parse_gke_context__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_6'] = x_parse_gke_context__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_7'] = x_parse_gke_context__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_8'] = x_parse_gke_context__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_9'] = x_parse_gke_context__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_10'] = x_parse_gke_context__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_11'] = x_parse_gke_context__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_12'] = x_parse_gke_context__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_13'] = x_parse_gke_context__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_14'] = x_parse_gke_context__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_15'] = x_parse_gke_context__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_16'] = x_parse_gke_context__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_17'] = x_parse_gke_context__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_18'] = x_parse_gke_context__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_gke_context__mutmut['x_parse_gke_context__mutmut_19'] = x_parse_gke_context__mutmut_19 # type: ignore # mutmut generated
