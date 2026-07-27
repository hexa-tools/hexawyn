from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.security_posture.security_posture_adapter import (
    SecurityPostureAdapter,
)


class TestSecurityPostureAdapter:
    def test_list_workload_compliance(self) -> None:
        p1 = Mock()
        p1.fetch.return_value = [
            {
                "workload": "a",
                "namespace": "ns",
                "category": "tls",
                "compliant": True,
                "exempt": False,
                "detail": "",
            }
        ]
        p1.category.return_value = "tls"

        adapter = SecurityPostureAdapter(providers=[p1])
        records = adapter.list_workload_compliance()
        assert len(records) == 1
        assert records[0]["workload"] == "a"

    def test_defined_categories(self) -> None:
        p1 = Mock()
        p1.fetch.return_value = []
        p1.category.return_value = "rbac"

        adapter = SecurityPostureAdapter(providers=[p1])
        adapter.list_workload_compliance()
        assert adapter.get_defined_categories() == ["rbac"]

    def test_is_partial_when_provider_fails(self) -> None:
        p1 = Mock()
        p1.fetch.side_effect = Exception("timeout")
        p1.category.return_value = "tls"

        p2 = Mock()
        p2.fetch.return_value = []
        p2.category.return_value = "rbac"

        adapter = SecurityPostureAdapter(providers=[p1, p2])
        adapter.list_workload_compliance()
        assert adapter.is_partial() is True
        assert adapter.get_defined_categories() == ["rbac"]

    def test_not_partial_when_all_succeed(self) -> None:
        p = Mock()
        p.fetch.return_value = []
        p.category.return_value = "tls"

        adapter = SecurityPostureAdapter(providers=[p])
        adapter.list_workload_compliance()
        assert adapter.is_partial() is False

    def test_empty_providers(self) -> None:
        adapter = SecurityPostureAdapter(providers=[])
        records = adapter.list_workload_compliance()
        assert records == []
        assert adapter.get_defined_categories() == []
        assert adapter.is_partial() is False
