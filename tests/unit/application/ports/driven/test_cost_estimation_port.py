from abc import ABC


class TestCostEstimationPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.cost_estimation_port import (
            CostEstimationPort,
        )

        assert issubclass(CostEstimationPort, ABC)

    def test_declares_estimate_cluster_cost(self) -> None:
        from hexawyn.application.ports.driven.cost_estimation_port import (
            CostEstimationPort,
        )

        assert "estimate_cluster_cost" in CostEstimationPort.__abstractmethods__


class TestCostReportRaw:
    def test_shape(self) -> None:
        from hexawyn.application.ports.driven.cost_estimation_port import CostReportRaw

        report: CostReportRaw = {
            "cluster_name": "eks-prod",
            "namespace_costs": [{"namespace": "payments", "monthly_cost_usd": 1450.0}],
            "total_monthly_cost_usd": 1450.0,
            "data_source": "aws",
            "currency": "USD",
        }

        assert report["data_source"] == "aws"
        assert report["namespace_costs"][0]["monthly_cost_usd"] == 1450.0
