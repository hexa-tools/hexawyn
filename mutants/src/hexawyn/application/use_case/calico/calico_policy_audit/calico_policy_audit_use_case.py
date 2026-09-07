"""CalicoPolicyAuditUseCase — audit Calico L3/L4 (and L7) coverage gaps."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_policy_audit.command import (
    CalicoPolicyAuditCommand,
)
from hexawyn.application.use_case.calico.calico_policy_audit.response import (
    CalicoPolicyAuditResponse,
)
from hexawyn.domain.services.calico.policy_audit_service import (
    build_calico_policy_audit,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCalicoPolicyAuditUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class CalicoPolicyAuditUseCase:
    """Orchestrates the Calico coverage audit — depends only on ``CalicoPort``."""

    @_mutmut_mutated(mutants_xǁCalicoPolicyAuditUseCaseǁ__init____mutmut)
    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoPolicyAuditUseCaseǁ__init____mutmut_orig(self, port: CalicoPort) -> None:
        self._port = port

    def xǁCalicoPolicyAuditUseCaseǁ__init____mutmut_1(self, port: CalicoPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut)
    def execute(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_orig(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_1(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = None
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_2(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_3(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=None,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_4(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=None,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_5(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=None,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_6(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=None,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_7(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=None,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_8(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=None,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_9(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_10(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_11(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_12(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_13(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_14(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_15(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=True,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_16(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=False,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_17(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=1,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_18(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = None
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_19(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = None
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_20(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(None)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_21(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = None
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_22(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=None,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_23(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=None,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_24(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=None,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_25(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_26(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_27(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_28(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=None,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_29(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=None,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_30(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=None,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_31(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=None,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_32(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=None,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_33(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=None,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_34(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=None,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_35(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=None,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_36(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_37(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_38(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_39(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_40(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_41(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_42(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_43(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_44(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=True,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(result.findings),
            summary=result.summary,
            error=result.error,
        )

    def xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_45(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoPolicyAuditResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                degraded_to_vanilla=True,
                gap_count=0,
                findings=[],
                error=detection.error,
            )

        workloads = self._port.list_workloads()
        policies = self._port.list_network_policies(command.namespace)
        result = build_calico_policy_audit(
            workloads=workloads,
            policies=policies,
            excluded_namespaces=command.excluded_namespaces,
        )
        return CalicoPolicyAuditResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            degraded_to_vanilla=False,
            total_namespaces_checked=result.total_namespaces_checked,
            gap_count=result.gap_count,
            findings=list(None),
            summary=result.summary,
            error=result.error,
        )

mutants_xǁCalicoPolicyAuditUseCaseǁ__init____mutmut['_mutmut_orig'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁ__init____mutmut['xǁCalicoPolicyAuditUseCaseǁ__init____mutmut_1'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['_mutmut_orig'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_1'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_2'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_3'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_4'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_5'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_6'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_7'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_8'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_9'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_10'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_11'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_12'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_13'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_14'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_15'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_16'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_17'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_18'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_19'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_20'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_21'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_22'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_23'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_24'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_25'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_26'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_27'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_28'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_29'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_30'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_31'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_32'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_33'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_34'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_35'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_36'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_37'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_38'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_39'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_40'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_41'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_42'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_43'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_44'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁCalicoPolicyAuditUseCaseǁexecute__mutmut['xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_45'] = CalicoPolicyAuditUseCase.xǁCalicoPolicyAuditUseCaseǁexecute__mutmut_45 # type: ignore # mutmut generated
