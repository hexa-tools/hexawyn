from __future__ import annotations

from hexawyn.domain.models.probe_audit import MissingProbe, ProbeAuditResult

_HTTP_PORTS = frozenset({80, 443, 3000, 8000, 8080, 8081, 8443, 9090})


class ProbeAuditEngine:
    def detect(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers", [])
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)

            if missing_probes:
                severity = _classify_severity(
                    str(dep.get("namespace", "")),
                    _as_bool(dep.get("has_service")),
                    _as_bool(dep.get("is_exposed_externally")),
                    str(dep.get("workload_type", "Deployment")),
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                readiness_suggestion = _suggest_readiness_probe(primary_port)
                liveness_suggestion = _suggest_liveness_probe(primary_port)

                probe = MissingProbe(
                    deployment_name=str(dep.get("deployment_name", "")),
                    namespace=str(dep.get("namespace", "")),
                    missing=missing_probes,
                    severity=severity,
                    exposed_port=primary_port,
                    readiness_suggestion=readiness_suggestion,
                    liveness_suggestion=liveness_suggestion,
                    has_service=_as_bool(dep.get("has_service")),
                    workload_type=str(dep.get("workload_type", "Deployment")),
                    is_exposed_externally=_as_bool(dep.get("is_exposed_externally")),
                )
                result.missing_probes.append(probe)

                if severity == "critical":
                    result.critical += 1
                elif severity == "warning":
                    result.warning += 1
                else:
                    result.informational += 1

                result.total_without_probes += 1

            elif misconfigurations:
                primary_port = _first_port(containers)
                probe = MissingProbe(
                    deployment_name=str(dep.get("deployment_name", "")),
                    namespace=str(dep.get("namespace", "")),
                    missing=misconfigurations,
                    severity="warning",
                    exposed_port=primary_port,
                    readiness_suggestion="",
                    liveness_suggestion="",
                    has_service=_as_bool(dep.get("has_service")),
                    workload_type=str(dep.get("workload_type", "Deployment")),
                    is_exposed_externally=_as_bool(dep.get("is_exposed_externally")),
                )
                result.misconfigured_probes.append(probe)

        return result


def _find_missing_probes(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()
    has_relevant_container = False

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        has_relevant_container = True

        ports_raw = c.get("exposed_ports", [])
        if isinstance(ports_raw, list):
            for p in ports_raw:
                port = _as_int(p)
                if port > 0:
                    all_exposed_ports.append(port)

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    if not has_relevant_container:
        return ([], all_exposed_ports)

    return (sorted(missing), all_exposed_ports)


def _find_misconfigurations(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_raw = c.get("exposed_ports", [])
        exposed_ints: list[int] = []
        if isinstance(exposed_raw, list):
            exposed_ints = [_as_int(x) for x in exposed_raw if _as_int(x) > 0]

        if _as_bool(c.get("has_readiness_probe")):
            rp = _as_int(c.get("readiness_port"))
            if rp > 0 and rp not in exposed_ints:
                issues.append("readiness_port_mismatch")

        if _as_bool(c.get("has_liveness_probe")):
            lp = _as_int(c.get("liveness_port"))
            if lp > 0 and lp not in exposed_ints:
                issues.append("liveness_port_mismatch")

    return issues


def _classify_severity(
    namespace: str,
    has_service: bool,
    is_exposed_externally: bool,
    workload_type: str,
) -> str:
    is_production = namespace in ("production", "prod")

    if workload_type in ("Job", "CronJob", "DaemonSet"):
        return "informational"

    if is_production and is_exposed_externally:
        return "critical"

    if is_production and has_service:
        return "warning"

    if workload_type == "StatefulSet" and has_service:
        return "critical"

    if has_service:
        return "warning"

    return "informational"


def _suggest_readiness_probe(port: int) -> str:
    if port == 0:
        return "exec: not supported"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, initialDelaySeconds: 10"
    return f"tcpSocket: {port}, initialDelaySeconds: 10"


def _suggest_liveness_probe(port: int) -> str:
    if port == 0:
        return "exec: not supported"
    if port in _HTTP_PORTS:
        return f"httpGet: /health path: {port}, periodSeconds: 30"
    return f"tcpSocket: {port}, periodSeconds: 30"


def _first_port(containers: list[dict[str, object]]) -> int:
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        ports_raw = c.get("exposed_ports", [])
        if isinstance(ports_raw, list):
            for p in ports_raw:
                port = _as_int(p)
                if port > 0:
                    return port
    return 0


def _as_bool(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def _as_int(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0
