from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.resource_search_port import (
    MatchedResourceRaw,
    ResourceSearchPort,
)
from hexawyn.application.use_case.cluster.search_resources_by_labels.command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.use_case.cluster.search_resources_by_labels.response import (
    MatchedResourceDict,
    NamespaceGroupDict,
    SearchResourcesByLabelsResponse,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.label_search import (
    LabelSearchRequest,
    LabelSearchResult,
    MatchedResourceResult,
    NamespaceGroup,
)
from hexawyn.domain.services.label_search.search import search_resources_by_labels


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut: MutantDict = {}  # type: ignore


class SearchResourcesByLabelsUseCase:
    @_mutmut_mutated(mutants_xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut)
    def __init__(self, port: ResourceSearchPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port
    def xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut_orig(self, port: ResourceSearchPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port
    def xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut_1(self, port: ResourceSearchPort, k8s_port: K8sPort) -> None:
        self._port = None
        self._k8s_port = k8s_port
    def xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut_2(self, port: ResourceSearchPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = None

    @_mutmut_mutated(mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut)
    def execute(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_orig(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_1(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_2(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(None)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_3(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = None

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_4(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(None)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_5(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = None
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_6(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=None,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_7(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=None,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_8(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=None,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_9(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_10(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_11(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_12(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = None
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_13(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(None, raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_14(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, None)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_15(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(raw_matches)
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_16(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, )
        return _to_response(result)

    def xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_17(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,  # type: ignore
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(None)

    @_mutmut_mutated(mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut)
    def _validate_namespace_exists(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_orig(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_1(self, namespace: str) -> None:
        namespaces = None
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_2(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_3(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(None):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_4(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["XXnameXX"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_5(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["NAME"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_6(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] != namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_7(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                None, context={"namespace": namespace}
            )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_8(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context=None
            )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_9(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                context={"namespace": namespace}
            )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_10(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_11(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"XXnamespaceXX": namespace}
            )

    def xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_12(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"NAMESPACE": namespace}
            )

    @_mutmut_mutated(mutants_xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut)
    def _fetch_all(self, command: SearchResourcesByLabelsCommand) -> list[MatchedResourceRaw]:
        raw_matches: list[MatchedResourceRaw] = []
        for resource_type in command.resource_types:
            raw_matches.extend(self._search_one(resource_type, command))
        return raw_matches

    def xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_orig(self, command: SearchResourcesByLabelsCommand) -> list[MatchedResourceRaw]:
        raw_matches: list[MatchedResourceRaw] = []
        for resource_type in command.resource_types:
            raw_matches.extend(self._search_one(resource_type, command))
        return raw_matches

    def xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_1(self, command: SearchResourcesByLabelsCommand) -> list[MatchedResourceRaw]:
        raw_matches: list[MatchedResourceRaw] = None
        for resource_type in command.resource_types:
            raw_matches.extend(self._search_one(resource_type, command))
        return raw_matches

    def xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_2(self, command: SearchResourcesByLabelsCommand) -> list[MatchedResourceRaw]:
        raw_matches: list[MatchedResourceRaw] = []
        for resource_type in command.resource_types:
            raw_matches.extend(None)
        return raw_matches

    def xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_3(self, command: SearchResourcesByLabelsCommand) -> list[MatchedResourceRaw]:
        raw_matches: list[MatchedResourceRaw] = []
        for resource_type in command.resource_types:
            raw_matches.extend(self._search_one(None, command))
        return raw_matches

    def xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_4(self, command: SearchResourcesByLabelsCommand) -> list[MatchedResourceRaw]:
        raw_matches: list[MatchedResourceRaw] = []
        for resource_type in command.resource_types:
            raw_matches.extend(self._search_one(resource_type, None))
        return raw_matches

    def xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_5(self, command: SearchResourcesByLabelsCommand) -> list[MatchedResourceRaw]:
        raw_matches: list[MatchedResourceRaw] = []
        for resource_type in command.resource_types:
            raw_matches.extend(self._search_one(command))
        return raw_matches

    def xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_6(self, command: SearchResourcesByLabelsCommand) -> list[MatchedResourceRaw]:
        raw_matches: list[MatchedResourceRaw] = []
        for resource_type in command.resource_types:
            raw_matches.extend(self._search_one(resource_type, ))
        return raw_matches

    @_mutmut_mutated(mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut)
    def _search_one(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_orig(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_1(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = None
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_2(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = None
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_3(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type != "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_4(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "XXpodsXX":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_5(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "PODS":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_6(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=None, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_7(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=None)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_8(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_9(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, )
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_10(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type != "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_11(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "XXdeploymentsXX":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_12(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "DEPLOYMENTS":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_13(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=None, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_14(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=None)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_15(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_16(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, )
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_17(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type != "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_18(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "XXservicesXX":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_19(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "SERVICES":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_20(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=None, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_21(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=None)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_22(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_23(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, )
        return self._port.search_configmaps(label_selector=selector, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_24(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=None, namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_25(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, namespace=None)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_26(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(namespace=namespace)

    def xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_27(
        self, resource_type: str, command: SearchResourcesByLabelsCommand
    ) -> list[MatchedResourceRaw]:
        selector = command.label_selector
        namespace = command.namespace
        if resource_type == "pods":
            return self._port.search_pods(label_selector=selector, namespace=namespace)
        if resource_type == "deployments":
            return self._port.search_deployments(label_selector=selector, namespace=namespace)
        if resource_type == "services":
            return self._port.search_services(label_selector=selector, namespace=namespace)
        return self._port.search_configmaps(label_selector=selector, )

mutants_xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut['_mutmut_orig'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut['xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut_1'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut['xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut_2'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['_mutmut_orig'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_1'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_2'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_3'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_4'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_5'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_6'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_7'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_8'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_9'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_10'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_11'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_12'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_13'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_14'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_15'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_16'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut['xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_17'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated

mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['_mutmut_orig'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_1'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_2'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_3'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_4'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_5'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_6'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_7'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_8'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_9'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_10'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_11'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_12'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_validate_namespace_exists__mutmut_12 # type: ignore # mutmut generated

mutants_xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut['_mutmut_orig'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_1'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_2'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_3'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_4'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_5'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_6'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_fetch_all__mutmut_6 # type: ignore # mutmut generated

mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['_mutmut_orig'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_1'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_2'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_3'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_4'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_5'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_6'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_7'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_8'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_9'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_10'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_11'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_12'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_13'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_14'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_15'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_16'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_17'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_18'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_19'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_20'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_21'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_22'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_23'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_24'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_25'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_26'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_26 # type: ignore # mutmut generated
mutants_xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut['xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_27'] = SearchResourcesByLabelsUseCase.xǁSearchResourcesByLabelsUseCaseǁ_search_one__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
def _to_response(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def x__to_response__mutmut_orig(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def x__to_response__mutmut_1(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=None,
        total_matched=result.total_matched,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def x__to_response__mutmut_2(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=None,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def x__to_response__mutmut_3(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        groups=None,
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def x__to_response__mutmut_4(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=None,
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def x__to_response__mutmut_5(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=result.has_more,
        remaining_count=None,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def x__to_response__mutmut_6(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        no_matches=None,
        summary=result.summary,
    )


def x__to_response__mutmut_7(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        summary=None,
    )


def x__to_response__mutmut_8(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        total_matched=result.total_matched,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def x__to_response__mutmut_9(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def x__to_response__mutmut_10(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def x__to_response__mutmut_11(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        groups=[_to_group_dict(group) for group in result.groups],
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def x__to_response__mutmut_12(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=result.has_more,
        no_matches=result.no_matches,
        summary=result.summary,
    )


def x__to_response__mutmut_13(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        summary=result.summary,
    )


def x__to_response__mutmut_14(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        groups=[_to_group_dict(group) for group in result.groups],
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        )


def x__to_response__mutmut_15(result: LabelSearchResult) -> SearchResourcesByLabelsResponse:
    return SearchResourcesByLabelsResponse(
        label_selector=result.label_selector,
        total_matched=result.total_matched,
        groups=[_to_group_dict(None) for group in result.groups],
        has_more=result.has_more,
        remaining_count=result.remaining_count,
        no_matches=result.no_matches,
        summary=result.summary,
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
mutants_x__to_group_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_group_dict__mutmut)
def _to_group_dict(group: NamespaceGroup) -> NamespaceGroupDict:
    return NamespaceGroupDict(
        namespace=group.namespace,
        resources=[_to_resource_dict(resource) for resource in group.resources],
    )


def x__to_group_dict__mutmut_orig(group: NamespaceGroup) -> NamespaceGroupDict:
    return NamespaceGroupDict(
        namespace=group.namespace,
        resources=[_to_resource_dict(resource) for resource in group.resources],
    )


def x__to_group_dict__mutmut_1(group: NamespaceGroup) -> NamespaceGroupDict:
    return NamespaceGroupDict(
        namespace=None,
        resources=[_to_resource_dict(resource) for resource in group.resources],
    )


def x__to_group_dict__mutmut_2(group: NamespaceGroup) -> NamespaceGroupDict:
    return NamespaceGroupDict(
        namespace=group.namespace,
        resources=None,
    )


def x__to_group_dict__mutmut_3(group: NamespaceGroup) -> NamespaceGroupDict:
    return NamespaceGroupDict(
        resources=[_to_resource_dict(resource) for resource in group.resources],
    )


def x__to_group_dict__mutmut_4(group: NamespaceGroup) -> NamespaceGroupDict:
    return NamespaceGroupDict(
        namespace=group.namespace,
        )


def x__to_group_dict__mutmut_5(group: NamespaceGroup) -> NamespaceGroupDict:
    return NamespaceGroupDict(
        namespace=group.namespace,
        resources=[_to_resource_dict(None) for resource in group.resources],
    )

mutants_x__to_group_dict__mutmut['_mutmut_orig'] = x__to_group_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_group_dict__mutmut['x__to_group_dict__mutmut_1'] = x__to_group_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_group_dict__mutmut['x__to_group_dict__mutmut_2'] = x__to_group_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_group_dict__mutmut['x__to_group_dict__mutmut_3'] = x__to_group_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_group_dict__mutmut['x__to_group_dict__mutmut_4'] = x__to_group_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_group_dict__mutmut['x__to_group_dict__mutmut_5'] = x__to_group_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_resource_dict__mutmut)
def _to_resource_dict(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_orig(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_1(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=None,
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_2(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=None,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_3(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=None,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_4(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        node=None,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_5(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=None,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_6(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=None,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_7(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=None,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_8(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=None,
    )


def x__to_resource_dict__mutmut_9(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_10(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_11(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_12(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_13(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_14(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_15(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        labels=resource.labels,
    )


def x__to_resource_dict__mutmut_16(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(  # type: ignore
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,  # type: ignore
        phase=resource.phase,  # type: ignore
        ready=resource.ready,  # type: ignore
        is_healthy=resource.is_healthy,
        )

mutants_x__to_resource_dict__mutmut['_mutmut_orig'] = x__to_resource_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_1'] = x__to_resource_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_2'] = x__to_resource_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_3'] = x__to_resource_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_4'] = x__to_resource_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_5'] = x__to_resource_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_6'] = x__to_resource_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_7'] = x__to_resource_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_8'] = x__to_resource_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_9'] = x__to_resource_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_10'] = x__to_resource_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_11'] = x__to_resource_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_12'] = x__to_resource_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_13'] = x__to_resource_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_14'] = x__to_resource_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_15'] = x__to_resource_dict__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_resource_dict__mutmut['x__to_resource_dict__mutmut_16'] = x__to_resource_dict__mutmut_16 # type: ignore # mutmut generated
