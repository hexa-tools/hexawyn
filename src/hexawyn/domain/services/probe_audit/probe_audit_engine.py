from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.probe_audit import MissingProbe, ProbeAuditResult

_HTTP_PORTS = frozenset({80, 443, 3000, 8000, 8080, 8081, 8443, 9090})


@dataclass(frozen=True)
class _DeploymentInfo:
    deployment_name: str
    namespace: str
    has_service: bool
    is_exposed: bool
    workload_type: str


def _deployment_info(dep: dict[str, object]) -> _DeploymentInfo:
    return _DeploymentInfo(
        deployment_name=str(dep.get("deployment_name", "")),
        namespace=str(dep.get("namespace", "")),
        has_service=_as_bool(dep.get("has_service")),
        is_exposed=_as_bool(dep.get("is_exposed_externally")),
        workload_type=str(dep.get("workload_type", "Deployment")),
    )


class ProbeAuditEngine:
    def detect(self, deployments: list[dict[str, object]]) -> ProbeAuditResult:
        result = ProbeAuditResult()

        for dep in deployments:
            containers_raw = dep.get("containers")
            containers: list[dict[str, object]] = (
                list(containers_raw) if isinstance(containers_raw, list) else []
            )

            missing_probes, exposed_ports = _find_missing_probes(containers)
            misconfigurations = _find_misconfigurations(containers)
            info = _deployment_info(dep)

            if missing_probes:
                severity = _classify_severity(
                    info.namespace, info.has_service, info.is_exposed, info.workload_type
                )
                primary_port = exposed_ports[0] if exposed_ports else 0
                suggestions = (
                    _suggest_readiness_probe(primary_port),
                    _suggest_liveness_probe(primary_port),
                )
                probe = _build_probe(info, missing_probes, severity, primary_port, suggestions)
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
                probe = _build_probe(info, misconfigurations, "warning", primary_port, ("", ""))
                result.misconfigured_probes.append(probe)

        return result


def _build_probe(
    info: _DeploymentInfo,
    missing: list[str],
    severity: str,
    exposed_port: int,
    suggestions: tuple[str, str],
) -> MissingProbe:
    readiness_suggestion, liveness_suggestion = suggestions
    return MissingProbe(
        deployment_name=info.deployment_name,
        namespace=info.namespace,
        missing=missing,
        severity=severity,
        exposed_port=exposed_port,
        readiness_suggestion=readiness_suggestion,
        liveness_suggestion=liveness_suggestion,
        has_service=info.has_service,
        workload_type=info.workload_type,
        is_exposed_externally=info.is_exposed,
    )


def _exposed_port_ints(c: dict[str, object]) -> list[int]:
    """Extract the valid (>0) integer ports exposed by a container."""
    raw = c.get("exposed_ports")
    if not isinstance(raw, list):
        return []
    return [_as_int(x) for x in raw if _as_int(x) > 0]


def _find_missing_probes(
    containers: list[dict[str, object]],
) -> tuple[list[str], list[int]]:
    all_exposed_ports: list[int] = []
    missing: set[str] = set()

    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        all_exposed_ports.extend(_exposed_port_ints(c))

        if not _as_bool(c.get("has_liveness_probe")):
            missing.add("livenessProbe")
        if not _as_bool(c.get("has_readiness_probe")):
            missing.add("readinessProbe")

    return (sorted(missing), all_exposed_ports)


def _find_misconfigurations(containers: list[dict[str, object]]) -> list[str]:
    issues: list[str] = []
    for c in containers:
        if _as_bool(c.get("is_init_container")):
            continue
        exposed_ints = _exposed_port_ints(c)

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
        ports = _exposed_port_ints(c)
        if ports:
            return ports[0]
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
