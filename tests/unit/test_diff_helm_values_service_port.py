from abc import ABC


class TestDiffHelmValuesServicePort:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_service_port import (  # noqa: E501
            DiffHelmValuesServicePort,
        )

        assert issubclass(DiffHelmValuesServicePort, ABC)

    def test_declares_diff_method(self) -> None:
        from hexawyn.application.ports.driving.diff_helm_values.diff_helm_values_service_port import (  # noqa: E501
            DiffHelmValuesServicePort,
        )

        assert "diff" in DiffHelmValuesServicePort.__abstractmethods__
