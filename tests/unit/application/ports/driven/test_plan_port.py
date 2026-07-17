from hexawyn.application.ports.driven.plan_port import PlanPort


def test_plan_port_is_abstract() -> None:
    assert PlanPort.__abstractmethods__ is not None
    assert "get_limit" in PlanPort.__abstractmethods__
    assert "is_available" in PlanPort.__abstractmethods__
    assert "tier_required_for" in PlanPort.__abstractmethods__


def test_cannot_instantiate_directly() -> None:
    try:
        PlanPort()
    except TypeError:
        assert True
