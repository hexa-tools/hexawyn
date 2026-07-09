from hexawyn.infrastructure.config.stack_resolver import StackDescription, resolve_stack


class TestResolveStack:
    def test_auto_detects_aws_when_supported(self) -> None:
        result = resolve_stack(override=None, aws_supported=True)

        assert result["provider"] == "aws-eks"
        assert result["metrics"] == "CloudWatch Container Insights"
        assert result["traces"] == "AWS X-Ray"
        assert result["logs"] == "CloudWatch Logs"
        assert result["source"] == "auto"

    def test_auto_falls_back_to_vanilla(self) -> None:
        result = resolve_stack(override=None, aws_supported=False)

        assert result["provider"] == "vanilla"
        assert result["metrics"] == "Prometheus"
        assert result["traces"] == "OpenTelemetry"
        assert result["logs"] == "Kubernetes"
        assert result["source"] == "auto"

    def test_override_aws_wins_even_if_not_supported(self) -> None:
        result = resolve_stack(override="aws", aws_supported=False)

        assert result["provider"] == "aws-eks"
        assert result["source"] == "override"

    def test_override_vanilla_wins_even_if_aws_supported(self) -> None:
        result = resolve_stack(override="vanilla", aws_supported=True)

        assert result["provider"] == "vanilla"
        assert result["source"] == "override"

    def test_returns_typed_dict_keys(self) -> None:
        result: StackDescription = resolve_stack(override=None, aws_supported=True)

        assert set(result.keys()) == {"provider", "metrics", "traces", "logs", "source"}
