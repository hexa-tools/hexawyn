"""CalicoConnectivityHealthUseCase — Calico dataplane end-to-end health."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_connectivity_health.command import (
    CalicoConnectivityHealthCommand,
)
from hexawyn.application.use_case.calico.calico_connectivity_health.response import (
    CalicoConnectivityHealthResponse,
)
from hexawyn.domain.models.calico import DataplaneMode
from hexawyn.domain.services.calico.connectivity_health_service import (
    build_calico_connectivity_health,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCalicoConnectivityHealthUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CalicoConnectivityHealthUseCase:
    """Orchestrates the connectivity verdict — depends only on ``CalicoPort``."""

    @_mutmut_mutated(mutants_xǁCalicoConnectivityHealthUseCaseǁ__init____mutmut)
    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoConnectivityHealthUseCaseǁ__init____mutmut_orig(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoConnectivityHealthUseCaseǁ__init____mutmut_1(self, port: CalicoPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut)
    def execute(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_orig(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_1(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = None
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_2(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_3(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=None,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_4(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=None,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_5(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict=None,
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_6(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=None,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_7(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_8(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_9(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_10(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_11(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=True,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_12(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="XXunknownXX",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_13(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="UNKNOWN",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_14(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = None
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_15(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = None
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_16(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=None, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_17(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=None)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_18(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_19(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, )
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_20(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = None
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_21(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=None,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_22(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=None,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_23(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=None,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_24(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=None,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_25(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=None,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_26(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=None,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_27(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=None,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_28(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=None,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_29(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=None,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_30(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=None,
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_31(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=None,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_32(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=None,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_33(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=None,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_34(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_35(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_36(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_37(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_38(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_39(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_40(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_41(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_42(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_43(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_44(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_45(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_46(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_47(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(None),
            degraded_nodes=list(result.degraded_nodes),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_48(self, command: CalicoConnectivityHealthCommand) -> CalicoConnectivityHealthResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoConnectivityHealthResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                verdict="unknown",
                error=detection.error,
            )
        connectivity = self._port.connectivity_health()
        result = build_calico_connectivity_health(detection=detection, connectivity=connectivity)
        mode = (
            result.dataplane_mode.value
            if isinstance(result.dataplane_mode, DataplaneMode)
            else result.dataplane_mode
        )
        return CalicoConnectivityHealthResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            verdict=result.verdict,
            ready_agents=result.ready_agents,
            total_agents=result.total_agents,
            dataplane_mode=mode,
            tunnel_summary=result.tunnel_summary,
            bgp_summary=result.bgp_summary,
            connectivity_probe=result.connectivity_probe,
            nodes=list(result.nodes),
            degraded_nodes=list(None),
            summary=result.summary,
            error=result.error,
        )

mutants_xǁCalicoConnectivityHealthUseCaseǁ__init____mutmut['_mutmut_orig'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁ__init____mutmut['xǁCalicoConnectivityHealthUseCaseǁ__init____mutmut_1'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['_mutmut_orig'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_1'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_2'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_3'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_4'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_5'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_6'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_7'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_8'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_9'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_10'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_11'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_12'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_13'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_14'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_15'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_16'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_17'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_18'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_19'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_20'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_21'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_22'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_23'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_24'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_25'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_26'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_27'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_28'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_29'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_30'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_31'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_32'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_33'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_34'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_35'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_36'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_37'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_38'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_39'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_40'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_41'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_42'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_43'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_44'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_45'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_46'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_47'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut['xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_48'] = CalicoConnectivityHealthUseCase.xǁCalicoConnectivityHealthUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
