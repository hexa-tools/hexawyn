"""CalicoSegmentationAuditUseCase — Calico east-west segmentation matrix."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_segmentation_audit.command import (
    CalicoSegmentationAuditCommand,
)
from hexawyn.application.use_case.calico.calico_segmentation_audit.response import (
    CalicoSegmentationAuditResponse,
)
from hexawyn.domain.services.calico.segmentation_service import (
    build_calico_segmentation_audit,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCalicoSegmentationAuditUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CalicoSegmentationAuditUseCase:
    """Orchestrates the Calico segmentation matrix — depends only on ``CalicoPort``."""

    @_mutmut_mutated(mutants_xǁCalicoSegmentationAuditUseCaseǁ__init____mutmut)
    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoSegmentationAuditUseCaseǁ__init____mutmut_orig(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoSegmentationAuditUseCaseǁ__init____mutmut_1(self, port: CalicoPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut)
    def execute(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_orig(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_1(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = None
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_2(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_3(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=None,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_4(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=None,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_5(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view=None,
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_6(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=None,
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_7(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=None,
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_8(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=None,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_9(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=None,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_10(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=None,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_11(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_12(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_13(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_14(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_15(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_16(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_17(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_18(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_19(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=True,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_20(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="XXvanillaXX",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_21(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="VANILLA",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_22(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=1,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_23(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=1,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_24(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = None
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_25(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = None
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_26(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(None)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_27(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = None
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_28(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=None,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_29(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=None,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_30(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=None,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_31(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_32(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_33(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_34(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=None,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_35(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=None,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_36(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=None,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_37(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=None,
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_38(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=None,
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_39(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=None,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_40(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=None,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_41(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=None,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_42(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=None,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_43(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_44(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_45(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_46(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_47(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_48(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_49(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_50(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_51(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_52(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(None),
            edges=list(result.edges),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_53(self, command: CalicoSegmentationAuditCommand) -> CalicoSegmentationAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoSegmentationAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                view="vanilla",
                tiers=[],
                edges=[],
                gap_count=0,
                total_paths=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_segmentation_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoSegmentationAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            view=result.view,
            tiers=list(result.tiers),
            edges=list(None),
            gap_count=result.gap_count,
            total_paths=result.total_paths,
            summary=result.summary,
            error=result.error,
        )

mutants_xǁCalicoSegmentationAuditUseCaseǁ__init____mutmut['_mutmut_orig'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁ__init____mutmut['xǁCalicoSegmentationAuditUseCaseǁ__init____mutmut_1'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['_mutmut_orig'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_1'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_2'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_3'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_4'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_5'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_6'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_7'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_8'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_9'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_10'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_11'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_12'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_13'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_14'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_15'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_16'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_17'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_18'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_19'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_20'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_21'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_22'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_23'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_24'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_25'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_26'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_27'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_28'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_29'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_30'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_31'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_32'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_33'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_34'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_35'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_36'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_37'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_38'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_39'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_40'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_41'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_42'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_43'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_44'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_45'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_46'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_47'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_48'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_49'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_50'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_51'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_52'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut['xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_53'] = CalicoSegmentationAuditUseCase.xǁCalicoSegmentationAuditUseCaseǁexecute__mutmut_53 # type: ignore # mutmut generated
