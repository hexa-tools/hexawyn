from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.cilium_policy_audit.command import (
    CiliumPolicyAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_policy_audit.response import (
    CiliumAuditFindingOutput,
    CiliumPolicyAuditResponse,
)
from hexawyn.domain.models.cilium import CiliumAuditFinding


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCiliumPolicyAuditUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut: MutantDict = {}  # type: ignore


class CiliumPolicyAuditUseCase:
    @_mutmut_mutated(mutants_xǁCiliumPolicyAuditUseCaseǁ__init____mutmut)
    def __init__(self, port: CiliumPort) -> None:
        self._port = port
    def xǁCiliumPolicyAuditUseCaseǁ__init____mutmut_orig(self, port: CiliumPort) -> None:
        self._port = port
    def xǁCiliumPolicyAuditUseCaseǁ__init____mutmut_1(self, port: CiliumPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut)
    def execute(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_orig(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_1(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = None
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_2(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = ""
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_3(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_4(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = None
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_5(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(None) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_6(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=None,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_7(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=None,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_8(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=None,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_9(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=None,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_10(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=None,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_11(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=None,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_12(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=None,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_13(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=None,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_14(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_15(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_16(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_17(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_18(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_19(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_20(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            note=result.note,
        )

    def xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_21(self, command: CiliumPolicyAuditCommand) -> CiliumPolicyAuditResponse:
        result = self._port.audit_policies()
        findings: list[CiliumAuditFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumPolicyAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_workloads=result.total_workloads,
            uncovered_count=result.uncovered_count,
            findings=findings,
            summary=result.summary,
            )

    @staticmethod
    @_mutmut_mutated(mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut)
    def _to_finding(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_orig(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_1(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "XXnamespaceXX": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_2(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "NAMESPACE": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_3(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "XXworkloadXX": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_4(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "WORKLOAD": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_5(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "XXcoverageXX": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_6(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "COVERAGE": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_7(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "XXingress_restrictedXX": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_8(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "INGRESS_RESTRICTED": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_9(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "XXegress_restrictedXX": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_10(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "EGRESS_RESTRICTED": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_11(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "XXl7_restrictedXX": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_12(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "L7_RESTRICTED": finding.l7_restricted,
            "risk": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_13(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "XXriskXX": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_14(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "RISK": finding.risk,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_15(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "XXnoteXX": finding.note,
        }

    @staticmethod
    def xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_16(finding: CiliumAuditFinding) -> CiliumAuditFindingOutput:
        return {
            "namespace": finding.namespace,
            "workload": finding.workload,
            "coverage": finding.coverage,
            "ingress_restricted": finding.ingress_restricted,
            "egress_restricted": finding.egress_restricted,
            "l7_restricted": finding.l7_restricted,
            "risk": finding.risk,
            "NOTE": finding.note,
        }

mutants_xǁCiliumPolicyAuditUseCaseǁ__init____mutmut['_mutmut_orig'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ__init____mutmut['xǁCiliumPolicyAuditUseCaseǁ__init____mutmut_1'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['_mutmut_orig'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_1'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_2'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_3'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_4'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_5'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_6'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_7'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_8'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_9'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_10'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_11'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_12'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_13'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_14'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_15'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_16'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_17'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_18'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_19'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_20'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁexecute__mutmut['xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_21'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated

mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['_mutmut_orig'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_1'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_2'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_3'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_4'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_5'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_6'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_7'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_8'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_9'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_10'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_11'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_12'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_13'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_14'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_15'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut['xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_16'] = CiliumPolicyAuditUseCase.xǁCiliumPolicyAuditUseCaseǁ_to_finding__mutmut_16 # type: ignore # mutmut generated
