"""RED → GREEN — Layer 2: ProbeAuditEngine pure domain logic."""

from hexawyn.domain.services.probe_audit.probe_audit_engine import (
    ProbeAuditEngine,
    _as_bool,
    _as_int,
)


def _deployment(
    name: str,
    namespace: str = "production",
    workload_type: str = "Deployment",
    containers: list[dict[str, object]] | None = None,
    has_service: bool = False,
    is_exposed_externally: bool = False,
) -> dict[str, object]:
    return {
        "deployment_name": name,
        "namespace": namespace,
        "workload_type": workload_type,
        "containers": containers or [],
        "has_service": has_service,
        "is_exposed_externally": is_exposed_externally,
    }


def _container(
    name: str = "main",
    is_init: bool = False,
    exposed_ports: list[int] | None = None,
    has_liveness: bool = False,
    has_readiness: bool = False,
) -> dict[str, object]:
    return {
        "container_name": name,
        "is_init_container": is_init,
        "exposed_ports": exposed_ports or [],
        "has_liveness_probe": has_liveness,
        "has_readiness_probe": has_readiness,
        "liveness_probe_type": "httpGet" if has_liveness else "",
        "readiness_probe_type": "httpGet" if has_readiness else "",
        "liveness_http_path": "/health" if has_liveness else "",
        "readiness_http_path": "/health" if has_readiness else "",
        "liveness_port": 8080 if has_liveness else 0,
        "readiness_port": 8080 if has_readiness else 0,
    }


class TestProbePresenceCheck:
    def test_both_probes_missing_critical(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "payment-service",
                namespace="production",
                is_exposed_externally=True,
                has_service=True,
                containers=[_container(exposed_ports=[8080])],
            ),
        ]

        result = engine.detect(deployments)

        assert result.total_without_probes == 1
        assert result.critical == 1
        assert result.missing_probes[0].deployment_name == "payment-service"
        assert result.missing_probes[0].severity == "critical"
        assert set(result.missing_probes[0].missing) == {"livenessProbe", "readinessProbe"}

    def test_has_readiness_but_no_liveness_warning(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "auth-service",
                namespace="production",
                has_service=True,
                containers=[_container(has_readiness=True, exposed_ports=[8081])],
            ),
        ]

        result = engine.detect(deployments)

        assert result.total_without_probes == 1
        assert result.warning == 1
        assert result.missing_probes[0].deployment_name == "auth-service"
        assert result.missing_probes[0].severity == "warning"
        assert result.missing_probes[0].missing == ["livenessProbe"]

    def test_batch_job_no_probes_informational(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "batch-processor",
                namespace="batch",
                workload_type="Job",
                containers=[_container()],
            ),
        ]

        result = engine.detect(deployments)

        assert result.total_without_probes == 1
        assert result.informational == 1
        assert result.missing_probes[0].severity == "informational"

    def test_all_probes_present_no_issues(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "healthy-service",
                namespace="production",
                has_service=True,
                is_exposed_externally=True,
                containers=[_container(has_liveness=True, has_readiness=True)],
            ),
        ]

        result = engine.detect(deployments)

        assert result.total_without_probes == 0
        assert result.critical == 0
        assert result.warning == 0

    def test_eight_deployments_missing_probes_all_listed(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                f"service-{i}",
                namespace="production",
                has_service=True,
                is_exposed_externally=(i < 3),
                containers=[_container()],
            )
            for i in range(8)
        ]

        result = engine.detect(deployments)

        assert result.total_without_probes == 8
        assert result.critical == 3
        assert result.warning == 5
        assert len(result.missing_probes) == 8


class TestEdgeCases:
    def test_daemonset_no_probes_informational(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "node-logger",
                namespace="kube-system",
                workload_type="DaemonSet",
                containers=[_container()],
            ),
        ]

        result = engine.detect(deployments)

        assert result.total_without_probes == 1
        assert result.informational == 1
        assert result.missing_probes[0].severity == "informational"

    def test_statefulset_no_probes_critical(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "db-cluster",
                namespace="production",
                workload_type="StatefulSet",
                has_service=True,
                is_exposed_externally=True,
                containers=[_container(exposed_ports=[5432])],
            ),
        ]

        result = engine.detect(deployments)

        assert result.total_without_probes == 1
        assert result.critical == 1
        assert result.missing_probes[0].deployment_name == "db-cluster"

    def test_init_containers_excluded_from_check(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "web-app",
                namespace="production",
                has_service=True,
                containers=[
                    _container(name="init-db", is_init=True),
                    _container(name="app", has_liveness=True, has_readiness=True),
                ],
            ),
        ]

        result = engine.detect(deployments)

        assert result.total_without_probes == 0

    def test_no_exposed_ports_exec_probe_suggestion(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "worker-processor",
                namespace="production",
                has_service=True,
                containers=[_container(exposed_ports=[])],
            ),
        ]

        result = engine.detect(deployments)

        assert len(result.missing_probes) == 1
        suggestion = result.missing_probes[0]
        assert (
            "exec:" in suggestion.liveness_suggestion
            or suggestion.liveness_suggestion == "exec: not supported"
        )
        assert (
            "exec:" in suggestion.readiness_suggestion
            or suggestion.readiness_suggestion == "exec: not supported"
        )

    def test_empty_deployments_list_returns_empty_result(self) -> None:
        engine = ProbeAuditEngine()

        result = engine.detect([])

        assert result.total_without_probes == 0
        assert result.missing_probes == []

    def test_only_init_containers_no_main_container(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "init-only",
                containers=[_container(name="setup", is_init=True, exposed_ports=[])],
            ),
        ]

        result = engine.detect(deployments)

        assert result.total_without_probes == 0

    def test_probe_misconfigured_wrong_path_detected(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "broken-probe",
                namespace="production",
                has_service=True,
                containers=[
                    {
                        "container_name": "app",
                        "is_init_container": False,
                        "exposed_ports": [8080],
                        "has_liveness_probe": True,
                        "has_readiness_probe": True,
                        "liveness_probe_type": "httpGet",
                        "readiness_probe_type": "httpGet",
                        "liveness_http_path": "/healthz",
                        "readiness_http_path": "/wrong-path",
                        "liveness_port": 8080,
                        "readiness_port": 9090,
                    },
                ],
            ),
        ]

        result = engine.detect(deployments)

        assert result.total_without_probes == 0
        assert len(result.misconfigured_probes) == 1
        mc = result.misconfigured_probes[0]
        assert mc.deployment_name == "broken-probe"
        assert mc.severity == "warning"
        assert len(mc.missing) > 0


class TestProbeSuggestion:
    def test_http_probe_suggestion_for_port_8080(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "web-app",
                namespace="production",
                containers=[_container(exposed_ports=[8080])],
            ),
        ]

        result = engine.detect(deployments)

        assert len(result.missing_probes) == 1
        suggestion = result.missing_probes[0]
        assert "httpGet" in suggestion.readiness_suggestion
        assert "8080" in suggestion.readiness_suggestion

    def test_tcp_probe_suggestion_for_non_http_port(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "db-service",
                namespace="production",
                containers=[_container(exposed_ports=[5432])],
            ),
        ]

        result = engine.detect(deployments)

        assert len(result.missing_probes) == 1
        suggestion = result.missing_probes[0]
        assert "tcpSocket" in suggestion.liveness_suggestion
        assert "5432" in suggestion.liveness_suggestion


class TestSeverityClassification:
    def test_production_exposed_missing_both_critical(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "api-gateway",
                namespace="production",
                has_service=True,
                is_exposed_externally=True,
                containers=[_container(exposed_ports=[443])],
            ),
        ]

        result = engine.detect(deployments)

        assert result.missing_probes[0].severity == "critical"

    def test_staging_namespace_warning(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "test-service",
                namespace="staging",
                has_service=True,
                containers=[_container()],
            ),
        ]

        result = engine.detect(deployments)

        assert result.missing_probes[0].severity == "warning"

    def test_non_prod_no_service_informational(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "experiment",
                namespace="dev",
                containers=[_container()],
            ),
        ]

        result = engine.detect(deployments)

        assert result.missing_probes[0].severity == "informational"

    def test_statefulset_with_service_non_production_critical(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "db-replica",
                namespace="staging",
                workload_type="StatefulSet",
                has_service=True,
                containers=[_container(exposed_ports=[5432])],
            ),
        ]

        result = engine.detect(deployments)

        assert result.critical == 1
        assert result.missing_probes[0].severity == "critical"
        assert result.missing_probes[0].deployment_name == "db-replica"


class TestResultMetadata:
    def test_total_counts_computed_correctly(self) -> None:
        engine = ProbeAuditEngine()
        deployments = [
            _deployment(
                "critical-svc",
                namespace="production",
                has_service=True,
                is_exposed_externally=True,
                containers=[_container(exposed_ports=[8080])],
            ),
            _deployment(
                "warning-svc",
                namespace="production",
                has_service=True,
                containers=[_container(exposed_ports=[3000])],
            ),
            _deployment(
                "info-job",
                namespace="batch",
                workload_type="Job",
                containers=[_container()],
            ),
        ]

        result = engine.detect(deployments)

        assert result.total_without_probes == 3
        assert result.critical == 1
        assert result.warning == 1
        assert result.informational == 1


class TestHelperFunctions:
    def test_as_bool_none_false(self) -> None:
        assert _as_bool(None) is False

    def test_as_bool_true_is_true(self) -> None:
        assert _as_bool(True) is True

    def test_as_bool_non_empty_string_true(self) -> None:
        assert _as_bool("yes") is True

    def test_as_bool_zero_false(self) -> None:
        assert _as_bool(0) is False

    def test_as_int_none_zero(self) -> None:
        assert _as_int(None) == 0

    def test_as_int_float_truncated(self) -> None:
        assert _as_int(3.9) == 3

    def test_as_int_list_zero(self) -> None:
        assert _as_int([1, 2]) == 0
