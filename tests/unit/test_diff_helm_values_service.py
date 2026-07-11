from unittest.mock import MagicMock

from hexawyn.application.ports.driven.helm_values_diff_port import (
    HelmReleaseValues,
    HelmValuesDiffPort,
)
from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_command import (
    DiffHelmValuesCommand,
)


def _values(namespace: str, values: dict[str, object]) -> HelmReleaseValues:
    return HelmReleaseValues(release="payment-service", namespace=namespace, values=values)


class TestDiffHelmValuesService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_service_port import (  # noqa: E501
            DiffHelmValuesServicePort,
        )
        from hexawyn.application.service.diff_helm_values_service import (
            DiffHelmValuesService,
        )

        service = DiffHelmValuesService(helm_values_port=MagicMock(spec=HelmValuesDiffPort))

        assert isinstance(service, DiffHelmValuesServicePort)

    def test_diff_retrieves_both_namespaces_and_reports(self) -> None:
        from hexawyn.application.service.diff_helm_values_service import (
            DiffHelmValuesService,
        )

        port = MagicMock(spec=HelmValuesDiffPort)
        port.get_effective_values.side_effect = [
            _values("staging", {"image": {"tag": "v1.3"}, "replicaCount": 1}),
            _values("production", {"image": {"tag": "v1.2"}, "replicaCount": 3}),
        ]
        service = DiffHelmValuesService(helm_values_port=port)

        response = service.diff(
            DiffHelmValuesCommand(
                release="payment-service",
                source_namespace="staging",
                target_namespace="production",
            )
        )

        assert port.get_effective_values.call_count == 2
        report = response.result
        assert report.release == "payment-service"
        assert report.in_sync is False
        assert [d.key_path for d in report.critical] == ["image.tag"]
        assert [d.key_path for d in report.warning] == ["replicaCount"]

    def test_diff_source_before_target(self) -> None:
        from hexawyn.application.service.diff_helm_values_service import (
            DiffHelmValuesService,
        )

        port = MagicMock(spec=HelmValuesDiffPort)
        port.get_effective_values.side_effect = [
            _values("staging", {"image": {"tag": "v1.3"}}),
            _values("production", {"image": {"tag": "v1.2"}}),
        ]
        service = DiffHelmValuesService(helm_values_port=port)

        service.diff(
            DiffHelmValuesCommand(
                release="payment-service",
                source_namespace="staging",
                target_namespace="production",
            )
        )

        first_call = port.get_effective_values.call_args_list[0]
        assert first_call.args == ("payment-service", "staging")
        second_call = port.get_effective_values.call_args_list[1]
        assert second_call.args == ("payment-service", "production")

    def test_diff_lets_helm_error_propagate(self) -> None:
        import pytest
        from hexawyn.application.service.diff_helm_values_service import (
            DiffHelmValuesService,
        )
        from hexawyn.domain.errors import HelmNotFoundError

        port = MagicMock(spec=HelmValuesDiffPort)
        port.get_effective_values.side_effect = HelmNotFoundError()
        service = DiffHelmValuesService(helm_values_port=port)

        with pytest.raises(HelmNotFoundError):
            service.diff(
                DiffHelmValuesCommand(
                    release="payment-service",
                    source_namespace="staging",
                    target_namespace="production",
                )
            )
