"""KedaAdapter — queries real KEDA CRDs via VanillaAdapter."""

from __future__ import annotations

from typing import cast

from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.domain.models.keda import (
    AuthType,
    HPAStatus,
    KedaDetectionResult,
    KedaScaledJob,
    KedaScaledObject,
    KedaScaledObjectPhase,
    KedaTrigger,
    KedaTriggerAuth,
    ScaledJobPhase,
    TriggerType,
)

_KEDA_GROUP = "keda.sh"
_KEDA_VERSION = "v1alpha1"


class KedaAdapter(KedaPort):
    """Real KEDA adapter using VanillaAdapter's CustomObjectsApi."""

    def __init__(self, vanilla: VanillaAdapter) -> None:
        self._vanilla = vanilla

    def _crd(self):  # type: ignore
        return self._vanilla._crd_api_client()

    def detect(self) -> KedaDetectionResult:
        try:
            sos = self._list("scaledobjects")
            sj = self._list("scaledjobs")
        except Exception:
            return KedaDetectionResult(
                installed=False,
                version=None,
                namespace=None,
                total_scaledobjects=0,
                ready_scaledobjects=0,
                error_scaledobjects=0,
                scaled_to_zero_count=0,
                total_scaledjobs=0,
                managed_namespaces=[],
            )
        ready = sum(1 for s in sos if s.phase == KedaScaledObjectPhase.READY)
        error_sos = sum(1 for s in sos if s.phase == KedaScaledObjectPhase.ERROR)
        scaled_to_zero = sum(1 for s in sos if s.phase == KedaScaledObjectPhase.SCALED_TO_ZERO)
        namespaces = sorted({s.namespace for s in sos} | {j.namespace for j in sj})
        return KedaDetectionResult(
            installed=True,
            version=None,
            namespace="keda",
            total_scaledobjects=len(sos),
            ready_scaledobjects=ready,
            error_scaledobjects=error_sos,
            scaled_to_zero_count=scaled_to_zero,
            total_scaledjobs=len(sj),
            managed_namespaces=namespaces,
        )

    def list_scaledobjects(self, namespace: str | None = None) -> list[KedaScaledObject]:
        return self._list("scaledobjects", namespace)

    def get_scaledobject(self, name: str, namespace: str) -> KedaScaledObject:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_KEDA_GROUP,
            version=_KEDA_VERSION,
            namespace=namespace,
            plural="scaledobjects",
            name=name,
        )
        return self._parse_scaledobject(cast(dict, raw))  # type: ignore

    def list_trigger_auths(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        return self._list_triggerauths(namespace)

    def get_trigger_auth(self, name: str, namespace: str) -> KedaTriggerAuth:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_KEDA_GROUP,
            version=_KEDA_VERSION,
            namespace=namespace,
            plural="triggerauthentications",
            name=name,
        )
        return self._parse_triggerauth(cast(dict, raw))  # type: ignore

    def list_scaledjobs(self, namespace: str | None = None) -> list[KedaScaledJob]:
        return self._list_scaledjobs(namespace)

    def get_scaledjob(self, name: str, namespace: str) -> KedaScaledJob:
        raw = self._crd().get_namespaced_custom_object(  # type: ignore
            group=_KEDA_GROUP,
            version=_KEDA_VERSION,
            namespace=namespace,
            plural="scaledjobs",
            name=name,
        )
        return self._parse_scaledjob(cast(dict, raw))  # type: ignore

    def _list(self, plural: str, namespace: str | None = None) -> list[KedaScaledObject]:
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_KEDA_GROUP,
                    version=_KEDA_VERSION,
                    namespace=namespace,
                    plural=plural,
                )
            else:
                raw = self._crd().list_cluster_custom_object(  # type: ignore
                    group=_KEDA_GROUP,
                    version=_KEDA_VERSION,
                    plural=plural,
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [self._parse_scaledobject(c) for c in items if isinstance(c, dict)]

    def _list_scaledjobs(self, namespace: str | None = None) -> list[KedaScaledJob]:
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_KEDA_GROUP,
                    version=_KEDA_VERSION,
                    namespace=namespace,
                    plural="scaledjobs",
                )
            else:
                raw = self._crd().list_cluster_custom_object(  # type: ignore
                    group=_KEDA_GROUP,
                    version=_KEDA_VERSION,
                    plural="scaledjobs",
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [self._parse_scaledjob(c) for c in items if isinstance(c, dict)]

    def _list_triggerauths(self, namespace: str | None = None) -> list[KedaTriggerAuth]:
        try:
            if namespace:
                raw = self._crd().list_namespaced_custom_object(  # type: ignore
                    group=_KEDA_GROUP,
                    version=_KEDA_VERSION,
                    namespace=namespace,
                    plural="triggerauthentications",
                )
            else:
                raw = self._crd().list_cluster_custom_object(  # type: ignore
                    group=_KEDA_GROUP,
                    version=_KEDA_VERSION,
                    plural="triggerauthentications",
                )
        except Exception:
            return []
        items = cast(dict, raw).get("items", [])  # type: ignore
        return [self._parse_triggerauth(c) for c in items if isinstance(c, dict)]

    def _parse_scaledobject(self, obj: dict) -> KedaScaledObject:  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        conditions = status.get("conditions", [])
        if not isinstance(conditions, list):
            conditions = []
        ready = False
        phase = KedaScaledObjectPhase.UNKNOWN
        for cond in conditions:
            if isinstance(cond, dict) and cond.get("type") == "Ready":
                if cond.get("status") == "True":
                    ready = True
                    phase = KedaScaledObjectPhase.READY
                elif cond.get("reason") == "Fallback":
                    phase = KedaScaledObjectPhase.FALLBACK
                else:
                    phase = KedaScaledObjectPhase.ERROR

        scale_hpa = status.get("externalMetricNames") or status.get("hpaName")
        current_replicas = obj.get("currentReplicas", 0)

        triggers_raw = spec.get("triggers", [])
        if not isinstance(triggers_raw, list):
            triggers_raw = []
        triggers = [self._parse_trigger(t) for t in triggers_raw if isinstance(t, dict)]

        scale_ref = (
            spec.get("scaleTargetRef", {}) if isinstance(spec.get("scaleTargetRef"), dict) else {}
        )

        return KedaScaledObject(
            name=str(meta.get("name", "")),
            namespace=str(meta.get("namespace", "default")),
            phase=phase,
            min_replicas=int(spec.get("minReplicaCount", 0)),
            max_replicas=int(spec.get("maxReplicaCount", 0)),
            current_replicas=int(current_replicas) if isinstance(current_replicas, int) else 0,
            hpa_target_replicas=0,
            hpa_name=str(scale_hpa) if scale_hpa else None,
            hpa_status=HPAStatus.ACTIVE if ready else HPAStatus.UNKNOWN,  # type: ignore
            triggers=triggers,
            cooldown_period_seconds=int(spec.get("cooldownPeriod", 0)),
            last_scale_time=None,
            idle_replicas=int(spec.get("idleReplicaCount", 0)),
            fallback_replicas=int(spec.get("fallback", {}).get("replicas", 0))
            if isinstance(spec.get("fallback"), dict)
            else None,
            workload_kind=str(scale_ref.get("kind", "Deployment")),
            workload_name=str(scale_ref.get("name", "")),
            ready=ready,
            message=str(conditions[0].get("message", "")) if conditions else None,
        )

    def _parse_scaledjob(self, obj: dict) -> KedaScaledJob:  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}
        status = obj.get("status", {}) if isinstance(obj.get("status"), dict) else {}

        triggers_raw = spec.get("triggers", [])
        if not isinstance(triggers_raw, list):
            triggers_raw = []
        triggers = [self._parse_trigger(t) for t in triggers_raw if isinstance(t, dict)]

        job_ref = spec.get("jobTargetRef", {}) if isinstance(spec.get("jobTargetRef"), dict) else {}
        job_name = (
            str(
                job_ref.get("template", {})
                .get("spec", {})
                .get("containers", [{}])[0]
                .get("name", "")
            )
            if isinstance(job_ref.get("template"), dict)
            else ""
        )

        conditions = status.get("conditions", [])
        if not isinstance(conditions, list):
            conditions = []
        phase = ScaledJobPhase.ACTIVE
        for cond in conditions:
            if isinstance(cond, dict) and cond.get("type") == "Ready":
                phase = (
                    ScaledJobPhase.ACTIVE if cond.get("status") == "True" else ScaledJobPhase.FAILED
                )

        return KedaScaledJob(
            name=str(meta.get("name", "")),
            namespace=str(meta.get("namespace", "default")),
            phase=phase,
            triggers=triggers,
            successful_jobs=0,
            failed_jobs=0,
            last_execution_time=None,
            job_target_ref=job_name,
            cooldown_period_seconds=int(spec.get("cooldownPeriod", 0)),
            max_replica_count=int(spec.get("maxReplicaCount", 0)),
            message=None,
        )

    def _parse_triggerauth(self, obj: dict) -> KedaTriggerAuth:  # type: ignore
        meta = obj.get("metadata", {}) if isinstance(obj.get("metadata"), dict) else {}
        spec = obj.get("spec", {}) if isinstance(obj.get("spec"), dict) else {}

        auth_type = AuthType.NONE
        secret_names: list[str] = []
        env_names: list[str] = []
        pod_identity = None

        st_refs = spec.get("secretTargetRef", [])
        if not isinstance(st_refs, list):
            st_refs = []
        for ref in st_refs:
            if isinstance(ref, dict):
                secret_names.append(str(ref.get("name", "")))

        env_refs = spec.get("env", [])
        if not isinstance(env_refs, list):
            env_refs = []
        for ref in env_refs:
            if isinstance(ref, dict):
                env_names.append(str(ref.get("name", "")))

        if secret_names:
            auth_type = AuthType.SECRET
        elif env_names:
            auth_type = AuthType.ENV
        if spec.get("podIdentity"):
            auth_type = AuthType.POD_IDENTITY
            pod_identity = str(spec["podIdentity"].get("provider", ""))

        return KedaTriggerAuth(
            name=str(meta.get("name", "")),
            namespace=str(meta.get("namespace", "default")),
            kind="TriggerAuthentication",
            trigger_types=[],
            auth_type=auth_type,
            secret_names=secret_names,
            environment_names=env_names,
            pod_identity_provider=pod_identity,
            ready=True,
            message=None,
        )

    @staticmethod
    def _parse_trigger(t: dict) -> KedaTrigger:  # type: ignore
        return KedaTrigger(
            type=KedaAdapter._parse_trigger_type(str(t.get("type", ""))),
            name=str(t.get("name", str(t.get("type", "")))),
            metadata={str(k): str(v) for k, v in t.get("metadata", {}).items()}
            if isinstance(t.get("metadata"), dict)
            else {},
            authentication_ref=str(t.get("authenticationRef", {}).get("name", "")) or None
            if isinstance(t.get("authenticationRef"), dict)
            else None,
            authentication_status=True,
            error_message=None,
        )

    @staticmethod
    def _parse_trigger_type(name: str) -> TriggerType:
        name_lower = name.lower()
        for tt in TriggerType:
            if tt.value in name_lower:
                return tt
        return TriggerType.CUSTOM
