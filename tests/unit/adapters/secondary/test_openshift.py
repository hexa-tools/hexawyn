from hexawyn.adapters.secondary.mock.scenarios.openshift import OPENSHIFT_SCENARIO

REQUIRED_KEYS = {"context", "health", "pods", "metrics", "findings", "chips", "slack_message"}


class TestOpenShift:
    def test_has_required_keys(self):
        for key in REQUIRED_KEYS:
            assert key in OPENSHIFT_SCENARIO

    def test_health_score(self):
        assert OPENSHIFT_SCENARIO["health"]["score"] == 71

    def test_has_projects(self):
        assert "projects" in OPENSHIFT_SCENARIO
        assert len(OPENSHIFT_SCENARIO["projects"]) == 3
