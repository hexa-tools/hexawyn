from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_overview_port import NamespaceOverviewPort
from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.command import (
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.response import (
    ConservativeNamespaceOverviewResponse,
    NamespaceCountsDict,
    UnhealthyResourceDict,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_overview import (
    NamespaceOverviewReport,
    NamespaceOverviewRequest,
    UnhealthyResource,
)
from hexawyn.domain.services.namespace_overview.overview import build_namespace_overview


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut: MutantDict = {}  # type: ignore
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut: MutantDict = {}  # type: ignore


class ConservativeNamespaceOverviewUseCase:
    @_mutmut_mutated(mutants_xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut)
    def __init__(self, port: NamespaceOverviewPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port
    def xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut_orig(self, port: NamespaceOverviewPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port
    def xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut_1(self, port: NamespaceOverviewPort, k8s_port: K8sPort) -> None:
        self._port = None
        self._k8s_port = k8s_port
    def xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut_2(self, port: NamespaceOverviewPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = None

    @_mutmut_mutated(mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut)
    def get_overview(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=command.max_tokens
        )
        report = build_namespace_overview(request, raw_data)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_orig(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=command.max_tokens
        )
        report = build_namespace_overview(request, raw_data)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_1(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(None)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=command.max_tokens
        )
        report = build_namespace_overview(request, raw_data)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_2(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = None
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=command.max_tokens
        )
        report = build_namespace_overview(request, raw_data)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_3(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(None)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=command.max_tokens
        )
        report = build_namespace_overview(request, raw_data)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_4(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = None
        report = build_namespace_overview(request, raw_data)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_5(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=None, max_tokens=command.max_tokens
        )
        report = build_namespace_overview(request, raw_data)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_6(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=None
        )
        report = build_namespace_overview(request, raw_data)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_7(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            max_tokens=command.max_tokens
        )
        report = build_namespace_overview(request, raw_data)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_8(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, )
        report = build_namespace_overview(request, raw_data)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_9(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=command.max_tokens
        )
        report = None
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_10(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=command.max_tokens
        )
        report = build_namespace_overview(None, raw_data)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_11(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=command.max_tokens
        )
        report = build_namespace_overview(request, None)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_12(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=command.max_tokens
        )
        report = build_namespace_overview(raw_data)
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_13(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=command.max_tokens
        )
        report = build_namespace_overview(request, )
        return _to_response(report)

    def xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_14(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=command.max_tokens
        )
        report = build_namespace_overview(request, raw_data)
        return _to_response(None)

    @_mutmut_mutated(mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut)
    def _validate_namespace_exists(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_orig(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_1(self, namespace: str) -> None:
        namespaces = None
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_2(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_3(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(None):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_4(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["XXnameXX"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_5(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["NAME"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_6(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] != namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_7(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                None, context={"namespace": namespace}
            )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_8(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context=None
            )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_9(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                context={"namespace": namespace}
            )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_10(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_11(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"XXnamespaceXX": namespace}
            )

    def xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_12(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"NAMESPACE": namespace}
            )

mutants_xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut['_mutmut_orig'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut['xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut_1'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut['xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut_2'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['_mutmut_orig'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_1'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_2'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_3'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_4'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_4 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_5'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_5 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_6'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_6 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_7'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_7 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_8'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_8 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_9'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_9 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_10'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_10 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_11'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_11 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_12'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_12 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_13'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_13 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut['xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_14'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁget_overview__mutmut_14 # type: ignore # mutmut generated

mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['_mutmut_orig'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_1'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_2'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_3'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_4'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_5'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_6'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_7'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_8'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_9'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_10'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_11'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut['xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_12'] = ConservativeNamespaceOverviewUseCase.xǁConservativeNamespaceOverviewUseCaseǁ_validate_namespace_exists__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_orig(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_1(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=None,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_2(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=None,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_3(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=None,
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_4(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=None,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_5(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=None,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_6(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=None,
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_7(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=None,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_8(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=None,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_9(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=None,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_10(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=None,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_11(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=None,
        summary=report.summary,
    )


def x__to_response__mutmut_12(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=None,
    )


def x__to_response__mutmut_13(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_14(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_15(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_16(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_17(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_18(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_19(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_20(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_21(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_22(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_23(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        summary=report.summary,
    )


def x__to_response__mutmut_24(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        )


def x__to_response__mutmut_25(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=None,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_26(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=None,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_27(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=None,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_28(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=None,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_29(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=None,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_30(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=None,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_31(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_32(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_33(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_34(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_35(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_36(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )


def x__to_response__mutmut_37(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(  # type: ignore
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(None) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,  # type: ignore
        has_more_unhealthy=report.has_more_unhealthy,  # type: ignore
        remaining_unhealthy_count=report.remaining_unhealthy_count,  # type: ignore
        estimated_tokens=report.estimated_tokens,  # type: ignore
        is_empty=report.is_empty,
        summary=report.summary,
    )

mutants_x__to_response__mutmut['_mutmut_orig'] = x__to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_1'] = x__to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_2'] = x__to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_3'] = x__to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_4'] = x__to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_5'] = x__to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_6'] = x__to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_7'] = x__to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_8'] = x__to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_9'] = x__to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_10'] = x__to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_11'] = x__to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_12'] = x__to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_13'] = x__to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_14'] = x__to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_15'] = x__to_response__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_16'] = x__to_response__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_17'] = x__to_response__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_18'] = x__to_response__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_19'] = x__to_response__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_20'] = x__to_response__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_21'] = x__to_response__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_22'] = x__to_response__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_23'] = x__to_response__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_24'] = x__to_response__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_25'] = x__to_response__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_26'] = x__to_response__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_27'] = x__to_response__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_28'] = x__to_response__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_29'] = x__to_response__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_30'] = x__to_response__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_31'] = x__to_response__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_32'] = x__to_response__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_33'] = x__to_response__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_34'] = x__to_response__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_35'] = x__to_response__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_36'] = x__to_response__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_37'] = x__to_response__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_resource_dict__mutmut)
def _to_resource_dict(resource: UnhealthyResource) -> UnhealthyResourceDict:
    return UnhealthyResourceDict(name=resource.name, kind=resource.kind, reason=resource.reason)  # type: ignore


def x__to_resource_dict__mutmut_orig(resource: UnhealthyResource) -> UnhealthyResourceDict:
    return UnhealthyResourceDict(name=resource.name, kind=resource.kind, reason=resource.reason)  # type: ignore


def x__to_resource_dict__mutmut_1(resource: UnhealthyResource) -> UnhealthyResourceDict:
    return UnhealthyResourceDict(name=None, kind=resource.kind, reason=resource.reason)  # type: ignore


def x__to_resource_dict__mutmut_2(resource: UnhealthyResource) -> UnhealthyResourceDict:
    return UnhealthyResourceDict(name=resource.name, kind=None, reason=resource.reason)  # type: ignore


def x__to_resource_dict__mutmut_3(resource: UnhealthyResource) -> UnhealthyResourceDict:
    return UnhealthyResourceDict(name=resource.name, kind=resource.kind, reason=None)  # type: ignore


def x__to_resource_dict__mutmut_4(resource: UnhealthyResource) -> UnhealthyResourceDict:
    return UnhealthyResourceDict(kind=resource.kind, reason=resource.reason)  # type: ignore


def x__to_resource_dict__mutmut_5(resource: UnhealthyResource) -> UnhealthyResourceDict:
    return UnhealthyResourceDict(name=resource.name, reason=resource.reason)  # type: ignore


def x__to_resource_dict__mutmut_6(resource: UnhealthyResource) -> UnhealthyResourceDict:
    return UnhealthyResourceDict(name=resource.name, kind=resource.kind, )  # type: ignore

mutants_x__to_resource_dict__mutmut['_mutmut_orig'] = x__to_resource_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_1'] = x__to_resource_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_2'] = x__to_resource_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_3'] = x__to_resource_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_4'] = x__to_resource_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_5'] = x__to_resource_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_6'] = x__to_resource_dict__mutmut_6 # type: ignore # mutmut generated
