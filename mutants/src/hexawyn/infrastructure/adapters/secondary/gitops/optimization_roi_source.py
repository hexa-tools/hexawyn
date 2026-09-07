from __future__ import annotations

from hexawyn.application.ports.driven.optimization_roi_port import SprintRoiData


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut: MutantDict = {}  # type: ignore


class EmptySprintRoiSource:
    """Default sprint ROI source used until a persistent sprint baseline store
    is wired in. Reports no baseline, so the domain asks the user to establish
    one rather than fabricating a misleading zero-ROI report."""

    @_mutmut_mutated(mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut)
    def fetch_sprint_roi_data(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            baseline_monthly_eur=0.0,
            current_monthly_eur=0.0,
            optimizations=[],
            performance_metrics=[],
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_orig(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            baseline_monthly_eur=0.0,
            current_monthly_eur=0.0,
            optimizations=[],
            performance_metrics=[],
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_1(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=None,
            baseline_monthly_eur=0.0,
            current_monthly_eur=0.0,
            optimizations=[],
            performance_metrics=[],
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_2(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            baseline_monthly_eur=None,
            current_monthly_eur=0.0,
            optimizations=[],
            performance_metrics=[],
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_3(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            baseline_monthly_eur=0.0,
            current_monthly_eur=None,
            optimizations=[],
            performance_metrics=[],
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_4(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            baseline_monthly_eur=0.0,
            current_monthly_eur=0.0,
            optimizations=None,
            performance_metrics=[],
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_5(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            baseline_monthly_eur=0.0,
            current_monthly_eur=0.0,
            optimizations=[],
            performance_metrics=None,
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_6(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            baseline_monthly_eur=0.0,
            current_monthly_eur=0.0,
            optimizations=[],
            performance_metrics=[],
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_7(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            current_monthly_eur=0.0,
            optimizations=[],
            performance_metrics=[],
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_8(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            baseline_monthly_eur=0.0,
            optimizations=[],
            performance_metrics=[],
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_9(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            baseline_monthly_eur=0.0,
            current_monthly_eur=0.0,
            performance_metrics=[],
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_10(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            baseline_monthly_eur=0.0,
            current_monthly_eur=0.0,
            optimizations=[],
            )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_11(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=True,
            baseline_monthly_eur=0.0,
            current_monthly_eur=0.0,
            optimizations=[],
            performance_metrics=[],
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_12(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            baseline_monthly_eur=1.0,
            current_monthly_eur=0.0,
            optimizations=[],
            performance_metrics=[],
        )

    def xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_13(self, sprint_id: str) -> SprintRoiData:
        return SprintRoiData(
            has_baseline=False,
            baseline_monthly_eur=0.0,
            current_monthly_eur=1.0,
            optimizations=[],
            performance_metrics=[],
        )

mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['_mutmut_orig'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_1'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_2'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_3'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_4'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_5'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_6'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_7'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_8'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_9'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_10'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_11'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_11 # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_12'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_12 # type: ignore # mutmut generated
mutants_xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut['xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_13'] = EmptySprintRoiSource.xǁEmptySprintRoiSourceǁfetch_sprint_roi_data__mutmut_13 # type: ignore # mutmut generated
