from typing import TypedDict

_PREFIX = "gke_"


class GKEContextInfo(TypedDict):
    project_id: str
    region: str
    cluster: str


def parse_gke_context(context_name: str) -> GKEContextInfo | None:
    """Parse a GKE kubeconfig context name into project/region/cluster.

    Expected format: gke_PROJECT_REGION_CLUSTER
    Returns None when the name does not match the GKE convention.
    """
    if not context_name.startswith(_PREFIX):
        return None
    parts = context_name[len(_PREFIX) :].split("_")
    if len(parts) != 3:
        return None
    project_id, region, cluster = parts
    if not project_id or not region or not cluster:
        return None
    return {"project_id": project_id, "region": region, "cluster": cluster}
