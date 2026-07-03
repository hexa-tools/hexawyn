from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.resource_search_port import (
    MatchedResourceRaw,
    ResourceSearchPort,
)
from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_command import (
    SearchResourcesByLabelsCommand,
)
from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_response import (
    MatchedResourceDict,
    NamespaceGroupDict,
    SearchResourcesByLabelsResponse,
)
from hexawyn.application.ports.driving.search_resources_by_labels.search_resources_by_labels_service_port import (
    SearchResourcesByLabelsServicePort,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.label_search import (
    LabelSearchRequest,
    LabelSearchResult,
    MatchedResourceResult,
    NamespaceGroup,
)
from hexawyn.domain.services.label_search.search import search_resources_by_labels


class SearchResourcesByLabelsService(SearchResourcesByLabelsServicePort):
    def __init__(self, port: ResourceSearchPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port

    def search(self, command: SearchResourcesByLabelsCommand) -> SearchResourcesByLabelsResponse:
        if command.namespace is not None:
            self._validate_namespace_exists(command.namespace)

        raw_matches = self._fetch_all(command)

        request = LabelSearchRequest(
            label_selector=command.label_selector,
            resource_types=command.resource_types,
            namespace=command.namespace,
        )
        result = search_resources_by_labels(request, raw_matches)
        return _to_response(result)

    def _validate_namespace_exists(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )

    def _fetch_all(self, command: SearchResourcesByLabelsCommand) -> list[MatchedResourceRaw]:
        raw_matches: list[MatchedResourceRaw] = []
        for resource_type in command.resource_types:
            raw_matches.extend(self._search_one(resource_type, command))
        return raw_matches

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


def _to_group_dict(group: NamespaceGroup) -> NamespaceGroupDict:
    return NamespaceGroupDict(
        namespace=group.namespace,
        resources=[_to_resource_dict(resource) for resource in group.resources],
    )


def _to_resource_dict(resource: MatchedResourceResult) -> MatchedResourceDict:
    return MatchedResourceDict(
        name=resource.name,
        namespace=resource.namespace,
        kind=resource.kind,
        node=resource.node,
        phase=resource.phase,
        ready=resource.ready,
        is_healthy=resource.is_healthy,
        labels=resource.labels,
    )
