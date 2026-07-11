from unittest.mock import MagicMock

from hexawyn.application.ports.driven.security_posture_port import (
    SecurityPosturePort,
    WorkloadComplianceRaw,
)
from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_command import (  # noqa: E501
    ComputeSecurityPostureCommand,
)

_ALL = ["tls", "rbac", "pod_security", "image_scanning", "secret_rotation"]


def _raw(workload: str, category: str, compliant: bool = True) -> WorkloadComplianceRaw:
    return WorkloadComplianceRaw(
        workload=workload,
        namespace="production",
        category=category,
        compliant=compliant,
        exempt=False,
        detail="",
    )


def _port(records: list[WorkloadComplianceRaw], partial: bool = False) -> MagicMock:
    port = MagicMock(spec=SecurityPosturePort)
    port.list_workload_compliance.return_value = records
    port.get_defined_categories.return_value = _ALL
    port.is_partial.return_value = partial
    return port


class TestComputeSecurityPostureService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_service_port import (  # noqa: E501
            ComputeSecurityPostureServicePort,
        )
        from hexawyn.application.service.compute_security_posture_service import (
            ComputeSecurityPostureService,
        )

        service = ComputeSecurityPostureService(posture_port=_port([]))

        assert isinstance(service, ComputeSecurityPostureServicePort)

    def test_compute_returns_scored_report(self) -> None:
        from hexawyn.application.service.compute_security_posture_service import (
            ComputeSecurityPostureService,
        )

        records = [_raw("a", "tls", compliant=True), _raw("b", "tls", compliant=False)]
        service = ComputeSecurityPostureService(posture_port=_port(records))

        response = service.compute(ComputeSecurityPostureCommand())

        tls = next(c for c in response.result.categories if c.category == "tls")
        assert tls.score_pct == 50.0

    def test_compute_passes_partial_flag(self) -> None:
        from hexawyn.application.service.compute_security_posture_service import (
            ComputeSecurityPostureService,
        )

        service = ComputeSecurityPostureService(
            posture_port=_port([_raw("a", "tls")], partial=True)
        )

        response = service.compute(ComputeSecurityPostureCommand())

        assert response.result.partial is True
        assert response.result.warning != ""

    def test_compute_passes_previous_score_for_trend(self) -> None:
        from hexawyn.application.service.compute_security_posture_service import (
            ComputeSecurityPostureService,
        )

        records = [_raw(f"w{i}", category) for i in range(4) for category in _ALL]
        service = ComputeSecurityPostureService(posture_port=_port(records))

        response = service.compute(ComputeSecurityPostureCommand(previous_score_pct=90.0))

        assert response.result.previous_score_pct == 90.0
        assert response.result.trend == "improving"

    def test_compute_lets_error_propagate(self) -> None:
        import pytest
        from hexawyn.application.service.compute_security_posture_service import (
            ComputeSecurityPostureService,
        )
        from hexawyn.domain.errors import ClusterUnreachableError

        port = MagicMock(spec=SecurityPosturePort)
        port.list_workload_compliance.side_effect = ClusterUnreachableError("down")
        service = ComputeSecurityPostureService(posture_port=port)

        with pytest.raises(ClusterUnreachableError):
            service.compute(ComputeSecurityPostureCommand())
