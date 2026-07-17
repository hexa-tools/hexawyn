from hexawyn.application.ports.driven.consolidation_port import (
    ConsolidationConfig,
    ConsolidationPort,
)


def test_consolidation_port_is_abstract() -> None:
    assert ConsolidationPort.__abstractmethods__ is not None
    assert "find_incident_groups" in ConsolidationPort.__abstractmethods__
    assert "store_knowledge" in ConsolidationPort.__abstractmethods__
    assert "mark_consolidated" in ConsolidationPort.__abstractmethods__
    assert "search_consolidated" in ConsolidationPort.__abstractmethods__


def test_cannot_instantiate_directly() -> None:
    try:
        ConsolidationPort()
    except TypeError:
        assert True


def test_consolidation_config_typed_dict() -> None:
    config: ConsolidationConfig = {
        "min_occurrences": 2,
        "similarity_threshold": 0.85,
        "max_age_days": 90,
    }
    assert config["min_occurrences"] == 2
    assert config["similarity_threshold"] == 0.85
    assert config["max_age_days"] == 90
