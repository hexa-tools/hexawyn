from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from hexawyn.application.ports.driven.gitops_drift_audit_port import (
    AuditEventRaw,
    AuditLogFetchResult,
    GitOpsDriftAuditPort,
    LiveConfigResourceRaw,
    ManagedFieldsEntryRaw,
)
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_K8S_FORBIDDEN = 403
_AUDIT_LOG_PATH_ENV_VAR = "K8S_AUDIT_LOG_PATH"
_DEFAULT_AUDIT_LOG_PATH = "/var/log/kubernetes/audit.log"
_RESOURCE_KIND_BY_PLURAL = {"configmaps": "ConfigMap", "secrets": "Secret"}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut: MutantDict = {}  # type: ignore
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut: MutantDict = {}  # type: ignore


class KubernetesAuditLogAdapter(GitOpsDriftAuditPort):
    """Secondary adapter — enumerates ConfigMap/Secret managedFields (always
    available via the K8s API) and, if configured, reads a local k8s audit
    log file used purely to enrich actor identity."""

    @_mutmut_mutated(mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut)
    def list_live_config_resources(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_orig(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_1(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = None
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_2(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = None
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_3(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(None)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_4(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = None
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_5(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(None)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_6(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(None) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_7(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = None
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_8(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource(None, item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_9(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", None) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_10(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource(item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_11(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", ) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_12(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("XXConfigMapXX", item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_13(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("configmap", item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_14(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("CONFIGMAP", item) for item in configmaps.items]
        resources += [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_15(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources = [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_16(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources -= [_to_resource("Secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_17(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource(None, item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_18(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("Secret", None) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_19(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource(item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_20(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("Secret", ) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_21(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("XXSecretXX", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_22(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("secret", item) for item in secrets.items]
        return resources

    def xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_23(self, namespace: str) -> list[LiveConfigResourceRaw]:
        from kubernetes import client as k8s

        core_api = k8s.CoreV1Api()
        try:
            configmaps = core_api.list_namespaced_config_map(namespace)
            secrets = core_api.list_namespaced_secret(namespace)
        except Exception as exc:
            raise _translate_error(exc) from exc

        resources = [_to_resource("ConfigMap", item) for item in configmaps.items]
        resources += [_to_resource("SECRET", item) for item in secrets.items]
        return resources

    @_mutmut_mutated(mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut)
    def fetch_audit_log_events(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_orig(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_1(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = None
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_2(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(None)
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_3(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(None, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_4(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, None))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_5(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_6(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, ))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_7(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_8(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=None, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_9(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=None, earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_10(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_11(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_12(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], )

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_13(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=True, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_14(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = None
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_15(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = None
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_16(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(None, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_17(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, None)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_18(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_19(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, )
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_20(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_21(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(None)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_22(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = None
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_23(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min(None, default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_24(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min(default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_25(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), )
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_26(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["XXtimestampXX"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_27(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["TIMESTAMP"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_28(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=None, events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_29(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=None, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_30(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, earliest_timestamp=None)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_31(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(events=events, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_32(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, earliest_timestamp=earliest)

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_33(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=True, events=events, )

    def xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_34(self, namespace: str, window_days: int) -> AuditLogFetchResult:
        path = Path(os.environ.get(_AUDIT_LOG_PATH_ENV_VAR, _DEFAULT_AUDIT_LOG_PATH))
        if not path.exists():
            return AuditLogFetchResult(available=False, events=[], earliest_timestamp=None)

        events: list[AuditEventRaw] = []
        for line in path.read_text().splitlines():
            event = _parse_audit_line(line, namespace)
            if event is not None:
                events.append(event)

        earliest = min((event["timestamp"] for event in events), default=None)
        return AuditLogFetchResult(available=False, events=events, earliest_timestamp=earliest)

mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['_mutmut_orig'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_1'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_2'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_3'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_4'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_5'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_6'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_7'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_8'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_9'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_10'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_11'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_12'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_13'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_14'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_15'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_16'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_17'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_18'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_19'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_20'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_21'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_22'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut['xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_23'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁlist_live_config_resources__mutmut_23 # type: ignore # mutmut generated

mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['_mutmut_orig'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_orig # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_1'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_1 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_2'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_2 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_3'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_3 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_4'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_4 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_5'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_5 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_6'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_6 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_7'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_7 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_8'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_8 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_9'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_9 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_10'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_10 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_11'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_11 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_12'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_12 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_13'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_13 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_14'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_14 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_15'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_15 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_16'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_16 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_17'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_17 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_18'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_18 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_19'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_19 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_20'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_20 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_21'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_21 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_22'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_22 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_23'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_23 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_24'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_24 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_25'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_25 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_26'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_26 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_27'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_27 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_28'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_28 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_29'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_29 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_30'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_30 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_31'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_31 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_32'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_32 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_33'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_33 # type: ignore # mutmut generated
mutants_xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut['xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_34'] = KubernetesAuditLogAdapter.xǁKubernetesAuditLogAdapterǁfetch_audit_log_events__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_resource__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_resource__mutmut)
def _to_resource(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        kind=kind,
        name=metadata.name,
        namespace=metadata.namespace,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
    )


def x__to_resource__mutmut_orig(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        kind=kind,
        name=metadata.name,
        namespace=metadata.namespace,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
    )


def x__to_resource__mutmut_1(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = None
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        kind=kind,
        name=metadata.name,
        namespace=metadata.namespace,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
    )


def x__to_resource__mutmut_2(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = None
    return LiveConfigResourceRaw(
        kind=kind,
        name=metadata.name,
        namespace=metadata.namespace,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
    )


def x__to_resource__mutmut_3(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields and []
    return LiveConfigResourceRaw(
        kind=kind,
        name=metadata.name,
        namespace=metadata.namespace,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
    )


def x__to_resource__mutmut_4(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        kind=None,
        name=metadata.name,
        namespace=metadata.namespace,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
    )


def x__to_resource__mutmut_5(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        kind=kind,
        name=None,
        namespace=metadata.namespace,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
    )


def x__to_resource__mutmut_6(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        kind=kind,
        name=metadata.name,
        namespace=None,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
    )


def x__to_resource__mutmut_7(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        kind=kind,
        name=metadata.name,
        namespace=metadata.namespace,
        managed_fields=None,
    )


def x__to_resource__mutmut_8(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        name=metadata.name,
        namespace=metadata.namespace,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
    )


def x__to_resource__mutmut_9(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        kind=kind,
        namespace=metadata.namespace,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
    )


def x__to_resource__mutmut_10(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        kind=kind,
        name=metadata.name,
        managed_fields=[_to_managed_fields_entry(entry) for entry in managed_fields],
    )


def x__to_resource__mutmut_11(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        kind=kind,
        name=metadata.name,
        namespace=metadata.namespace,
        )


def x__to_resource__mutmut_12(kind: str, item: Any) -> LiveConfigResourceRaw:
    metadata = item.metadata
    managed_fields = metadata.managed_fields or []
    return LiveConfigResourceRaw(
        kind=kind,
        name=metadata.name,
        namespace=metadata.namespace,
        managed_fields=[_to_managed_fields_entry(None) for entry in managed_fields],
    )

mutants_x__to_resource__mutmut['_mutmut_orig'] = x__to_resource__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_resource__mutmut['x__to_resource__mutmut_1'] = x__to_resource__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_resource__mutmut['x__to_resource__mutmut_2'] = x__to_resource__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_resource__mutmut['x__to_resource__mutmut_3'] = x__to_resource__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_resource__mutmut['x__to_resource__mutmut_4'] = x__to_resource__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_resource__mutmut['x__to_resource__mutmut_5'] = x__to_resource__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_resource__mutmut['x__to_resource__mutmut_6'] = x__to_resource__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_resource__mutmut['x__to_resource__mutmut_7'] = x__to_resource__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_resource__mutmut['x__to_resource__mutmut_8'] = x__to_resource__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_resource__mutmut['x__to_resource__mutmut_9'] = x__to_resource__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_resource__mutmut['x__to_resource__mutmut_10'] = x__to_resource__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_resource__mutmut['x__to_resource__mutmut_11'] = x__to_resource__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_resource__mutmut['x__to_resource__mutmut_12'] = x__to_resource__mutmut_12 # type: ignore # mutmut generated
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
mutants_x__parse_audit_line__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_audit_line__mutmut)
def _parse_audit_line(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_orig(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_1(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = None
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_2(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(None)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_3(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_4(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = None
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_5(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get(None)
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_6(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("XXobjectRefXX")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_7(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectref")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_8(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("OBJECTREF")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_9(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_10(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = None
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_11(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get(None)
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_12(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("XXresourceXX")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_13(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("RESOURCE")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_14(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_15(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = None
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_16(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(None)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_17(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None and object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_18(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is not None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_19(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get(None) != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_20(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("XXnamespaceXX") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_21(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("NAMESPACE") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_22(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") == namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_23(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = None
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_24(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get(None)
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_25(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("XXuserXX")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_26(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("USER")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_27(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_28(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get(None) if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_29(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("XXusernameXX") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_30(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("USERNAME") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_31(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = None
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_32(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get(None)
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_33(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("XXrequestReceivedTimestampXX")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_34(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestreceivedtimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_35(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("REQUESTRECEIVEDTIMESTAMP")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_36(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = None
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_37(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get(None)
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_38(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("XXverbXX")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_39(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("VERB")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_40(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = None
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_41(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get(None)
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_42(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("XXnameXX")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_43(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("NAME")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_44(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str) and not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_45(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str) and not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_46(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str) and not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_47(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_48(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_49(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_50(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_51(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=None, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_52(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=None, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_53(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=None, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_54(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=None, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_55(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=None, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_56(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, timestamp=None
    )


def x__parse_audit_line__mutmut_57(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        name=name, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_58(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, namespace=namespace, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_59(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, actor=actor, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_60(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, verb=verb, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_61(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, timestamp=timestamp
    )


def x__parse_audit_line__mutmut_62(line: str, namespace: str) -> AuditEventRaw | None:
    try:
        raw = json.loads(line)
    except json.JSONDecodeError:
        return None
    if not isinstance(raw, dict):
        return None

    object_ref = raw.get("objectRef")
    if not isinstance(object_ref, dict):
        return None
    resource = object_ref.get("resource")
    if not isinstance(resource, str):
        return None
    kind = _RESOURCE_KIND_BY_PLURAL.get(resource)
    if kind is None or object_ref.get("namespace") != namespace:
        return None

    user = raw.get("user")
    actor = user.get("username") if isinstance(user, dict) else None
    timestamp = raw.get("requestReceivedTimestamp")
    verb = raw.get("verb")
    name = object_ref.get("name")
    if (
        not isinstance(actor, str)
        or not isinstance(timestamp, str)
        or not isinstance(verb, str)
        or not isinstance(name, str)
    ):
        return None

    return AuditEventRaw(
        kind=kind, name=name, namespace=namespace, actor=actor, verb=verb, )

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
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_57'] = x__parse_audit_line__mutmut_57 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_58'] = x__parse_audit_line__mutmut_58 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_59'] = x__parse_audit_line__mutmut_59 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_60'] = x__parse_audit_line__mutmut_60 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_61'] = x__parse_audit_line__mutmut_61 # type: ignore # mutmut generated
mutants_x__parse_audit_line__mutmut['x__parse_audit_line__mutmut_62'] = x__parse_audit_line__mutmut_62 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError(None)
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("XXRBAC denied access to ConfigMap/Secret infoXX")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("rbac denied access to configmap/secret info")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC DENIED ACCESS TO CONFIGMAP/SECRET INFO")
    return ClusterUnreachableError(f"Cannot list ConfigMap/Secret info: {exc}")


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _K8S_FORBIDDEN:
        return InsufficientPermissionsError("RBAC denied access to ConfigMap/Secret info")
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
