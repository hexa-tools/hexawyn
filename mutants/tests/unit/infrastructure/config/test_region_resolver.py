from hexawyn.infrastructure.config.region_resolver import resolve_region


class TestResolveRegion:
    def test_aws_region_env_wins(self) -> None:
        region = resolve_region(
            "arn:aws:eks:eu-west-1:123456789012:cluster/prod",
            {"AWS_REGION": "ap-south-1"},
        )

        assert region == "ap-south-1"

    def test_aws_default_region_used_when_aws_region_absent(self) -> None:
        region = resolve_region("eks-prod", {"AWS_DEFAULT_REGION": "us-west-2"})

        assert region == "us-west-2"

    def test_aws_region_takes_priority_over_default(self) -> None:
        region = resolve_region(
            "eks-prod", {"AWS_REGION": "eu-central-1", "AWS_DEFAULT_REGION": "us-west-2"}
        )

        assert region == "eu-central-1"

    def test_empty_env_value_is_ignored(self) -> None:
        region = resolve_region(
            "arn:aws:eks:eu-west-1:123456789012:cluster/prod", {"AWS_REGION": ""}
        )

        assert region == "eu-west-1"

    def test_detected_from_arn_when_no_env(self) -> None:
        region = resolve_region("arn:aws:eks:eu-west-1:123456789012:cluster/prod", {})

        assert region == "eu-west-1"

    def test_detected_from_name_pattern(self) -> None:
        region = resolve_region("prod.us-east-2.eksctl.io", {})

        assert region == "us-east-2"

    def test_returns_none_when_undetectable(self) -> None:
        region = resolve_region("eks-prod", {})

        assert region is None
