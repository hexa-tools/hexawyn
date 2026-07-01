from __future__ import annotations

from hexawyn.application.ports.driven.what_if_simulation_port import WhatIfSimulationPort
from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_command import (
    RunWhatIfSimulationCommand,
)
from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_response import (
    RunWhatIfSimulationResponse,
)
from hexawyn.application.ports.driving.run_what_if_simulation.run_what_if_simulation_service_port import (
    RunWhatIfSimulationServicePort,
)
from hexawyn.domain.models.simulation import ScenarioInput
from hexawyn.domain.services.simulation.what_if_scenario_simulator_service import (
    WhatIfScenarioSimulatorService,
)


class RunWhatIfSimulationService(RunWhatIfSimulationServicePort):
    def __init__(self, simulation_port: WhatIfSimulationPort) -> None:
        self._port = simulation_port
        self._engine = WhatIfScenarioSimulatorService()

    def simulate(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = command.current_replicas
        if current_replicas is None:
            current_replicas = self._port.get_current_replicas(
                namespace=command.namespace,
                service_name=command.target_service,
            )

        current_cpu = command.current_cpu_utilization
        if current_cpu is None:
            current_cpu = self._port.get_current_cpu_utilization(
                namespace=command.namespace,
                service_name=command.target_service,
            )

        scenario = ScenarioInput(
            target_service=command.target_service,
            namespace=command.namespace,
            current_replicas=current_replicas,
            proposed_replicas=command.proposed_replicas,
            current_cpu_utilization=current_cpu,
        )

        topology_raw = self._port.get_service_topology(
            namespace=command.namespace,
            service_name=command.target_service,
        )
        topology: dict[str, object] = {k: [dict(svc) for svc in v] for k, v in topology_raw.items()}

        pdb_data = self._port.get_pdb_info(
            namespace=command.namespace,
            service_name=command.target_service,
        )
        pdb_info: dict[str, object] | None = dict(pdb_data) if pdb_data is not None else None

        hpa_data = self._port.get_hpa_info(
            namespace=command.namespace,
            service_name=command.target_service,
        )
        hpa_info: dict[str, object] | None = dict(hpa_data) if hpa_data is not None else None

        dependency_graph = self._port.get_dependency_graph(
            namespace=command.namespace,
        )

        impact = self._engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=pdb_info,
            hpa_info=hpa_info,
            dependency_graph=dependency_graph,
        )

        return RunWhatIfSimulationResponse.from_impact_report(impact)
