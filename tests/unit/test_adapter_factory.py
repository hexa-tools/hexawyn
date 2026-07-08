import os
from unittest.mock import patch


class TestAdapterFactory:
    def test_demo_mode_returns_demo_adapter(self):
        with patch.dict(
            os.environ,
            {
                "HEXAWYN_DEMO_MODE": "true",
                "HEXAWYN_DEMO_SCENARIO": "aws_eks",
            },
        ):
            from hexawyn.adapters.secondary.adapter_factory import build_adapters
            from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

            adapter = build_adapters("any-cluster")
            assert isinstance(adapter, DemoAdapter)
            assert adapter.scenario == "aws_eks"

    def test_demo_mode_false_does_not_return_demo_adapter(self):
        with patch.dict(os.environ, {"HEXAWYN_DEMO_MODE": "false"}):
            from hexawyn.adapters.secondary.adapter_factory import build_adapters
            from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

            adapter = build_adapters("any-cluster")
            assert not isinstance(adapter, DemoAdapter)

    def test_demo_scenario_openshift(self):
        with patch.dict(
            os.environ,
            {
                "HEXAWYN_DEMO_MODE": "true",
                "HEXAWYN_DEMO_SCENARIO": "openshift",
            },
        ):
            from hexawyn.adapters.secondary.adapter_factory import build_adapters
            from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

            adapter = build_adapters("ocp-prod")
            assert isinstance(adapter, DemoAdapter)
            assert adapter.scenario == "openshift"

    def test_unknown_demo_scenario_falls_back_to_aws_eks(self):
        with patch.dict(
            os.environ,
            {
                "HEXAWYN_DEMO_MODE": "true",
                "HEXAWYN_DEMO_SCENARIO": "unknown",
            },
        ):
            from hexawyn.adapters.secondary.adapter_factory import build_adapters
            from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

            adapter = build_adapters("any-cluster")
            assert isinstance(adapter, DemoAdapter)
            assert adapter.scenario == "aws_eks"
