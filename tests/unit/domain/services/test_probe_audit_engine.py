"""RED → GREEN — Layer 2: ProbeAuditEngine pure domain logic."""

from hexawyn.domain.services.probe_audit.probe_audit_engine import (
    ProbeAuditEngine,
    _as_bool,
    _as_int,
    _classify_severity,
    _exposed_port_ints,
    _find_misconfigurations,
    _find_missing_probes,
    _first_port,
)


def _deployment(  # noqa: PLR0913
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
        assert result.warning == 0
        assert result.informational == 0
        probe = result.missing_probes[0]
        assert probe.deployment_name == "payment-service"
        assert probe.namespace == "production"
        assert probe.severity == "critical"
        assert set(probe.missing) == {"livenessProbe", "readinessProbe"}
        assert probe.exposed_port == 8080  # noqa: PLR2004
        assert probe.has_service is True
        assert probe.workload_type == "Deployment"
        assert probe.is_exposed_externally is True
        assert probe.readiness_suggestion == "httpGet: /health path: 8080, initialDelaySeconds: 10"
        assert probe.liveness_suggestion == "httpGet: /health path: 8080, periodSeconds: 30"

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
                is_exposed_externally=(i < 3),  # noqa: PLR2004
                containers=[_container()],
            )
            for i in range(8)
        ]

        result = engine.detect(deployments)

        assert result.total_without_probes == 8  # noqa: PLR2004
        assert result.critical == 3  # noqa: PLR2004
        assert result.warning == 5  # noqa: PLR2004
        assert len(result.missing_probes) == 8  # noqa: PLR2004


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
        assert suggestion.liveness_suggestion == "exec: not supported"
        assert suggestion.readiness_suggestion == "exec: not supported"

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

        assert result.total_without_probes == 3  # noqa: PLR2004
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
        assert _as_int(3.9) == 3  # noqa: PLR2004

    def test_as_int_list_zero(self) -> None:
        assert _as_int([1, 2]) == 0


class TestFullFieldsDetection:
    def test_misconfigured_probe_all_fields(self) -> None:
        # probes presentes mais port mismatch -> pas de "missing", branche elif
        engine = ProbeAuditEngine()
        deployments = [
            {
                "deployment_name": "mis",
                "namespace": "staging",
                "workload_type": "Deployment",
                "has_service": True,
                "is_exposed_externally": False,
                "containers": [
                    {
                        "container_name": "app",
                        "is_init_container": False,
                        "exposed_ports": [8080],
                        "has_liveness_probe": True,
                        "has_readiness_probe": True,
                        "liveness_port": 9090,
                        "readiness_port": 9090,
                    }
                ],
            }
        ]
        result = engine.detect(deployments)
        assert result.total_without_probes == 0
        assert result.critical == 0
        assert len(result.missing_probes) == 0
        assert len(result.misconfigured_probes) == 1
        m = result.misconfigured_probes[0]
        assert m.deployment_name == "mis"
        assert m.namespace == "staging"
        assert m.missing == ["readiness_port_mismatch", "liveness_port_mismatch"]
        assert m.severity == "warning"
        assert m.exposed_port == 8080  # noqa: PLR2004
        assert m.readiness_suggestion == ""
        assert m.liveness_suggestion == ""
        assert m.has_service is True
        assert m.workload_type == "Deployment"
        assert m.is_exposed_externally is False

    def test_dep_without_containers_ignored(self) -> None:
        # deployment sans containers (ou containers non-liste) -> rien
        engine = ProbeAuditEngine()
        result = engine.detect(
            [
                {"deployment_name": "empty", "namespace": "prod", "containers": None},
                {"deployment_name": "bad", "namespace": "prod", "containers": "nope"},
            ]
        )
        assert result.total_without_probes == 0
        assert result.missing_probes == []
        assert result.misconfigured_probes == []


class TestDefaultsAndMultiCount:
    def test_minimal_deployment_uses_defaults(self) -> None:
        # sans deployment_name/namespace/workload_type -> defauts
        engine = ProbeAuditEngine()
        result = engine.detect(
            [
                {
                    "containers": [
                        {
                            "container_name": "m",
                            "is_init_container": False,
                            "exposed_ports": [8080],
                        }
                    ]
                }
            ]
        )
        probe = result.missing_probes[0]
        assert probe.deployment_name == ""
        assert probe.namespace == ""
        assert probe.workload_type == "Deployment"
        assert probe.severity == "informational"

    def test_multiple_informational_counted(self) -> None:
        # 2 jobs sans probes -> informational == 2 (mutant += 1 / = 1 detecte)
        engine = ProbeAuditEngine()
        deployments = [
            {
                "deployment_name": f"j{i}",
                "namespace": "batch",
                "workload_type": "Job",
                "containers": [
                    {"container_name": "m", "is_init_container": False, "exposed_ports": [80]}
                ],
            }
            for i in range(2)
        ]
        result = engine.detect(deployments)
        assert result.informational == 2  # noqa: PLR2004
        assert result.total_without_probes == 2  # noqa: PLR2004


class TestFindMisconfigurationsDirect:
    def test_init_container_then_normal_continue_not_break(self) -> None:
        # init container avec port valide suivi d'un normal avec mismatch :
        # si break apres init, le normal ne serait jamais traite
        containers = [
            {
                "is_init_container": True,
                "exposed_ports": [9999],
                "has_readiness_probe": True,
                "readiness_port": 9999,
            },
            {
                "is_init_container": False,
                "exposed_ports": [8080],
                "has_readiness_probe": True,
                "readiness_port": 9090,
            },
        ]
        assert _find_misconfigurations(containers) == ["readiness_port_mismatch"]

    def test_readiness_port_one_mismatch(self) -> None:
        # rp=1 : > 0 est TRUE -> mismatch (mutant > 1 le laisserait passer)
        containers = [
            {
                "is_init_container": False,
                "exposed_ports": [8080],
                "has_readiness_probe": True,
                "readiness_port": 1,
            }
        ]
        assert _find_misconfigurations(containers) == ["readiness_port_mismatch"]

    def test_zero_readiness_port_no_mismatch(self) -> None:
        # rp=0 : > 0 FALSE -> pas de mismatch (mutant >= 0 le detecterait a tort)
        containers = [
            {
                "is_init_container": False,
                "exposed_ports": [8080],
                "has_readiness_probe": True,
                "readiness_port": 0,
            }
        ]
        assert _find_misconfigurations(containers) == []

    def test_liveness_port_mismatch_only(self) -> None:
        containers = [
            {
                "is_init_container": False,
                "exposed_ports": [8080],
                "has_liveness_probe": True,
                "liveness_port": 9090,
            }
        ]
        assert _find_misconfigurations(containers) == ["liveness_port_mismatch"]


class TestClassifySeverityDirect:
    def test_prod_exposed_critical(self) -> None:
        assert _classify_severity("prod", True, True, "Deployment") == "critical"

    def test_production_exposed_critical(self) -> None:
        assert _classify_severity("production", True, True, "Deployment") == "critical"

    def test_prod_service_warning(self) -> None:
        assert _classify_severity("prod", True, False, "Deployment") == "warning"

    def test_job_informational(self) -> None:
        assert _classify_severity("prod", True, True, "Job") == "informational"

    def test_cronjob_informational(self) -> None:
        assert _classify_severity("prod", True, True, "CronJob") == "informational"

    def test_daemonset_informational(self) -> None:
        assert _classify_severity("prod", True, True, "DaemonSet") == "informational"

    def test_statefulset_service_non_prod_critical(self) -> None:
        assert _classify_severity("staging", True, False, "StatefulSet") == "critical"

    def test_staging_service_warning(self) -> None:
        assert _classify_severity("staging", True, False, "Deployment") == "warning"

    def test_no_service_informational(self) -> None:
        assert _classify_severity("staging", False, False, "Deployment") == "informational"


class TestFirstPortDirect:
    def test_skips_init_container(self) -> None:
        # init container avec port puis normal : si break sur init, on perdrait le normal
        containers = [
            {"is_init_container": True, "exposed_ports": [9999]},
            {"is_init_container": False, "exposed_ports": [8080]},
        ]
        assert _first_port(containers) == 8080  # noqa: PLR2004

    def test_no_container_returns_zero(self) -> None:
        assert _first_port([]) == 0

    def test_port_zero_skipped(self) -> None:
        # port 0 -> pas valide ; port 1 est le premier valide (mutant port > 1 le sauterait)
        containers = [{"is_init_container": False, "exposed_ports": [0, 1]}]
        assert _first_port(containers) == 1  # noqa: PLR2004


class TestFindMissingProbesDirect:
    def test_init_only_no_main_container(self) -> None:
        # que des init containers -> pas de container pertinent -> ([], [])
        containers = [{"is_init_container": True, "exposed_ports": [80]}]
        assert _find_missing_probes(containers) == ([], [])

    def test_missing_liveness_and_readiness(self) -> None:
        containers = [
            {
                "is_init_container": False,
                "exposed_ports": [8080],
                "has_liveness_probe": False,
                "has_readiness_probe": False,
            }
        ]
        missing, ports = _find_missing_probes(containers)
        assert set(missing) == {"livenessProbe", "readinessProbe"}
        assert ports == [8080]  # noqa: PLR2004

    def test_port_one_included(self) -> None:
        # port 1 > 0 -> inclus (mutant port > 1 l'exclurait)
        containers = [
            {
                "is_init_container": False,
                "exposed_ports": [1],
                "has_liveness_probe": False,
                "has_readiness_probe": False,
            }
        ]
        missing, ports = _find_missing_probes(containers)
        assert ports == [1]  # noqa: PLR2004


class TestMisconfigDefaults:
    def test_misconfig_uses_default_fields(self) -> None:
        # deployment misconfigure sans workload_type/namespace/deployment_name/has_service
        # -> defauts (kills get(...,None)/XX dans la branche elif)
        engine = ProbeAuditEngine()
        result = engine.detect(
            [
                {
                    "containers": [
                        {
                            "container_name": "app",
                            "exposed_ports": [8080],
                            "has_liveness_probe": True,
                            "has_readiness_probe": True,
                            "liveness_port": 9090,
                            "readiness_port": 9090,
                        }
                    ]
                }
            ]
        )
        assert len(result.misconfigured_probes) == 1
        m = result.misconfigured_probes[0]
        assert m.deployment_name == ""
        assert m.namespace == ""
        assert m.workload_type == "Deployment"
        assert m.has_service is False
        assert m.is_exposed_externally is False
        assert m.missing == ["readiness_port_mismatch", "liveness_port_mismatch"]


class TestMisconfigBoundaries:
    def test_liveness_port_one_mismatch(self) -> None:
        # lp=1 : > 0 TRUE -> mismatch (mutant > 1 le laisserait passer)
        containers = [
            {
                "is_init_container": False,
                "exposed_ports": [8080],
                "has_liveness_probe": True,
                "liveness_port": 1,
            }
        ]
        assert _find_misconfigurations(containers) == ["liveness_port_mismatch"]

    def test_zero_liveness_port_no_mismatch(self) -> None:
        # lp=0 : > 0 FALSE -> pas de mismatch (mutant >= 0 le detecterait a tort)
        containers = [
            {
                "is_init_container": False,
                "exposed_ports": [8080],
                "has_liveness_probe": True,
                "liveness_port": 0,
            }
        ]
        assert _find_misconfigurations(containers) == []

    def test_exposed_ports_non_list_treated_empty(self) -> None:
        # exposed_ports non-liste -> exposed_ints vide -> lp mismatch detecte
        containers = [
            {
                "is_init_container": False,
                "exposed_ports": "not-a-list",
                "has_liveness_probe": True,
                "liveness_port": 9090,
            }
        ]
        assert _find_misconfigurations(containers) == ["liveness_port_mismatch"]

    def test_readiness_and_liveness_both_mismatched_order(self) -> None:
        containers = [
            {
                "is_init_container": False,
                "exposed_ports": [8080],
                "has_readiness_probe": True,
                "readiness_port": 9090,
                "has_liveness_probe": True,
                "liveness_port": 9091,
            }
        ]
        assert _find_misconfigurations(containers) == [
            "readiness_port_mismatch",
            "liveness_port_mismatch",
        ]


class TestExposedPortInts:
    def test_valid_ports_extracted(self) -> None:
        assert _exposed_port_ints({"exposed_ports": [8080, 9090, 0, -1]}) == [8080, 9090]

    def test_string_ports_parsed(self) -> None:
        assert _exposed_port_ints({"exposed_ports": ["80", "443"]}) == [80, 443]  # noqa: PLR2004

    def test_non_list_returns_empty(self) -> None:
        assert _exposed_port_ints({"exposed_ports": "nope"}) == []

    def test_missing_returns_empty(self) -> None:
        assert _exposed_port_ints({}) == []


class TestHelperKills:
    def test_port_one_extracted(self) -> None:
        # port=1 > 0 : extrait (mutant > 1 l'exclurait)
        assert _exposed_port_ints({"exposed_ports": [1]}) == [1]  # noqa: PLR2004

    def test_init_container_with_mismatch_skipped(self) -> None:
        # container init avec readiness mismatch : normal le saute -> [].
        # mutant qui traiterait l'init detecterait readiness_port_mismatch
        container = {
            "is_init_container": True,
            "exposed_ports": [8080],
            "has_readiness_probe": True,
            "readiness_port": 9090,
        }
        assert _find_misconfigurations([container]) == []

    def test_init_then_normal_missing_probe(self) -> None:
        # init suivi d'un normal sans probes : si break apres init, le normal serait perdu
        init = {"is_init_container": True, "exposed_ports": [8080]}
        normal = {
            "is_init_container": False,
            "exposed_ports": [8080],
            "has_liveness_probe": False,
            "has_readiness_probe": False,
        }
        missing, ports = _find_missing_probes([init, normal])
        assert set(missing) == {"livenessProbe", "readinessProbe"}
        assert ports == [8080]  # noqa: PLR2004
