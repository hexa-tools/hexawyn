from unittest.mock import MagicMock, patch

from hexawyn.cli.presentation import stack_view


def _texts(lines: list[tuple[str, str]]) -> str:
    return "\n".join(text for text, _ in lines)


class TestViewStack:
    def test_shows_active_stack_and_installed_providers(self) -> None:
        with (
            patch.object(stack_view, "get_stack_override", return_value=None),
            patch.object(stack_view, "_aws_supported", return_value=True),
            patch.object(stack_view, "_gcp_supported", return_value=False),
            patch.object(stack_view, "_azure_supported", return_value=False),
            patch.object(stack_view, "_datadog_supported", return_value=False),
            patch.object(stack_view, "_installed_provider_names", return_value=["AWS EKS"]),
        ):
            lines = stack_view.run_stack_command("/stack", "prod-eks")

        body = _texts(lines)
        assert "prod-eks" in body
        assert "CloudWatch Container Insights" in body
        assert "AWS EKS" in body
        assert "auto" in body

    def test_shows_gcp_stack_when_gke(self) -> None:
        with (
            patch.object(stack_view, "get_stack_override", return_value=None),
            patch.object(stack_view, "_aws_supported", return_value=False),
            patch.object(stack_view, "_gcp_supported", return_value=True),
            patch.object(stack_view, "_azure_supported", return_value=False),
            patch.object(stack_view, "_installed_provider_names", return_value=["GCP GKE"]),
        ):
            lines = stack_view.run_stack_command("/stack", "gke_p_r_c")

        body = _texts(lines)
        assert "GCP Managed Prometheus" in body
        assert "Google Cloud Trace" in body

    def test_shows_azure_stack_when_aks(self) -> None:
        with (
            patch.object(stack_view, "get_stack_override", return_value=None),
            patch.object(stack_view, "_aws_supported", return_value=False),
            patch.object(stack_view, "_gcp_supported", return_value=False),
            patch.object(stack_view, "_azure_supported", return_value=True),
            patch.object(stack_view, "_datadog_supported", return_value=False),
            patch.object(stack_view, "_installed_provider_names", return_value=["Azure AKS"]),
        ):
            lines = stack_view.run_stack_command("/stack", "aks-prod")

        body = _texts(lines)
        assert "Azure Monitor Prometheus" in body
        assert "Azure Log Analytics" in body

    def test_shows_datadog_stack_when_configured(self) -> None:
        with (
            patch.object(stack_view, "get_stack_override", return_value=None),
            patch.object(stack_view, "_aws_supported", return_value=False),
            patch.object(stack_view, "_gcp_supported", return_value=False),
            patch.object(stack_view, "_azure_supported", return_value=False),
            patch.object(stack_view, "_datadog_supported", return_value=True),
            patch.object(stack_view, "_installed_provider_names", return_value=[]),
        ):
            lines = stack_view.run_stack_command("/stack", "any-cluster")

        body = _texts(lines)
        assert "Datadog Metrics" in body
        assert "Datadog APM" in body
        assert "Datadog Logs" in body

    def test_shows_override_source_when_forced(self) -> None:
        with (
            patch.object(stack_view, "get_stack_override", return_value="vanilla"),
            patch.object(stack_view, "_aws_supported", return_value=True),
            patch.object(stack_view, "_gcp_supported", return_value=True),
            patch.object(stack_view, "_azure_supported", return_value=True),
            patch.object(stack_view, "_datadog_supported", return_value=True),
            patch.object(stack_view, "_installed_provider_names", return_value=[]),
        ):
            lines = stack_view.run_stack_command("/stack", "prod-eks")

        body = _texts(lines)
        assert "Prometheus" in body
        assert "override" in body


class TestOverrideCommands:
    def test_force_aws_persists_override(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override") as set_override,
            patch.object(stack_view, "_provider_installed", return_value=True),
        ):
            lines = stack_view.run_stack_command("/stack aws", "prod-eks")

        set_override.assert_called_once_with("prod-eks", "aws")
        assert "aws" in _texts(lines).lower()

    def test_force_gcp_persists_override(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override") as set_override,
            patch.object(stack_view, "_provider_installed", return_value=True),
        ):
            stack_view.run_stack_command("/stack gcp", "gke_p_r_c")

        set_override.assert_called_once_with("gke_p_r_c", "gcp")

    def test_force_azure_persists_override(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override") as set_override,
            patch.object(stack_view, "_provider_installed", return_value=True),
        ):
            stack_view.run_stack_command("/stack azure", "aks-prod")

        set_override.assert_called_once_with("aks-prod", "azure")

    def test_force_azure_warns_when_libs_missing(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override"),
            patch.object(stack_view, "_provider_installed", return_value=False),
        ):
            lines = stack_view.run_stack_command("/stack azure", "aks-prod")

        assert "hexawyn[azure]" in _texts(lines)

    def test_force_datadog_persists_override(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override") as set_override,
            patch.object(stack_view, "_provider_installed", return_value=True),
        ):
            stack_view.run_stack_command("/stack datadog", "any-cluster")

        set_override.assert_called_once_with("any-cluster", "datadog")

    def test_force_datadog_warns_when_libs_missing(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override"),
            patch.object(stack_view, "_provider_installed", return_value=False),
        ):
            lines = stack_view.run_stack_command("/stack datadog", "any-cluster")

        assert "hexawyn[datadog]" in _texts(lines)

    def test_force_gcp_warns_when_libs_missing(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override"),
            patch.object(stack_view, "_provider_installed", return_value=False),
        ):
            lines = stack_view.run_stack_command("/stack gcp", "gke_p_r_c")

        assert "hexawyn[gcp]" in _texts(lines)

    def test_force_aws_warns_when_boto3_missing(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override"),
            patch.object(stack_view, "_provider_installed", return_value=False),
        ):
            lines = stack_view.run_stack_command("/stack aws", "prod-eks")

        assert "hexawyn[aws]" in _texts(lines)

    def test_force_vanilla_persists_override(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override") as set_override,
            patch.object(stack_view, "_provider_installed", return_value=True),
        ):
            stack_view.run_stack_command("/stack vanilla", "prod-eks")

        set_override.assert_called_once_with("prod-eks", "vanilla")

    def test_auto_clears_override(self) -> None:
        with patch.object(stack_view, "clear_stack_override") as clear_override:
            lines = stack_view.run_stack_command("/stack auto", "prod-eks")

        clear_override.assert_called_once_with("prod-eks")
        assert "auto" in _texts(lines).lower()

    def test_unknown_argument_returns_usage(self) -> None:
        lines = stack_view.run_stack_command("/stack oracle", "prod-eks")

        body = _texts(lines)
        assert "oracle" in body.lower()
        assert "/stack" in body

    def test_argument_is_case_insensitive(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override") as set_override,
            patch.object(stack_view, "_provider_installed", return_value=True),
        ):
            stack_view.run_stack_command("/stack GCP", "gke_p_r_c")

        set_override.assert_called_once_with("gke_p_r_c", "gcp")


class TestHelpers:
    def test_aws_supported_delegates_to_provider(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.aws.aws_eks_provider.AWSEKSProvider.supports",
            return_value=True,
        ) as supports:
            assert stack_view._aws_supported("prod-eks") is True
        assert supports.call_args.args[0]["name"] == "prod-eks"

    def test_gcp_supported_delegates_to_provider(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.gcp.gcp_gke_provider.GCPGKEProvider.supports",
            return_value=True,
        ) as supports:
            assert stack_view._gcp_supported("gke_p_r_c") is True
        assert supports.call_args.args[0]["name"] == "gke_p_r_c"

    def test_azure_supported_delegates_to_provider(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.azure.azure_aks_provider.AzureAKSProvider.supports",
            return_value=True,
        ) as supports:
            assert stack_view._azure_supported("aks-prod") is True
        assert supports.call_args.args[0]["name"] == "aks-prod"

    def test_datadog_supported_reads_config(self) -> None:
        with patch.object(stack_view, "is_datadog_configured", return_value=True):
            assert stack_view._datadog_supported() is True

    def test_provider_installed_vanilla_always_true(self) -> None:
        assert stack_view._provider_installed("vanilla") is True

    def test_provider_installed_reads_detector(self) -> None:
        with patch.object(stack_view, "detect_installed_providers", return_value={"gcp": True}):
            assert stack_view._provider_installed("gcp") is True

    def test_installed_provider_names_maps_provider_name(self) -> None:
        provider = MagicMock()
        provider.provider_name.return_value = "GCP GKE"
        with patch.object(stack_view, "list_installed_providers", return_value=[provider]):
            assert stack_view._installed_provider_names() == ["GCP GKE"]
