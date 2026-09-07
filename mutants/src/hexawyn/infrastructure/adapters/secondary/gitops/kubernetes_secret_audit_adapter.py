from __future__ import annotations

from typing import Any

from hexawyn.application.ports.driven.secret_rotation_audit_port import (
    ManagedFieldsEntryRaw,
    SecretRaw,
    SecretReferenceRaw,
    SecretRotationAuditPort,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403
_ROTATION_EXEMPT_ANNOTATION_KEY = "hexawyn.io/secret-rotation-exempt"
_ROTATION_EXEMPT_ANNOTATION_VALUE = "true"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut: MutantDict = {}  # type: ignore


class KubernetesSecretAuditAdapter(SecretRotationAuditPort):
    """Secondary adapter — enumerates every Secret (with managedFields) via
    the K8s API, every Deployment/standalone-Pod reference to a Secret (env,
    envFrom, volumes, projected volumes), and namespace-level rotation
    exemptions."""

    @_mutmut_mutated(mutants_xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut)
    def list_secrets(self) -> list[SecretRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_secret_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_secret_raw(item) for item in result.items]

    def xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_orig(self) -> list[SecretRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_secret_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_secret_raw(item) for item in result.items]

    def xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_1(self) -> list[SecretRaw]:
        from kubernetes import client as k8s

        core_api = None
        try:
            result = core_api.list_secret_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_secret_raw(item) for item in result.items]

    def xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_2(self) -> list[SecretRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = None
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_secret_raw(item) for item in result.items]

    def xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_3(self) -> list[SecretRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_secret_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(None) from exc
        return [_to_secret_raw(item) for item in result.items]

    def xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_4(self) -> list[SecretRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_secret_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [_to_secret_raw(None) for item in result.items]

    @_mutmut_mutated(mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut)
    def list_secret_references(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(_references_from_deployment(deployment))
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(_references_from_pod(pod))
        return references

    def xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_orig(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(_references_from_deployment(deployment))
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(_references_from_pod(pod))
        return references

    def xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_1(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = None
        core_api = k8s.CoreV1Api()
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(_references_from_deployment(deployment))
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(_references_from_pod(pod))
        return references

    def xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_2(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = None
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(_references_from_deployment(deployment))
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(_references_from_pod(pod))
        return references

    def xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_3(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()
        try:
            deployments = None
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(_references_from_deployment(deployment))
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(_references_from_pod(pod))
        return references

    def xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_4(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(_references_from_deployment(deployment))
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(_references_from_pod(pod))
        return references

    def xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_5(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(None) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(_references_from_deployment(deployment))
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(_references_from_pod(pod))
        return references

    def xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_6(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = None
        for deployment in deployments.items:
            references.extend(_references_from_deployment(deployment))
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(_references_from_pod(pod))
        return references

    def xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_7(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(None)
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(_references_from_pod(pod))
        return references

    def xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_8(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(_references_from_deployment(None))
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(_references_from_pod(pod))
        return references

    def xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_9(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(_references_from_deployment(deployment))
        for pod in pods.items:
            if pod.metadata.owner_references:
                references.extend(_references_from_pod(pod))
        return references

    def xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_10(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(_references_from_deployment(deployment))
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(None)
        return references

    def xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_11(self) -> list[SecretReferenceRaw]:
        from kubernetes import client as k8s

        apps_api = k8s.AppsV1Api()
        core_api = k8s.CoreV1Api()
        try:
            deployments = apps_api.list_deployment_for_all_namespaces()
            pods = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        references: list[SecretReferenceRaw] = []
        for deployment in deployments.items:
            references.extend(_references_from_deployment(deployment))
        for pod in pods.items:
            if not pod.metadata.owner_references:
                references.extend(_references_from_pod(None))
        return references

    @_mutmut_mutated(mutants_xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut)
    def get_namespace_rotation_exemptions(self) -> set[str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return {
            namespace.metadata.name
            for namespace in result.items
            if (namespace.metadata.annotations or {}).get(_ROTATION_EXEMPT_ANNOTATION_KEY)
            == _ROTATION_EXEMPT_ANNOTATION_VALUE
        }

    def xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_orig(self) -> set[str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return {
            namespace.metadata.name
            for namespace in result.items
            if (namespace.metadata.annotations or {}).get(_ROTATION_EXEMPT_ANNOTATION_KEY)
            == _ROTATION_EXEMPT_ANNOTATION_VALUE
        }

    def xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_1(self) -> set[str]:
        from kubernetes import client as k8s

        core_api = None
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return {
            namespace.metadata.name
            for namespace in result.items
            if (namespace.metadata.annotations or {}).get(_ROTATION_EXEMPT_ANNOTATION_KEY)
            == _ROTATION_EXEMPT_ANNOTATION_VALUE
        }

    def xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_2(self) -> set[str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        return {
            namespace.metadata.name
            for namespace in result.items
            if (namespace.metadata.annotations or {}).get(_ROTATION_EXEMPT_ANNOTATION_KEY)
            == _ROTATION_EXEMPT_ANNOTATION_VALUE
        }

    def xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_3(self) -> set[str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(None) from exc

        return {
            namespace.metadata.name
            for namespace in result.items
            if (namespace.metadata.annotations or {}).get(_ROTATION_EXEMPT_ANNOTATION_KEY)
            == _ROTATION_EXEMPT_ANNOTATION_VALUE
        }

    def xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_4(self) -> set[str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return {
            namespace.metadata.name
            for namespace in result.items
            if (namespace.metadata.annotations or {}).get(None)
            == _ROTATION_EXEMPT_ANNOTATION_VALUE
        }

    def xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_5(self) -> set[str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return {
            namespace.metadata.name
            for namespace in result.items
            if (namespace.metadata.annotations and {}).get(_ROTATION_EXEMPT_ANNOTATION_KEY)
            == _ROTATION_EXEMPT_ANNOTATION_VALUE
        }

    def xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_6(self) -> set[str]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_namespace()
        except Exception as exc:
            raise _translate_error(exc) from exc

        return {
            namespace.metadata.name
            for namespace in result.items
            if (namespace.metadata.annotations or {}).get(_ROTATION_EXEMPT_ANNOTATION_KEY) != _ROTATION_EXEMPT_ANNOTATION_VALUE
        }

mutants_xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut['_mutmut_orig'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_1'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_2'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_3'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_4'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secrets__mutmut_4 # type: ignore # mutmut generated

mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut['_mutmut_orig'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_1'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_2'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_3'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_4'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_5'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_6'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_7'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_8'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_9'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_10'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut['xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_11'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁlist_secret_references__mutmut_11 # type: ignore # mutmut generated

mutants_xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut['_mutmut_orig'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut['xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_1'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut['xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_2'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut['xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_3'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut['xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_4'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut['xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_5'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut['xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_6'] = KubernetesSecretAuditAdapter.xǁKubernetesSecretAuditAdapterǁget_namespace_rotation_exemptions__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_secret_raw__mutmut)
def _to_secret_raw(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_orig(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_1(item: Any) -> SecretRaw:
    managed_fields = None
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_2(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields and []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_3(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=None,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_4(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=None,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_5(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=None,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_6(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=None,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_7(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=None,
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_8(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=None,
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_9(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=None,
    )


def x__to_secret_raw__mutmut_10(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_11(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_12(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_13(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_14(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_15(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_16(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        )


def x__to_secret_raw__mutmut_17(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted(None),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_18(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data and {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_19(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(None) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations or {},
    )


def x__to_secret_raw__mutmut_20(item: Any) -> SecretRaw:
    managed_fields = item.metadata.managed_fields or []
    return SecretRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        secret_type=item.type,
        data_keys=sorted((item.data or {}).keys()),
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
        creation_timestamp=item.metadata.creation_timestamp.isoformat(),
        annotations=item.metadata.annotations and {},
    )

mutants_x__to_secret_raw__mutmut['_mutmut_orig'] = x__to_secret_raw__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_1'] = x__to_secret_raw__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_2'] = x__to_secret_raw__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_3'] = x__to_secret_raw__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_4'] = x__to_secret_raw__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_5'] = x__to_secret_raw__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_6'] = x__to_secret_raw__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_7'] = x__to_secret_raw__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_8'] = x__to_secret_raw__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_9'] = x__to_secret_raw__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_10'] = x__to_secret_raw__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_11'] = x__to_secret_raw__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_12'] = x__to_secret_raw__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_13'] = x__to_secret_raw__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_14'] = x__to_secret_raw__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_15'] = x__to_secret_raw__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_16'] = x__to_secret_raw__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_17'] = x__to_secret_raw__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_18'] = x__to_secret_raw__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_19'] = x__to_secret_raw__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_secret_raw__mutmut['x__to_secret_raw__mutmut_20'] = x__to_secret_raw__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_managed_fields_entry__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_managed_fields_entry__mutmut)
def _to_managed_fields_entry(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        manager=entry.manager,
        operation=entry.operation,
        time=entry.time.isoformat(),
        fields_v1_raw=fields_v1_raw,
    )


def x__to_managed_fields_entry__mutmut_orig(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        manager=entry.manager,
        operation=entry.operation,
        time=entry.time.isoformat(),
        fields_v1_raw=fields_v1_raw,
    )


def x__to_managed_fields_entry__mutmut_1(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = None
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        manager=entry.manager,
        operation=entry.operation,
        time=entry.time.isoformat(),
        fields_v1_raw=fields_v1_raw,
    )


def x__to_managed_fields_entry__mutmut_2(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = None
    return ManagedFieldsEntryRaw(
        manager=entry.manager,
        operation=entry.operation,
        time=entry.time.isoformat(),
        fields_v1_raw=fields_v1_raw,
    )


def x__to_managed_fields_entry__mutmut_3(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        manager=None,
        operation=entry.operation,
        time=entry.time.isoformat(),
        fields_v1_raw=fields_v1_raw,
    )


def x__to_managed_fields_entry__mutmut_4(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        manager=entry.manager,
        operation=None,
        time=entry.time.isoformat(),
        fields_v1_raw=fields_v1_raw,
    )


def x__to_managed_fields_entry__mutmut_5(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        manager=entry.manager,
        operation=entry.operation,
        time=None,
        fields_v1_raw=fields_v1_raw,
    )


def x__to_managed_fields_entry__mutmut_6(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        manager=entry.manager,
        operation=entry.operation,
        time=entry.time.isoformat(),
        fields_v1_raw=None,
    )


def x__to_managed_fields_entry__mutmut_7(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        operation=entry.operation,
        time=entry.time.isoformat(),
        fields_v1_raw=fields_v1_raw,
    )


def x__to_managed_fields_entry__mutmut_8(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        manager=entry.manager,
        time=entry.time.isoformat(),
        fields_v1_raw=fields_v1_raw,
    )


def x__to_managed_fields_entry__mutmut_9(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        manager=entry.manager,
        operation=entry.operation,
        fields_v1_raw=fields_v1_raw,
    )


def x__to_managed_fields_entry__mutmut_10(entry: Any) -> ManagedFieldsEntryRaw:
    fields_v1 = entry.fields_v1
    fields_v1_raw = fields_v1 if isinstance(fields_v1, dict) else {}
    return ManagedFieldsEntryRaw(
        manager=entry.manager,
        operation=entry.operation,
        time=entry.time.isoformat(),
        )

mutants_x__to_managed_fields_entry__mutmut['_mutmut_orig'] = x__to_managed_fields_entry__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_managed_fields_entry__mutmut['x__to_managed_fields_entry__mutmut_1'] = x__to_managed_fields_entry__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_managed_fields_entry__mutmut['x__to_managed_fields_entry__mutmut_2'] = x__to_managed_fields_entry__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_managed_fields_entry__mutmut['x__to_managed_fields_entry__mutmut_3'] = x__to_managed_fields_entry__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_managed_fields_entry__mutmut['x__to_managed_fields_entry__mutmut_4'] = x__to_managed_fields_entry__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_managed_fields_entry__mutmut['x__to_managed_fields_entry__mutmut_5'] = x__to_managed_fields_entry__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_managed_fields_entry__mutmut['x__to_managed_fields_entry__mutmut_6'] = x__to_managed_fields_entry__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_managed_fields_entry__mutmut['x__to_managed_fields_entry__mutmut_7'] = x__to_managed_fields_entry__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_managed_fields_entry__mutmut['x__to_managed_fields_entry__mutmut_8'] = x__to_managed_fields_entry__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_managed_fields_entry__mutmut['x__to_managed_fields_entry__mutmut_9'] = x__to_managed_fields_entry__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_managed_fields_entry__mutmut['x__to_managed_fields_entry__mutmut_10'] = x__to_managed_fields_entry__mutmut_10 # type: ignore # mutmut generated
mutants_x__references_from_deployment__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__references_from_deployment__mutmut)
def _references_from_deployment(deployment: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(deployment.spec.template.spec)
    return [
        SecretReferenceRaw(
            secret_name=name,
            namespace=deployment.metadata.namespace,
            workload_name=deployment.metadata.name,
        )
        for name in secret_names
    ]


def x__references_from_deployment__mutmut_orig(deployment: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(deployment.spec.template.spec)
    return [
        SecretReferenceRaw(
            secret_name=name,
            namespace=deployment.metadata.namespace,
            workload_name=deployment.metadata.name,
        )
        for name in secret_names
    ]


def x__references_from_deployment__mutmut_1(deployment: Any) -> list[SecretReferenceRaw]:
    secret_names = None
    return [
        SecretReferenceRaw(
            secret_name=name,
            namespace=deployment.metadata.namespace,
            workload_name=deployment.metadata.name,
        )
        for name in secret_names
    ]


def x__references_from_deployment__mutmut_2(deployment: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(None)
    return [
        SecretReferenceRaw(
            secret_name=name,
            namespace=deployment.metadata.namespace,
            workload_name=deployment.metadata.name,
        )
        for name in secret_names
    ]


def x__references_from_deployment__mutmut_3(deployment: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(deployment.spec.template.spec)
    return [
        SecretReferenceRaw(
            secret_name=None,
            namespace=deployment.metadata.namespace,
            workload_name=deployment.metadata.name,
        )
        for name in secret_names
    ]


def x__references_from_deployment__mutmut_4(deployment: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(deployment.spec.template.spec)
    return [
        SecretReferenceRaw(
            secret_name=name,
            namespace=None,
            workload_name=deployment.metadata.name,
        )
        for name in secret_names
    ]


def x__references_from_deployment__mutmut_5(deployment: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(deployment.spec.template.spec)
    return [
        SecretReferenceRaw(
            secret_name=name,
            namespace=deployment.metadata.namespace,
            workload_name=None,
        )
        for name in secret_names
    ]


def x__references_from_deployment__mutmut_6(deployment: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(deployment.spec.template.spec)
    return [
        SecretReferenceRaw(
            namespace=deployment.metadata.namespace,
            workload_name=deployment.metadata.name,
        )
        for name in secret_names
    ]


def x__references_from_deployment__mutmut_7(deployment: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(deployment.spec.template.spec)
    return [
        SecretReferenceRaw(
            secret_name=name,
            workload_name=deployment.metadata.name,
        )
        for name in secret_names
    ]


def x__references_from_deployment__mutmut_8(deployment: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(deployment.spec.template.spec)
    return [
        SecretReferenceRaw(
            secret_name=name,
            namespace=deployment.metadata.namespace,
            )
        for name in secret_names
    ]

mutants_x__references_from_deployment__mutmut['_mutmut_orig'] = x__references_from_deployment__mutmut_orig # type: ignore # mutmut generated
mutants_x__references_from_deployment__mutmut['x__references_from_deployment__mutmut_1'] = x__references_from_deployment__mutmut_1 # type: ignore # mutmut generated
mutants_x__references_from_deployment__mutmut['x__references_from_deployment__mutmut_2'] = x__references_from_deployment__mutmut_2 # type: ignore # mutmut generated
mutants_x__references_from_deployment__mutmut['x__references_from_deployment__mutmut_3'] = x__references_from_deployment__mutmut_3 # type: ignore # mutmut generated
mutants_x__references_from_deployment__mutmut['x__references_from_deployment__mutmut_4'] = x__references_from_deployment__mutmut_4 # type: ignore # mutmut generated
mutants_x__references_from_deployment__mutmut['x__references_from_deployment__mutmut_5'] = x__references_from_deployment__mutmut_5 # type: ignore # mutmut generated
mutants_x__references_from_deployment__mutmut['x__references_from_deployment__mutmut_6'] = x__references_from_deployment__mutmut_6 # type: ignore # mutmut generated
mutants_x__references_from_deployment__mutmut['x__references_from_deployment__mutmut_7'] = x__references_from_deployment__mutmut_7 # type: ignore # mutmut generated
mutants_x__references_from_deployment__mutmut['x__references_from_deployment__mutmut_8'] = x__references_from_deployment__mutmut_8 # type: ignore # mutmut generated
mutants_x__references_from_pod__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__references_from_pod__mutmut)
def _references_from_pod(pod: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(pod.spec)
    return [
        SecretReferenceRaw(
            secret_name=name, namespace=pod.metadata.namespace, workload_name=pod.metadata.name
        )
        for name in secret_names
    ]


def x__references_from_pod__mutmut_orig(pod: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(pod.spec)
    return [
        SecretReferenceRaw(
            secret_name=name, namespace=pod.metadata.namespace, workload_name=pod.metadata.name
        )
        for name in secret_names
    ]


def x__references_from_pod__mutmut_1(pod: Any) -> list[SecretReferenceRaw]:
    secret_names = None
    return [
        SecretReferenceRaw(
            secret_name=name, namespace=pod.metadata.namespace, workload_name=pod.metadata.name
        )
        for name in secret_names
    ]


def x__references_from_pod__mutmut_2(pod: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(None)
    return [
        SecretReferenceRaw(
            secret_name=name, namespace=pod.metadata.namespace, workload_name=pod.metadata.name
        )
        for name in secret_names
    ]


def x__references_from_pod__mutmut_3(pod: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(pod.spec)
    return [
        SecretReferenceRaw(
            secret_name=None, namespace=pod.metadata.namespace, workload_name=pod.metadata.name
        )
        for name in secret_names
    ]


def x__references_from_pod__mutmut_4(pod: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(pod.spec)
    return [
        SecretReferenceRaw(
            secret_name=name, namespace=None, workload_name=pod.metadata.name
        )
        for name in secret_names
    ]


def x__references_from_pod__mutmut_5(pod: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(pod.spec)
    return [
        SecretReferenceRaw(
            secret_name=name, namespace=pod.metadata.namespace, workload_name=None
        )
        for name in secret_names
    ]


def x__references_from_pod__mutmut_6(pod: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(pod.spec)
    return [
        SecretReferenceRaw(
            namespace=pod.metadata.namespace, workload_name=pod.metadata.name
        )
        for name in secret_names
    ]


def x__references_from_pod__mutmut_7(pod: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(pod.spec)
    return [
        SecretReferenceRaw(
            secret_name=name, workload_name=pod.metadata.name
        )
        for name in secret_names
    ]


def x__references_from_pod__mutmut_8(pod: Any) -> list[SecretReferenceRaw]:
    secret_names = _extract_secret_names(pod.spec)
    return [
        SecretReferenceRaw(
            secret_name=name, namespace=pod.metadata.namespace, )
        for name in secret_names
    ]

mutants_x__references_from_pod__mutmut['_mutmut_orig'] = x__references_from_pod__mutmut_orig # type: ignore # mutmut generated
mutants_x__references_from_pod__mutmut['x__references_from_pod__mutmut_1'] = x__references_from_pod__mutmut_1 # type: ignore # mutmut generated
mutants_x__references_from_pod__mutmut['x__references_from_pod__mutmut_2'] = x__references_from_pod__mutmut_2 # type: ignore # mutmut generated
mutants_x__references_from_pod__mutmut['x__references_from_pod__mutmut_3'] = x__references_from_pod__mutmut_3 # type: ignore # mutmut generated
mutants_x__references_from_pod__mutmut['x__references_from_pod__mutmut_4'] = x__references_from_pod__mutmut_4 # type: ignore # mutmut generated
mutants_x__references_from_pod__mutmut['x__references_from_pod__mutmut_5'] = x__references_from_pod__mutmut_5 # type: ignore # mutmut generated
mutants_x__references_from_pod__mutmut['x__references_from_pod__mutmut_6'] = x__references_from_pod__mutmut_6 # type: ignore # mutmut generated
mutants_x__references_from_pod__mutmut['x__references_from_pod__mutmut_7'] = x__references_from_pod__mutmut_7 # type: ignore # mutmut generated
mutants_x__references_from_pod__mutmut['x__references_from_pod__mutmut_8'] = x__references_from_pod__mutmut_8 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__extract_secret_names__mutmut)
def _extract_secret_names(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_orig(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_1(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = None
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_2(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = None
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_3(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) - list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_4(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(None) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_5(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers and []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_6(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(None)
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_7(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers and [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_8(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from and []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_9(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_10(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(None)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_11(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env and []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_12(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None or env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_13(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_14(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_15(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(None)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_16(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes and []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_17(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_18(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(None)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_19(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_20(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources and []:
                if source.secret is not None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_21(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is None:
                    names.add(source.secret.name)
    return names


def x__extract_secret_names__mutmut_22(pod_spec: Any) -> set[str]:  # noqa: C901
    names: set[str] = set()
    containers = list(pod_spec.containers or []) + list(pod_spec.init_containers or [])
    for container in containers:
        for env_from in container.env_from or []:
            if env_from.secret_ref is not None:
                names.add(env_from.secret_ref.name)
        for env in container.env or []:
            if env.value_from is not None and env.value_from.secret_key_ref is not None:
                names.add(env.value_from.secret_key_ref.name)
    for volume in pod_spec.volumes or []:
        if volume.secret is not None:
            names.add(volume.secret.secret_name)
        if volume.projected is not None:
            for source in volume.projected.sources or []:
                if source.secret is not None:
                    names.add(None)
    return names

mutants_x__extract_secret_names__mutmut['_mutmut_orig'] = x__extract_secret_names__mutmut_orig # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_1'] = x__extract_secret_names__mutmut_1 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_2'] = x__extract_secret_names__mutmut_2 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_3'] = x__extract_secret_names__mutmut_3 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_4'] = x__extract_secret_names__mutmut_4 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_5'] = x__extract_secret_names__mutmut_5 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_6'] = x__extract_secret_names__mutmut_6 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_7'] = x__extract_secret_names__mutmut_7 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_8'] = x__extract_secret_names__mutmut_8 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_9'] = x__extract_secret_names__mutmut_9 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_10'] = x__extract_secret_names__mutmut_10 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_11'] = x__extract_secret_names__mutmut_11 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_12'] = x__extract_secret_names__mutmut_12 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_13'] = x__extract_secret_names__mutmut_13 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_14'] = x__extract_secret_names__mutmut_14 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_15'] = x__extract_secret_names__mutmut_15 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_16'] = x__extract_secret_names__mutmut_16 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_17'] = x__extract_secret_names__mutmut_17 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_18'] = x__extract_secret_names__mutmut_18 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_19'] = x__extract_secret_names__mutmut_19 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_20'] = x__extract_secret_names__mutmut_20 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_21'] = x__extract_secret_names__mutmut_21 # type: ignore # mutmut generated
mutants_x__extract_secret_names__mutmut['x__extract_secret_names__mutmut_22'] = x__extract_secret_names__mutmut_22 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(None)
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("XXRBAC denied access to Secret/workload infoXX")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("rbac denied access to secret/workload info")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC DENIED ACCESS TO SECRET/WORKLOAD INFO")
    return ClusterUnreachableError(f"Cannot list Secret/workload info: {exc}")


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to Secret/workload info")
    return ClusterUnreachableError(None)

mutants_x__translate_error__mutmut['_mutmut_orig'] = x__translate_error__mutmut_orig # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_1'] = x__translate_error__mutmut_1 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_2'] = x__translate_error__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_3'] = x__translate_error__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_4'] = x__translate_error__mutmut_4 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_5'] = x__translate_error__mutmut_5 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_6'] = x__translate_error__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_7'] = x__translate_error__mutmut_7 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_8'] = x__translate_error__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_9'] = x__translate_error__mutmut_9 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_10'] = x__translate_error__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_11'] = x__translate_error__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_12'] = x__translate_error__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_13'] = x__translate_error__mutmut_13 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_14'] = x__translate_error__mutmut_14 # type: ignore # mutmut generated
