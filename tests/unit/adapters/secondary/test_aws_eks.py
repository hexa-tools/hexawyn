from hexawyn.adapters.secondary.mock.scenarios.aws_eks import AWS_EKS_SCENARIO

REQUIRED_KEYS = {"context", "health", "pods", "metrics", "findings", "chips", "slack_message"}


class TestAWSEKS:
    def test_has_required_keys(self):
        for key in REQUIRED_KEYS:
            assert key in AWS_EKS_SCENARIO

    def test_health_score(self):
        assert AWS_EKS_SCENARIO["health"]["score"] == 76  # noqa: PLR2004

    def test_has_crashloop_pod(self):
        crashloop = [p for p in AWS_EKS_SCENARIO["pods"] if p["status"] == "CrashLoop"]
        assert len(crashloop) == 1
        assert crashloop[0]["name"] == "payments-api-7d9f8b-m3ql"
