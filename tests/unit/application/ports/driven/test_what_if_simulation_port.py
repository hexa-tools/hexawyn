from __future__ import annotations

import pytest
from hexawyn.application.ports.driven.what_if_simulation_port import (
    DependentServiceData,
    HPAData,
    PDBData,
    WhatIfSimulationPort,
)


class TestWhatIfSimulationPort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(WhatIfSimulationPort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            WhatIfSimulationPort()  # type: ignore[abstract]

    def test_dependent_service_data_typed_dict(self) -> None:
        svc: DependentServiceData = {"name": "checkout", "calls_per_second": 100.0}
        assert svc["name"] == "checkout"

    def test_pdb_data_typed_dict(self) -> None:
        pdb: PDBData = {"min_available": 2}
        assert pdb["min_available"] == 2

    def test_hpa_data_typed_dict(self) -> None:
        hpa: HPAData = {"min_replicas": 1, "max_replicas": 5, "current_replicas": 3}
        assert hpa["max_replicas"] == 5
