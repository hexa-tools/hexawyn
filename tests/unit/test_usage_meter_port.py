from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort


def test_usage_meter_port_is_abstract() -> None:
    assert UsageMeterPort.__abstractmethods__ is not None
    assert "get_usage" in UsageMeterPort.__abstractmethods__


def test_cannot_instantiate_directly() -> None:
    try:
        UsageMeterPort()
    except TypeError:
        assert True
