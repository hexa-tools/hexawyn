"""Unit tests for NamespaceWasteAnalysisPort (driven port contract)."""

import pytest
from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort


class TestNamespaceWasteAnalysisPort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(NamespaceWasteAnalysisPort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            NamespaceWasteAnalysisPort()  # type: ignore[abstract]

    def test_get_all_namespace_waste_data_is_abstract(self) -> None:
        assert hasattr(NamespaceWasteAnalysisPort, "get_all_namespace_waste_data")
