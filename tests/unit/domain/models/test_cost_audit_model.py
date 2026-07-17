from hexawyn.domain.models.cost_audit import CostAudit


class TestCostAudit:
    def test_minimal_construction(self) -> None:
        entry = CostAudit(namespace="production")
        assert entry.namespace == "production"
        assert entry.pod_count == 0
        assert entry.total_cost == 0.0
        assert entry.total_waste == 0.0
        assert entry.waste_percent == 0.0
        assert entry.savings_total == 0.0
        assert entry.details == {}

    def test_full_construction(self) -> None:
        entry = CostAudit(
            namespace="payments",
            pod_count=12,
            total_cost=342.50,
            total_waste=85.63,
            waste_percent=25.0,
            savings_right_sizing=50.00,
            savings_spot=35.63,
            savings_total=85.63,
            details={"cluster": "prod-eu"},
        )
        assert entry.namespace == "payments"
        assert entry.pod_count == 12
        assert entry.total_cost == 342.50
        assert entry.total_waste == 85.63
        assert entry.waste_percent == 25.0
        assert entry.savings_right_sizing == 50.00
        assert entry.savings_spot == 35.63
        assert entry.savings_total == 85.63
        assert entry.details == {"cluster": "prod-eu"}

    def test_is_dataclass(self) -> None:
        entry = CostAudit(namespace="test")
        assert hasattr(entry, "__dataclass_fields__")

    def test_effective_cost_excludes_waste(self) -> None:
        entry = CostAudit(namespace="web", total_cost=200.0, total_waste=50.0)
        assert entry.effective_cost == 150.0

    def test_savings_percent_returns_ratio(self) -> None:
        entry = CostAudit(namespace="ml", total_cost=500.0, savings_total=75.0)
        assert entry.savings_percent == 15.0

    def test_savings_percent_returns_zero_when_no_cost(self) -> None:
        entry = CostAudit(namespace="empty", total_cost=0.0, savings_total=50.0)
        assert entry.savings_percent == 0.0

    def test_is_waste_high_true_above_20_percent(self) -> None:
        entry = CostAudit(namespace="wasteful", waste_percent=25.0)
        assert entry.is_waste_high is True

    def test_is_waste_high_false_below_20_percent(self) -> None:
        entry = CostAudit(namespace="efficient", waste_percent=10.0)
        assert entry.is_waste_high is False

    def test_is_waste_high_false_at_zero(self) -> None:
        entry = CostAudit(namespace="perfect")
        assert entry.is_waste_high is False

    def test_from_dict_constructs_full_object(self) -> None:
        data: dict[str, object] = {
            "namespace": "infra",
            "pod_count": 5,
            "total_cost": 120.75,
            "total_waste": 30.00,
            "waste_percent": 24.84,
            "savings_right_sizing": 20.00,
            "savings_spot": 10.00,
            "savings_total": 30.00,
            "details": {"region": "eu-west"},
        }
        entry = CostAudit.from_dict(data)
        assert entry.namespace == "infra"
        assert entry.pod_count == 5
        assert entry.total_cost == 120.75
        assert entry.savings_total == 30.00
        assert entry.details == {"region": "eu-west"}
        assert entry.is_waste_high is True

    def test_from_dict_uses_defaults_for_missing_keys(self) -> None:
        entry = CostAudit.from_dict({"namespace": "minimal"})
        assert entry.namespace == "minimal"
        assert entry.pod_count == 0
        assert entry.total_cost == 0.0
        assert entry.waste_percent == 0.0
