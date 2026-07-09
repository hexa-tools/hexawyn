from unittest.mock import MagicMock, patch

from hexawyn.cli.presentation import stack_view


def _texts(lines: list[tuple[str, str]]) -> str:
    return "\n".join(text for text, _ in lines)


class TestViewStack:
    def test_shows_active_stack_and_installed_providers(self) -> None:
        with (
            patch.object(stack_view, "get_stack_override", return_value=None),
            patch.object(stack_view, "_aws_supported", return_value=True),
            patch.object(stack_view, "_installed_provider_names", return_value=["AWS EKS"]),
        ):
            lines = stack_view.run_stack_command("/stack", "prod-eks")

        body = _texts(lines)
        assert "prod-eks" in body
        assert "CloudWatch Container Insights" in body
        assert "AWS X-Ray" in body
        assert "AWS EKS" in body
        assert "auto" in body

    def test_shows_override_source_when_forced(self) -> None:
        with (
            patch.object(stack_view, "get_stack_override", return_value="vanilla"),
            patch.object(stack_view, "_aws_supported", return_value=True),
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
            patch.object(stack_view, "_aws_installed", return_value=True),
        ):
            lines = stack_view.run_stack_command("/stack aws", "prod-eks")

        set_override.assert_called_once_with("prod-eks", "aws")
        assert "aws" in _texts(lines).lower()

    def test_force_aws_warns_when_boto3_missing(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override"),
            patch.object(stack_view, "_aws_installed", return_value=False),
        ):
            lines = stack_view.run_stack_command("/stack aws", "prod-eks")

        assert "hexawyn[aws]" in _texts(lines)

    def test_force_vanilla_persists_override(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override") as set_override,
            patch.object(stack_view, "_aws_installed", return_value=True),
        ):
            stack_view.run_stack_command("/stack vanilla", "prod-eks")

        set_override.assert_called_once_with("prod-eks", "vanilla")

    def test_auto_clears_override(self) -> None:
        with patch.object(stack_view, "clear_stack_override") as clear_override:
            lines = stack_view.run_stack_command("/stack auto", "prod-eks")

        clear_override.assert_called_once_with("prod-eks")
        assert "auto" in _texts(lines).lower()

    def test_unknown_argument_returns_usage(self) -> None:
        lines = stack_view.run_stack_command("/stack gcp", "prod-eks")

        body = _texts(lines)
        assert "gcp" in body.lower()
        assert "/stack" in body

    def test_argument_is_case_insensitive(self) -> None:
        with (
            patch.object(stack_view, "set_stack_override") as set_override,
            patch.object(stack_view, "_aws_installed", return_value=True),
        ):
            stack_view.run_stack_command("/stack AWS", "prod-eks")

        set_override.assert_called_once_with("prod-eks", "aws")


class TestHelpers:
    def test_aws_supported_delegates_to_provider(self) -> None:
        with patch.object(stack_view.AWSEKSProvider, "supports", return_value=True) as supports:
            assert stack_view._aws_supported("prod-eks") is True

        context = supports.call_args.args[0]
        assert context["name"] == "prod-eks"

    def test_aws_installed_reads_detector(self) -> None:
        with patch.object(stack_view, "detect_installed_providers", return_value={"aws": True}):
            assert stack_view._aws_installed() is True

    def test_installed_provider_names_maps_provider_name(self) -> None:
        provider = MagicMock()
        provider.provider_name.return_value = "AWS EKS"
        with patch.object(stack_view, "list_installed_providers", return_value=[provider]):
            assert stack_view._installed_provider_names() == ["AWS EKS"]
