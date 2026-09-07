from hexawyn.infrastructure.config.stack_resolver import StackDescription, resolve_stack


def _resolve(
    override: str | None = None,
    aws: bool = False,
    gcp: bool = False,
    azure: bool = False,
    dd: bool = False,
) -> StackDescription:
    return resolve_stack(
        override=override,
        aws_supported=aws,
        gcp_supported=gcp,
        azure_supported=azure,
        datadog_supported=dd,
    )


class TestResolveStack:
    def test_override_datadog_wins(self) -> None:
        result = _resolve(override="datadog", aws=True, gcp=True)

        assert result["provider"] == "datadog"
        assert result["metrics"] == "Datadog Metrics"
        assert result["traces"] == "Datadog APM"
        assert result["logs"] == "Datadog Logs"
        assert result["source"] == "override"

    def test_auto_detects_datadog_priority_over_others(self) -> None:
        result = _resolve(dd=True, aws=True, gcp=True, azure=True)

        assert result["provider"] == "datadog"
        assert result["source"] == "auto"

    def test_auto_detects_azure_when_supported(self) -> None:
        result = _resolve(azure=True)

        assert result["provider"] == "azure-aks"

    def test_auto_detects_gcp_when_supported(self) -> None:
        result = _resolve(gcp=True)

        assert result["provider"] == "gcp-gke"

    def test_auto_detects_aws_when_supported(self) -> None:
        result = _resolve(aws=True)

        assert result["provider"] == "aws-eks"

    def test_auto_falls_back_to_vanilla(self) -> None:
        result = _resolve()

        assert result["provider"] == "vanilla"

    def test_override_aws_wins(self) -> None:
        result = _resolve(override="aws", gcp=True, azure=True)

        assert result["provider"] == "aws-eks"
        assert result["source"] == "override"

    def test_override_gcp_wins(self) -> None:
        result = _resolve(override="gcp", aws=True, azure=True)

        assert result["provider"] == "gcp-gke"

    def test_override_azure_wins(self) -> None:
        result = _resolve(override="azure", aws=True, gcp=True)

        assert result["provider"] == "azure-aks"

    def test_override_vanilla_wins(self) -> None:
        result = _resolve(override="vanilla", aws=True, gcp=True, azure=True, dd=True)

        assert result["provider"] == "vanilla"

    def test_returns_typed_dict_keys(self) -> None:
        result: StackDescription = _resolve(aws=True)

        assert set(result.keys()) == {"provider", "metrics", "traces", "logs", "source"}
