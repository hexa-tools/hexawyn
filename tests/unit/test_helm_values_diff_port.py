from abc import ABC


class TestHelmValuesDiffPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.helm_values_diff_port import (
            HelmValuesDiffPort,
        )

        assert issubclass(HelmValuesDiffPort, ABC)

    def test_declares_get_effective_values(self) -> None:
        from hexawyn.application.ports.driven.helm_values_diff_port import (
            HelmValuesDiffPort,
        )

        assert "get_effective_values" in HelmValuesDiffPort.__abstractmethods__


class TestHelmReleaseValues:
    def test_shape(self) -> None:
        from hexawyn.application.ports.driven.helm_values_diff_port import (
            HelmReleaseValues,
        )

        values: HelmReleaseValues = {
            "release": "payment-service",
            "namespace": "staging",
            "values": {"image": {"tag": "v1.3"}, "replicaCount": 1},
        }

        assert values["release"] == "payment-service"
        assert values["namespace"] == "staging"
        assert values["values"]["replicaCount"] == 1
