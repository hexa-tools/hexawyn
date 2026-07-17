from __future__ import annotations

from hexawyn.application.ports.driven.security_posture_port import (
    SecurityPosturePort,
    WorkloadComplianceRaw,
)


def _record(workload: str, category: str, compliant: bool = True) -> WorkloadComplianceRaw:
    return WorkloadComplianceRaw(
        workload=workload,
        namespace="production",
        category=category,
        compliant=compliant,
        exempt=False,
        detail="",
    )


class _FakeProvider:
    def __init__(
        self, category: str, records: list[WorkloadComplianceRaw], ok: bool = True
    ) -> None:
        self._category = category
        self._records = records
        self._ok = ok

    def category(self) -> str:
        return self._category

    def fetch(self) -> list[WorkloadComplianceRaw]:
        if not self._ok:
            raise TimeoutError("provider timed out")
        return self._records


class TestPortImplementation:
    def test_is_a_security_posture_port(self) -> None:
        from hexawyn.adapters.secondary.security_posture.security_posture_adapter import (
            SecurityPostureAdapter,
        )

        assert isinstance(SecurityPostureAdapter(providers=[]), SecurityPosturePort)


class TestListWorkloadCompliance:
    def test_aggregates_records_from_all_providers(self) -> None:
        from hexawyn.adapters.secondary.security_posture.security_posture_adapter import (
            SecurityPostureAdapter,
        )

        providers = [
            _FakeProvider("tls", [_record("a", "tls")]),
            _FakeProvider("rbac", [_record("b", "rbac", compliant=False)]),
        ]
        adapter = SecurityPostureAdapter(providers=providers)

        records = adapter.list_workload_compliance()

        assert len(records) == 2
        assert {r["category"] for r in records} == {"tls", "rbac"}

    def test_failed_provider_is_skipped_and_marks_partial(self) -> None:
        from hexawyn.adapters.secondary.security_posture.security_posture_adapter import (
            SecurityPostureAdapter,
        )

        providers = [
            _FakeProvider("tls", [_record("a", "tls")]),
            _FakeProvider("rbac", [], ok=False),
        ]
        adapter = SecurityPostureAdapter(providers=providers)

        records = adapter.list_workload_compliance()

        assert [r["category"] for r in records] == ["tls"]
        assert adapter.is_partial() is True


class TestDefinedCategories:
    def test_returns_categories_of_successful_providers(self) -> None:
        from hexawyn.adapters.secondary.security_posture.security_posture_adapter import (
            SecurityPostureAdapter,
        )

        providers = [
            _FakeProvider("tls", [_record("a", "tls")]),
            _FakeProvider("rbac", [_record("b", "rbac")]),
        ]
        adapter = SecurityPostureAdapter(providers=providers)
        adapter.list_workload_compliance()

        assert set(adapter.get_defined_categories()) == {"tls", "rbac"}

    def test_failed_provider_category_not_defined(self) -> None:
        from hexawyn.adapters.secondary.security_posture.security_posture_adapter import (
            SecurityPostureAdapter,
        )

        providers = [
            _FakeProvider("tls", [_record("a", "tls")]),
            _FakeProvider("secret_rotation", [], ok=False),
        ]
        adapter = SecurityPostureAdapter(providers=providers)
        adapter.list_workload_compliance()

        assert adapter.get_defined_categories() == ["tls"]


class TestIsPartial:
    def test_false_before_scan(self) -> None:
        from hexawyn.adapters.secondary.security_posture.security_posture_adapter import (
            SecurityPostureAdapter,
        )

        assert SecurityPostureAdapter(providers=[]).is_partial() is False

    def test_false_when_all_providers_succeed(self) -> None:
        from hexawyn.adapters.secondary.security_posture.security_posture_adapter import (
            SecurityPostureAdapter,
        )

        adapter = SecurityPostureAdapter(providers=[_FakeProvider("tls", [_record("a", "tls")])])
        adapter.list_workload_compliance()

        assert adapter.is_partial() is False
