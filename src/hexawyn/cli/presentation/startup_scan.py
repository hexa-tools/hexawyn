from hexawyn.cli.presentation.findings import is_error_narrative


def is_valid_startup_result(result_dict: dict[str, object]) -> bool:
    health_score = result_dict.get("health_score", 0)
    narrative = str(result_dict.get("narrative_summary", ""))
    cluster_summary = result_dict.get("cluster_summary", {})

    if not isinstance(health_score, int) or health_score <= 0:
        return False

    total_pods = cluster_summary.get("total_pods", 0) if isinstance(cluster_summary, dict) else 0
    if total_pods <= 0:
        return False

    if is_error_narrative(narrative):
        return False

    return True
