from hexawyn.domain.services.schedule.check_runner import UseCaseRegistry


def _certs_list(params: dict[str, str]) -> dict[str, object]:
    from hexawyn.mcp.tools.check_cluster_certificate_health import check_cluster_certificate_health

    return check_cluster_certificate_health()


def _global_health(params: dict[str, str]) -> dict[str, object]:
    from hexawyn.mcp.tools.global_health_check import global_health_check

    return global_health_check()


def build_registry() -> UseCaseRegistry:
    registry: UseCaseRegistry = {}
    registry["certs_list"] = _certs_list
    registry["global_health_check"] = _global_health
    return registry
