from hexawyn.application.ports.driven.cost_estimation_port import CostEstimationPort


class TestPortImplementation:
    def test_is_cost_estimation_port(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_cost_adapter import VanillaCostAdapter

        assert isinstance(VanillaCostAdapter(), CostEstimationPort)

    def test_returns_zero_cost(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_cost_adapter import VanillaCostAdapter

        report = VanillaCostAdapter().estimate_cluster_cost("minikube")

        assert report["total_monthly_cost_usd"] == 0.0
        assert report["data_source"] == "vanilla"
