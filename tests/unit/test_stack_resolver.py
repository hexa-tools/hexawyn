from hexawyn.infrastructure.config.stack_resolver import StackDescription, resolve_stack


class TestResolveStack:
    def test_auto_detects_gcp_when_supported(self) -> None:
        result = resolve_stack(override=None, aws_supported=False, gcp_supported=True)

        assert result["provider"] == "gcp-gke"
        assert result["metrics"] == "GCP Managed Prometheus"
        assert result["traces"] == "Google Cloud Trace"
        assert result["logs"] == "Google Cloud Logging"
        assert result["source"] == "auto"

    def test_auto_detects_aws_when_supported(self) -> None:
        result = resolve_stack(override=None, aws_supported=True, gcp_supported=False)

        assert result["provider"] == "aws-eks"
        assert result["source"] == "auto"

    def test_auto_falls_back_to_vanilla(self) -> None:
        result = resolve_stack(override=None, aws_supported=False, gcp_supported=False)

        assert result["provider"] == "vanilla"
        assert result["metrics"] == "Prometheus"
        assert result["source"] == "auto"

    def test_override_aws_wins(self) -> None:
        result = resolve_stack(override="aws", aws_supported=False, gcp_supported=True)

        assert result["provider"] == "aws-eks"
        assert result["source"] == "override"

    def test_override_gcp_wins(self) -> None:
        result = resolve_stack(override="gcp", aws_supported=True, gcp_supported=False)

        assert result["provider"] == "gcp-gke"
        assert result["source"] == "override"

    def test_override_vanilla_wins(self) -> None:
        result = resolve_stack(override="vanilla", aws_supported=True, gcp_supported=True)

        assert result["provider"] == "vanilla"
        assert result["source"] == "override"

    def test_returns_typed_dict_keys(self) -> None:
        result: StackDescription = resolve_stack(
            override=None, aws_supported=True, gcp_supported=False
        )

        assert set(result.keys()) == {"provider", "metrics", "traces", "logs", "source"}
