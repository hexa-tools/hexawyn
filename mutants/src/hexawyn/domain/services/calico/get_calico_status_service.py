"""Pure Calico status composition — no infrastructure imports.

Turns the detection snapshot plus the (best-effort) felix metrics and
connectivity probe into a truthful ``CalicoStatusResult``. Degradation is never
hidden: agent shortfall, felix errors or a degraded connectivity probe all raise
the overall status to DEGRADED.
"""

from __future__ import annotations

from collections.abc import Mapping

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoStatusResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_calico_status_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_calico_status_result__mutmut)
def build_calico_status_result(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_orig(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_1(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_2(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=None,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_3(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=None,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_4(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=None,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_5(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=None,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_6(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=None,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_7(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=None,
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_8(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=None,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_9(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=None,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_10(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=None,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_11(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_12(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_13(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_14(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_15(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_16(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_17(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_18(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_19(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_20(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_21(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_22(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_23(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_24(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=True,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_25(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=1,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_26(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=1,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_27(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=True,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_28(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=True,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_29(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = None
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_30(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(None)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_31(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = None
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_32(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(None)
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_33(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get(None))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_34(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("XXavailableXX"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_35(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("AVAILABLE"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_36(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = None
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_37(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(None)
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_38(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get(None))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_39(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("XXavailableXX"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_40(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("AVAILABLE"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_41(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = None

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_42(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(None)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_43(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = None
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_44(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0) and conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_45(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED and (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_46(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status != CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_47(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None or felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_48(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_49(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors >= 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_50(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 1)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_51(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status != "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_52(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "XXdegradedXX"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_53(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "DEGRADED"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_54(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = None
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_55(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = None

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_56(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=None,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_57(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=None,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_58(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=None,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_59(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=None,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_60(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=None,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_61(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_62(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_63(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_64(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_65(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_66(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=None,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_67(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=None,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_68(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=None,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_69(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=None,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_70(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=None,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_71(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=None,
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_72(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=None,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_73(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=None,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_74(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=None,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_75(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=None,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_76(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_77(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=None,
    )


def x_build_calico_status_result__mutmut_78(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_79(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_80(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_81(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_82(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_83(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_84(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_85(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_86(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_87(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_88(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_89(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_90(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        )


def x_build_calico_status_result__mutmut_91(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=False,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_92(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(None),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_93(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(None) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_94(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get(None)) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_95(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("XXdetailXX")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_96(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("DETAIL")) if connectivity.get("detail") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_97(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get(None) else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_98(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("XXdetailXX") else None,
        error=detection.error,
    )


def x_build_calico_status_result__mutmut_99(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
    felix: Mapping[str, object],
) -> CalicoStatusResult:
    """Compose the datapath status from detection, connectivity and felix info."""
    if not detection.installed:
        return CalicoStatusResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            agents=[],
            felix_errors_available=False,
            felix_errors=None,
            connectivity_available=False,
            connectivity_status=None,
            connectivity_detail=None,
            error=detection.error,
        )

    felix_errors = _felix_error_total(felix)
    felix_available = bool(felix.get("available"))
    conn_available = bool(connectivity.get("available"))
    conn_status = _connectivity_status(connectivity)

    degraded = (
        detection.status == CalicoDetectionStatus.DEGRADED
        or (felix_errors is not None and felix_errors > 0)
        or conn_status == "degraded"
    )
    status = CalicoDetectionStatus.DEGRADED if degraded else CalicoDetectionStatus.INSTALLED
    degraded_summary = (
        _compose_degraded_summary(
            ready=detection.ready_agents,
            total=detection.total_nodes,
            agent_summary=detection.degraded_summary,
            felix_errors=felix_errors,
            connectivity_status=conn_status,
        )
        if degraded
        else None
    )

    return CalicoStatusResult(
        installed=True,
        not_installed_marker=None,
        status=status,
        ready_agents=detection.ready_agents,
        total_agents=detection.total_nodes,
        degraded_summary=degraded_summary,
        agents=list(detection.agents),
        felix_errors_available=felix_available,
        felix_errors=felix_errors,
        connectivity_available=conn_available,
        connectivity_status=conn_status,
        connectivity_detail=str(connectivity.get("detail")) if connectivity.get("DETAIL") else None,
        error=detection.error,
    )

mutants_x_build_calico_status_result__mutmut['_mutmut_orig'] = x_build_calico_status_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_1'] = x_build_calico_status_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_2'] = x_build_calico_status_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_3'] = x_build_calico_status_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_4'] = x_build_calico_status_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_5'] = x_build_calico_status_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_6'] = x_build_calico_status_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_7'] = x_build_calico_status_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_8'] = x_build_calico_status_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_9'] = x_build_calico_status_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_10'] = x_build_calico_status_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_11'] = x_build_calico_status_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_12'] = x_build_calico_status_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_13'] = x_build_calico_status_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_14'] = x_build_calico_status_result__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_15'] = x_build_calico_status_result__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_16'] = x_build_calico_status_result__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_17'] = x_build_calico_status_result__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_18'] = x_build_calico_status_result__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_19'] = x_build_calico_status_result__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_20'] = x_build_calico_status_result__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_21'] = x_build_calico_status_result__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_22'] = x_build_calico_status_result__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_23'] = x_build_calico_status_result__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_24'] = x_build_calico_status_result__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_25'] = x_build_calico_status_result__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_26'] = x_build_calico_status_result__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_27'] = x_build_calico_status_result__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_28'] = x_build_calico_status_result__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_29'] = x_build_calico_status_result__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_30'] = x_build_calico_status_result__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_31'] = x_build_calico_status_result__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_32'] = x_build_calico_status_result__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_33'] = x_build_calico_status_result__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_34'] = x_build_calico_status_result__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_35'] = x_build_calico_status_result__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_36'] = x_build_calico_status_result__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_37'] = x_build_calico_status_result__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_38'] = x_build_calico_status_result__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_39'] = x_build_calico_status_result__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_40'] = x_build_calico_status_result__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_41'] = x_build_calico_status_result__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_42'] = x_build_calico_status_result__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_43'] = x_build_calico_status_result__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_44'] = x_build_calico_status_result__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_45'] = x_build_calico_status_result__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_46'] = x_build_calico_status_result__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_47'] = x_build_calico_status_result__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_48'] = x_build_calico_status_result__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_49'] = x_build_calico_status_result__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_50'] = x_build_calico_status_result__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_51'] = x_build_calico_status_result__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_52'] = x_build_calico_status_result__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_53'] = x_build_calico_status_result__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_54'] = x_build_calico_status_result__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_55'] = x_build_calico_status_result__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_56'] = x_build_calico_status_result__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_57'] = x_build_calico_status_result__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_58'] = x_build_calico_status_result__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_59'] = x_build_calico_status_result__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_60'] = x_build_calico_status_result__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_61'] = x_build_calico_status_result__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_62'] = x_build_calico_status_result__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_63'] = x_build_calico_status_result__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_64'] = x_build_calico_status_result__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_65'] = x_build_calico_status_result__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_66'] = x_build_calico_status_result__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_67'] = x_build_calico_status_result__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_68'] = x_build_calico_status_result__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_69'] = x_build_calico_status_result__mutmut_69 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_70'] = x_build_calico_status_result__mutmut_70 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_71'] = x_build_calico_status_result__mutmut_71 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_72'] = x_build_calico_status_result__mutmut_72 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_73'] = x_build_calico_status_result__mutmut_73 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_74'] = x_build_calico_status_result__mutmut_74 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_75'] = x_build_calico_status_result__mutmut_75 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_76'] = x_build_calico_status_result__mutmut_76 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_77'] = x_build_calico_status_result__mutmut_77 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_78'] = x_build_calico_status_result__mutmut_78 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_79'] = x_build_calico_status_result__mutmut_79 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_80'] = x_build_calico_status_result__mutmut_80 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_81'] = x_build_calico_status_result__mutmut_81 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_82'] = x_build_calico_status_result__mutmut_82 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_83'] = x_build_calico_status_result__mutmut_83 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_84'] = x_build_calico_status_result__mutmut_84 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_85'] = x_build_calico_status_result__mutmut_85 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_86'] = x_build_calico_status_result__mutmut_86 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_87'] = x_build_calico_status_result__mutmut_87 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_88'] = x_build_calico_status_result__mutmut_88 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_89'] = x_build_calico_status_result__mutmut_89 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_90'] = x_build_calico_status_result__mutmut_90 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_91'] = x_build_calico_status_result__mutmut_91 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_92'] = x_build_calico_status_result__mutmut_92 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_93'] = x_build_calico_status_result__mutmut_93 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_94'] = x_build_calico_status_result__mutmut_94 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_95'] = x_build_calico_status_result__mutmut_95 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_96'] = x_build_calico_status_result__mutmut_96 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_97'] = x_build_calico_status_result__mutmut_97 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_98'] = x_build_calico_status_result__mutmut_98 # type: ignore # mutmut generated
mutants_x_build_calico_status_result__mutmut['x_build_calico_status_result__mutmut_99'] = x_build_calico_status_result__mutmut_99 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__felix_error_total__mutmut)
def _felix_error_total(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_orig(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_1(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_2(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get(None):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_3(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("XXavailableXX"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_4(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("AVAILABLE"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_5(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = None
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_6(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get(None)
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_7(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("XXmetricsXX")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_8(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("METRICS")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_9(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_10(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 1
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_11(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = None
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_12(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "XXerrorXX" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_13(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "ERROR" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_14(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" not in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_15(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).upper()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_16(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(None).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_17(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_18(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 1
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_19(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = None
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_20(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 1.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_21(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total = float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_22(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total -= float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_23(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(None)
        except (TypeError, ValueError):
            continue
    return int(total)


def x__felix_error_total__mutmut_24(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            break
    return int(total)


def x__felix_error_total__mutmut_25(felix: Mapping[str, object]) -> int | None:
    """Sum observed felix error metrics. None when felix metrics are unavailable."""
    if not felix.get("available"):
        return None
    metrics = felix.get("metrics")
    if not isinstance(metrics, Mapping):
        return 0
    error_keys = [key for key in metrics if "error" in str(key).lower()]
    if not error_keys:
        return 0
    total = 0.0
    for key in error_keys:
        try:
            total += float(metrics[key])
        except (TypeError, ValueError):
            continue
    return int(None)

mutants_x__felix_error_total__mutmut['_mutmut_orig'] = x__felix_error_total__mutmut_orig # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_1'] = x__felix_error_total__mutmut_1 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_2'] = x__felix_error_total__mutmut_2 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_3'] = x__felix_error_total__mutmut_3 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_4'] = x__felix_error_total__mutmut_4 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_5'] = x__felix_error_total__mutmut_5 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_6'] = x__felix_error_total__mutmut_6 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_7'] = x__felix_error_total__mutmut_7 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_8'] = x__felix_error_total__mutmut_8 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_9'] = x__felix_error_total__mutmut_9 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_10'] = x__felix_error_total__mutmut_10 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_11'] = x__felix_error_total__mutmut_11 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_12'] = x__felix_error_total__mutmut_12 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_13'] = x__felix_error_total__mutmut_13 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_14'] = x__felix_error_total__mutmut_14 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_15'] = x__felix_error_total__mutmut_15 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_16'] = x__felix_error_total__mutmut_16 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_17'] = x__felix_error_total__mutmut_17 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_18'] = x__felix_error_total__mutmut_18 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_19'] = x__felix_error_total__mutmut_19 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_20'] = x__felix_error_total__mutmut_20 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_21'] = x__felix_error_total__mutmut_21 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_22'] = x__felix_error_total__mutmut_22 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_23'] = x__felix_error_total__mutmut_23 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_24'] = x__felix_error_total__mutmut_24 # type: ignore # mutmut generated
mutants_x__felix_error_total__mutmut['x__felix_error_total__mutmut_25'] = x__felix_error_total__mutmut_25 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__connectivity_status__mutmut)
def _connectivity_status(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_orig(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_1(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_2(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get(None):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_3(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("XXavailableXX"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_4(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("AVAILABLE"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_5(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = None
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_6(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get(None)
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_7(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("XXstatusXX")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_8(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("STATUS")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_9(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is not None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_10(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get(None) in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_11(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("XXstatusXX") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_12(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("STATUS") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_13(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") not in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_14(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("XXhealthyXX", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_15(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("HEALTHY", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_16(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "XXdegradedXX"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_17(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "DEGRADED"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_18(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(None)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_19(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "XXdegradedXX" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_20(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "DEGRADED" if not connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_21(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if connectivity.get("active_endpoint_agents") else "healthy"


def x__connectivity_status__mutmut_22(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get(None) else "healthy"


def x__connectivity_status__mutmut_23(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("XXactive_endpoint_agentsXX") else "healthy"


def x__connectivity_status__mutmut_24(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("ACTIVE_ENDPOINT_AGENTS") else "healthy"


def x__connectivity_status__mutmut_25(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "XXhealthyXX"


def x__connectivity_status__mutmut_26(connectivity: Mapping[str, object]) -> str | None:
    """Return the probe status string, honouring availability."""
    if not connectivity.get("available"):
        return None
    status = connectivity.get("status")
    if status is None:
        return None
    if connectivity.get("status") in ("healthy", "degraded"):
        return str(status)
    return "degraded" if not connectivity.get("active_endpoint_agents") else "HEALTHY"

mutants_x__connectivity_status__mutmut['_mutmut_orig'] = x__connectivity_status__mutmut_orig # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_1'] = x__connectivity_status__mutmut_1 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_2'] = x__connectivity_status__mutmut_2 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_3'] = x__connectivity_status__mutmut_3 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_4'] = x__connectivity_status__mutmut_4 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_5'] = x__connectivity_status__mutmut_5 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_6'] = x__connectivity_status__mutmut_6 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_7'] = x__connectivity_status__mutmut_7 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_8'] = x__connectivity_status__mutmut_8 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_9'] = x__connectivity_status__mutmut_9 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_10'] = x__connectivity_status__mutmut_10 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_11'] = x__connectivity_status__mutmut_11 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_12'] = x__connectivity_status__mutmut_12 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_13'] = x__connectivity_status__mutmut_13 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_14'] = x__connectivity_status__mutmut_14 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_15'] = x__connectivity_status__mutmut_15 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_16'] = x__connectivity_status__mutmut_16 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_17'] = x__connectivity_status__mutmut_17 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_18'] = x__connectivity_status__mutmut_18 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_19'] = x__connectivity_status__mutmut_19 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_20'] = x__connectivity_status__mutmut_20 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_21'] = x__connectivity_status__mutmut_21 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_22'] = x__connectivity_status__mutmut_22 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_23'] = x__connectivity_status__mutmut_23 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_24'] = x__connectivity_status__mutmut_24 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_25'] = x__connectivity_status__mutmut_25 # type: ignore # mutmut generated
mutants_x__connectivity_status__mutmut['x__connectivity_status__mutmut_26'] = x__connectivity_status__mutmut_26 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compose_degraded_summary__mutmut)
def _compose_degraded_summary(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_orig(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_1(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = None
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_2(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(None)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_3(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 or ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_4(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total >= 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_5(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 1 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_6(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready <= total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_7(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(None)
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_8(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total != 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_9(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 1:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_10(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append(None)
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_11(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("XX0 calico-node agents detectedXX")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_12(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 CALICO-NODE AGENTS DETECTED")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_13(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None or felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_14(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_15(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors >= 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_16(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 1:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_17(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(None)
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_18(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status != "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_19(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "XXdegradedXX":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_20(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "DEGRADED":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_21(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append(None)
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_22(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("XXdataplane connectivity degradedXX")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_23(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("DATAPLANE CONNECTIVITY DEGRADED")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_24(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if parts:
        return "Calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_25(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "XXCalico datapath degradedXX"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_26(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "calico datapath degraded"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_27(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "CALICO DATAPATH DEGRADED"
    return "; ".join(parts)


def x__compose_degraded_summary__mutmut_28(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "; ".join(None)


def x__compose_degraded_summary__mutmut_29(
    *,
    ready: int,
    total: int,
    agent_summary: str | None,
    felix_errors: int | None,
    connectivity_status: str | None,
) -> str:
    """Human-readable degradation reasons (never fabricated)."""
    parts: list[str] = []
    if agent_summary:
        parts.append(agent_summary)
    elif total > 0 and ready < total:
        parts.append(f"{ready}/{total} calico-node agents ready")
    elif total == 0:
        parts.append("0 calico-node agents detected")
    if felix_errors is not None and felix_errors > 0:
        parts.append(f"{felix_errors} felix dataplane errors")
    if connectivity_status == "degraded":
        parts.append("dataplane connectivity degraded")
    if not parts:
        return "Calico datapath degraded"
    return "XX; XX".join(parts)

mutants_x__compose_degraded_summary__mutmut['_mutmut_orig'] = x__compose_degraded_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_1'] = x__compose_degraded_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_2'] = x__compose_degraded_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_3'] = x__compose_degraded_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_4'] = x__compose_degraded_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_5'] = x__compose_degraded_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_6'] = x__compose_degraded_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_7'] = x__compose_degraded_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_8'] = x__compose_degraded_summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_9'] = x__compose_degraded_summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_10'] = x__compose_degraded_summary__mutmut_10 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_11'] = x__compose_degraded_summary__mutmut_11 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_12'] = x__compose_degraded_summary__mutmut_12 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_13'] = x__compose_degraded_summary__mutmut_13 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_14'] = x__compose_degraded_summary__mutmut_14 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_15'] = x__compose_degraded_summary__mutmut_15 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_16'] = x__compose_degraded_summary__mutmut_16 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_17'] = x__compose_degraded_summary__mutmut_17 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_18'] = x__compose_degraded_summary__mutmut_18 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_19'] = x__compose_degraded_summary__mutmut_19 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_20'] = x__compose_degraded_summary__mutmut_20 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_21'] = x__compose_degraded_summary__mutmut_21 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_22'] = x__compose_degraded_summary__mutmut_22 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_23'] = x__compose_degraded_summary__mutmut_23 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_24'] = x__compose_degraded_summary__mutmut_24 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_25'] = x__compose_degraded_summary__mutmut_25 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_26'] = x__compose_degraded_summary__mutmut_26 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_27'] = x__compose_degraded_summary__mutmut_27 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_28'] = x__compose_degraded_summary__mutmut_28 # type: ignore # mutmut generated
mutants_x__compose_degraded_summary__mutmut['x__compose_degraded_summary__mutmut_29'] = x__compose_degraded_summary__mutmut_29 # type: ignore # mutmut generated
