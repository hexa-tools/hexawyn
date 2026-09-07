from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.cilium_segmentation_audit.command import (
    CiliumSegmentationAuditCommand,
)
from hexawyn.application.use_case.cilium.cilium_segmentation_audit.response import (
    CiliumPathFindingOutput,
    CiliumSegmentationAuditResponse,
)
from hexawyn.domain.models.cilium import CiliumPathFinding


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCiliumSegmentationAuditUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut: MutantDict = {}  # type: ignore


class CiliumSegmentationAuditUseCase:
    @_mutmut_mutated(mutants_xǁCiliumSegmentationAuditUseCaseǁ__init____mutmut)
    def __init__(self, port: CiliumPort) -> None:
        self._port = port
    def xǁCiliumSegmentationAuditUseCaseǁ__init____mutmut_orig(self, port: CiliumPort) -> None:
        self._port = port
    def xǁCiliumSegmentationAuditUseCaseǁ__init____mutmut_1(self, port: CiliumPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut)
    def execute(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_orig(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_1(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = None
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_2(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = ""
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_3(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_4(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = None
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_5(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(None) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_6(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=None,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_7(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=None,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_8(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=None,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_9(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=None,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_10(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=None,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_11(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=None,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_12(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=None,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_13(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=None,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_14(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=None,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_15(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_16(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_17(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_18(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_19(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_20(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            findings=findings,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_21(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            summary=result.summary,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_22(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            note=result.note,
        )

    def xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_23(self, command: CiliumSegmentationAuditCommand) -> CiliumSegmentationAuditResponse:
        result = self._port.segmentation_audit()
        findings: list[CiliumPathFindingOutput] | None = None
        if result.findings is not None:
            findings = [self._to_finding(finding) for finding in result.findings]
        return CiliumSegmentationAuditResponse(
            installed=result.installed,
            status=result.status,
            view=result.view,
            total_identities=result.total_identities,
            total_paths=result.total_paths,
            uncovered_paths=result.uncovered_paths,
            findings=findings,
            summary=result.summary,
            )

    @staticmethod
    @_mutmut_mutated(mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut)
    def _to_finding(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "severity": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_orig(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "severity": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_1(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "XXsource_idXX": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "severity": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_2(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "SOURCE_ID": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "severity": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_3(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "XXdestination_idXX": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "severity": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_4(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "DESTINATION_ID": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "severity": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_5(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "XXsource_labelsXX": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "severity": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_6(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "SOURCE_LABELS": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "severity": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_7(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(None),
            "destination_labels": list(finding.destination_labels),
            "severity": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_8(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "XXdestination_labelsXX": list(finding.destination_labels),
            "severity": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_9(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "DESTINATION_LABELS": list(finding.destination_labels),
            "severity": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_10(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "destination_labels": list(None),
            "severity": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_11(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "XXseverityXX": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_12(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "SEVERITY": finding.severity,
            "note": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_13(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "severity": finding.severity,
            "XXnoteXX": finding.note,
        }

    @staticmethod
    def xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_14(finding: CiliumPathFinding) -> CiliumPathFindingOutput:
        return {
            "source_id": finding.source_id,
            "destination_id": finding.destination_id,
            "source_labels": list(finding.source_labels),
            "destination_labels": list(finding.destination_labels),
            "severity": finding.severity,
            "NOTE": finding.note,
        }

mutants_xǁCiliumSegmentationAuditUseCaseǁ__init____mutmut['_mutmut_orig'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ__init____mutmut['xǁCiliumSegmentationAuditUseCaseǁ__init____mutmut_1'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['_mutmut_orig'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_1'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_2'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_3'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_4'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_5'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_6'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_7'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_8'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_9'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_10'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_11'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_12'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_13'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_14'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_15'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_16'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_17'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_18'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_19'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_20'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_21'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_22'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut['xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_23'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated

mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['_mutmut_orig'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_1'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_2'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_3'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_4'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_5'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_6'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_7'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_8'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_9'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_10'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_11'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_12'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_13'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut['xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_14'] = CiliumSegmentationAuditUseCase.xǁCiliumSegmentationAuditUseCaseǁ_to_finding__mutmut_14 # type: ignore # mutmut generated
