import pytest
from hexawyn.domain.errors import (
    AdapterTimeoutError,
    AmbiguousResultError,
    CheckerNodeError,
    ClusterOperatorCRDNotFoundError,
    ClusterUnreachableError,
    ComponentNotInstalledError,
    DuckDBUnavailableError,
    EncryptionError,
    HexawynError,
    InsufficientDataError,
    InsufficientPermissionsError,
    InvestigationError,
    LabelSelectorError,
    LogPatternError,
    MachineConfigPoolCRDNotFoundError,
    ManifestRenderError,
    MetricsUnavailableError,
    MutationGuardTriggeredError,
    PipelineNotFoundError,
    PrometheusQueryError,
    ResourceNotFoundError,
    SchemaMigrationError,
    SemanticLayerError,
    ServiceNotFoundError,
    TracesUnavailableError,
)

ALL_EXCEPTIONS = [
    ClusterUnreachableError,
    ResourceNotFoundError,
    InsufficientPermissionsError,
    AdapterTimeoutError,
    MetricsUnavailableError,
    TracesUnavailableError,
    InvestigationError,
    InsufficientDataError,
    AmbiguousResultError,
    CheckerNodeError,
    SemanticLayerError,
    MutationGuardTriggeredError,
    DuckDBUnavailableError,
    SchemaMigrationError,
    EncryptionError,
]


class TestHexawynError:
    def test_base_construction(self):
        err = HexawynError("something broke")
        assert str(err) == "something broke"
        assert err.context == {}

    def test_base_with_context(self):
        err = HexawynError("fail", {"key": "value"})
        assert err.context == {"key": "value"}

    def test_context_defaults_to_empty_dict(self):
        err = HexawynError("msg")
        assert err.context == {}


class TestAllExceptions:
    @pytest.mark.parametrize("exc_cls", ALL_EXCEPTIONS)
    def test_inherits_from_hexawyn_error(self, exc_cls):
        assert issubclass(exc_cls, HexawynError)

    @pytest.mark.parametrize("exc_cls", ALL_EXCEPTIONS)
    def test_can_be_raised_and_caught(self, exc_cls):
        with pytest.raises(exc_cls) as exc_info:
            raise exc_cls("test message")
        assert str(exc_info.value) == "test message"

    @pytest.mark.parametrize("exc_cls", ALL_EXCEPTIONS)
    def test_can_be_caught_as_hexawyn_error(self, exc_cls):
        with pytest.raises(HexawynError):
            raise exc_cls("catch me")


class TestComponentNotInstalledError:
    def test_inherits_from_hexawyn_error(self) -> None:
        assert issubclass(ComponentNotInstalledError, HexawynError)

    def test_message_mentions_component(self) -> None:
        err = ComponentNotInstalledError("Tekton", "https://tekton.dev/docs/installation/")
        assert "Tekton" in str(err)
        assert "not installed" in str(err)

    def test_install_url_in_message(self) -> None:
        err = ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")
        assert "https://keda.sh/docs/deploy/" in str(err)

    def test_stores_component_and_url(self) -> None:
        err = ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")
        assert err.component_name == "KEDA"
        assert err.install_url == "https://keda.sh/docs/deploy/"

    def test_can_be_caught_as_hexawyn_error(self) -> None:
        with pytest.raises(HexawynError):
            raise ComponentNotInstalledError("KEDA", "https://keda.sh/docs/deploy/")


class TestClusterOperatorCRDNotFoundError:
    def test_inherits_from_hexawyn_error(self) -> None:
        assert issubclass(ClusterOperatorCRDNotFoundError, HexawynError)

    def test_message_mentions_openshift_hint(self) -> None:
        err = ClusterOperatorCRDNotFoundError()
        assert "ClusterOperator" in str(err)
        assert "OpenShift" in str(err)

    def test_can_be_caught_as_hexawyn_error(self) -> None:
        with pytest.raises(HexawynError):
            raise ClusterOperatorCRDNotFoundError()


class TestMachineConfigPoolCRDNotFoundError:
    def test_inherits_from_hexawyn_error(self) -> None:
        assert issubclass(MachineConfigPoolCRDNotFoundError, HexawynError)

    def test_message_mentions_openshift_hint(self) -> None:
        err = MachineConfigPoolCRDNotFoundError()
        assert "MachineConfigPool" in str(err)
        assert "OpenShift" in str(err)

    def test_can_be_caught_as_hexawyn_error(self) -> None:
        with pytest.raises(HexawynError):
            raise MachineConfigPoolCRDNotFoundError()


class TestServiceNotFoundError:
    def test_inherits_from_hexawyn_error(self) -> None:
        assert issubclass(ServiceNotFoundError, HexawynError)

    def test_stores_service_name(self) -> None:
        err = ServiceNotFoundError(service_name="payment-service")
        assert err.service_name == "payment-service"

    def test_message_contains_service_name(self) -> None:
        err = ServiceNotFoundError(service_name="payment-service")
        assert "payment-service" in str(err)

    def test_can_be_caught_as_hexawyn_error(self) -> None:
        with pytest.raises(HexawynError):
            raise ServiceNotFoundError(service_name="ghost-svc")


class TestPipelineNotFoundError:
    def test_inherits_from_hexawyn_error(self) -> None:
        assert issubclass(PipelineNotFoundError, HexawynError)

    def test_stores_pipeline_name(self) -> None:
        err = PipelineNotFoundError(pipeline_name="build-deploy")
        assert err.pipeline_name == "build-deploy"

    def test_message_contains_pipeline_name(self) -> None:
        err = PipelineNotFoundError(pipeline_name="build-deploy")
        assert "build-deploy" in str(err)

    def test_can_be_caught_as_hexawyn_error(self) -> None:
        with pytest.raises(HexawynError):
            raise PipelineNotFoundError(pipeline_name="ghost")


class TestPrometheusQueryError:
    def test_inherits_from_hexawyn_error(self) -> None:
        assert issubclass(PrometheusQueryError, HexawynError)

    def test_stores_promql_and_detail(self) -> None:
        err = PrometheusQueryError(promql="rate(foo[5m]", detail="unexpected end of input")
        assert err.promql == "rate(foo[5m]"
        assert err.detail == "unexpected end of input"

    def test_message_contains_promql_and_detail(self) -> None:
        err = PrometheusQueryError(promql="rate(foo[5m]", detail="unexpected end of input")
        assert "rate(foo[5m]" in str(err)
        assert "unexpected end of input" in str(err)

    def test_can_be_caught_as_hexawyn_error(self) -> None:
        with pytest.raises(HexawynError):
            raise PrometheusQueryError(promql="bad{", detail="parse error")


class TestManifestRenderError:
    def test_inherits_from_hexawyn_error(self) -> None:
        assert issubclass(ManifestRenderError, HexawynError)

    def test_stores_source_and_detail(self) -> None:
        err = ManifestRenderError(source="payment-chart", detail="chart not found")
        assert err.source == "payment-chart"
        assert err.detail == "chart not found"

    def test_message_contains_source_and_detail(self) -> None:
        err = ManifestRenderError(source="payment-chart", detail="chart not found")
        assert "payment-chart" in str(err)
        assert "chart not found" in str(err)

    def test_can_be_caught_as_hexawyn_error(self) -> None:
        with pytest.raises(HexawynError):
            raise ManifestRenderError(source="payment-chart", detail="chart not found")


class TestLabelSelectorError:
    def test_inherits_from_hexawyn_error(self) -> None:
        assert issubclass(LabelSelectorError, HexawynError)

    def test_stores_selector_and_detail(self) -> None:
        err = LabelSelectorError(selector="app=", detail="empty value")
        assert err.selector == "app="
        assert err.detail == "empty value"

    def test_message_contains_selector_and_detail(self) -> None:
        err = LabelSelectorError(selector="app=", detail="empty value")
        assert "app=" in str(err)
        assert "empty value" in str(err)

    def test_can_be_caught_as_hexawyn_error(self) -> None:
        with pytest.raises(HexawynError):
            raise LabelSelectorError(selector="bad", detail="missing '='")


class TestLogPatternError:
    def test_inherits_from_hexawyn_error(self) -> None:
        assert issubclass(LogPatternError, HexawynError)

    def test_stores_pattern_and_detail(self) -> None:
        err = LogPatternError(pattern="foo(", detail="unbalanced parenthesis")
        assert err.pattern == "foo("
        assert err.detail == "unbalanced parenthesis"

    def test_message_contains_pattern_and_detail(self) -> None:
        err = LogPatternError(pattern="foo(", detail="unbalanced parenthesis")
        assert "foo(" in str(err)
        assert "unbalanced parenthesis" in str(err)

    def test_can_be_caught_as_hexawyn_error(self) -> None:
        with pytest.raises(HexawynError):
            raise LogPatternError(pattern="bad(", detail="invalid regex")


class TestContextPropagation:
    def test_duckdb_unavailable_context(self):
        err = DuckDBUnavailableError(
            "DB down", context={"path": "/tmp/test.db", "error": "corrupt"}
        )
        assert err.context["path"] == "/tmp/test.db"

    def test_service_error_never_catches(self):
        # R6: services never catch, they let HexawynError propagate
        err = InvestigationError("pipeline failed")
        assert isinstance(err, HexawynError)
        # Just verifying the exception can be instantiated and is correct type
