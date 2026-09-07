from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from hexawyn.application.ports.driven.rbac_security_audit_port import (
    ApiUsageEventRaw,
    ApiUsageFetchResult,
    PodOwnerRaw,
    PolicyRuleRaw,
    RBACSecurityAuditPort,
    RoleBindingRaw,
    RoleRaw,
    RoleRefRaw,
    ServiceAccountRaw,
    SubjectRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403
_AUDIT_LOG_PATH_ENV_VAR = "K8S_AUDIT_LOG_PATH"
_DEFAULT_AUDIT_LOG_PATH = "/var/log/kubernetes/audit.log"
_SERVICE_ACCOUNT_USERNAME_PREFIX = "system:serviceaccount:"
_DEFAULT_SERVICE_ACCOUNT_NAME = "default"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesRBACAdapterǁlist_roles__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut: MutantDict = {}  # type: ignore


class KubernetesRBACAdapter(RBACSecurityAuditPort):
    """Secondary adapter — enumerates ServiceAccounts, RoleBindings/
    ClusterRoleBindings, Role/ClusterRole rules (with raw aggregationRule
    label-selector data) and owning Pods via the K8s API, and, if configured,
    reads a local k8s audit log file to compute actual per-service-account
    API usage."""

    @_mutmut_mutated(mutants_xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut)
    def list_service_accounts(self) -> list[ServiceAccountRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_account_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            ServiceAccountRaw(name=item.metadata.name, namespace=item.metadata.namespace)
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_orig(self) -> list[ServiceAccountRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_account_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            ServiceAccountRaw(name=item.metadata.name, namespace=item.metadata.namespace)
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_1(self) -> list[ServiceAccountRaw]:
        from kubernetes import client as k8s

        core_api = None
        try:
            result = core_api.list_service_account_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            ServiceAccountRaw(name=item.metadata.name, namespace=item.metadata.namespace)
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_2(self) -> list[ServiceAccountRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = None
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            ServiceAccountRaw(name=item.metadata.name, namespace=item.metadata.namespace)
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_3(self) -> list[ServiceAccountRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_account_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(None) from exc
        return [
            ServiceAccountRaw(name=item.metadata.name, namespace=item.metadata.namespace)
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_4(self) -> list[ServiceAccountRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_account_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            ServiceAccountRaw(name=None, namespace=item.metadata.namespace)
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_5(self) -> list[ServiceAccountRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_account_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            ServiceAccountRaw(name=item.metadata.name, namespace=None)
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_6(self) -> list[ServiceAccountRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_account_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            ServiceAccountRaw(namespace=item.metadata.namespace)
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_7(self) -> list[ServiceAccountRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_service_account_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            ServiceAccountRaw(name=item.metadata.name, )
            for item in result.items
        ]

    @_mutmut_mutated(mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut)
    def list_role_bindings(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_orig(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_1(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = None
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_2(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = None
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_3(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_4(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(None) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_5(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = None
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_6(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding(None, item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_7(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", None, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_8(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding(item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_9(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_10(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, )
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_11(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("XXClusterRoleBindingXX", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_12(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("clusterrolebinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_13(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("CLUSTERROLEBINDING", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_14(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings = [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_15(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings -= [
            _to_binding("RoleBinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_16(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding(None, item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_17(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", None, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_18(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, namespace=None)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_19(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding(item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_20(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_21(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("RoleBinding", item, )
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_22(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("XXRoleBindingXX", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_23(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("rolebinding", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    def xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_24(self) -> list[RoleBindingRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_bindings = rbac_api.list_cluster_role_binding()
            namespaced_bindings = rbac_api.list_role_binding_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        bindings = [
            _to_binding("ClusterRoleBinding", item, namespace=None)
            for item in cluster_bindings.items
        ]
        bindings += [
            _to_binding("ROLEBINDING", item, namespace=item.metadata.namespace)
            for item in namespaced_bindings.items
        ]
        return bindings

    @_mutmut_mutated(mutants_xǁKubernetesRBACAdapterǁlist_roles__mutmut)
    def list_roles(self) -> list[RoleRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_roles = rbac_api.list_cluster_role()
            namespaced_roles = rbac_api.list_role_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        roles = [_to_cluster_role(item) for item in cluster_roles.items]
        roles += [_to_namespaced_role(item) for item in namespaced_roles.items]
        return roles

    def xǁKubernetesRBACAdapterǁlist_roles__mutmut_orig(self) -> list[RoleRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_roles = rbac_api.list_cluster_role()
            namespaced_roles = rbac_api.list_role_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        roles = [_to_cluster_role(item) for item in cluster_roles.items]
        roles += [_to_namespaced_role(item) for item in namespaced_roles.items]
        return roles

    def xǁKubernetesRBACAdapterǁlist_roles__mutmut_1(self) -> list[RoleRaw]:
        from kubernetes import client as k8s

        rbac_api = None
        try:
            cluster_roles = rbac_api.list_cluster_role()
            namespaced_roles = rbac_api.list_role_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        roles = [_to_cluster_role(item) for item in cluster_roles.items]
        roles += [_to_namespaced_role(item) for item in namespaced_roles.items]
        return roles

    def xǁKubernetesRBACAdapterǁlist_roles__mutmut_2(self) -> list[RoleRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_roles = None
            namespaced_roles = rbac_api.list_role_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        roles = [_to_cluster_role(item) for item in cluster_roles.items]
        roles += [_to_namespaced_role(item) for item in namespaced_roles.items]
        return roles

    def xǁKubernetesRBACAdapterǁlist_roles__mutmut_3(self) -> list[RoleRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_roles = rbac_api.list_cluster_role()
            namespaced_roles = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        roles = [_to_cluster_role(item) for item in cluster_roles.items]
        roles += [_to_namespaced_role(item) for item in namespaced_roles.items]
        return roles

    def xǁKubernetesRBACAdapterǁlist_roles__mutmut_4(self) -> list[RoleRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_roles = rbac_api.list_cluster_role()
            namespaced_roles = rbac_api.list_role_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(None) from exc

        roles = [_to_cluster_role(item) for item in cluster_roles.items]
        roles += [_to_namespaced_role(item) for item in namespaced_roles.items]
        return roles

    def xǁKubernetesRBACAdapterǁlist_roles__mutmut_5(self) -> list[RoleRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_roles = rbac_api.list_cluster_role()
            namespaced_roles = rbac_api.list_role_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        roles = None
        roles += [_to_namespaced_role(item) for item in namespaced_roles.items]
        return roles

    def xǁKubernetesRBACAdapterǁlist_roles__mutmut_6(self) -> list[RoleRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_roles = rbac_api.list_cluster_role()
            namespaced_roles = rbac_api.list_role_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        roles = [_to_cluster_role(None) for item in cluster_roles.items]
        roles += [_to_namespaced_role(item) for item in namespaced_roles.items]
        return roles

    def xǁKubernetesRBACAdapterǁlist_roles__mutmut_7(self) -> list[RoleRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_roles = rbac_api.list_cluster_role()
            namespaced_roles = rbac_api.list_role_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        roles = [_to_cluster_role(item) for item in cluster_roles.items]
        roles = [_to_namespaced_role(item) for item in namespaced_roles.items]
        return roles

    def xǁKubernetesRBACAdapterǁlist_roles__mutmut_8(self) -> list[RoleRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_roles = rbac_api.list_cluster_role()
            namespaced_roles = rbac_api.list_role_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        roles = [_to_cluster_role(item) for item in cluster_roles.items]
        roles -= [_to_namespaced_role(item) for item in namespaced_roles.items]
        return roles

    def xǁKubernetesRBACAdapterǁlist_roles__mutmut_9(self) -> list[RoleRaw]:
        from kubernetes import client as k8s

        rbac_api = k8s.RbacAuthorizationV1Api()
        try:
            cluster_roles = rbac_api.list_cluster_role()
            namespaced_roles = rbac_api.list_role_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc

        roles = [_to_cluster_role(item) for item in cluster_roles.items]
        roles += [_to_namespaced_role(None) for item in namespaced_roles.items]
        return roles

    @_mutmut_mutated(mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut)
    def list_pods_by_service_account(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            PodOwnerRaw(
                pod_name=item.metadata.name,
                namespace=item.metadata.namespace,
                service_account_name=item.spec.service_account_name
                or _DEFAULT_SERVICE_ACCOUNT_NAME,
            )
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_orig(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            PodOwnerRaw(
                pod_name=item.metadata.name,
                namespace=item.metadata.namespace,
                service_account_name=item.spec.service_account_name
                or _DEFAULT_SERVICE_ACCOUNT_NAME,
            )
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_1(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = None
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            PodOwnerRaw(
                pod_name=item.metadata.name,
                namespace=item.metadata.namespace,
                service_account_name=item.spec.service_account_name
                or _DEFAULT_SERVICE_ACCOUNT_NAME,
            )
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_2(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = None
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            PodOwnerRaw(
                pod_name=item.metadata.name,
                namespace=item.metadata.namespace,
                service_account_name=item.spec.service_account_name
                or _DEFAULT_SERVICE_ACCOUNT_NAME,
            )
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_3(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(None) from exc
        return [
            PodOwnerRaw(
                pod_name=item.metadata.name,
                namespace=item.metadata.namespace,
                service_account_name=item.spec.service_account_name
                or _DEFAULT_SERVICE_ACCOUNT_NAME,
            )
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_4(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            PodOwnerRaw(
                pod_name=None,
                namespace=item.metadata.namespace,
                service_account_name=item.spec.service_account_name
                or _DEFAULT_SERVICE_ACCOUNT_NAME,
            )
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_5(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            PodOwnerRaw(
                pod_name=item.metadata.name,
                namespace=None,
                service_account_name=item.spec.service_account_name
                or _DEFAULT_SERVICE_ACCOUNT_NAME,
            )
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_6(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            PodOwnerRaw(
                pod_name=item.metadata.name,
                namespace=item.metadata.namespace,
                service_account_name=None,
            )
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_7(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            PodOwnerRaw(
                namespace=item.metadata.namespace,
                service_account_name=item.spec.service_account_name
                or _DEFAULT_SERVICE_ACCOUNT_NAME,
            )
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_8(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            PodOwnerRaw(
                pod_name=item.metadata.name,
                service_account_name=item.spec.service_account_name
                or _DEFAULT_SERVICE_ACCOUNT_NAME,
            )
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_9(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            PodOwnerRaw(
                pod_name=item.metadata.name,
                namespace=item.metadata.namespace,
                )
            for item in result.items
        ]

    def xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_10(self) -> list[PodOwnerRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            result = core_api.list_pod_for_all_namespaces()
        except Exception as exc:
            raise _translate_error(exc) from exc
        return [
            PodOwnerRaw(
                pod_name=item.metadata.name,
                namespace=item.metadata.namespace,
                service_account_name=item.spec.service_account_name and _DEFAULT_SERVICE_ACCOUNT_NAME,
            )
            for item in result.items
        ]

    @_mutmut_mutated(mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut)
    def fetch_api_usage(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_orig(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_1(self, window_days: int) -> ApiUsageFetchResult:
        path = None
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_2(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(None)
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_3(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(None, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_4(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, None))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_5(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_6(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, ))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_7(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_8(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=None, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_9(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=None)

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_10(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_11(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, )

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_12(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=True, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_13(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = None
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_14(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = None
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_15(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(None)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_16(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_17(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(None)
        return ApiUsageFetchResult(available=True, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_18(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=None, events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_19(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, events=None)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_20(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(events=events)

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_21(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=True, )

    def xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_22(self, window_days: int) -> ApiUsageFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return ApiUsageFetchResult(available=False, events=[])

        events: list[ApiUsageEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line)
            if event is not None:
                events.append(event)
        return ApiUsageFetchResult(available=False, events=events)

mutants_xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut['_mutmut_orig'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut['xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_1'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut['xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_2'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut['xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_3'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut['xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_4'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut['xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_5'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut['xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_6'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut['xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_7'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_service_accounts__mutmut_7 # type: ignore # mutmut generated

mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['_mutmut_orig'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_1'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_2'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_3'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_4'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_5'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_6'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_7'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_8'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_9'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_10'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_11'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_12'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_13'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_14'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_15'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_16'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_17'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_18'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_19'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_20'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_21'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_22'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_23'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut['xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_24'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_role_bindings__mutmut_24 # type: ignore # mutmut generated

mutants_xǁKubernetesRBACAdapterǁlist_roles__mutmut['_mutmut_orig'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_roles__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_roles__mutmut['xǁKubernetesRBACAdapterǁlist_roles__mutmut_1'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_roles__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_roles__mutmut['xǁKubernetesRBACAdapterǁlist_roles__mutmut_2'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_roles__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_roles__mutmut['xǁKubernetesRBACAdapterǁlist_roles__mutmut_3'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_roles__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_roles__mutmut['xǁKubernetesRBACAdapterǁlist_roles__mutmut_4'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_roles__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_roles__mutmut['xǁKubernetesRBACAdapterǁlist_roles__mutmut_5'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_roles__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_roles__mutmut['xǁKubernetesRBACAdapterǁlist_roles__mutmut_6'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_roles__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_roles__mutmut['xǁKubernetesRBACAdapterǁlist_roles__mutmut_7'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_roles__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_roles__mutmut['xǁKubernetesRBACAdapterǁlist_roles__mutmut_8'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_roles__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_roles__mutmut['xǁKubernetesRBACAdapterǁlist_roles__mutmut_9'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_roles__mutmut_9 # type: ignore # mutmut generated

mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut['_mutmut_orig'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut['xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_1'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut['xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_2'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut['xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_3'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut['xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_4'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut['xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_5'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut['xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_6'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut['xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_7'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut['xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_8'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut['xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_9'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut['xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_10'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁlist_pods_by_service_account__mutmut_10 # type: ignore # mutmut generated

mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['_mutmut_orig'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_1'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_2'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_3'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_4'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_5'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_6'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_7'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_8'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_9'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_10'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_11'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_12'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_13'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_14'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_15'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_16'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_17'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_18'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_19'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_20'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_21'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut['xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_22'] = KubernetesRBACAdapter.xǁKubernetesRBACAdapterǁfetch_api_usage__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_binding__mutmut)
def _to_binding(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_orig(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_1(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = None
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_2(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects and []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_3(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=None,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_4(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=None,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_5(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=None,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_6(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=None,
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_7(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=None,
    )


def x__to_binding__mutmut_8(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_9(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_10(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_11(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_12(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        )


def x__to_binding__mutmut_13(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(None) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=item.role_ref.name),
    )


def x__to_binding__mutmut_14(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=None, name=item.role_ref.name),
    )


def x__to_binding__mutmut_15(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, name=None),
    )


def x__to_binding__mutmut_16(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(name=item.role_ref.name),
    )


def x__to_binding__mutmut_17(kind: str, item: Any, namespace: str | None) -> RoleBindingRaw:
    subjects = item.subjects or []
    return RoleBindingRaw(
        binding_kind=kind,  # type: ignore[typeddict-item]
        binding_name=item.metadata.name,
        namespace=namespace,
        subjects=[_to_subject(subject) for subject in subjects],
        role_ref=RoleRefRaw(kind=item.role_ref.kind, ),
    )

mutants_x__to_binding__mutmut['_mutmut_orig'] = x__to_binding__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_1'] = x__to_binding__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_2'] = x__to_binding__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_3'] = x__to_binding__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_4'] = x__to_binding__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_5'] = x__to_binding__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_6'] = x__to_binding__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_7'] = x__to_binding__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_8'] = x__to_binding__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_9'] = x__to_binding__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_10'] = x__to_binding__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_11'] = x__to_binding__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_12'] = x__to_binding__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_13'] = x__to_binding__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_14'] = x__to_binding__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_15'] = x__to_binding__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_16'] = x__to_binding__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_binding__mutmut['x__to_binding__mutmut_17'] = x__to_binding__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_subject__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_subject__mutmut)
def _to_subject(subject: Any) -> SubjectRaw:
    return SubjectRaw(kind=subject.kind, name=subject.name, namespace=subject.namespace)


def x__to_subject__mutmut_orig(subject: Any) -> SubjectRaw:
    return SubjectRaw(kind=subject.kind, name=subject.name, namespace=subject.namespace)


def x__to_subject__mutmut_1(subject: Any) -> SubjectRaw:
    return SubjectRaw(kind=None, name=subject.name, namespace=subject.namespace)


def x__to_subject__mutmut_2(subject: Any) -> SubjectRaw:
    return SubjectRaw(kind=subject.kind, name=None, namespace=subject.namespace)


def x__to_subject__mutmut_3(subject: Any) -> SubjectRaw:
    return SubjectRaw(kind=subject.kind, name=subject.name, namespace=None)


def x__to_subject__mutmut_4(subject: Any) -> SubjectRaw:
    return SubjectRaw(name=subject.name, namespace=subject.namespace)


def x__to_subject__mutmut_5(subject: Any) -> SubjectRaw:
    return SubjectRaw(kind=subject.kind, namespace=subject.namespace)


def x__to_subject__mutmut_6(subject: Any) -> SubjectRaw:
    return SubjectRaw(kind=subject.kind, name=subject.name, )

mutants_x__to_subject__mutmut['_mutmut_orig'] = x__to_subject__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_subject__mutmut['x__to_subject__mutmut_1'] = x__to_subject__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_subject__mutmut['x__to_subject__mutmut_2'] = x__to_subject__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_subject__mutmut['x__to_subject__mutmut_3'] = x__to_subject__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_subject__mutmut['x__to_subject__mutmut_4'] = x__to_subject__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_subject__mutmut['x__to_subject__mutmut_5'] = x__to_subject__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_subject__mutmut['x__to_subject__mutmut_6'] = x__to_subject__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_cluster_role__mutmut)
def _to_cluster_role(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_orig(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_1(item: Any) -> RoleRaw:
    return RoleRaw(
        kind=None,
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_2(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=None,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_3(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        rules=None,
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_4(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=None,
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_5(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=None,
    )


def x__to_cluster_role__mutmut_6(item: Any) -> RoleRaw:
    return RoleRaw(
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_7(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_8(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_9(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_10(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_11(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        )


def x__to_cluster_role__mutmut_12(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="XXClusterRoleXX",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_13(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="clusterrole",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_14(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="CLUSTERROLE",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_15(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(None) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_16(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules and [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_17(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels and {},
        aggregation_selectors=_to_aggregation_selectors(item.aggregation_rule),
    )


def x__to_cluster_role__mutmut_18(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ClusterRole",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=_to_aggregation_selectors(None),
    )

mutants_x__to_cluster_role__mutmut['_mutmut_orig'] = x__to_cluster_role__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_1'] = x__to_cluster_role__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_2'] = x__to_cluster_role__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_3'] = x__to_cluster_role__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_4'] = x__to_cluster_role__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_5'] = x__to_cluster_role__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_6'] = x__to_cluster_role__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_7'] = x__to_cluster_role__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_8'] = x__to_cluster_role__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_9'] = x__to_cluster_role__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_10'] = x__to_cluster_role__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_11'] = x__to_cluster_role__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_12'] = x__to_cluster_role__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_13'] = x__to_cluster_role__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_14'] = x__to_cluster_role__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_15'] = x__to_cluster_role__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_16'] = x__to_cluster_role__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_17'] = x__to_cluster_role__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_cluster_role__mutmut['x__to_cluster_role__mutmut_18'] = x__to_cluster_role__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_namespaced_role__mutmut)
def _to_namespaced_role(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_orig(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_1(item: Any) -> RoleRaw:
    return RoleRaw(
        kind=None,
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_2(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=None,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_3(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=None,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_4(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=None,
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_5(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=None,
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_6(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=None,
    )


def x__to_namespaced_role__mutmut_7(item: Any) -> RoleRaw:
    return RoleRaw(
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_8(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_9(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_10(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_11(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_12(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        )


def x__to_namespaced_role__mutmut_13(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="XXRoleXX",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_14(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_15(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="ROLE",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_16(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(None) for rule in (item.rules or [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_17(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules and [])],
        labels=item.metadata.labels or {},
        aggregation_selectors=[],
    )


def x__to_namespaced_role__mutmut_18(item: Any) -> RoleRaw:
    return RoleRaw(
        kind="Role",
        name=item.metadata.name,
        namespace=item.metadata.namespace,
        rules=[_to_rule(rule) for rule in (item.rules or [])],
        labels=item.metadata.labels and {},
        aggregation_selectors=[],
    )

mutants_x__to_namespaced_role__mutmut['_mutmut_orig'] = x__to_namespaced_role__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_1'] = x__to_namespaced_role__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_2'] = x__to_namespaced_role__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_3'] = x__to_namespaced_role__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_4'] = x__to_namespaced_role__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_5'] = x__to_namespaced_role__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_6'] = x__to_namespaced_role__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_7'] = x__to_namespaced_role__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_8'] = x__to_namespaced_role__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_9'] = x__to_namespaced_role__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_10'] = x__to_namespaced_role__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_11'] = x__to_namespaced_role__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_12'] = x__to_namespaced_role__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_13'] = x__to_namespaced_role__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_14'] = x__to_namespaced_role__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_15'] = x__to_namespaced_role__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_16'] = x__to_namespaced_role__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_17'] = x__to_namespaced_role__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_namespaced_role__mutmut['x__to_namespaced_role__mutmut_18'] = x__to_namespaced_role__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_rule__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_rule__mutmut)
def _to_rule(rule: Any) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        verbs=rule.verbs or [],
        resources=rule.resources or [],
        api_groups=rule.api_groups or [],
    )


def x__to_rule__mutmut_orig(rule: Any) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        verbs=rule.verbs or [],
        resources=rule.resources or [],
        api_groups=rule.api_groups or [],
    )


def x__to_rule__mutmut_1(rule: Any) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        verbs=None,
        resources=rule.resources or [],
        api_groups=rule.api_groups or [],
    )


def x__to_rule__mutmut_2(rule: Any) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        verbs=rule.verbs or [],
        resources=None,
        api_groups=rule.api_groups or [],
    )


def x__to_rule__mutmut_3(rule: Any) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        verbs=rule.verbs or [],
        resources=rule.resources or [],
        api_groups=None,
    )


def x__to_rule__mutmut_4(rule: Any) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        resources=rule.resources or [],
        api_groups=rule.api_groups or [],
    )


def x__to_rule__mutmut_5(rule: Any) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        verbs=rule.verbs or [],
        api_groups=rule.api_groups or [],
    )


def x__to_rule__mutmut_6(rule: Any) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        verbs=rule.verbs or [],
        resources=rule.resources or [],
        )


def x__to_rule__mutmut_7(rule: Any) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        verbs=rule.verbs and [],
        resources=rule.resources or [],
        api_groups=rule.api_groups or [],
    )


def x__to_rule__mutmut_8(rule: Any) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        verbs=rule.verbs or [],
        resources=rule.resources and [],
        api_groups=rule.api_groups or [],
    )


def x__to_rule__mutmut_9(rule: Any) -> PolicyRuleRaw:
    return PolicyRuleRaw(
        verbs=rule.verbs or [],
        resources=rule.resources or [],
        api_groups=rule.api_groups and [],
    )

mutants_x__to_rule__mutmut['_mutmut_orig'] = x__to_rule__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_rule__mutmut['x__to_rule__mutmut_1'] = x__to_rule__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_rule__mutmut['x__to_rule__mutmut_2'] = x__to_rule__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_rule__mutmut['x__to_rule__mutmut_3'] = x__to_rule__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_rule__mutmut['x__to_rule__mutmut_4'] = x__to_rule__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_rule__mutmut['x__to_rule__mutmut_5'] = x__to_rule__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_rule__mutmut['x__to_rule__mutmut_6'] = x__to_rule__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_rule__mutmut['x__to_rule__mutmut_7'] = x__to_rule__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_rule__mutmut['x__to_rule__mutmut_8'] = x__to_rule__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_rule__mutmut['x__to_rule__mutmut_9'] = x__to_rule__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_aggregation_selectors__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_aggregation_selectors__mutmut)
def _to_aggregation_selectors(aggregation_rule: Any) -> list[dict[str, str]]:
    if aggregation_rule is None or not aggregation_rule.cluster_role_selectors:
        return []
    return [selector.match_labels or {} for selector in aggregation_rule.cluster_role_selectors]


def x__to_aggregation_selectors__mutmut_orig(aggregation_rule: Any) -> list[dict[str, str]]:
    if aggregation_rule is None or not aggregation_rule.cluster_role_selectors:
        return []
    return [selector.match_labels or {} for selector in aggregation_rule.cluster_role_selectors]


def x__to_aggregation_selectors__mutmut_1(aggregation_rule: Any) -> list[dict[str, str]]:
    if aggregation_rule is None and not aggregation_rule.cluster_role_selectors:
        return []
    return [selector.match_labels or {} for selector in aggregation_rule.cluster_role_selectors]


def x__to_aggregation_selectors__mutmut_2(aggregation_rule: Any) -> list[dict[str, str]]:
    if aggregation_rule is not None or not aggregation_rule.cluster_role_selectors:
        return []
    return [selector.match_labels or {} for selector in aggregation_rule.cluster_role_selectors]


def x__to_aggregation_selectors__mutmut_3(aggregation_rule: Any) -> list[dict[str, str]]:
    if aggregation_rule is None or aggregation_rule.cluster_role_selectors:
        return []
    return [selector.match_labels or {} for selector in aggregation_rule.cluster_role_selectors]


def x__to_aggregation_selectors__mutmut_4(aggregation_rule: Any) -> list[dict[str, str]]:
    if aggregation_rule is None or not aggregation_rule.cluster_role_selectors:
        return []
    return [selector.match_labels and {} for selector in aggregation_rule.cluster_role_selectors]

mutants_x__to_aggregation_selectors__mutmut['_mutmut_orig'] = x__to_aggregation_selectors__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_aggregation_selectors__mutmut['x__to_aggregation_selectors__mutmut_1'] = x__to_aggregation_selectors__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_aggregation_selectors__mutmut['x__to_aggregation_selectors__mutmut_2'] = x__to_aggregation_selectors__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_aggregation_selectors__mutmut['x__to_aggregation_selectors__mutmut_3'] = x__to_aggregation_selectors__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_aggregation_selectors__mutmut['x__to_aggregation_selectors__mutmut_4'] = x__to_aggregation_selectors__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_audit_line__mutmut)
def _parse_audit_line(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_orig(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_1(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = None
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_2(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(None)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_3(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_4(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = None
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_5(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get(None)
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_6(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("XXuserXX")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_7(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("USER")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_8(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_9(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get(None) if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_10(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("XXusernameXX") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_11(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("USERNAME") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_12(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) and not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_13(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_14(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_15(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(None):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_16(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = None
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_17(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(None)
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_18(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split("XX:XX")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_19(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) == 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_20(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 5:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_21(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = None

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_22(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[3], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_23(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[4]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_24(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = None
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_25(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get(None)
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_26(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("XXobjectRefXX")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_27(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectref")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_28(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("OBJECTREF")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_29(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_30(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get(None) if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_31(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("XXresourceXX") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_32(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("RESOURCE") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_33(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = None
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_34(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get(None)
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_35(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("XXverbXX")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_36(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("VERB")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_37(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = None
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_38(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get(None)
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_39(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("XXrequestReceivedTimestampXX")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_40(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestreceivedtimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_41(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("REQUESTRECEIVEDTIMESTAMP")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_42(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) and not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_43(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) and not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_44(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_45(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_46(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_47(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=None,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_48(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=None,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_49(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=None,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_50(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=None,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_51(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=None,
    )


def x__parse_audit_line__mutmut_52(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        namespace=namespace,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_53(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        verb=verb,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_54(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        resource=resource,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_55(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        timestamp=timestamp,
    )


def x__parse_audit_line__mutmut_56(line: str) -> ApiUsageEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    user = raw.get("user")
    username = user.get("username") if isinstance(user, dict) else None
    if not isinstance(username, str) or not username.startswith(_SERVICE_ACCOUNT_USERNAME_PREFIX):
        return None
    parts = username.split(":")
    if len(parts) != 4:  # noqa: PLR2004
        return None
    namespace, name = parts[2], parts[3]

    object_ref = raw.get("objectRef")
    resource = object_ref.get("resource") if isinstance(object_ref, dict) else None
    verb = raw.get("verb")
    timestamp = raw.get("requestReceivedTimestamp")
    if not isinstance(resource, str) or not isinstance(verb, str) or not isinstance(timestamp, str):
        return None

    return ApiUsageEventRaw(
        service_account=name,
        namespace=namespace,
        verb=verb,
        resource=resource,
        )

mutants_x__parse_audit_line__mutmut['_mutmut_orig'] = x__parse_audit_line__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_1'] = x__parse_audit_line__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_2'] = x__parse_audit_line__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_3'] = x__parse_audit_line__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_4'] = x__parse_audit_line__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_5'] = x__parse_audit_line__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_6'] = x__parse_audit_line__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_7'] = x__parse_audit_line__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_8'] = x__parse_audit_line__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_9'] = x__parse_audit_line__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_10'] = x__parse_audit_line__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_11'] = x__parse_audit_line__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_12'] = x__parse_audit_line__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_13'] = x__parse_audit_line__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_14'] = x__parse_audit_line__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_15'] = x__parse_audit_line__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_16'] = x__parse_audit_line__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_17'] = x__parse_audit_line__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_18'] = x__parse_audit_line__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_19'] = x__parse_audit_line__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_20'] = x__parse_audit_line__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_21'] = x__parse_audit_line__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_22'] = x__parse_audit_line__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_23'] = x__parse_audit_line__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_24'] = x__parse_audit_line__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_25'] = x__parse_audit_line__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_26'] = x__parse_audit_line__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_27'] = x__parse_audit_line__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_28'] = x__parse_audit_line__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_29'] = x__parse_audit_line__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_30'] = x__parse_audit_line__mutmut_30 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_31'] = x__parse_audit_line__mutmut_31 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_32'] = x__parse_audit_line__mutmut_32 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_33'] = x__parse_audit_line__mutmut_33 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_34'] = x__parse_audit_line__mutmut_34 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_35'] = x__parse_audit_line__mutmut_35 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_36'] = x__parse_audit_line__mutmut_36 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_37'] = x__parse_audit_line__mutmut_37 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_38'] = x__parse_audit_line__mutmut_38 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_39'] = x__parse_audit_line__mutmut_39 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_40'] = x__parse_audit_line__mutmut_40 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_41'] = x__parse_audit_line__mutmut_41 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_42'] = x__parse_audit_line__mutmut_42 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_43'] = x__parse_audit_line__mutmut_43 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_44'] = x__parse_audit_line__mutmut_44 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_45'] = x__parse_audit_line__mutmut_45 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_46'] = x__parse_audit_line__mutmut_46 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_47'] = x__parse_audit_line__mutmut_47 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_48'] = x__parse_audit_line__mutmut_48 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_49'] = x__parse_audit_line__mutmut_49 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_50'] = x__parse_audit_line__mutmut_50 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_51'] = x__parse_audit_line__mutmut_51 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_52'] = x__parse_audit_line__mutmut_52 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_53'] = x__parse_audit_line__mutmut_53 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_54'] = x__parse_audit_line__mutmut_54 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_55'] = x__parse_audit_line__mutmut_55 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_56'] = x__parse_audit_line__mutmut_56 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(None)
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("XXRBAC denied access to ServiceAccount/RBAC infoXX")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("rbac denied access to serviceaccount/rbac info")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC DENIED ACCESS TO SERVICEACCOUNT/RBAC INFO")
    return ClusterUnreachableError(f"Cannot list ServiceAccount/RBAC info: {exc}")


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ServiceAccount/RBAC info")
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
