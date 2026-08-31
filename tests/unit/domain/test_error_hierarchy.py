from __future__ import annotations

from hexawyn.domain.errors import (
    AdapterTimeoutError,
    CheckerNodeError,
    ClusterOperatorCRDNotFoundError,
    ClusterUnreachableError,
    ComponentNotInstalledError,
    DuckDBUnavailableError,
    EncryptionError,
    GitOpsEngineNotFoundError,
    HexawynError,
    HistoricalDataWindowExpiredError,
    InsufficientPermissionsError,
    InvestigationError,
    LabelSelectorError,
    LogPatternError,
    MachineConfigPoolCRDNotFoundError,
    ManifestRenderError,
    MetricsUnavailableError,
    MutationGuardTriggeredError,
    PipelineNotFoundError,
    PolicyEngineNotFoundError,
    PrometheusQueryError,
    PrometheusUnavailableError,
    QuotaExceededError,
    ResourceNotFoundError,
    SchemaMigrationError,
    SemanticLayerError,
    ServiceNotFoundError,
    SlackQuotaExceededError,
    TracesUnavailableError,
)


class TestErrorHierarchy:
    def test_base_error_defaults(self) -> None:
        err = HexawynError("test message")
        assert str(err) == "test message"
        assert err.context == {}

    def test_base_error_with_context(self) -> None:
        err = HexawynError("msg", {"key": "val"})
        assert err.context == {"key": "val"}

    def test_cluster_unreachable(self) -> None:
        err = ClusterUnreachableError("no cluster")
        assert isinstance(err, HexawynError)

    def test_resource_not_found(self) -> None:
        err = ResourceNotFoundError("pod not found")
        assert isinstance(err, HexawynError)

    def test_insufficient_permissions(self) -> None:
        err = InsufficientPermissionsError("RBAC denied", {"user": "admin"})
        assert isinstance(err, HexawynError)
        assert err.context["user"] == "admin"

    def test_adapter_timeout(self) -> None:
        err = AdapterTimeoutError("timeout")
        assert isinstance(err, HexawynError)

    def test_metrics_unavailable(self) -> None:
        err = MetricsUnavailableError("prometheus down")
        assert isinstance(err, HexawynError)

    def test_traces_unavailable(self) -> None:
        err = TracesUnavailableError("jaeger down")
        assert isinstance(err, HexawynError)

    def test_investigation_error(self) -> None:
        err = InvestigationError("pipeline failed")
        assert isinstance(err, HexawynError)

    def test_checker_node_error(self) -> None:
        err = CheckerNodeError("check failed")
        assert isinstance(err, HexawynError)

    def test_semantic_layer_error(self) -> None:
        err = SemanticLayerError("vss search failed")
        assert isinstance(err, HexawynError)

    def test_mutation_guard_triggered(self) -> None:
        err = MutationGuardTriggeredError("delete blocked")
        assert isinstance(err, HexawynError)

    def test_duckdb_unavailable(self) -> None:
        err = DuckDBUnavailableError("duckdb down")
        assert isinstance(err, HexawynError)

    def test_schema_migration_error(self) -> None:
        err = SchemaMigrationError("migration failed")
        assert isinstance(err, HexawynError)

    def test_encryption_error(self) -> None:
        err = EncryptionError("key invalid")
        assert isinstance(err, HexawynError)

    def test_quota_exceeded(self) -> None:
        err = QuotaExceededError(used=50, limit=50)
        assert isinstance(err, HexawynError)
        assert err.used == 50  # noqa: PLR2004
        assert err.limit == 50  # noqa: PLR2004

    def test_slack_quota_exceeded(self) -> None:
        err = SlackQuotaExceededError(used=5, limit=5)
        assert isinstance(err, HexawynError)
        assert err.used == 5  # noqa: PLR2004

    def test_pipeline_not_found(self) -> None:
        err = PipelineNotFoundError("build-pipeline")
        assert isinstance(err, HexawynError)
        assert err.pipeline_name == "build-pipeline"

    def test_svc_not_found(self) -> None:  # noqa: ANN201
        err = ServiceNotFoundError("my-service")
        assert isinstance(err, HexawynError)
        assert err.service_name == "my-service"

    def test_prometheus_unavailable(self) -> None:
        err = PrometheusUnavailableError("http://localhost:9090")
        assert isinstance(err, HexawynError)
        assert err.url == "http://localhost:9090"

    def test_prometheus_query_error(self) -> None:
        err = PrometheusQueryError("up", "syntax error")
        assert isinstance(err, HexawynError)
        assert err.promql == "up"

    def test_label_selector_error(self) -> None:
        err = LabelSelectorError("app", "missing =")
        assert isinstance(err, HexawynError)

    def test_log_pattern_error(self) -> None:
        err = LogPatternError("[invalid", "bad regex")
        assert isinstance(err, HexawynError)

    def test_component_not_installed(self) -> None:
        err = ComponentNotInstalledError("Tekton", "https://tekton.dev/docs/installation/")
        assert isinstance(err, HexawynError)
        assert err.component_name == "Tekton"
        assert err.install_url == "https://tekton.dev/docs/installation/"

    def test_component_not_installed_with_context(self) -> None:
        err = ComponentNotInstalledError(
            "KubeArchive", "https://kubearchive.org/docs/installation", context={"endpoint": "x"}
        )
        assert isinstance(err, HexawynError)
        assert err.context == {"endpoint": "x"}

    def test_historical_window_expired(self) -> None:
        err = HistoricalDataWindowExpiredError("2020-01-01", "90d")
        assert isinstance(err, HexawynError)
        assert err.queried_timestamp == "2020-01-01"
        assert err.retention_window == "90d"

    def test_gitops_engine_not_found(self) -> None:
        err = GitOpsEngineNotFoundError()
        assert isinstance(err, HexawynError)

    def test_policy_engine_not_found(self) -> None:
        err = PolicyEngineNotFoundError()
        assert isinstance(err, HexawynError)

    def test_manifest_render_error(self) -> None:
        err = ManifestRenderError("my-chart", "YAML parse error")
        assert isinstance(err, HexawynError)
        assert err.source == "my-chart"

    def test_cluster_operator_crd_not_found(self) -> None:
        err = ClusterOperatorCRDNotFoundError()
        assert isinstance(err, HexawynError)

    def test_machine_config_pool_crd_not_found(self) -> None:
        err = MachineConfigPoolCRDNotFoundError()
        assert isinstance(err, HexawynError)
