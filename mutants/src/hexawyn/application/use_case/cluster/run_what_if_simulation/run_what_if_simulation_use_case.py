from __future__ import annotations

from hexawyn.application.ports.driven.what_if_simulation_port import WhatIfSimulationPort
from hexawyn.application.use_case.cluster.run_what_if_simulation.command import (
    RunWhatIfSimulationCommand,
)
from hexawyn.application.use_case.cluster.run_what_if_simulation.response import (
    RunWhatIfSimulationResponse,
)
from hexawyn.domain.models.simulation import ScenarioInput
from hexawyn.domain.services.simulation.what_if_scenario_simulator_service import (
    WhatIfScenarioSimulatorService,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRunWhatIfSimulationUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class RunWhatIfSimulationUseCase:
    @_mutmut_mutated(mutants_xǁRunWhatIfSimulationUseCaseǁ__init____mutmut)
    def __init__(self, simulation_port: WhatIfSimulationPort) -> None:
        self._port = simulation_port
        self._engine = WhatIfScenarioSimulatorService()
    def xǁRunWhatIfSimulationUseCaseǁ__init____mutmut_orig(self, simulation_port: WhatIfSimulationPort) -> None:
        self._port = simulation_port
        self._engine = WhatIfScenarioSimulatorService()
    def xǁRunWhatIfSimulationUseCaseǁ__init____mutmut_1(self, simulation_port: WhatIfSimulationPort) -> None:
        self._port = None
        self._engine = WhatIfScenarioSimulatorService()
    def xǁRunWhatIfSimulationUseCaseǁ__init____mutmut_2(self, simulation_port: WhatIfSimulationPort) -> None:
        self._port = simulation_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut)
    def execute(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_orig(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_1(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = None
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_2(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = command.current_replicas
        if current_replicas is not None:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_3(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = command.current_replicas
        if current_replicas is None:
            current_replicas = None

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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_4(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = command.current_replicas
        if current_replicas is None:
            current_replicas = self._port.get_current_replicas(
                namespace=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_5(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = command.current_replicas
        if current_replicas is None:
            current_replicas = self._port.get_current_replicas(
                namespace=command.namespace,
                service_name=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_6(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = command.current_replicas
        if current_replicas is None:
            current_replicas = self._port.get_current_replicas(
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_7(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = command.current_replicas
        if current_replicas is None:
            current_replicas = self._port.get_current_replicas(
                namespace=command.namespace,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_8(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = command.current_replicas
        if current_replicas is None:
            current_replicas = self._port.get_current_replicas(
                namespace=command.namespace,
                service_name=command.target_service,
            )

        current_cpu = None
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_9(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = command.current_replicas
        if current_replicas is None:
            current_replicas = self._port.get_current_replicas(
                namespace=command.namespace,
                service_name=command.target_service,
            )

        current_cpu = command.current_cpu_utilization
        if current_cpu is not None:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_10(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = command.current_replicas
        if current_replicas is None:
            current_replicas = self._port.get_current_replicas(
                namespace=command.namespace,
                service_name=command.target_service,
            )

        current_cpu = command.current_cpu_utilization
        if current_cpu is None:
            current_cpu = None

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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_11(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = command.current_replicas
        if current_replicas is None:
            current_replicas = self._port.get_current_replicas(
                namespace=command.namespace,
                service_name=command.target_service,
            )

        current_cpu = command.current_cpu_utilization
        if current_cpu is None:
            current_cpu = self._port.get_current_cpu_utilization(
                namespace=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_12(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
                service_name=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_13(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
        current_replicas = command.current_replicas
        if current_replicas is None:
            current_replicas = self._port.get_current_replicas(
                namespace=command.namespace,
                service_name=command.target_service,
            )

        current_cpu = command.current_cpu_utilization
        if current_cpu is None:
            current_cpu = self._port.get_current_cpu_utilization(
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_14(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_15(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

        scenario = None

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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_16(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            target_service=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_17(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            namespace=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_18(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            current_replicas=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_19(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            proposed_replicas=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_20(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            current_cpu_utilization=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_21(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_22(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_23(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_24(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_25(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_26(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

        topology_raw = None
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_27(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            namespace=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_28(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            service_name=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_29(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_30(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_31(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
        topology: dict[str, object] = None

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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_32(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
        topology: dict[str, object] = {k: [dict(None) for svc in v] for k, v in topology_raw.items()}

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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_33(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

        pdb_data = None
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_34(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            namespace=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_35(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            service_name=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_36(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_37(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_38(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
        pdb_info: dict[str, object] | None = None

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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_39(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
        pdb_info: dict[str, object] | None = dict(None) if pdb_data is not None else None

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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_40(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
        pdb_info: dict[str, object] | None = dict(pdb_data) if pdb_data is None else None

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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_41(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

        hpa_data = None
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_42(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            namespace=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_43(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            service_name=None,
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_44(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_45(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_46(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
        hpa_info: dict[str, object] | None = None

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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_47(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
        hpa_info: dict[str, object] | None = dict(None) if hpa_data is not None else None

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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_48(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
        hpa_info: dict[str, object] | None = dict(hpa_data) if hpa_data is None else None

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

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_49(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

        dependency_graph = None

        impact = self._engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=pdb_info,
            hpa_info=hpa_info,
            dependency_graph=dependency_graph,
        )

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_50(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            namespace=None,
        )

        impact = self._engine.compute_scenario(
            scenario=scenario,
            topology=topology,
            pdb_info=pdb_info,
            hpa_info=hpa_info,
            dependency_graph=dependency_graph,
        )

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_51(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

        impact = None

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_52(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            scenario=None,
            topology=topology,
            pdb_info=pdb_info,
            hpa_info=hpa_info,
            dependency_graph=dependency_graph,
        )

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_53(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            topology=None,
            pdb_info=pdb_info,
            hpa_info=hpa_info,
            dependency_graph=dependency_graph,
        )

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_54(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            pdb_info=None,
            hpa_info=hpa_info,
            dependency_graph=dependency_graph,
        )

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_55(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            hpa_info=None,
            dependency_graph=dependency_graph,
        )

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_56(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            dependency_graph=None,
        )

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_57(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            topology=topology,
            pdb_info=pdb_info,
            hpa_info=hpa_info,
            dependency_graph=dependency_graph,
        )

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_58(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            pdb_info=pdb_info,
            hpa_info=hpa_info,
            dependency_graph=dependency_graph,
        )

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_59(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            hpa_info=hpa_info,
            dependency_graph=dependency_graph,
        )

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_60(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            dependency_graph=dependency_graph,
        )

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_61(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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
            )

        return RunWhatIfSimulationResponse.from_impact_report(impact)

    def xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_62(self, command: RunWhatIfSimulationCommand) -> RunWhatIfSimulationResponse:
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

        return RunWhatIfSimulationResponse.from_impact_report(None)

mutants_xǁRunWhatIfSimulationUseCaseǁ__init____mutmut['_mutmut_orig'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁ__init____mutmut['xǁRunWhatIfSimulationUseCaseǁ__init____mutmut_1'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁ__init____mutmut['xǁRunWhatIfSimulationUseCaseǁ__init____mutmut_2'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['_mutmut_orig'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_1'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_2'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_3'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_4'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_5'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_6'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_7'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_8'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_9'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_10'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_11'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_12'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_13'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_14'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_15'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_16'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_17'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_18'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_19'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_20'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_21'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_22'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_23'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_24'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_25'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_26'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_27'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_28'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_29'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_30'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_31'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_32'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_33'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_34'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_35'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_36'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_37'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_38'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_39'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_40'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_41'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_42'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_43'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_44'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_45'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_46'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_47'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_48'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_49'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_50'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_51'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_52'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_53'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_54'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_55'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_56'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_57'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_58'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_59'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_60'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_61'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁRunWhatIfSimulationUseCaseǁexecute__mutmut['xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_62'] = RunWhatIfSimulationUseCase.xǁRunWhatIfSimulationUseCaseǁexecute__mutmut_62 # type: ignore # mutmut generated
