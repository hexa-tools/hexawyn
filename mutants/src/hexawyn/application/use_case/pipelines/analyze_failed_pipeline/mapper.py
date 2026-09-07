from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.response import (
    AnalyzeFailedPipelineResponse,
    FailureAnalysisDict,
)
from hexawyn.domain.models.pipeline_failure_analysis import (
    AnalyzeFailedPipelineResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_to_response__mutmut)
def to_response(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_orig(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_1(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=None,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_2(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=None,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_3(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=None,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_4(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=None,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_5(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=None,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_6(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=None,
    )


def x_to_response__mutmut_7(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_8(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_9(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_10(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_11(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_12(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        )


def x_to_response__mutmut_13(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=None,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_14(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=None,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_15(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=None,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_16(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=None,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_17(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=None,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_18(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=None,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_19(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_20(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_21(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_22(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                impact_score=failure.impact_score,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_23(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                remediation=failure.remediation,
            )
            for failure in result.failures
        ],
    )


def x_to_response__mutmut_24(
    result: AnalyzeFailedPipelineResult,
) -> AnalyzeFailedPipelineResponse:
    return AnalyzeFailedPipelineResponse(
        pipeline_name=result.pipeline_name,
        namespace=result.namespace,
        pipeline_run_found=result.pipeline_run_found,
        aggregated_root_cause=result.aggregated_root_cause,
        summary=result.summary,
        failures=[
            FailureAnalysisDict(
                task_name=failure.task_name,
                root_cause=failure.root_cause,
                failure_type=failure.failure_type.value,
                confidence=failure.confidence,
                impact_score=failure.impact_score,
                )
            for failure in result.failures
        ],
    )

mutants_x_to_response__mutmut['_mutmut_orig'] = x_to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_1'] = x_to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_2'] = x_to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_3'] = x_to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_4'] = x_to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_5'] = x_to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_6'] = x_to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_7'] = x_to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_8'] = x_to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_9'] = x_to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_10'] = x_to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_11'] = x_to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_12'] = x_to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_13'] = x_to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_14'] = x_to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_15'] = x_to_response__mutmut_15 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_16'] = x_to_response__mutmut_16 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_17'] = x_to_response__mutmut_17 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_18'] = x_to_response__mutmut_18 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_19'] = x_to_response__mutmut_19 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_20'] = x_to_response__mutmut_20 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_21'] = x_to_response__mutmut_21 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_22'] = x_to_response__mutmut_22 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_23'] = x_to_response__mutmut_23 # type: ignore # mutmut generated
mutants_x_to_response__mutmut['x_to_response__mutmut_24'] = x_to_response__mutmut_24 # type: ignore # mutmut generated
